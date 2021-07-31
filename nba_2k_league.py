
import pandas as pd
import streamlit as st



st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )


@st.cache
def get_data(filename):
    data = pd.read_csv(filename)

return data





header_container = st.beta_container()
stats_container = st.beta_container()	





with header_container:

	
	st.image('logo.png')

	
	st.title("NBA 2K League Stats Explorer")
	st.header("All Data is from https://2kleague.nba.com/stats/ ")
	st.subheader("Web App created by @IAMHKTR")
	









with stats_container:





	data = get.data('data/nba2kleague_stats.csv')
   







	