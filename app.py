import streamlit as st
import fitz  # PyMuPDF
import pandas as pd

# Function to extract tables from PDF text
def extract_tables_from_pdf(pdf_file):
    tables = []
    doc = fitz.open(pdf_file)
    
    for page in doc:
        text = page.get_text()
        # Assuming that tables are separated by newline characters
        table_data = [line.split('\t') for line in text.split('\n')]
        if table_data:
            tables.append(table_data)
    
    return tables

# Streamlit UI
st.title("PDF to Tables Converter")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("You've uploaded a PDF file!")

    # Extract tables from the PDF
    tables = extract_tables_from_pdf(uploaded_file)

    if not tables:
        st.write("No tables found in the PDF.")
    else:
        st.write(f"Number of tables found: {len(tables)}")

        # Display tables as DataFrames
        for i, table in enumerate(tables):
            df = pd.DataFrame(table[1:], columns=table[0])
            st.write(f"Table {i + 1}:")
            st.write(df)
