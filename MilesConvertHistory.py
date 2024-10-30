import streamlit as st


# Function to convert kilometers to miles
def km_to_miles(km):
    return km * 0.621371


# Function to convert miles to kilometers
def miles_to_km(miles):
    return miles / 0.621371


# Streamlit app layout
st.title('Kilometers ⇄ Miles Converter')

# User selection for conversion direction
conversion_direction = st.radio("Choose the conversion direction:", ("Kilometers to Miles", "Miles to Kilometers"))

# Initialize a session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

# User input for the value to convert
if conversion_direction == "Kilometers to Miles":
    km = st.number_input("Enter the distance in kilometers:", min_value=0.0, format="%.2f")
    if st.button('Convert'):
        miles = km_to_miles(km)
        result = f"{km:.2f} kilometers is equal to {miles:.2f} miles."
        st.success(result)
        st.session_state.history.append(result)
else:
    miles = st.number_input("Enter the distance in miles:", min_value=0.0, format="%.2f")
    if st.button('Convert'):
        km = miles_to_km(miles)
        result = f"{miles:.2f} miles is equal to {km:.2f} kilometers."
        st.success(result)
        st.session_state.history.append(result)

# Display conversion history
if st.session_state.history:
    st.write("Conversion History:")
    for entry in st.session_state.history:
        st.write(entry)