from src.player import ImpulsivePlayer, SelectPlayer, WaryPlayer, RandomPlayer


class Report:
    @staticmethod
    def get_mean_lap(g: list):
        """Function to get mean duration of lap
        :param g: list of game instances
        :return:
        """
        mean = 0
        for i in g:
            mean += i.get("end_lap")
        return round(mean / len(g), 2)

    @staticmethod
    def get_reached_max_lap(g: list):
        """Function to get match was reached max lap
        :param g: list of game instances
        :return:
        """
        r = 0
        for x in g:
            if x.get("reached_max_lap") is True:
                r += 1
        return r

    @staticmethod
    def get_profile_player_reccurent(g: list):
        """Function to get profile of player reccurent
        :param g: list of game instances
        :return:
        """
        profiles = [ImpulsivePlayer, SelectPlayer, WaryPlayer, RandomPlayer]
        reccurent_percent = []
        res = {}
        # get list of player reccurent
        for d in g:
            res.setdefault(d["type_of_winner"], []).append(1)
        # get reccurent percent
        for p in profiles:
            reccurent_percent.append(
                {
                    "type of winner": p.__type__,
                    "percent": round(
                        sum(res[p.__type__]) / sum(sum(res.values(), [])) * 100, 2
                    ),
                }
            )
        return max(res, key=res.get), reccurent_percent
