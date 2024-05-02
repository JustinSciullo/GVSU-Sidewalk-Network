#!/usr/bin/env python #
"""A script for calculating and displaying the shortest path between buildings at GVSU using Dijkstra's algorithm,
and then displaying the results using Tkinter for user readability.
"""

__author__ = "Justin Sciullo"
__email__ = "JustinDSciullo@Gmail.com"
__date__ = "05/02/2024"

# Import dependencies
from sys import maxsize
from tkinter import *

import networkx as nx
import tkintermapview

from read_data import *


def shortest_path_between_buildings(starting_building: str, destination_building: str) -> tuple[float, list]:
    """This function finds the shortest path between two buildings on the Grand Valley State University Allendale
    campus, and returns the shortest path through our network between the two buildings as well as the length of this
    path.

    :param starting_building: The name of the building that one is starting in.
    :param destination_building: The name
    of the building that one wants to end in.
    :returns: A tuple of the length of the shortest path between the two buildings and
    a list of the shortest path taken through the graph.
    """

    # Reverse building_name_dict to easily access acronyms
    name_to_node_dict = {j: i for i, j in building_name_dict.items()}

    # Convert the full building name into the acronym for the building entrance nodes =
    initial_node_name = name_to_node_dict[starting_building]
    destination_node_name = name_to_node_dict[destination_building]

    # Create a list of every entrance node for our buildings
    initial_nodes = [node for node in GVSU.nodes if node.split('_')[0] == initial_node_name]
    destination_nodes = [node for node in GVSU.nodes if node.split('_')[0] == destination_node_name]

    # Run Dijkstra's alg on every combination of nodes, and return the best one
    shortest_distance = maxsize
    shortest_path = -1
    for u in initial_nodes:
        for v in destination_nodes:
            path = nx.dijkstra_path(GVSU, u, v)
            distance = nx.path_weight(GVSU, path, weight="weight")
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path
    return shortest_distance, shortest_path


def display_results(starting_building: StringVar(), destination_building: StringVar()):
    """This function calls shortest_path_between_buildings, and then displays the results in our window.

    :param starting_building: The name of the building that one is starting in.
    :param destination_building: The name
    of the building that one wants to end in.
    """
    global results  # Access the text box beneath the buttons, so we can modify it

    # Calculate the shortest path between our two buildings
    distance, path_taken = shortest_path_between_buildings(starting_building.get(), destination_building.get())

    # Draw our path on the map
    map_widget.delete_all_path()
    path_coords = [(gps_coordinate_dict[i][0], -1 * gps_coordinate_dict[i][1]) for i in path_taken]
    map_widget.set_path(path_coords, color='red', width=4)

    # Reframe our window around our new path
    x_coords, y_coords = zip(*path_coords)
    bottom, top = min(x_coords), max(x_coords)
    left, right = min(y_coords), max(y_coords)
    map_widget.fit_bounding_box((top, left), (bottom, right))

    # Update the text in the results variable
    results['text'] = (
        f'The shortest path from {starting_building.get()} to {destination_building.get()} is {distance:.2f}m long.'
        f' \n It will take you about {round(distance * (1 / 1.42) * (1 / 60), 1)} minutes to get there.')
    results.pack()


if __name__ == "__main__":
    window = Tk()  # Create the window
    window.geometry('800x700')
    window.title("Dijkstra's Algorithm Assistant")

    initial_node = StringVar()
    destination_node = StringVar()

    building_names = sorted([i for i in building_name_dict.values()])

    # Create dropdown menu for initial node
    Label(window, text='Select Starting Building: ').pack()
    OptionMenu(window, initial_node, *building_names).pack()

    # Create dropdown menu for destination node
    Label(window, text='Select Destination Building: ').pack()
    OptionMenu(window, destination_node, *building_names).pack()

    # Create a button to calculate the shortest path
    calculate = Button(window, text='Calculate Shortest Path', bd='5',
                       command=lambda: display_results(initial_node, destination_node))
    calculate.pack()

    # Create an empty text box to display the results once found
    results = Label(window, text='')
    results.pack()

    # Create the map widget with high quality map tiles
    map_widget = tkintermapview.TkinterMapView(window, width=700, height=500, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.99, anchor=S)
    map_widget.set_tile_server(r"https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map_widget.set_position(42.9626606, -85.8874659)  # Center on GVSU
    map_widget.set_zoom(15)

    window.mainloop()
