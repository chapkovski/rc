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
# from .widgets import OtherRadioSelect
from django.utils.translation import gettext_lazy as _

from .widgets import LikertWidget

doc = """
 Regional corruption. 
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1
    HARD_TO_SAY_CHOICE = [999, _('Предпочиатаю не указывать')]

    GENDER_CHOICES = [
        [0, _('Мужской')],
        [1, _('Женский')],
        HARD_TO_SAY_CHOICE
    ]

    Heads = [
        [1, _('Орел')],
        [0, 'Решка'],
    ]

    Control_quest = [
        [1, _('$0')],
        [2, _('$0.30')],
        [3, _('$0.50')],
        [4, _('$0.90')],
        [5, _('$1.50')],
    ]

    Education = [
        [1, _('Неполное среднее')],
        [2, _('Полное среднее')],
        [3, _('Среднее специальное')],
        [4, _('Бакалавр')],
        [5, _('Специалист')],
        [6, _('Магистр')],
        [7, _('Кандидат/Доктор наук')],
        HARD_TO_SAY_CHOICE
    ]

    Income = [
        [1, _('Еле хватает на самое необходимое')],
        [2, _('Хватает только на самое необходимое')],
        [3, _('Могу удовлетворить часть своих потребностей в одежде и развлечениях')],
        [4, _('Нет необходимости экономить')],
        HARD_TO_SAY_CHOICE
    ]

    Employed = [
        [1, _('Да')],
        [0, _('Нет')],
        HARD_TO_SAY_CHOICE
    ]
    Clarity = [
        [1, _('1')],
        [2, _('2')],
        [3, _('3')],
        [4, _('4')],
        [5, _('5')],
    ]


Heads = models.IntegerField(label=_(
    'Что Вам выпало?'),
    choices=Constants.Heads, widget=widgets.RadioSelect)

cq_1 = models.IntegerField(label=_(
    'Если Вы ничего не посылете Участнику Б, тогда какую максимальную сумму он может Вам вернуть?'),
    choices=Constants.Heads, widget=widgets.RadioSelect)

cq_2 = models.IntegerField(label=_(
    'Если Вы посылете Участнику Б $0.30, тогда какую максимальную сумму он может Вам вернуть?'),
    choices=Constants.Heads, widget=widgets.RadioSelect)

cq_3 = models.IntegerField(label=_(
    'Если Вы посылете Участнику Б $0.50, тогда какую максимальную сумму он может Вам вернуть?'),
    choices=Constants.Heads, widget=widgets.RadioSelect, )

Gender = models.IntegerField(label=_(
    'Укажите Ваш пол'),
    choices=Constants.GENDER_CHOICES, widget=widgets.RadioSelect)

Age = models.IntegerField(label=_(
    'Укажите Ваш возраст:'),
)

Education = models.IntegerField(label=_(
    'Какую высшую ступень образования Вы имеете на данный момент?'),
    choices=Constants.Education, widget=widgets.RadioSelect)

Income = models.IntegerField(label=_(
    'Оцените Ваш уровень дохода:'),
    choices=Constants.Income, widget=widgets.RadioSelect)

Employed = models.IntegerField(label=_(
    'Трудоустроены ли Вы в данный момент?'),
    choices=Constants.Employed, widget=widgets.RadioSelect)

Inst_clarity = models.IntegerField(label=_(
    'Пожалуйста, оцените, насколько Вам были понятны инструкции к заданию по шкале от 1 до 5, где 1 - совсем непонятно, а 5 - все понятно:'),
    choices=Constants.Clarity, widget=widgets.RadioSelect)

Comments = models.TextField(label=_(
    'Пожалуйста, укажите Ваши комментарии по поводу исследования. Мы будем Вам очень признательны за любые Ваши замечания:'))
