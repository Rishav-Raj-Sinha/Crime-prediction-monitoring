import streamlit as st
import matplotlib.pyplot as plt
import numpy
import pandas as pd
import streamlit.components.v1 as components
# Page configs
st.set_page_config(layout="wide")
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# Design hide "made with streamlit" footer menu area
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}</style>"""
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)
#title and description page
st.title("Crime monitoring/prediction model 🚨")
#with st.popover("About Us"):
#    st.write("Introducing our cutting-edge Crime Prediction and Monitoring System (CPMS) – a revolutionary machine learning model designed to forecast crime-prone regions and effectively monitor criminal activities. By analyzing historical crime data, socio-economic factors, demographic information, and real-time inputs such as weather and local events, CPMS generates predictive insights to identify areas at high risk of criminal incidents.Utilizing advanced algorithms, CPMS not only predicts potential crime hotspots but also continuously monitors and updates its predictions based on evolving data patterns. Through integration with law enforcement databases and surveillance systems, CPMS provides actionable intelligence to law enforcement agencies, enabling proactive deployment of resources for crime prevention and rapid response.With its proactive approach and real-time monitoring capabilities, CPMS empowers communities to enhance public safety, allocate resources efficiently, and combat crime effectively in today's dynamic urban environments.")
#with st.popover("Github"):
#    st.write("Repo link : ")
#tabs

tab1, tab2, tab3 = st.tabs(["About Us", "Github", "Dataset"])

with tab1:
   st.write("Introducing our cutting-edge Crime Prediction and Monitoring System (CPMS) – a revolutionary machine learning model designed to forecast crime-prone regions and effectively monitor criminal activities. By analyzing historical crime data, socio-economic factors, demographic information, and real-time inputs such as weather and local events, CPMS generates predictive insights to identify areas at high risk of criminal incidents.Utilizing advanced algorithms, CPMS not only predicts potential crime hotspots but also continuously monitors and updates its predictions based on evolving data patterns. Through integration with law enforcement databases and surveillance systems, CPMS provides actionable intelligence to law enforcement agencies, enabling proactive deployment of resources for crime prevention and rapid response.With its proactive approach and real-time monitoring capabilities, CPMS empowers communities to enhance public safety, allocate resources efficiently, and combat crime effectively in today's dynamic urban environments.")


with tab2:
   st.write("Github link")

with tab3:
   st.write("Dataset")

st.divider()
#selection widgets
districts_karnataka = [
    "Bangalore Urban",
    "Bangalore Rural",
    "Belgaum",
    "Bellary",
    "Bidar",
    "Bijapur (Vijayapura)",
    "Chamarajanagar",
    "Chikballapur",
    "Chikmagalur",
    "Chitradurga",
    "Dakshina Kannada",
    "Davanagere",
    "Dharwad",
    "Gadag",
    "Gulbarga (Kalaburagi)",
    "Hassan",
    "Haveri",
    "Kodagu (Coorg)",
    "Kolar",
    "Koppal",
    "Mandya",
    "Mysore (Mysuru)",
    "Raichur",
    "Ramanagara",
    "Shimoga (Shivamogga)",
    "Tumkur (Tumakuru)",
    "Udupi",
    "Uttara Kannada (Karwar)",
    "Yadgir"
]
st.header("Please select your district")
selected_district = st.selectbox("Karnataka districts :", districts_karnataka)
# columns
col1,col2,col3 = st.columns(3)



