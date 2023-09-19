import streamlit as st
import tabula
import pandas as pd

# Function to extract tables from a PDF file using tabula
def extract_tables_from_pdf(pdf_file):
    tables = tabula.read_pdf(pdf_file, pages="all", multiple_tables=True)
    return tables

# Streamlit App
st.title("PDF Table Extractor")

# Upload a PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file is not None:
    # Extract tables from the PDF
    tables = extract_tables_from_pdf(pdf_file)

    # Display each table as a DataFrame
    for i, table_df in enumerate(tables):
        st.subheader(f"Table {i+1}")
        st.write(table_df)

    # You can perform further data analysis or visualization here as needed
