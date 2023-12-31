import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number Among Three")

    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")

    if st.button("Find Largest Number"):
        largest_number = find_largest_number(a, b, c)
        st.success(f"The largest number is: {largest_number}")
if __name__ == "__main__":
    main()
