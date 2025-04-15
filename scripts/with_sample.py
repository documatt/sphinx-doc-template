"""Move samples to source/ (or root if flat), overwrite existing files."""

import os
import shutil


def copy_sample_to_root(root_dir="."):
    print("Copying sample documents...")

    sample_path = os.path.join(root_dir, "with_sample")
    if not os.path.exists(sample_path):
        print(f"Sample directory '{sample_path}' does not exist.")
        return

    for item in os.listdir(sample_path):
        src_item = os.path.join(sample_path, item)

        # Source or flat layout?
        if os.path.exists(os.path.join(root_dir, "source")):
            dest_item = os.path.join(root_dir, "source", item)
        else:
            dest_item = os.path.join(root_dir, item)

        try:
            shutil.move(src_item, dest_item)
        except Exception as e:
            print(f"Error moving {src_item} to {dest_item}: {e}")

    try:
        os.rmdir(sample_path)
        print(f"Removed empty directory: {sample_path}")
    except Exception as e:
        print(f"Error removing directory {sample_path}: {e}")

    print("Sample documents copied.")


if __name__ == "__main__":
    copy_sample_to_root()
