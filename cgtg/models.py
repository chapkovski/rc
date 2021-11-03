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
Cheating game and trust game together for the interregional project.
"""


class Constants(BaseConstants):
    name_in_url = 'cgtg'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    treatment = models.StringField()
    def creating_session(subsession):
        subsession.treatment = subsession.session.config.get('name')
        apps = itertools.cycle([Constants.apps.copy(), list(reversed(Constants.apps.copy()))])
        for p in subsession.session.get_participants():
            p.vars['appseq'] = next(apps)
        for p in subsession.get_players():
            p.app = p.participant.vars['appseq'][p.round_number - 1]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    app = models.StringField()
