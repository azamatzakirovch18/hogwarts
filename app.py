import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
from o_winter_school_2022 import winter_school_2022
from summer_school_2023 import summer_school_2023
from u_summer_school_2024 import summer_school_2024
from t_winter_school_2024 import win_24



st.set_page_config(page_title="Hogwarts School Dashboard", layout="wide")

# Load custom CSS to hide the Streamlit branding button in the bottom right
with open("aka.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Your main app code goes here


# st.set_page_config(
#     page_title="Hogwarts School Dashboard",
#     page_icon=":school:",  
#     layout="wide"           
# )


# with open("aka.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# with open("paka.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



with st.sidebar:
    options = option_menu(
        menu_title="Hogwarts school",
        options=[
            "Winter School 2022",
            "Summer School 2023",
            "Winter School 2024",
            "Summer School 2024",
        ],
        icons=["house", "book-half", "journal-bookmark", "pen-fill", "flower1"],
        menu_icon="cast",
        default_index=0,
    )
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if options == "Winter School 2022":
    winter_school_2022()
elif options == "Summer School 2023":
    summer_school_2023()
elif options == "Summer School 2024":
    summer_school_2024()
elif options == "Winter School 2024":
    win_24()
