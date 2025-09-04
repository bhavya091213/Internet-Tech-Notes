import sys
import time
import logging
import difflib
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class DiffLoggingEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.file_snapshots = {}

    def on_modified(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)

        # Only watch markdown files
        if file_path.suffix.lower() != ".md":
            return

        try:
            new_content = file_path.read_text(errors="ignore").splitlines()
        except Exception as e:
            logging.error(f"Could not read {file_path}: {e}")
            return

        old_content = self.file_snapshots.get(file_path, [])
        diff = difflib.unified_diff(
            old_content,
            new_content,
            fromfile=f"{file_path} (old)",
            tofile=f"{file_path} (new)",
            lineterm=""
        )

        diff_output = "\n".join(diff)
        if diff_output:
            logging.info(f"Changes detected in {file_path}:\n{diff_output}")

        self.file_snapshots[file_path] = new_content

    def initialize_snapshots(self, base_path: Path):
        """
        Read all existing .md files under base_path and store their current contents
        so the first modification won't look like a full-file addition.
        """
        for md in base_path.rglob("*.md"):
            try:
                self.file_snapshots[md] = md.read_text(errors="ignore").splitlines()
            except Exception:
                # If a file can't be read, just skip it
                continue


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")

    # If a path is provided, monitor the directory ABOVE it.
    # If no path provided, use current working directory and monitor its parent.
    provided = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    path_to_monitor = provided.parent.resolve()

    logging.info(f"Monitoring all .md files in parent directory: {path_to_monitor}")

    event_handler = DiffLoggingEventHandler()
    # Seed initial snapshots to avoid a giant diff on first modification
    event_handler.initialize_snapshots(path_to_monitor)

    observer = Observer()
    observer.schedule(event_handler, str(path_to_monitor), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
