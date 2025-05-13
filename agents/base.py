"""
base.py

This module defines an abstract base class for chess agents.
It serves as a common interface for all types of agents (e.g., AI agents, random agents, human agents).
The goal is to provide a consistent and reusable structure for extending agent behavior.

All concrete agents should inherit from the BaseAgent class and implement the `get_move` method.
"""

from abc import ABC, abstractmethod
import chess

class BaseAgent(ABC):
    def __init__(self, name: str):
        """
        Initialize the agent with a given name.
        """
        self.name = name

    @abstractmethod
    def get_move(self, board: chess.Board) -> chess.Move:
        """
        Given the current board state, return a valid move.

        Args:
            board (chess.Board): The current chess board object.

        Returns:
            chess.Move: The move selected by the agent.
        """
        pass

    def __str__(self):
        return f"<Agent: {self.name}>"
