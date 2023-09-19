import streamlit as st
import pdfplumber
import pandas as pd

# Function to extract tables from a PDF and convert them into Pandas DataFrames
def extract_tables(pdf_file):
    tables = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_tables = page.extract_tables()
            if page_tables:
                tables.extend(page_tables)
    return tables

# Streamlit UI
st.title("PDF to Tables Converter")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("You've uploaded a PDF file!")

    # Extract tables from the PDF
    tables = extract_tables(uploaded_file)

    if not tables:
        st.write("No tables found in the PDF.")
    else:
        st.write(f"Number of tables found: {len(tables)}")

        # Display tables as DataFrames
        for i, table in enumerate(tables):
            df = pd.DataFrame(table[1:], columns=table[0])
            st.write(f"Table {i + 1}:")
            st.write(df)
