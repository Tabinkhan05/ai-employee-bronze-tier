
import os
import time
from pathlib import Path
from datetime import datetime

# --- Configuration ---
INBOX_FOLDER = Path("Inbox")
NEEDS_ACTION_FOLDER = Path("Needs_Action")
CHECK_INTERVAL = 5  # seconds

# --- Helper Functions ---
def log_activity(message):
    print(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {message}")

def create_action_file(txt_file_path):
    try:
        # Read file content
        with open(txt_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Create .md file path
        filename = txt_file_path.stem
        md_file_path = NEEDS_ACTION_FOLDER / f"{filename}.md"

        # Get current date
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Create frontmatter and content
        frontmatter = f"""---
type: inbox_item
filename: {filename}.txt
date: {current_date}
priority: medium
---"""
        suggested_actions = f"""
## Suggested Actions

- [ ] Review content
- [ ] Determine next steps
- [ ] File/Archive original
"""

        # Write to .md file
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(frontmatter)
            f.write("\n\n") # Separator between frontmatter and content
            f.write(content)
            f.write(suggested_actions)

        log_activity(f"Created action file: {md_file_path}")
        return True

    except Exception as e:
        log_activity(f"Error processing {txt_file_path}: {e}")
        return False

# --- Main Watcher Logic ---
def watch_inbox():
    log_activity("Starting file watcher...")
    log_activity(f"Watching: {INBOX_FOLDER.resolve()}")
    log_activity(f"Outputting to: {NEEDS_ACTION_FOLDER.resolve()}")

    # Create folders if they dont exist
    INBOX_FOLDER.mkdir(exist_ok=True)
    NEEDS_ACTION_FOLDER.mkdir(exist_ok=True)

    processed_files = set()

    while True:
        try:
            # Scan Inbox folder
            for item in INBOX_FOLDER.iterdir():
                if item.is_file() and item.suffix == ".txt":
                    if item not in processed_files:
                        log_activity(f"New file detected: {item.name}")
                        if create_action_file(item):
                            processed_files.add(item)
                        # Optional: uncomment to delete original file after processing
                        # else:
                        #     try:
                        #         item.unlink()
                        #         log_activity(f"Deleted original file: {item.name}")
                        #     except OSError as e:
                        #         log_activity(f"Error deleting {item.name}: {e}")

            # Clean up processed_files set from deleted files
            current_files = set(INBOX_FOLDER.glob("*.txt"))
            processed_files.intersection_update(current_files)

            time.sleep(CHECK_INTERVAL)

        except FileNotFoundError:
            log_activity(f"Error: Inbox folder not found at {INBOX_FOLDER.resolve()}. Please create it.")
            time.sleep(CHECK_INTERVAL * 2) # Wait longer if folder is missing
        except Exception as e:
            log_activity(f"An unexpected error occurred: {e}")
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    watch_inbox()
