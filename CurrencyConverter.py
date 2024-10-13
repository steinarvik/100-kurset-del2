import streamlit as st
import requests

api_key = "a07574c5737521eafce0b2d2"
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

def convert(currency, currency_value):
    response = requests.get(url)
    print(response)
    data = response.json()
    conversion_rate = data['conversion_rates']['EUR']
    result = conversion_rate * currency_value
    return result

st.title("Currency Converter: EUR to USD")

conversion = st.radio("Choose the conversion:", ("EUR to USD", "USD to EUR"))
# print(conversion)

input_value = st.number_input(label='Enter the input amount:')

button = st.button("Convert")

if conversion == "USD to EUR":
    if button:
        print(conversion[:3])
        print(input_value)
        euros = convert(conversion[:3], input_value)
        st.success(f"The result is {euros:.2f}")
else:
    if button:
        print(conversion[:3])
        print(input_value)
        dollars = convert(conversion[:3], input_value)
        st.success(f"The result is {dollars:.2f}")