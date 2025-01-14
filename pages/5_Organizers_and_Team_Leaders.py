import streamlit as st

st.title("Organizers & Team Leaders")

# Example of a two-column layout for organizers
col1, col2 = st.columns(2)

with col1:
    st.subheader("Test 1")
    st.write("**Institution**: Demo Center (Placeholder)")
    st.write("**Role**: Team Leader 1")
    st.write("**Email**: tleader1@example.com")

with col2:
    st.subheader("Test 2")
    st.write("**Institution**: Demo Center (Placeholder)")
    st.write("**Role**: Team Leader 2")
    st.write("**Email**: tleader2@example.com")
