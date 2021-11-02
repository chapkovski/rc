from otree.api import *
import yaml
from pprint import pprint


class Constants(BaseConstants):
    name_in_url = 'polar'
    players_per_group = None
    num_rounds = 2
    apps = ['cg', 'tg']
    with open(r'./data/regions.yaml') as file:
        regions = yaml.load(file, Loader=yaml.FullLoader)
