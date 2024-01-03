import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Multi App! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This framework is built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what data analysis and predictions!
    The app demonstrates bike rentals, bart stops and outbound flow of traffic.
"""
)