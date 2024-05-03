Grand Valley State University Sidewalk Network
=====================================

This repository is a collection of the data and python scripts used for my research titled "An analysis of Grand Valley State Universities Campus using Network Theory." This research was funded by the Alayont Undergraduate Research Fellowship in Mathematics during the the Fall 2023 semester at Grand Valley State University.

File Descriptions
-----------------
**graph_data.csv** - A CSV file where each row is an edge in our network, and each column is described by the following table.

|  Column Name | Description |
|---|---|
| node 1  | The first node of the edge. |
| node 2  | The second node of the edge. |
| weight  | The length of the edge in meters. |

**campus sidewalk diagrams** - A folder of PNG files that I used to seperate the sidewalks of campus into sections for me to measure.

**pickled data** - A folder of compressed objects I used in my wayfinding program. I used the `pickle` library for compression.

**read_data.py** - A python script to read the pickled data.

**wayfinding_program.py** - A python script that calculates and displays the shortest path from one building on campus to another. To run the program, download the last three files (pickled data, read_data.py, wayfinding_program.py). Then, in the directory containing these three files, execute ```python3 wayfinding_program.py``` in your terminal.

**index.html, script.js, style.css** - These files calculate and display the wayfinding program on the [GitHub Pages website corresponding to this repository](https://justinsciullo.github.io/GVSU-Sidewalk-Network/). 

Other Resources
---------------
* [Video of me presenting my research at the 100th MAA Michigan Section Meeting](https://youtu.be/fxUMsT53juE?si=eu5d3tRRmDyCAX08)
* [Link to the wayfinding program hosted online](https://justinsciullo.github.io/JS-GVSU-Map.github.io/)
