from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants


class Page(oTreePage):
    instructions = False

    def get_context_data(self, **context):
        r = super().get_context_data(**context)
        r['maxpages'] = self.participant._max_page_index
        r['page_index'] = self._index_in_pages
        r['progress'] = f'{int(self._index_in_pages / self.participant._max_page_index * 100):d}'
        r['instructions'] = self.instructions
        return r


class AppPage(Page):
    app = None

    def _is_displayed(self):
        return self.player.app == self.app


class FirstPage(Page):
    app = None

    def is_displayed(self):
        return self.round_number == 1


class Consent(FirstPage):
    pass


class GeneralInstructions(FirstPage):
    pass


class RegionalInfoChoose(FirstPage):
    def is_displayed(self):
        return self.session.config.get('endo', False)


class RegionalInfoFixed(FirstPage):
    pass




class CGInstructions(AppPage):
    app = 'cg'


class CGquiz(AppPage):
    app = 'cg'


class CGdecision(AppPage):
    app = 'cg'


class CGBeliefsInstructions(AppPage):
    app = 'cg'


class CGBeliefsquiz(AppPage):
    app = 'cg'


class CGBeliefDecision(AppPage):
    app = 'cg'
    form_model = 'player'
    form_fields = ['r1_cg_estimate', 'r2_cg_estimate', 'r3_cg_estimate']

    def vars_for_template(self):
        form = self.get_form()
        return dict(data_to_show=zip(self.player.get_regional_data(), form))

class Part2Announcement(Page):
    def is_displayed(self):
        return self.round_number == 2


class TGInstructions(AppPage):
    app = 'tg'


class TGQuiz(AppPage):
    app = 'tg'


class TGRoleAnnouncement(AppPage):
    app = 'tg'


class TGDecision(AppPage):
    app = 'tg'
    form_model = 'player'
    form_fields = ['r1_trust', 'r2_trust', 'r3_trust']

    def vars_for_template(self):
        form = self.get_form()
        return dict(data_to_show=zip(self.player.get_regional_data(), form))
class TGBeliefs(AppPage):
    app = 'tg'
    form_model = 'player'
    form_fields = ['r1_trust_belief', 'r2_trust_belief', 'r3_trust_belief']

    def vars_for_template(self):
        form = self.get_form()
        return dict(data_to_show=zip(self.player.get_regional_data(), form))


page_sequence = [
    # Consent,
    # GeneralInstructions,
    # RegionalInfoChoose,
    # RegionalInfoFixed,
    # CGInstructions,

    # CGdecision,
    # CGBeliefsInstructions,
    # CGBeliefsquiz,
    CGBeliefDecision,
    # Part2Announcement,
    # TGInstructions,
    # TGQuiz,
    # TGRoleAnnouncement,
    TGDecision,
    TGBeliefs,
]
