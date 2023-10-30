import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import random
import geopandas as gpd
from shapely.geometry import Polygon 

markdown = """
Web App URL: <https://noah-map.streamlit.app>
GitHub Repository: <https://github.com/noportman/map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
# logo = ""
# st.sidebar.image(logo)

st.title("My Map")

col1, col2 = st.columns([7, 3])

with col2:
    st.header("Bounding Box Input")
    st.write("Currently set to West Virginia")
    min_lat = st.number_input("Min Latitude", value=37.201483)
    max_lat = st.number_input("Max Latitude", value=40.637151)
    min_lon = st.number_input("Min Longitude", value=-82.644739)
    max_lon = st.number_input("Max Longitude", value=-77.719519)

with col2:
    # Use checkboxes to allow users to select multiple basemaps
    selected_basemaps = st.multiselect("Basemaps", ["HYBRID", "OpenTopoMap", "NLCD 2021 CONUS Land Cover"])

# Create a GeoJSON bounding box based on user input
bbox_polygon = Polygon([(min_lon, min_lat), (max_lon, min_lat), (max_lon, max_lat), (min_lon, max_lat), (min_lon, min_lat)])
bbox_geojson = gpd.GeoSeries([bbox_polygon]).__geo_interface__

# Load the county GeoJSON file locally
county_geojson_path = "C:\Users\noahportman\apps\map-template\shapefiles\WV_County_Boundaries.geojson"

# Calculate the center of the bounding box
center_lat = (min_lat + max_lat) / 2
center_lon = (min_lon + max_lon) / 2

# Calculate the map bounds to constrain the basemaps within the bounding box
map_bounds = [(min_lat, min_lon), (max_lat, max_lon)]

# Add the user-defined bounding box to the map
m = leafmap.Map(center=[center_lat, center_lon], zoom=7, max_bounds=True, max_bounds_2=map_bounds)
m.add_geojson(in_geojson=bbox_geojson, layer_name="User Bounding Box")
m.add_geojson(county_geojson_path, layer_name="counties")

# Loop through selected basemaps and add them to the map if they intersect the bounding box
for basemap in selected_basemaps:
    if basemap == "NLCD 2021 CONUS Land Cover":
        # Display the legend when NLCD is selected
        m.add_legend(title='NLCD Land Cover Type', builtin_legend='NLCD')
    m.add_basemap(basemap)

with col1:
    m.to_streamlit()