from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants
import json
from pprint import pprint


class Page(oTreePage):
    def title(self):
        return self.__class__.__name__

    template_name = ''
    form_model = 'player'


class Introduction(Page):
    pass


class Part_1(Page):
    form_fields = [
        "Heads",
    ]


class Part_2_Inst_corr(Page):
    pass


class Control_questions(Page):
    form_fields = [
        "cq_1",
        "cq_2",
        "cq_3",
    ]


class Questionnaire(Page):
    form_fields = [
        "Gender",
        "Age",
        "Education",
        "Income",
        "Employed",
        "Inst_clarity",
        "Comments",
    ]


page_sequence = [
    Introduction,
    Part_1,
    Part_2_Inst_corr,
    Control_questions,
    Questionnaire,

]
