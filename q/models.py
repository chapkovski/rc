from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)



author = ' Authors: Chapkovski, Mozolyuk. HSE-Moscow.'

doc = """
Post experimental questionnaire for the interregional project.
"""


class Constants(BaseConstants):
    name_in_url = 'q'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # knowledge block
    knowledge_arkhangelsk_live_in = models.BooleanField()
    knowledge_arkhangelsk_family = models.BooleanField()
    knowledge_arkhangelsk_press = models.BooleanField()
    knowledge_arkhangelsk_network = models.BooleanField()
    knowledge_arkhangelsk_other = models.BooleanField()
    knowledge_arkhangelsk_none = models.BooleanField()
    knowledge_moscow_live_in = models.BooleanField()
    knowledge_moscow_family = models.BooleanField()
    knowledge_moscow_press = models.BooleanField()
    knowledge_moscow_network = models.BooleanField()
    knowledge_moscow_other = models.BooleanField()
    knowledge_moscow_none = models.BooleanField()
    knowledge_voronezh_live_in = models.BooleanField()
    knowledge_voronezh_family = models.BooleanField()
    knowledge_voronezh_press = models.BooleanField()
    knowledge_voronezh_network = models.BooleanField()
    knowledge_voronezh_other = models.BooleanField()
    knowledge_voronezh_none = models.BooleanField()




    # end of knowledge block
