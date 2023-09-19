import streamlit as st
import tabula
import pandas as pd
import numpy as np

# Function to process the PDF and create the DataFrame
def process_pdf(pdf_file):
    tables = tabula.read_pdf(pdf_file, pages="all")
    df = pd.concat(tables)
    df.columns = df.iloc[0]
    df = df.drop(0)
    df.reset_index(drop=True, inplace=True)
    df.columns = ['Category', '2022', '2021', '2020']
    
    # Data cleaning
    df['2022'] = df['2022'].str.replace('$', '').str.replace(',', '').str.replace(r'\((.*?)\)', r'-\1').astype(float)
    df['2021'] = df['2021'].str.replace('$', '').str.replace(',', '').str.replace(r'\((.*?)\)', r'-\1').astype(float)
    df['2020'] = df['2020'].str.replace('$', '').str.replace(',', '').str.replace(r'\((.*?)\)', r'-\1').astype(float)
    
    # Initialize a new column 'Level' to track hierarchy
    df['Level'] = np.nan
    current_level = 0
    
    # Set the hierarchy level based on NaN values in the 'Category' column
    for i, row in df.iterrows():
        if pd.isna(row['2021']):
            current_level += 1
        df.at[i, 'Level'] = current_level
    
    # Find the unique categories where '2022' is null for each level
    null_2022_categories = df[df['2022'].isnull()].groupby('Level')['Category'].first().reset_index()
    
    # Merge the unique categories back to the original DataFrame
    df = df.merge(null_2022_categories, on='Level', suffixes=('', '_Parent'), how='left')
    
    # Rename the 'Category_Parent' column to 'Parent Category' and fill NaN values with 'Category'
    df['Parent Category'] = df['Category_Parent'].fillna(df['Category'])
    
    # Drop the 'Category_Parent' column
    df.drop('Category_Parent', axis=1, inplace=True)
    
    df['Parent Category'] = df['Parent Category'].str.replace(':', '')
    
    # Reorder columns to have 'Parent Category' as the first column
    df = df[['Parent Category'] + [col for col in df if col != 'Parent Category']]
    
    df = df.iloc[:, :-1]
    
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

