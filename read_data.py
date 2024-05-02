#!/usr/bin/env python #
"""This script creates three variables from pickled python data.
"""

__author__ = "Justin Sciullo"
__email__ = "JustinDSciullo@Gmail.com"
__date__ = "05/02/2024"

# Import dependency
from pickle import load

# Load graph object from file
GVSU = load(open('pickled data/GVSU-NetworkData.pickle', 'rb'))

# Load GPS coordinates of node from file
gps_coordinate_dict = load(open('pickled data/gps-coordinates.pickle', 'rb'))

# Load the official names of the buildings from file
building_name_dict = load(open('pickled data/building-names.pickle', 'rb'))
