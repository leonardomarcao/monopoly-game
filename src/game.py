import uuid
import random
from src.estate import Estate
from src.player import Player, ImpulsivePlayer, SelectPlayer, WaryPlayer, RandomPlayer


# SETTINGS (edit these values to change game settings)
BOARD_NUMBER = 20
DICE_NUMBER = 6
INCREASE_ACCOUNT_BALANCE_LAP = 100
GAME_MAX_LAP = 1000


class Game:
    def __init__(self):
        self.hash_id = uuid.uuid4().hex
        self.board = [Estate() for _ in range(BOARD_NUMBER)]
        self.players = [ImpulsivePlayer(), SelectPlayer(), WaryPlayer(), RandomPlayer()]
        self.lap = 0
        self.winner: Player = None

    @staticmethod
    def play_dice():
        """Dice random choice face
        :return int: dice random choice face
        """
        return random.randint(1, DICE_NUMBER)

    @staticmethod
    def check_board_lap(player: Player, walk_distance: int):
        """
        Check if any player is on board lap
        :param player: the player instance
        :param walk_distance: the distance player has moved
        :return:
        """
        if player.board_position + walk_distance >= BOARD_NUMBER:
            player.board_position = player.board_position + walk_distance - BOARD_NUMBER
            player.increase_account_balance(INCREASE_ACCOUNT_BALANCE_LAP)
            return True
        return False

    def check_account_balance(self, player: Player):
        """Check account balance of player
        :param player: the player instance
        """
        if player.account_balance <= 0:
            # if player has no account balance, he is out of the game
            player.set_status(False)
            # remove player from estate owner
            for estate in self.board:
                if estate.player_owner == player.hash_id:
                    estate.unset_player()

    def check_winner(self):
        """Get winner of game based on rules
        1. Rule 1: if game hit max lap, then winner is the player with highes't account balance
        2. Rule 2: if game left only one active player, then winner is that player
        """
        # check winner if game lap hit max lap
        if self.lap == GAME_MAX_LAP:
            # order players by account balance (descending)
            self.players.sort(key=lambda x: x.account_balance, reverse=True)
            self.winner = self.players[0]
        # check winner if left only one player with status active
        active_players = [player for player in self.players if player.active]
        if len(active_players) == 1:
            self.winner = active_players[0]

    def next_lap(self):
        """
        Set game lap
        :return:
        """
        self.lap += 1

    def get_summary(self):
        """
        Get summary of game
        :return:
        """
        return {
            "type_of_winner": self.winner.__type__,
            "reached_max_lap": True if self.lap == GAME_MAX_LAP else False,
            "end_lap": self.lap,
        }

    def play(self):
        """
        Steps:
            - Shuffle players for random choices
            - Make move player using dice random choice face
            - If player is on board, check if it has owner:
                - If it has owner, pay rent
                - If not, then buy estate (if possible)
        :return: the summary of game
        """
        # first lap
        self.lap = 1
        while self.lap <= GAME_MAX_LAP:
            random.shuffle(self.players)
            for player in self.players:
                # get dice random choice face
                dice_choice = self.play_dice()
                # check board lap
                if not self.check_board_lap(player, dice_choice):
                    # make move player using dice random choice face
                    player.move(dice_choice)
                # if player is on board, check if it has owner then pay rent
                player.pay_rent(self.board[player.board_position])
                # if player is on board, check if it has owner then buy estate (if possible)
                player.buy_estate(self.board[player.board_position])
                # check account balance
                self.check_account_balance(player)
                # check winner
                self.check_winner()
                if self.winner:
                    return self.get_summary()
            # next lap
            self.next_lap()
