# Import module
from sys import maxsize
from tkinter import *
import networkx as nx
import tkintermapview
from read_data import *


def shortest_path_between_buildings(initial_building=str, destination_building=str):
    # Find the short version of our building names
    name_to_node_dict = {j: i for i, j in building_name_dict.items()}
    initial_node_name = name_to_node_dict[initial_building]
    destination_node_name = name_to_node_dict[destination_building]

    # Create a list of every node with a matching name
    initial_nodes = []
    destination_nodes = []
    for node in GVSU.nodes:
        if node.split('_')[0] == initial_node_name:
            initial_nodes.append(node)
        elif node.split('_')[0] == destination_node_name:
            destination_nodes.append(node)

    # Run Dijkstras alg on every combinaiton of nodes, and return the best one
    shortest_distance = maxsize
    shortest_path = []
    for u in initial_nodes:
        for v in destination_nodes:
            path = nx.dijkstra_path(GVSU, u, v)
            distance = nx.path_weight(GVSU, path, weight="weight")
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

    return shortest_distance, shortest_path


# Def function to display the results of our alg
def display_results(starting_building, destination_building):
    global results
    distance, path_taken = shortest_path_between_buildings(starting_building.get(), destination_building.get())

    # Draw our path
    path_width = 4
    path_color = 'red'

    map_widget.delete_all_path()
    path_coords = [(gps_coordinate_dict[i][0], -1 * gps_coordinate_dict[i][1]) for i in path_taken]
    map_widget.set_path(path_coords, color=path_color, width=path_width)

    # Reframe our screen
    bottom = 100
    top = 0
    left = 0
    right = -100
    for path in path_coords:
        x, y = path
        if x < bottom:
            bottom = x
        if x > top:
            top = x
        if y < left:
            left = y
        if y > right:
            right = y
    map_widget.fit_bounding_box((top, left), (bottom, right))

    results['text'] = (
        f'The shortest path from {starting_building.get()} to {destination_building.get()} is {distance}m long. \n It '
        f'will take you about {round(distance * (1 / 1.42) * (1 / 60), 1)} minutes to get there.')
    results.pack()
    # path.pack()


if __name__ == "__main__":
    # Create the window
    window = Tk()
    window.geometry('800x700')
    window.title('Dijkstras Algorithim Assitant')

    # Specifiy our variables
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

    # Create a text box to display the results
    results = Label(window, text='')
    results.pack()

    # Create the map widget
    map_widget = tkintermapview.TkinterMapView(window, width=700, height=500, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.99, anchor=S)
    map_widget.set_tile_server(r"https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map_widget.set_position(42.9626606, -85.8874659)
    map_widget.set_zoom(15)

    window.mainloop()
