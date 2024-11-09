import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
def data():
    df = pd.read_csv("winter_2023.csv")
    return df


def data_summer_2023():
    df = pd.read_csv("summer_2023.csv")
    return df

def data_winter_2024():
    df = pd.read_csv("winter_2024.csv")
    return df

def data_summer_2024():
    df = pd.read_csv("summer_2024.csv")
    return df
