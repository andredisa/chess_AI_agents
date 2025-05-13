import streamlit as st
from ui.sidebar import configure_sidebar
from utils.session import init_session_state
from chess_logic.board_utils import render_initial_board, render_move_history
from agents.game_agents import setup_agents_and_play

st.set_page_config(page_title="Chess with AutoGen Agents", layout="centered")
init_session_state()
configure_sidebar()

st.title("Chess with AutoGen Agents")
render_initial_board()

if st.button("Start Game"):
    setup_agents_and_play()

if st.button("Reset Game"):
    st.session_state.board.reset()
    st.session_state.made_move = False
    st.session_state.move_history = []
    st.session_state.board_svg = None
    st.success("Game reset! Click 'Start Game' to play again.")
