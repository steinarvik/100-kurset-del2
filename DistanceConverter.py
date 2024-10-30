import streamlit as st

st.title("Kilometers to Miles Converter")

conversion_direction = st.radio("Choose the conversion direction:",
                                ("Kilometers to Miles", "Miles to Kilometers"))
# print(conversion)

# User input for the value to convert
if conversion_direction == "Kilometers to Miles":
    km = st.number_input("Enter the distance in kilometers:", min_value=0.0, format="%.2f")
    if st.button('Convert'):
        # Convert kilometers to miles
        miles = km * 0.621371
        st.success(f"{km:.2f} kilometers is equal to {miles:.2f} miles.")
else:
    miles = st.number_input("Enter the distance in miles:", min_value=0.0, format="%.2f")
    if st.button('Convert'):
        # Convert miles to kilometers
        km = miles / 0.621371
        st.success(f"{miles:.2f} miles is equal to {km:.2f} kilometers.")