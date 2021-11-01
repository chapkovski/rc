from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Corr'
    players_per_group = None
    num_rounds = 1


class Player(BasePlayer):
    pass


