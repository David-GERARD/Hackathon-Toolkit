import streamlit as st

# Title
st.title("<Hackathon>")

# Text field
user_input = st.text_input("Enter some text:")

# Button
if st.button("Submit"):
    st.write(f"You entered: {user_input}")

# PDF Dragging Function
uploaded_file = st.file_uploader("Drag and drop your PDF here:", type=["pdf"])

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")
    # Optional: Display the PDF name or handle it further
    with open(f"uploaded_{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())
        st.write(f"Saved as uploaded_{uploaded_file.name}")
