from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # demographics
    age = models.IntegerField(label="¿Cuál es su edad actual? (Escriba un número, por ejemplo: 27)")
    gender = models.StringField(label="¿Cuál es su sexo? Seleccione una opción.",
                                 choices=[['Male','Hombre'],
                                          ['Female','Mujer'],
                                          ['Not disclosed','Prefiero no decirlo']],
                                widget=widgets.RadioSelectHorizontal)

    pass


# PAGES

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']



page_sequence = [Demographics]
