import random

# SETTINGS (edit these values to change game settings)
ESTATE_SALE_COST = (50, 200)
ESTATE_RENT_VALUE = (10, 50)


class Estate:
    def __init__(self):
        self.sale_cost = random.randint(ESTATE_SALE_COST[0], ESTATE_SALE_COST[1])
        self.rent_value = random.randint(ESTATE_RENT_VALUE[0], ESTATE_RENT_VALUE[1])
        self.has_owner = random.randint(0, 1)
        self.player_owner = None

    def set_player(self, hash_id: str):
        """Function to set player owner of estate
        :param hash_id: the hash id of player
        """
        self.player_owner = hash_id
        self.has_owner = True

    def unset_player(self):
        """Function to unset player owner of estate"""
        self.player_owner = None
        self.has_owner = False
