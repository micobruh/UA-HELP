# Code reference: https://stackoverflow.com/questions/36994746/how-to-find-path-and-distance-between-two-coordinates-using-osm-and-python
# Ukraine Checkpoint File Source: https://data.humdata.org/dataset/ukraine-border-crossings

import osmnx as ox
import networkx as nx
from datetime import timedelta
from ukraine_app.data import get_data
from geopy.geocoders import Nominatim
#import geocoder as gc
import warnings

warnings.filterwarnings("ignore")

# Import the data from the excel file
df = get_data()
checkpoint_lst = df['coordinates'].tolist()
# TODO: Replace the location name with any other location names in HK
location_name = "Hung Shui Kiu"
 
# Call the Nominatim tool
loc = Nominatim(user_agent = "GetLoc")

# Enter the location name to obtain its latitude and longitude
getLoc = loc.geocode(location_name)
origin_coordinates = (getLoc.latitude, getLoc.longitude)

# Can be deleted, just used to indicate the loading progress
print(origin_coordinates)

# Just to show that we have the capability to obtain GPS signal data
#g = gc.ipinfo('me')
#print(g.ip, g.city, tuple(g.latlng))

# The codes between hashtag long lines show how the map data file is created
#################################################################################################################################

# # Select the map area that you are interested with. In this example, hk is used.
# graph_area = ("hk")
# # graph_area = ("Ukraine")

# # Create the graph of the area from OSM data. It will download the data and create the graph.
# G = ox.graph_from_place(graph_area, network_type='drive')

# # OSM data are sometime incomplete so we use the speed module of osmnx to add missing edge speeds and travel times
# G = ox.add_edge_speeds(G)
# G = ox.add_edge_travel_times(G)

# # Save graph to disk if you want to reuse it
# ox.save_graphml(G, "HK.graphml")
# # ox.save_graphml(G, "Ukraine.graphml")

#################################################################################################################################

# Load the graph file
G = ox.load_graphml("HK.graphml")
# G = ox.load_graphml("Ukraine.graphml")

# Can be deleted, just used to indicate the loading progress
print("Load map success!")

# In the graph, get the nodes closest to the point
origin_node = ox.get_nearest_node(G, origin_coordinates)

time_lst = []
distance_lst = []
# Find the distance and travelling time from the origin to each checkpoint
for destination_coordinates in checkpoint_lst:
    # In the graph, get the nodes closest to the point
    destination_node = ox.get_nearest_node(G, destination_coordinates)
    # Get the travel time, in seconds
    # Note here that we use "nx" (networkx), not "ox" (osmnx)
    travel_time_in_seconds = nx.shortest_path_length(G, origin_node, destination_node, weight='travel_time')
    # Get the distance in kilometers
    distance_in_kilometers = nx.shortest_path_length(G, origin_node, destination_node, weight='length') / 1000
    # Append two values found above into the lists
    time_lst.append(timedelta(seconds=travel_time_in_seconds))
    distance_lst.append(distance_in_kilometers)

# Match the distance and travelling time to their respective checkpoint coordinates
time_dct = dict(zip(checkpoint_lst, time_lst))
distance_dct = dict(zip(checkpoint_lst, distance_lst))

# The travel time in "HOURS:MINUTES:SECONDS" format
best_time_point = min(time_dct.keys(), key = (lambda k: time_dct[k]))
# Select the row that contains the checkpoint information with shortest travelling time
df_time = df.loc[df['coordinates'] == best_time_point]
df_time = df_time.reset_index(drop = True)

best_distance_point = min(distance_dct.keys(), key = (lambda k: distance_dct[k]))
# Select the row that contains the checkpoint information with shortest distance time
df_distance = df.loc[df['coordinates'] == best_distance_point]
df_distance = df_distance.reset_index(drop = True)

# Print the information of checkpoint with shortest travelling time
travel_text = 'Shortest Travelling Time: ' + str(time_dct[best_time_point]) + '\n English Name of Checkpoint: ' + df_time.loc[0, 'Name - English'] + '\n Ukrainian Name of Checkpoint: ' + df_time.loc[0, 'Name - Ukrainian'] + '\n Country: ' + df_time.loc[0, 'Country']

# Print the information of checkpoint with shortest distance
distance_text = 'Shortest Travelling Distance: ' + str(distance_dct[best_distance_point]) + ' km\n English Name of Checkpoint: ' + df_distance.loc[0, 'Name - English'] + '\n Ukrainian Name of Checkpoint: ' + df_distance.loc[0, 'Name - Ukrainian'] + '\n Country: ' + df_time.loc[0, 'Country']

overall_text = travel_text + '\n \n \n' + distance_text

print(overall_text)

# Output 
with open('output_text.txt', 'w') as f:
    f.write(overall_text)

# In the graph, get the nodes closest to the points for the optimal checkpoint
short_node = ox.get_nearest_node(G, df_distance.loc[0, 'coordinates'])
fast_node = ox.get_nearest_node(G, df_time.loc[0, 'coordinates'])

# Get the shortest route by distance
shortest_route_by_distance = ox.shortest_path(G, origin_node, short_node, weight='length')
# Get the shortest route by travelling time
shortest_route_by_travel_time = ox.shortest_path(G, origin_node, fast_node, weight='travel_time')
# Plot the 2 routes on a map, where red route is the shortest route by distance, and yellow route is the shortest route by travelling time
fig, ax = ox.plot_graph_routes(G, routes=[shortest_route_by_distance, shortest_route_by_travel_time], route_colors=['r', 'y'], route_linewidth=6, node_size=0)
fig.savefig('output_graph.png')