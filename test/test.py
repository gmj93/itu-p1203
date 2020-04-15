#!/usr/bin/env python3
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../')

from itu_p1203 import __version__
from itu_p1203 import P1203Standalone
from itu_p1203 import P1203Pv
import itu_p1203.utils as utils

BASEDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..')
    )

TEST_FILES = [os.path.join(BASEDIR, "examples", f + ".json") for f in [
    "mode0",
    "mode0_no_stalling",
    "mode0_with_representation_ids",
    "mode1",
    "mode1_without_audio_without_stalling",
    "mode3",
    "mode3_without_audio_without_stalling",
    "request"
]]

TEST_OUTPUT = {
    "mode0": {'O23': 5.0, 'O34': [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0], 'O35': 5.0, 'O46': 4.9209299083625, 'streamId': 42, 'mode': 0, 'date': '2019-11-28T15:00:30.995702', 'O21': [4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587950522131, 4.559587950522131, 4.559587950522131, 4.559587950522131, 4.559587950522131, 4.559587954215205, 4.559587954215205, 4.559587954215205, 4.559587954215205, 4.559587954215205], 'O22': [4.072543327408124, 4.072543327408124, 4.072543327408124, 4.072543327408124, 4.072543327408124, 4.387760507756067, 4.387760507756067, 4.387760507756067, 4.387760507756067, 4.387760507756067, 4.468355547928019, 4.468355547928019, 4.468355547928019, 4.468355547928019, 4.468355547928019, 4.457277347608129, 4.457277347608129, 4.457277347608129, 4.457277347608129, 4.457277347608129]},
    "mode0_no_stalling": {'O23': 5.0, 'O34': [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0], 'O35': 5.0, 'O46': 4.9209299083625, 'streamId': 42, 'mode': 0, 'date': '2019-11-28T15:00:31.035760', 'O21': [4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587950522131, 4.559587950522131, 4.559587950522131, 4.559587950522131, 4.559587950522131, 4.559587954215205, 4.559587954215205, 4.559587954215205, 4.559587954215205, 4.559587954215205], 'O22': [4.072543327408124, 4.072543327408124, 4.072543327408124, 4.072543327408124, 4.072543327408124, 4.387760507756067, 4.387760507756067, 4.387760507756067, 4.387760507756067, 4.387760507756067, 4.468355547928019, 4.468355547928019, 4.468355547928019, 4.468355547928019, 4.468355547928019, 4.457277347608129, 4.457277347608129, 4.457277347608129, 4.457277347608129, 4.457277347608129]},
    "mode0_with_representation_ids": {'O23': 5.0, 'O34': [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0], 'O35': 5.0, 'O46': 4.961923180975, 'streamId': 42, 'mode': 0, 'date': '2019-11-28T15:00:31.085150', 'O21': [4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646], 'O22': [4.30516560172426, 4.329739960430606, 4.347946198589225, 4.361959054902873, 4.373070922914738, 4.38125524673496, 4.387473093999078, 4.392752753500756, 4.397294260217984, 4.401511740115189, 4.408172522275777, 4.415400191213707, 4.42295556167193, 4.430851286042517, 4.439104909169541, 4.444770221275506, 4.448072949690574, 4.45176947859782, 4.455952861200819, 4.460718934572159]},
    "mode0_without_audio": {"O21": [], "O22": [4.072543327408124, 4.072543327408124, 4.072543327408124, 4.072543327408124, 4.072543327408124, 4.387760507756067, 4.387760507756067, 4.387760507756067, 4.387760507756067, 4.387760507756067, 4.468355547928019, 4.468355547928019, 4.468355547928019, 4.468355547928019, 4.468355547928019, 4.457277347608129, 4.457277347608129, 4.457277347608129, 4.457277347608129, 4.457277347608129 ], "O23": 3.7471461951950604, "O34": [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0 ], "O35": 5.0, "O46": 3.8389490826337953, "date": "2020-01-27T15:31:14.636377", "mode": 0, "streamId": 42},
    "mode1": {'O23': 5.0, 'O34': [4.6440688251727185, 4.6440688251727185, 4.6440688251727185, 4.6440688251727185, 4.6440688251727185, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0], 'O35': 4.909548628348856, 'O46': 4.818608875849142, 'streamId': 42, 'mode': 1, 'date': '2019-11-28T15:00:31.129015', 'O21': [4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587950522131, 4.559587950522131, 4.559587950522131, 4.559587950522131, 4.559587950522131, 4.559587954215205, 4.559587954215205, 4.559587954215205, 4.559587954215205, 4.559587954215205], 'O22': [3.6388712431005263, 3.6388712431005263, 3.6388712431005263, 3.6388712431005263, 3.6388712431005263, 3.9788931026764653, 3.9788931026764653, 3.9788931026764653, 3.9788931026764653, 3.9788931026764653, 4.391670686490885, 4.391670686490885, 4.391670686490885, 4.391670686490885, 4.391670686490885, 4.40424388391557, 4.40424388391557, 4.40424388391557, 4.40424388391557]},
    "mode1_without_audio_without_stalling": {'O23': 5.0, 'O34': [3.7937758648099997, 3.7937758648099997, 3.7937758648099997, 3.7937758648099997, 3.7937758648099997, 3.7937758648099997, 3.7937758648099997, 3.7937758648099997, 3.7937758648099997], 'O35': 3.7937758648099993, 'O46': 3.806818024694999, 'streamId': 42, 'mode': 1, 'date': '2019-11-28T15:00:31.161693', 'O21': [], 'O22': [2.7641848972245264, 2.7641848972245264, 2.7641848972245264, 2.7641848972245264, 2.7641848972245264, 2.7641848972245264, 2.7641848972245264, 2.7641848972245264, 2.7641848972245264]},
    "mode3": {'O23': 5.0, 'O34': [4.907096052292074, 4.907096052292074, 4.907096052292074, 4.907096052292074, 4.907096052292074, 4.78291263001335, 4.78291263001335, 4.78291263001335, 4.78291263001335, 4.78291263001335, 4.679107719012344, 4.679107719012344, 4.679107719012344, 4.679107719012344], 'O35': 4.758171591956921, 'O46': 4.687482789417691, 'streamId': 42, 'mode': 3, 'date': '2019-11-28T15:00:31.575464', 'O21': [4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.5595879322084585, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.559587948700646, 4.55958795880896, 4.55958795880896, 4.55958795880896, 4.55958795880896, 4.55958795880896], 'O22': [3.8815643211227364, 3.8815643211227364, 3.8815643211227364, 3.8815643211227364, 3.8815643211227364, 3.7669812860933813, 3.7669812860933813, 3.7669812860933813, 3.7669812860933813, 3.7669812860933813, 3.671201338785246, 3.671201338785246, 3.671201338785246, 3.671201338785246]},
    "mode3_without_audio_without_stalling": {'O23': 5.0, 'O34': [2.055784057874599, 2.055784057874599, 2.055784057874599, 2.055784057874599, 2.055784057874599, 2.055784057874599, 2.055784057874599, 2.055784057874599, 2.055784057874599], 'O35': 2.055784057874599, 'O46': 2.0799483337434492, 'streamId': 42, 'mode': 3, 'date': '2019-11-28T15:00:32.619832', 'O21': [], 'O22': [1.17643751299321, 1.17643751299321, 1.17643751299321, 1.17643751299321, 1.17643751299321, 1.17643751299321, 1.17643751299321, 1.17643751299321, 1.17643751299321]},
    "request": {'O23': 4.5816540429887915, 'O34': [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0], 'O35': 5.000000000000003, 'O46': 4.555725748329095, 'streamId': None, 'mode': 0, 'date': '2019-11-28T15:51:53.052184', 'O21': [4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559, 4.553814018489559], 'O22': [4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369, 4.136734047915369]}
}

