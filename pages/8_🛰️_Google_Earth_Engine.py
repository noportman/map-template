import streamlit as st
# import geemap.foliumap as geemap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: 
Web App URL: <https://noah-map.streamlit.app>
GitHub Repository: <https://github.com/noportman/map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
# logo = ""
# st.sidebar.image(logo)

# Customize page title
st.title("Earth Engine Web App")

st.markdown(
    """
    """
)

markdown = """
"""

st.markdown(markdown)

# m = geemap.Map()
# m.add_basemap("OpenTopoMap")
# m.to_streamlit(height=500)