import chess
from config.settings import DEFAULT_MAX_TURNS
import streamlit as st

def init_session_state():
    if "openai_api_key" not in st.session_state:
        st.session_state.openai_api_key = None
    if "board" not in st.session_state:
        st.session_state.board = chess.Board()
    if "made_move" not in st.session_state:
        st.session_state.made_move = False
    if "board_svg" not in st.session_state:
        st.session_state.board_svg = None
    if "move_history" not in st.session_state:
        st.session_state.move_history = []
    if "max_turns" not in st.session_state:
        st.session_state.max_turns = DEFAULT_MAX_TURNS
