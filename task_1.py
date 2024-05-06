import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path):
            copy_files(item_path, dest_dir)
        else:
            try:
                extension = os.path.splitext(item)[1]
                dest_subdir = os.path.join(dest_dir, extension[1:])
                os.makedirs(dest_subdir, exist_ok=True)
                shutil.copy(item_path, dest_subdir)
                print(f"File '{item}' copied to '{dest_subdir}'")
            except Exception as e:
                print(f"Error copying '{item}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them by extension")
    parser.add_argument("source_dir", help="Path to the source directory")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Path to the destination directory (default: dist)")
    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.destination_dir

    if not os.path.isdir(source_dir):
        print(f"Error: '{source_dir}' is not a directory.")
        return
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copy_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()
