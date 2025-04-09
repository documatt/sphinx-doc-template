import os
import shutil


def move_source_to_root(root_dir="."):
    print("Moving source directory to root...")

    source_path = os.path.join(root_dir, "source")
    if not os.path.exists(source_path):
        print(f"Source directory '{source_path}' does not exist.")
        return

    for item in os.listdir(source_path):
        src_item = os.path.join(source_path, item)
        dest_item = os.path.join(root_dir, item)
        try:
            shutil.move(src_item, dest_item)
        except Exception as e:
            print(f"Error moving {src_item} to {dest_item}: {e}")

    try:
        os.rmdir(source_path)
        print(f"Removed empty directory: {source_path}")
    except Exception as e:
        print(f"Error removing directory {source_path}: {e}")

    print("Move completed.")


if __name__ == "__main__":
    move_source_to_root()
