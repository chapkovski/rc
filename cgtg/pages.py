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
        return self.player.app == self.app and self.is_displayed()


class FirstPage(Page):
    app = None

    def is_displayed(self):
        return self.round_number == 1


class Consent(FirstPage):
    pass


class GeneralRules(FirstPage):
    form_model = 'player'
    form_fields = ['confirm_time', 'confirm_block']


class GeneralInstructions(FirstPage):
    pass


class RegionalInfoChoose(FirstPage):

    def is_displayed(self):
        return self.session.config.get('endo', False) and super().is_displayed()

    def post(self):
        self.object = self.get_object()
        data = self.request.POST.dict()
        form = self.get_form(data=data, files=self.request.FILES, instance=self.object)
        data.pop('csrfmiddlewaretoken')
        if len(data.items()) != 3:
            form.add_error(None, 'Выберите ровно 3 параметра')
            return self.form_invalid(form)
        names = data.keys()
        infos_to_update = self.player.infos.filter(name__in=names).update(to_show=True)
        return super().post()


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


class TGReturnDecision(AppPage):
    app = 'tg'

    def is_displayed(self):
        return self.subsession.treatment == 'return'

    form_model = 'player'
    form_fields = ['r1_trust_return', 'r2_trust_return', 'r3_trust_return']

    def vars_for_template(self):
        form = self.get_form()
        return dict(data_to_show=zip(self.player.get_regional_data(), form))


class TGDecision(AppPage):
    app = 'tg'
    form_model = 'player'
    form_fields = ['r1_trust', 'r2_trust', 'r3_trust']

    def is_displayed(self):
        return not self.subsession.treatment == 'return'

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
    # Part2Announcement,
    # Consent,
    # GeneralRules,
    #
    # GeneralInstructions,
    RegionalInfoChoose,
    # RegionalInfoFixed,
    # CGInstructions,
    #
    # CGdecision,
    # CGBeliefsInstructions,
    # CGBeliefsquiz,
    # CGBeliefDecision,
    #
    # TGInstructions,
    # TGQuiz,
    # TGRoleAnnouncement,
    # TGDecision,
    # TGBeliefs,
    # TGReturnDecision
]
