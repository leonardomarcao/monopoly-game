from src.game import Game
from pprint import pprint
import statistics
from src.report import Report

MAX_GAME_SIMULATION = 300

if __name__ == "__main__":
    i = 0
    simulations = []
    # Run game simulation
    while i <= MAX_GAME_SIMULATION:
        simulations.append(Game().play())
        i += 1
    pprint(f"The mean of duration of lap is: {Report.get_mean_lap(simulations)}")
    pprint(f"The number of games that reached max lap is: {Report.get_reached_max_lap(simulations)}")
    pprint(f"The profile of player reccurent is: {Report.get_profile_player_reccurent(simulations)}")