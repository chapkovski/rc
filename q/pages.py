from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants
import json


class Page(oTreePage):
    instructions = False

    def _is_displayed(self):
        return not self.participant.vars.get('blocked') and self.is_displayed()

    def get_context_data(self, **context):
        r = super().get_context_data(**context)
        r['maxpages'] = self.participant._max_page_index
        r['page_index'] = self._index_in_pages
        r['progress'] = f'{int(self._index_in_pages / self.participant._max_page_index * 100):d}'
        r['instructions'] = self.instructions
        return r


class Demand(Page):
    form_model = 'player'
    form_fields = ["demand", 'instructions_clarity']


class Risk(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('risk')
        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()


class RegionKnowledge(Page):

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('region_knowledge')

        if data:
            for k, v in data.items():
                fs = v.get('col1')
                for f in fs:
                    full_field = f'knowledge_{k}_{f}'
                    setattr(self.player, full_field, True)
        return super().post()


class WVSCorr(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder'))
        if data:
            for k, v in data.items():
                setattr(self.player, k, v)
        return super().post()


class WVSJustifiability(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('wvs_just')

        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('just'))
        return super().post()


class TrustNRisk(Page):

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder'))
        print(data)
        if data:
            for k, v in data.items():
                setattr(self.player, k, v)
        return super().post()


class Demographics(Page):
    form_model = 'player'
    form_fields = [
        "age",
        "education",
        "gender",
        "marital",
        "employment",
        "income",
    ]

    def before_next_page(self):
        self.player.payable = True
        self.participant.vars['payable_status'] = True


class FinalForToloka(Page):
    def is_displayed(self):
        return self.player.session.config.get('for_toloka') and not self.participant.vars.get('blocked')


page_sequence = [
    Demand,
    RegionKnowledge,
    WVSCorr,
    WVSJustifiability,
    TrustNRisk,
    Demographics,
    FinalForToloka,
]
