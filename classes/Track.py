#!/usr/bin/env python

import csv

from typing import List
import xml.etree.ElementTree as ET
from zipfile import ZipFile

from .Node import Node
from .Segment import Segment

class Track:
    attributes = {}
    stats = {}
    nodes = []
    segments = []

    def __init__(self, track_xml: str, nodes_csv: str, photos_csv: str, segment_csv: str) -> None:
        self.parse_track_xml(track_xml)

    def parse_track_xml(self, track_xml: str) -> None:
        xml_root = ET.fromstring(track_xml)
        self.attributes = xml_root.attrib
        self.stats = {element.tag: element.text for element in xml_root.find("metrics").iter() if element.text.strip()}

    def parse_node_csv(self, nodes_csv: str) -> None:
        pass

    def parse_segment_csv(self, segment_csv: str) -> None:
        pass

    @classmethod
    def from_skiz_file(cls, skiz_path: str):
        with ZipFile(skiz_path) as skiz:
            track_xml = skiz.read("Track.xml").decode("utf8")
            nodes_csv = skiz.read("Nodes.csv").decode("utf8")
            photos_csv = skiz.read("Photos.csv").decode("utf8")
            segment_csv = skiz.read("Segment.csv").decode("utf8")
        return cls(track_xml, nodes_csv, photos_csv, segment_csv)