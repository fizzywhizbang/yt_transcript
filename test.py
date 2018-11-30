#!/usr/bin/env python3

from yt_transcript import fetch
from yt_transcript import utils
import sys

yt = fetch.tsFetch

url = sys.argv[1]
video_id = utils.parse_url(url)

lists = yt.get_transcript(video_id)

for dict in lists:
    for key in dict:
        value = dict[key]
        if key == "text":
            print(value)

