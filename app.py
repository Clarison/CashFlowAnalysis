import streamlit as st
import tabula

def pdf_to_tables(pdf_file):
    # Use tabula to extract tables from the PDF
    tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)
    return tables

st.title("PDF to Tables Converter")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.subheader("Uploaded PDF:")
    st.write(uploaded_file)

    # Check if the user has uploaded a file
    if st.button("Convert to Tables"):
        try:
            tables = pdf_to_tables(uploaded_file)

            if not tables:
                st.warning("No tables found in the PDF.")
            else:
                st.subheader("Tables Extracted:")
                for i, table in enumerate(tables):
                    st.write(f"Table {i + 1}")
                    st.write(table)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
