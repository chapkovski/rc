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
from itertools import cycle
import itertools
import yaml
import json
import random
from pprint import pprint
from django.db import models as djmodels

author = ' Authors: Chapkovski, Mozolyuk. HSE-Moscow.'

doc = """
Cheating game and trust game together for the interregional project.
"""
fic_params = ['corruption', 'grp', 'pop_age', 'cpi']
fin_params = ['grp', 'pop_age', 'cpi']


def shuffler(params):
    c = params.copy()
    random.shuffle(c)
    return c


def gen_info(player):
    """generate infos to show"""
    res = []
    info = Constants.regions.copy()

    params = player.participant.vars.get('params')
    regions = player.participant.vars.get('regions')
    region_names = [r.get('name') for r in regions]
    for r_position, region in enumerate(regions):
        regionname = region.get('name')
        values = region.get('values')

        params_to_create = []
        for i_position, p in enumerate(params):
            t = dict(owner=player,
                     region=regionname,
                     region_position=r_position,
                     info=p,
                     info_label=values.get(p).get('label'),
                     info_description=values.get(p).get('description'),
                     info_position=i_position,
                     value=values.get(p).get('value')
                     )

            info_obj = Info(**t)
            res.append(info_obj)
    return dict(regions=region_names, infos=res, params=params)


class Constants(BaseConstants):
    name_in_url = 'cgtg'
    players_per_group = None
    num_rounds = 2
    apps = ['cg', 'tg']
    tg_coef = 3
    tg_endowment = 1
    tg_full = tg_coef * tg_endowment
    bonus_for_cg_belief = c(1)
    TRUST_CHOICES = [(0, '0$'), (tg_endowment, f'{tg_endowment}$')]
    TG_BELIEF_CHOICES = [(i / 10, f'{i / 10}$') for i in range(0, tg_full * 10, 1)]
    MAX_CQ_ATTEMPTS = 4
    formatter = lambda  x: 'раз' if x in [0] or x> 5 else 'раза'
    MAX_CQ_ATTEMPTS_formatted = f'{MAX_CQ_ATTEMPTS} {formatter(MAX_CQ_ATTEMPTS)}'
    expected_time = '20  минут'
    with open(r'./data/regions.yaml') as file:
        regions = yaml.load(file, Loader=yaml.FullLoader)


class Subsession(BaseSubsession):
    treatment = models.StringField()

    def creating_session(self):
        self.treatment = self.session.config.get('name')
        apps = itertools.cycle([Constants.apps.copy(), list(reversed(Constants.apps.copy()))])
        if self.round_number == 1:
            for p in self.session.get_participants():
                p.vars['regions'] = shuffler(Constants.regions)
                if self.treatment == 'fic':
                    params = fic_params
                else:
                    params = fin_params
                if self.treatment == 'return':
                    params = random.choice([fic_params, fin_params])
                p.vars['params'] = shuffler(params)
                p.vars['appseq'] = next(apps)
        infos = []
        for p in self.get_players():
            p.app = p.participant.vars['appseq'][p.round_number - 1]
            info = gen_info(p)
            infos.extend(info.get('infos'))
            p.r1_name, p.r2_name, p.r3_name = info.get('regions')
            p.params = json.dumps(info.get('params'))
        Info.objects.bulk_create(infos)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def role(self):
        if   self.subsession.treatment == 'return':
            return 'Б'
        else:
            return 'A'
    def get_regions(self):
        return [self.r1_name, self.r2_name, self.r3_name]

    def get_regional_data(self):
        regs = self.infos.all().order_by('region_position', 'info_position')
        res = []
        for r in self.get_regions():
            t = dict(name=r, info=regs.filter(region=r).values())
            res.append(t)
        return res

    params = models.StringField()
    app = models.StringField()
    r1_name = models.StringField()
    r2_name = models.StringField()
    r3_name = models.StringField()
    r1_cg_estimate = models.IntegerField(min=0, max=100)
    r2_cg_estimate = models.IntegerField(min=0, max=100)
    r3_cg_estimate = models.IntegerField(min=0, max=100)
    r1_trust = models.IntegerField(min=0, max=Constants.tg_endowment)
    r2_trust = models.IntegerField(min=0, max=Constants.tg_endowment)
    r3_trust = models.IntegerField(min=0, max=Constants.tg_endowment)
    r1_trust_return = models.IntegerField(min=0, max=Constants.tg_full)
    r2_trust_return = models.IntegerField(min=0, max=Constants.tg_full)
    r3_trust_return = models.IntegerField(min=0, max=Constants.tg_full)
    # TODO: think about slider for beliefs
    r1_trust_belief = models.FloatField(min=0, max=Constants.tg_full, )
    r2_trust_belief = models.FloatField(min=0, max=Constants.tg_full, )
    r3_trust_belief = models.FloatField(min=0, max=Constants.tg_full, )
    confirm_time = models.BooleanField(widget=widgets.CheckboxInput, label='Я понимаю, что расчет бонусов может занять вплоть до нескольких рабочих дней')
    confirm_block= models.BooleanField(widget=widgets.CheckboxInput,
                                       label=f'Я понимаю, что если я не смогу ответить на проверочные вопросы более чем {Constants.MAX_CQ_ATTEMPTS_formatted}, то не смогу принять дальнейшее участие в исследовании.')

class Info(djmodels.Model):
    owner = djmodels.ForeignKey(to=Player, on_delete=djmodels.CASCADE, related_name="infos")
    region = models.StringField()
    region_position = models.IntegerField()
    info = models.StringField()
    info_position = models.IntegerField()
    info_label = models.StringField()
    info_description = models.StringField()
    value = models.FloatField()
