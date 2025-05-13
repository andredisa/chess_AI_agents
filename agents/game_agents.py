from autogen import ConversableAgent, register_function
from chess_logic.game_state import available_moves, execute_move, check_made_move
import streamlit as st
from chess_logic.board_utils import render_move_history

def setup_agents_and_play():
    try:
        white_cfg = [{"model": "gpt-4o-mini", "api_key": st.session_state.openai_api_key}]
        black_cfg = [{"model": "gpt-4o-mini", "api_key": st.session_state.openai_api_key}]

        agent_white = ConversableAgent("Agent_White",
            system_message="You play white. Call available_moves() then execute_move().",
            llm_config={"config_list": white_cfg, "cache_seed": None})

        agent_black = ConversableAgent("Agent_Black",
            system_message="You play black. Call available_moves() then execute_move().",
            llm_config={"config_list": black_cfg, "cache_seed": None})

        game_master = ConversableAgent("Game_Master", llm_config=False,
                                       is_termination_msg=check_made_move,
                                       default_auto_reply="Please make a move.",
                                       human_input_mode="NEVER")

        # Register tools
        for agent in [agent_white, agent_black]:
            register_function(execute_move, caller=agent, executor=game_master, name="execute_move", description="Make a move.")
            register_function(available_moves, caller=agent, executor=game_master, name="available_moves", description="Get legal moves.")

        # Trigger loop
        agent_white.register_nested_chats(trigger=agent_black, chat_queue=[{"sender": game_master, "recipient": agent_white, "summary_method": "last_msg"}])
        agent_black.register_nested_chats(trigger=agent_white, chat_queue=[{"sender": game_master, "recipient": agent_black, "summary_method": "last_msg"}])

        chat_result = agent_black.initiate_chat(
            recipient=agent_white,
            message="Let's play chess!",
            max_turns=st.session_state.max_turns,
            summary_method="reflection_with_llm"
        )

        st.markdown(chat_result.summary)
        render_move_history()

    except Exception as e:
        st.error(f"Error: {e}")
