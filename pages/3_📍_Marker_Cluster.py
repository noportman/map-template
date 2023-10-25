import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://noah-map.streamlit.app>
GitHub Repository: <https://github.com/noportman/map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://media.licdn.com/dms/image/D4E35AQFj0aysS6dqdQ/profile-framedphoto-shrink_400_400/0/1694531240649?e=1698847200&v=beta&t=yjABcii5ifUPj63oBUyECbqro0Jtj_WhxpOxnYFr4Rc"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
        regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'

        m.add_geojson(regions, layer_name='US Regions')
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column='region',
            icon_names=['gear', 'map', 'leaf', 'globe'],
            spin=True,
            add_legend=True,
        )
        
m.to_streamlit(height=700)
