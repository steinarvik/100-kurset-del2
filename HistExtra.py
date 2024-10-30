import requests
import streamlit as st


def get_historical_data(month, day):
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        events = data['data']['Events']
        births = data['data']['Births']
        deaths = data['data']['Deaths']
        return events, births, deaths
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return [], [], []
    except KeyError:
        st.error("No data found for this date.")
        return [], [], []


st.title('Historical Events Viewer')
st.write('Enter a date to retrieve historical events.')

# Input fields for month and day
month = st.number_input('Enter the month (e.g., 7 for July):', min_value=1, max_value=12, step=1)
day = st.number_input('Enter the day (e.g., 1 for 1st):', min_value=1, max_value=31, step=1)

# Button to trigger event retrieval
if st.button('Show Events'):
    events, births, deaths = get_historical_data(month, day)

    if events:
        st.subheader(f"Historical Events on {month}/{day}:")
        for event in events:
            st.write(f"Year: {event['year']}")
            st.write(f"Description: {event['text']}")
            if event['links']:
                st.write(f"Link: {event['links'][0]['link']}")
            st.divider()

    if births:
        st.subheader(f"Famous Births on {month}/{day}:")
        for birth in births:
            st.write(f"Year: {birth['year']}, Name: {birth['text']}")
            st.divider()

    if deaths:
        st.subheader(f"Famous Deaths on {month}/{day}:")
        for death in deaths:
            st.write(f"Year: {death['year']}, Name: {death['text']}")
            st.divider()