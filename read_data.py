# Import dependencies
import pickle

# Load graph object from file
GVSU = pickle.load(open('pickled data/GVSU-NetworkData.pickle', 'rb'))

# Load GPS coordinates of node from file
gps_coordinate_dict = pickle.load(open('pickled data/gps-coordinates.pickle', 'rb'))

# Load the official names of the buildings from file
building_name_dict = pickle.load(open('pickled data/building-names.pickle', 'rb'))
