import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://noah-map.streamlit.app>
GitHub Repository: <https://github.com/noportman/map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://media.licdn.com/dms/image/D4E35AQFj0aysS6dqdQ/profile-framedphoto-shrink_400_400/0/1694531240649?e=1698847200&v=beta&t=yjABcii5ifUPj63oBUyECbqro0Jtj_WhxpOxnYFr4Rc"
st.sidebar.image(logo)
st.sidebar.write("Modified by Noah Portman 2023")
st.sidebar.markdown('[LinkedIn](https://www.linkedin.com/in/noah-portman/)')
st.sidebar.markdown('[Website](https://www.noahportman.com/)')

# Customize page title
st.title("Welcome to My Geosptial Application")

st.markdown(
    """
    This multipage app demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project inspired by [Professor Qiusheng Wu](https://geography.utk.edu/about-us/faculty/dr-qiusheng-wu/) at University of Tennessee and you are very welcome to contribute to his [GitHub repository](https://github.com/giswqs/streamlit-multipage-template).
    """
)

markdown = """


"""

# st.markdown(markdown)

# m = leafmap.Map(minimap_control=True)
# m.add_basemap("OpenTopoMap")
# m.to_streamlit(height=500)
