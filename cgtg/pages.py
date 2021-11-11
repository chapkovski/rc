from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants, Info


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

        infos_to_update = Info.objects.filter(owner__participant=self.participant, name__in=names).update(to_show=True)
        return super().post()


class RegionalInfoFixed(FirstPage):
    def is_displayed(self):
        return self.subsession.treatment != 'return' and super().is_displayed()


class CGAnnouncement(AppPage):
    app = 'cg'


class CGInstructions(AppPage):
    app = 'cg'


class CGdecision(AppPage):
    app = 'cg'
    form_model = 'player'
    form_fields = ['cg_decision']


class CGBeliefsInstructions(AppPage):
    def is_displayed(self):
        return self.subsession.treatment != 'return' and super().is_displayed()

    app = 'cg'


class CGBeliefsquiz(AppPage):
    def is_displayed(self):
        return self.subsession.treatment != 'return' and super().is_displayed()

    app = 'cg'
    form_model = 'player'
    form_fields = [
        'cq_cg_belief_1',
        'cq_cg_belief_2',
        'cq_cg_belief_3',
        'cq_cg_belief_4']

    def vars_for_template(self):
        return dict(attempts=Constants.MAX_CQ_ATTEMPTS - self.player.cq_cg_err_counter)

    def form_invalid(self, form):
        self.player.cq_cg_err_counter += 1
        if self.player.cq_cg_err_counter > Constants.MAX_CQ_ATTEMPTS:
            self.player.blocked = True
            return
        return super().form_invalid(form)


class CGBeliefDecision(AppPage):
    app = 'cg'
    form_model = 'player'
    form_fields = ['r1_cg_estimate', 'r2_cg_estimate', 'r3_cg_estimate']
    def is_displayed(self):
        return self.subsession.treatment!='return' and super().is_displayed()

    def vars_for_template(self):
        form = self.get_form()
        fdata = []
        for i, f in enumerate(form, start=1):
            regname = getattr(self.player, f'r{i}_name')
            label = f'Из 100 участников из региона {regname} сколько назовут "Орел"?'
            t = {'field': f,
                 'label': label}
            fdata.append(t)

        return dict(data_to_show=zip(self.player.get_regional_data(), fdata))


class Part1Announcement(Page):
    def is_displayed(self):
        return self.round_number == 1
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
    form_fields = ['trust_return']




class TGDecision(AppPage):
    app = 'tg'
    form_model = 'player'
    form_fields = ['r1_trust', 'r2_trust', 'r3_trust']

    def is_displayed(self):
        return not self.subsession.treatment == 'return'

    def vars_for_template(self):
        form = self.get_form()
        fdata = []
        for i, f in enumerate(form, start=1):
            regname = getattr(self.player, f'r{i}_name')
            label = f'Сколько центов из 100 вы пошлете участнику Б, если он окажется из региона: {regname}?'
            t = {'field': f,
                 'label': label}
            fdata.append(t)

        return dict(data_to_show=zip(self.player.get_regional_data(), fdata))


page_sequence = [

    Consent,
    GeneralRules,

    Part1Announcement,
Part2Announcement,
    CGInstructions,
    CGdecision,
    CGBeliefsInstructions,
    CGBeliefsquiz,
    TGInstructions,
    TGQuiz,
    TGRoleAnnouncement,
    RegionalInfoChoose,
    CGBeliefDecision,
    TGDecision,
    TGReturnDecision
]
