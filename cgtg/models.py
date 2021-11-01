from otree.api import *
from .choices import *
from .constants import Constants
import json
import itertools
import random
from math import copysign

# TODO: remove proportions from methods
# TODO: write down the logic of treatment
# TODO: what to do with recipieints?
f = lambda x: f'{(x / 100):.2f}$'


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

