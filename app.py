import streamlit as st
import PyPDF2
import pandas as pd

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_text += page.extractText()
    
    return pdf_text

# Function to convert extracted text into a DataFrame
def convert_to_dataframe(pdf_text):
    # Split the text into lines and create a list of rows
    rows = pdf_text.split('\n')
    
    # Split each row into columns using a delimiter (e.g., tab or comma)
    # Modify the split logic based on your PDF's structure
    data = [row.split('\t') for row in rows]
    
    # Create a DataFrame from the list of data
    df = pd.DataFrame(data, columns=["Column 1", "Column 2", "Column 3"])  # Modify column names as needed
    
    return df

# Streamlit App
st.title("PDF to Table Converter")

# Upload a PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file is not None:
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_file)

    # Convert extracted text into a DataFrame
    df = convert_to_dataframe(pdf_text)

    # Display the DataFrame
    st.write("Converted Data:")
    st.write(df)

    # You can perform further data analysis or visualization here as needed
