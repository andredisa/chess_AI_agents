import streamlit as st
import chess.svg

def render_initial_board():
    st.subheader("Initial Board")
    st.image(chess.svg.board(st.session_state.board, size=300))

def render_move_history():
    st.subheader("Move History")
    for i, move_svg in enumerate(st.session_state.move_history):
        move_by = "Agent White" if i % 2 == 0 else "Agent Black"
        st.write(f"Move {i + 1} by {move_by}")
        st.image(move_svg)
