from io import StringIO
from collections import namedtuple

import altair as alt
import math
import pandas as pd
import streamlit as st


st.sidebar.title("Streamlit Upload Examples")
nav = st.sidebar.selectbox(
    "Choose an Example",
    ("--- Choose one ---", "CSV to DataFrame", "Excel file to DataFrame", "Image"),
)

if nav == "CSV to DataFrame":

    """
    # CSV to DataFrame

    Upload a CSV file and display the results as a Pandas DataFrame
    """
    with st.echo(code_location="below"):

        uploaded_csv_file = st.file_uploader("Choose a CSV file", type="csv")

        if uploaded_csv_file is not None:

            st.write(uploaded_csv_file)

            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_csv_file)
            st.write(dataframe)


if nav == "Excel file to DataFrame":

    """
    # Excel (xlsx) to DataFrame

    Upload a xlsx file and display the results as a Pandas DataFrame
    """
    with st.echo(code_location="below"):
        uploaded_excel_file = st.file_uploader("Choose an Excel file", type="xlsx")

        if uploaded_excel_file is not None:

            st.write(uploaded_excel_file)

            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_excel(uploaded_excel_file)
            st.write(dataframe)


if nav == "Image":

    """
    # Image Upload Example

    Upload a imagefile and display the image
    """
    with st.echo(code_location="below"):
        uploaded_image_file = st.file_uploader(
            "Choose an Image file",
        )

        if uploaded_image_file is not None:

            st.image(uploaded_image_file)
