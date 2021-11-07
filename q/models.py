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
from .choices import choices
author = ' Authors: Chapkovski, Mozolyuk. HSE-Moscow.'

doc = """
Post experimental questionnaire for the interregional project.
"""


class Constants(BaseConstants):
    name_in_url = 'q'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # knowledge block
    knowledge_arkhangelsk_live_in = models.BooleanField()
    knowledge_arkhangelsk_family = models.BooleanField()
    knowledge_arkhangelsk_press = models.BooleanField()
    knowledge_arkhangelsk_network = models.BooleanField()
    knowledge_arkhangelsk_other = models.BooleanField()
    knowledge_arkhangelsk_none = models.BooleanField()
    knowledge_moscow_live_in = models.BooleanField()
    knowledge_moscow_family = models.BooleanField()
    knowledge_moscow_press = models.BooleanField()
    knowledge_moscow_network = models.BooleanField()
    knowledge_moscow_other = models.BooleanField()
    knowledge_moscow_none = models.BooleanField()
    knowledge_voronezh_live_in = models.BooleanField()
    knowledge_voronezh_family = models.BooleanField()
    knowledge_voronezh_press = models.BooleanField()
    knowledge_voronezh_network = models.BooleanField()
    knowledge_voronezh_other = models.BooleanField()
    knowledge_voronezh_none = models.BooleanField()
    # end of knowledge block
    #     WVS corruption block
    wvs_q112 = models.IntegerField()
    # """112.
    #     1 2 3 4 5 6 7 8 9 10
    #     Совсем нет Коррупция
    #     коррупции в России
    #     повсеместна"""
    #
    # wvs_q118 = models.IntegerField(label="""
    #  Как часто, по Вашему опыту, обычные люди вроде Вас или живущие с Вами по
    #     соседству вынуждены давать взятки, дарить подарки или делать одолжения другим для того, чтобы были
    #     решены их вопросы или оказаны услуги, на которые они и так имеют право?
    # """,
    #                                choices=choices.WVS_Q118)
    #
    # wvs_q120= models.IntegerField()
    # """
    # 20. Как Вы считаете, насколько велик в нашей стране риск быть привлеченным к ответственности за дачу
    # или получение взятки, подарка или одолжения, чтобы получить государственные услуги? Дайте ответ по
    # шкале от 1 до 10, где 1 означает "совсем никакого риска", а 10 - "риск очень велик". Вы можете выбрать любое
    # значение шкалы в соответствии с Вашим собственным мнением.
    # 1 2 3 4 5 6 7 8 9 10
    # Совсем Риск
    # никакого риска очень велик
    # """
    # """q177-181"""
    # """
    # Теперь я буду называть Вам различные действия, а Вы, используя шкалу на карточке, скажите мне, в какой
    # степени это действие, на Ваш взгляд, может быть оправдано? «10» означает, что оно может быть оправдано
    # всегда, а «1» - никогда не может быть оправдано. Вы также можете выбрать любую цифру между этими
    # оценками. Итак, может ли, по Вашему мнению, быть оправдано и в какой степени? /
    # """
