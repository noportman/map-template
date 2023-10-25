import streamlit as st
import leafmap.foliumap as leafmap

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
    dropdown = st.selectbox("Basemap", ["HYBRID", "USGS 3DEP Elevation", "NLCD 2021 CONUS Land Cover"])

    url = st.text_input("Enter URL")

m= leafmap.Map()
m.add_basemap(dropdown)

if url:
    m.add_tile_layer(url, name='Tile Layer', attribution=' ')

with col1:
    m.to_streamlit()
