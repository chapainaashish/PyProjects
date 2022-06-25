"""Music mover Python"""
import os
import shutil
import sys


def music_mover(path):
    os.mkdir(f"{path}/Music")
    for folder in os.listdir(path):
        if folder != "Music":
            for music in os.listdir(f"{path}/{folder}"):
                shutil.move(f"{path}/{folder}/{music}", f"{path}/Music")
            os.rmdir(f"{path}/{folder}")


def main():
    file_path = sys.argv[1]
    music_mover(file_path)


main()
