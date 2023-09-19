import streamlit as st
import camelot
import pandas as pd
import numpy as np

# Function to process the PDF and create the DataFrame
def process_pdf(pdf_file):
    tables = camelot.read_pdf(pdf_file, pages="all")
    dfs = [table.df for table in tables]
    df = pd.concat(dfs, ignore_index=True)
    df.columns = ['Category', '2022', '2021', '2020']

    # Data cleaning (similar to your previous code)
    df['2022'] = df['2022'].str.replace('$', '').str.replace(',', '').str.replace(r'\((.*?)\)', r'-\1').astype(float)
    df['2021'] = df['2021'].str.replace('$', '').str.replace(',', '').str.replace(r'\((.*?)\)', r'-\1').astype(float)
    df['2020'] = df['2020'].str.replace('$', '').str.replace(',', '').str.replace(r'\((.*?)\)', r'-\1').astype(float)

    # Hierarchy and parent category logic (similar to your previous code)
    # ...

    return df

# Streamlit App
st.title("PDF Table Extraction and Transformation")

# Upload a PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file is not None:
    # Process the PDF and create the DataFrame
    df = process_pdf(pdf_file)

    # Display the DataFrame
    st.write("Processed Data:")
    st.write(df)

    # You can perform further data analysis or visualization here as needed


