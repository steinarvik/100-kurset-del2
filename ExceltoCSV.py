import streamlit
import pandas


streamlit.title('Excel to CSV Converter')
streamlit.write("Upload an Excel file to convert it to CSV format")

uploaded_file=streamlit.file_uploader("Choose an excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pandas.read_excel(uploaded_file)

    ###  df.to_csv("europe.csv")
    csv_data=df.to_csv(index=False)

    streamlit.download_button(label="Download CSV",
                              data=csv_data,
                              file_name='converted.csv',
                              mime='application/csv')