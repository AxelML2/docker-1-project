import os
import shutil
import time


def get_src_and_dest():
    SRC = os.environ.get("SRC")
    DST = os.environ.get("DST")
    return SRC, DST


def copy_from_to(src, dst):
    for file_name in os.listdir(src):
        src_file_path = os.path.join(src, file_name)
        dst_file_path = os.path.join(dst, file_name)
        print(f"{src_file_path} copied to {dst_file_path}")
        shutil.copy(src_file_path, dst_file_path)


if __name__ == "__main__":
    SRC, DST = get_src_and_dest()
    copy_from_to(SRC, DST)
    time.sleep(10000)