if not os.path.isdir(os.path.join(BASEDIR, "examples")):
    print("Examples folder is missing.")
    sys.exit(1)


def fuzzy_equal(d1, d2, precision):
    """
    Compare two objects recursively (just as standard '==' except floating point
    values are compared within given precision.

    Based on https://gist.github.com/durden/4236551, modified to handle lists
    """

    if len(d1) != len(d2):
        return False

    if isinstance(d1, list):
        for v1, v2 in zip(d1, d2):
            if not abs(v1 - 2) < precision:
                return False
    elif isinstance(d1, dict):
        for k, v in d1.items():
            # Make sure all the keys are equal
            if k not in d2:
                return False

            # Fuzzy float comparison
            if isinstance(v, float) and isinstance(d2[k], float):
                if not abs(v - d2[k]) < precision:
                    return False

            # Recursive compare if there are nested dicts
            elif isinstance(v, dict):
                if not fuzzy_equal(v, d2[k], precision):
                    return False

            # Fall back to default
            elif v != d2[k]:
                return False
    else:
        if not abs(d1 - d2) < precision:
            return False

    return True


class TestP1203Parts(unittest.TestCase):
    def test_output(self):
        """
        Perform a small in-built test using example files
        """
        print("Testing model version {}".format(__version__))

        for test_file in sorted(TEST_FILES):
            test_case = os.path.splitext(os.path.basename(test_file))[0]
            test_data = utils.read_json_without_comments(test_file)

            print("Checking {}".format(test_case))
            test_model = P1203Standalone(test_data)
            output = test_model.calculate_complete(print_intermediate=True)

            del output["date"]

            expected_output = TEST_OUTPUT[test_case]
            del expected_output["date"]

            assert fuzzy_equal(output, expected_output, 0.0001)

    def test_model_functions(self):
        """
        Run a series of tests against models
        """
        print("Testing model version {}".format(__version__))

        failed = 0

        avg_qp_per_frame = [26.605956612329944, 30.17195734771418, 32.89184549356223, 34.06182531894014, 33.44129901960784, 29.722637578134574, 32.251378845446744, 33.26394507784725, 33.490804315841096, 29.593455080279448, 32.308805494235955, 33.448791855758614, 33.38045610593428, 29.569117647058825, 32.68492647058824, 33.27613678146832, 34.02036310107949, 29.60178943497978, 32.25796568627451, 33.3860294117647, 33.087388160313765, 29.707807329329576, 31.710413344781063, 33.097842079450714, 32.612452506434614, 29.593577644319158, 32.02500306410099, 32.81556372549019, 32.641666666666666, 34.54432863274065, 27.31764705882353, 30.356171099399436, 33.393111056631525, 34.91981363413438, 34.78062538320049, 30.418014705882353, 32.86985294117647, 34.362009803921566, 34.08370098039216, 30.840299056256896, 33.34681372549019, 33.40818828144153, 33.68730839975475, 31.09020713322711, 32.777178575805856, 33.80122549019608, 34.54001715896556, 31.11925481063856, 33.01911999019487, 34.29921549399363, 33.37153714145624, 31.462434121828654, 33.70106630714548, 34.37690044139284, 33.96542422756253, 31.5828431372549, 33.469607843137254, 34.24031862745098, 34.18799019607843, 35.191053921568624, 27.845833333333335, 31.17526657678637, 33.77561274509804, 34.446829387955354, 34.78239548853745, 31.00147076847653, 33.45030028189729, 34.64620098039216, 34.44056372549019, 31.30935163622993, 33.18163990685133, 34.2268660375046, 34.10626302242922, 31.07683823529412, 33.406004901960785, 34.60110294117647, 34.0031862745098, 31.03382767496017, 33.43982843137255, 34.810661764705884, 34.432598039215684, 30.966299019607842, 33.298811128814805, 34.02242921926707, 34.22904411764706, 30.73970588235294, 33.20269607843137, 34.1203431372549, 33.605343792131386, 36.01176470588236, 27.516666666666666, 30.825468807451895, 33.60220588235294, 35.32078940916892, 34.96678514523839, 30.816053921568628, 33.31629901960784, 34.98369498590168, 34.762319195881346, 31.131633778649345, 33.0015931372549, 33.88039215686275, 33.90783184213752, 30.938717980144627, 33.17904411764706, 34.2640931372549, 33.92719696041181, 31.126853781100625, 32.86076725088859, 34.1049148179924, 34.30187522980757, 31.080514705882354, 33.37124647628386, 34.11078431372549, 33.75781345753156, 30.7171568627451, 33.2371614168403, 33.86307918607502, 33.58666339789164, 35.29170241451158, 27.558892021081014, 30.987745098039216, 33.668219144503006, 35.569572146622534, 35.132720588235294, 31.158965559504843, 33.39441107978919, 34.090808823529414, 34.71356783919598, 30.907586714058095, 33.16055889202108, 34.32736635605689, 34.669733774996935, 30.881358009559996, 33.09597940671733, 34.663357843137256, 34.45919117647059, 30.64611424368718, 32.79568574580218, 34.22946800686443, 33.81470588235294, 30.834048290231646, 32.867140580953546, 34.171323529411765, 33.54057367001716, 31.029411764705884, 32.579237651673, 33.299509803921566, 33.12072557911509, 35.06545721990684, 27.720921681578623, 31.65510479225395, 33.56580882352941, 35.30134803921569, 34.6875842627773, 31.472116680965804, 33.74632352941177, 34.78886709171162, 34.991299019607844, 31.698039215686276, 33.51415614658659, 34.09411764705882, 34.722671568627455, 31.667238632185317, 33.43235294117647, 34.162377450980394, 34.56976459048553, 31.29031862745098, 33.24684397597745, 34.32189262074038, 33.98198529411765, 31.28949626179679, 32.90290547995587, 33.60343137254902, 34.200539347879385, 31.32099522000245, 33.12650159352783, 34.55232843137255, 34.53218094887826, 35.17796298566001, 28.126470588235293, 31.594607843137254, 33.75781345753156, 35.236209855356705, 34.658700980392155, 31.624877450980392, 33.898529411764706, 34.73406862745098, 34.6780637254902, 31.439705882352943, 33.74138987621032, 34.386539168812064, 34.56875, 31.53511459737713, 33.35171568627451, 34.8363569502329, 34.32700085794828, 31.65657556073048, 33.32769607843137, 34.62401960784314, 34.38921568627451, 31.586714058095353, 33.202550269740065, 34.99644477136202, 34.133823529411764, 31.738970588235293, 33.39154411764706, 34.513420762348325, 34.431372549019606, 35.01274509803922, 28.088981492830005, 31.47640642235568, 33.83956367201863, 34.95808823529412, 34.998896923642604, 31.674347346488542, 33.48394214268203, 34.74522058823529, 34.657433509008456, 31.460661764705883, 33.78686113494301, 34.73455882352941, 34.473161764705885, 31.331045471258733, 33.86260571148425, 34.78235294117647, 35.271936274509805, 31.622380193651182, 33.59840588595954, 34.74773117488349, 34.93713235294118, 31.464338235294118, 33.3879627359647, 34.86666666666667, 34.536764705882355, 31.547549019607843, 33.10712097070719, 34.12489275646525, 34.52923152347101, 35.229166666666664, 28.084324059320995, 32.025122549019606, 34.08848039215686, 35.199044000490254, 35.36891775952935, 31.686113494300773, 33.79654369408016, 34.70078450600637, 35.05247027093294, 31.674387254901962, 33.65931372549019, 35.03235294117647, 34.8938465310125, 31.730481676676064, 33.462132352941175, 34.74166666666667, 34.412867647058825, 31.54105392156863, 33.60424071577399, 34.321813725490195, 35.006005637945826, 31.856600073538424, 33.577573529411765, 34.89154411764706, 34.554479715651425, 31.653799019607842, 33.36609878661601, 34.666748376026476, 34.373130669281686, 35.40078440985415, 28.21289373697757, 31.628385831597008, 34.037254901960786, 35.17046568627451, 35.0234068627451, 31.579973035911262, 33.99436205417331, 34.90796568627451, 34.90686274509804, 31.70045348694693, 33.7109068627451, 34.69150631204805, 34.90145851207256, 31.48621154553254, 33.45740899620051, 34.9019487682314, 34.80781958573355, 31.74264705882353, 33.46825980392157, 34.48664215686274, 34.92313350496506, 31.46421568627451, 33.62046568627451, 34.84985905135433, 34.138007108714305, 31.483210784313727, 33.344485294117646, 34.30889924000981, 34.443804387792625, 35.37708333333333, 28.170976835396495, 31.956004901960785, 33.93345588235294, 35.29450711132908, 35.08335376317725, 31.724230910650814, 33.79671407552722, 35.314950980392155, 34.797916666666666, 31.761367814683172, 33.743718592964825, 34.753553921568624, 34.71997549019608, 31.56482843137255, 33.61691176470588, 34.767373452629, 34.947781318950724, 31.78208113739429, 33.56209390707368, 34.615686274509805, 34.90281862745098, 31.91469542836132, 33.58034072803039, 34.52120098039216, 34.77561274509804, 31.781468317195735, 33.27228147603285, 34.23664215686274, 34.34931338891614, 35.006624141315015, 28.3569064836377]
        tests = {
            "mode0": [
                { "mos": 4.311, "args": (1920*1080, 1920*1080, 2801.27587623, 30) },
                { "mos": 2.664, "args": (852*480, 1920*1080, 629.203792838, 30) },
                { "mos": 1.085, "args": (426*240, 1920*1080, 224.771246112, 30) }
            ],
            "mode1": [
                { "mos": 4.061, "args": (1920*1080, 1920*1080, 2409.39329393, 30, [], 10.9551545708) },
                { "mos": 3.76, "args": (1920*1080, 1920*1080, 2805.94165942, 30, [], 7.4658972759) },
                { "mos": 2.551, "args": (852*480, 1920*1080, 529.580495805, 30, [], 11.7097170972) },
                { "mos": 1.118, "args": (426*240, 1920*1080, 132.874928749, 30, [], 22.5031055901) }
            ],
            "mode3": [
                { "mos": 3.665, "args": (1920*1080, 1920*1080, 30, [], 0.6537627021) },
                { "mos": 1.05, "args": (102240, 1920*1080, 30, [], 0.7688713219) },
                { "mos": 3.671, "args": (1920*1080, 1920*1080, 30, [], None, avg_qp_per_frame)}
            ]
        }

        for mode, mode_tests in tests.items():
            for test_data in mode_tests:
                fun = getattr(P1203Pv, "video_model_function_" + mode)
                ret = round(fun(*test_data["args"]), 3)
                mos = test_data["mos"]
                if abs(ret - mos) > 0.01:
                    print("{mode} test failed, expected {mos}, got {ret}".format(**locals()))
                    failed += 1

        self.assertTrue(failed == 0)


if __name__ == '__main__':
    unittest.main()
