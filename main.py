#!/usr/bin/env python

import argparse
import logging
import os

from typing import List

from classes.Track import Track

def track_reader(tracks_folder: str) -> List[Track]:
    track_list = []
    for root, _, files in os.walk(tracks_folder):
        for file_name in files:
            if os.path.splitext(file_name)[1] == ".skiz":
                logging.info("Creating Track from %s" % file_name)
                track_list.append(Track.from_skiz_file(os.path.join(root, file_name)))
    return track_list

def main():
    parser = argparse.ArgumentParser(description="Ski Tracks Viewer")
    parser.add_argument("tracks_folder", default="./")
    # Add argument for django server ports
    args = parser.parse_args()

    track_list = track_reader(args.tracks_folder)
    for track in track_list:
        print(track.attributes)

if __name__ == "__main__":
    main()