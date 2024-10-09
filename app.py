import streamlit
from ExceltoJsonWebapp import convert_excel_to_json


streamlit.title('Excel to JSON Converter')
streamlit.write("Upload an Excel file to convert it ro JSON format")

uploaded_file=streamlit.file_uploader("Choose an excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    json_data=convert_excel_to_json(uploaded_file)
    # streamlit.json(json_data)

    streamlit.download_button(label="Download JSON",
                              data=json_data,
                              file_name='converted.json',
                              mime='application/json')