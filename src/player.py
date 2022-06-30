import random
import uuid
from src.estate import Estate


class Player:
    __type__ = "default"

    def __init__(self):
        self.hash_id = uuid.uuid4().hex
        self.account_balance = 300
        self.board_position = 0
        self.active = True

    def move(self, walk_distance: int):
        """Move player to next position
        :param walk_distance: the distance player has moved
        """
        self.board_position += walk_distance

    def buy_estate(self, estate: Estate):
        """Buy estate if possible
        :param estate: the estate instance
        """
        estate.set_player(self.hash_id)
        self.decrease_account_balance(estate.sale_cost)

    def pay_rent(self, estate: Estate):
        """Pay rent to estate owner
        :param estate: the estate instance
        """
        if estate.has_owner:
            self.decrease_account_balance(estate.rent_value)

    def decrease_account_balance(self, value: int):
        """Decrease account balance
        :param value: the value to decrease
        """
        self.account_balance -= value

    def increase_account_balance(self, value: int):
        """Increase account balance
        :param value: the value to increase
        """
        self.account_balance += value

    def set_status(self, status: bool):
        """Set player status
        :param status: the status to set
        """
        self.active = status


class ImpulsivePlayer(Player):
    __type__ = "impulsive player"

    def buy_estate(self, estate: Estate):
        if not estate.has_owner:
            super().buy_estate(estate)


class SelectPlayer(Player):
    __type__ = "select player"

    def buy_estate(self, estate: Estate):
        if not estate.has_owner and estate.sale_cost >= 50:
            super().buy_estate(estate)


class WaryPlayer(Player):
    __type__ = "wary player"

    def buy_estate(self, estate: Estate):
        if not estate.has_owner and (self.account_balance - estate.sale_cost) >= 80:
            super().buy_estate(estate)


class RandomPlayer(Player):
    __type__ = "random player"

    def buy_estate(self, estate: Estate):
        if not estate.has_owner and random.randrange(2):
            super().buy_estate(estate)
