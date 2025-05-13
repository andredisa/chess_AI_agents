import streamlit as st

def configure_sidebar():
    st.sidebar.title("Chess Agent Configuration")
    api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
    if api_key:
        st.session_state.openai_api_key = api_key
        st.sidebar.success("API key saved!")

    st.sidebar.info("""
Using more than 200 turns is costly and slow. For demos, 5-10 turns are ideal.
""")

    max_turns_input = st.sidebar.number_input(
        "Number of turns:",
        min_value=1,
        max_value=1000,
        value=st.session_state.max_turns,
        step=1
    )
    st.session_state.max_turns = max_turns_input
