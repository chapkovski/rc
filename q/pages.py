from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants
import json

class Page(oTreePage):
    instructions = False

    def get_context_data(self, **context):
        r = super().get_context_data(**context)
        r['maxpages'] = self.participant._max_page_index
        r['page_index'] = self._index_in_pages
        r['progress'] = f'{int(self._index_in_pages / self.participant._max_page_index * 100):d}'
        r['instructions'] = self.instructions
        return r



class Risk(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('risk')
        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()


class RegionKnowledge(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('big5')
        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()
class Big5(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('big5')
        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()


class Demographics(Page):
    form_model = 'player'
    form_fields = ["religion",
                   "political",
                   "age",
                   "education",
                   "gender",
                   "marital",
                   "employment",
                   "income", ]


class Demand(Page):
    form_model = 'player'
    form_fields = ["demand", 'instructions_clarity']






class FinalForToloka(Page):

    def is_displayed(self):
        return self.player.session.config.get('for_toloka') and not self.player.blocked


page_sequence = [
    # Risk,
    # Big5,
    RegionKnowledge,
    # Demographics,
    # Demand,
    # FinalForToloka,

]
