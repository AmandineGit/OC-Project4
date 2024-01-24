""" Entry point."""

from controllers.base import Controllers
from models.tournament import Tournament

#tournament = Tournament.current_tournament()
Controllers.main_menu()
#Controllers.create_pairs(tournament, 5)
