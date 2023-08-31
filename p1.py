import streamlit as st

def find_largest_number(numbers):
    return max(numbers)

st.title("Largest Number Finder")

number_count = 3
numbers = []

for i in range(number_count):
    number = st.number_input(f"Enter number {i+1}:")
    numbers.append(number)

if st.button("Find Largest"):
    largest = find_largest_number(numbers)
    st.write(f"The largest number is: {largest}")