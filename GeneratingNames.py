import streamlit as st
from faker import Faker

fake = Faker()

# name = fake.name()
# print(name)

def generate_names(number_of_names):
    names = []
    for i in range(number_of_names):
        name = fake.name()
        names.append(name)
    return names

names = generate_names(10)
# print(names)

st.title("Random Name generator")

num_names = st.number_input("Enter the number of names to generate:",
                            min_value=1, max_value=1000, value=5, step=1)

button = st.button("Generate Names")

if button:
    names = generate_names(num_names)
    st.subheader("Generated Names")
    for name in names:
        st.write(name)