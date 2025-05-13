import chess
import chess.svg
import streamlit as st

def available_moves():
    return "Available moves are: " + ",".join(str(m) for m in st.session_state.board.legal_moves)

def execute_move(move: str) -> str:
    try:
        move_obj = chess.Move.from_uci(move)
        if move_obj not in st.session_state.board.legal_moves:
            return f"Invalid move: {move}. Try available_moves()."

        st.session_state.board.push(move_obj)
        st.session_state.made_move = True
        svg = chess.svg.board(st.session_state.board,
                              arrows=[(move_obj.from_square, move_obj.to_square)],
                              fill={move_obj.from_square: "gray"},
                              size=400)
        st.session_state.board_svg = svg
        st.session_state.move_history.append(svg)

        piece = st.session_state.board.piece_at(move_obj.to_square)
        name = chess.piece_name(piece.piece_type)
        from_sq = chess.SQUARE_NAMES[move_obj.from_square]
        to_sq = chess.SQUARE_NAMES[move_obj.to_square]
        desc = f"Moved {name} from {from_sq} to {to_sq}."

        if st.session_state.board.is_checkmate():
            desc += f"\nCheckmate! {'White' if st.session_state.board.turn == chess.BLACK else 'Black'} wins!"
        elif st.session_state.board.is_stalemate():
            desc += "\nStalemate!"
        elif st.session_state.board.is_insufficient_material():
            desc += "\nDraw - Insufficient material!"
        elif st.session_state.board.is_check():
            desc += "\nCheck!"

        return desc
    except Exception:
        return "Invalid move format. Use UCI (e.g., e2e4)."

def check_made_move(_msg):
    if st.session_state.made_move:
        st.session_state.made_move = False
        return True
    return False
