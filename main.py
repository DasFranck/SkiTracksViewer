#!/usr/bin/env python

import argparse
import logging
import os

from typing import List

from classes.Track import Track

def track_reader(tracks_folder: str) -> List[Track]:
    track_list = []

    for _, _, file_name in os.walk(tracks_folder):
        if os.path.splitext(file_name)[1] == ".skiz":
            logging.info("Creating Track from %s" % file_name)
            Track.from_skiz_file(file_name)

    return track_list

def main():
    parser = argparse.ArgumentParser(description="Ski Tracks Viewer")
    parser.add_argument("tracks_folder", default="./")
    # Add argument for django server ports
    args = parser.parse_args()

    track_list = track_reader(args.tracks_folder)

if __name__ == "__main__":
    main()