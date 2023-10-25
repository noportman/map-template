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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
        )
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)
