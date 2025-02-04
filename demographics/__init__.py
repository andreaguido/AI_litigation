from cProfile import label

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
    age = models.IntegerField(label="¿Cuál es su edad actual? (Escriba la cifra de años)")
    gender = models.StringField(label="¿Cuál es su sexo? Seleccione una opción.",
                                 choices=[['Male','Hombre'],
                                          ['Female','Mujer'],
                                          ['Not disclosed','Prefiero no decirlo']],
                                widget=widgets.RadioSelectHorizontal)
    nationality = models.StringField(label="¿Qué nacionalidad tiene?")
    education = models.StringField(label="¿Cuál es el nivel máximo de estudios que ha completado? Seleccione una opción.",
                                   choices=[
                                       ['Educación primaria','Educación primaria'],
                                       ['Educación secundaria','Educación secundaria'],
                                       ['Bachillerato','Bachillerato'],
                                       ['Formación Profesional','Formación Profesional'],
                                       ['Educación universitaria grado/ licenciatura','Educación universitaria grado/ licenciatura'],
                                       ['Máster','Máster'],
                                       ['Doctorado','Doctorado']
                                   ])
    education_field = models.StringField(label="¿Qué campo de estudios universitarios tiene? Seleccione una opción.",
                                   choices=[
                                       ['Ninguno','Ninguno'],
                                       ['Derecho','Derecho'],
                                       ['Economía/ Empresa/ Gestión','Economía/ Empresa/ Gestión'],
                                       ['STEM (Ciencia, Tecnología, Ingeniería o Matemáticas)','STEM (Ciencia, Tecnología, Ingeniería o Matemáticas)'],
                                       ['Otro','Otro']
                                   ])
    experience_sector = models.StringField(label="¿En qué sector tiene experiencia profesional? Seleccione una opción.",
                                 choices= [["Ninguno", "Ninguno"], ["Público", "Público"],
                                           ["Privado", "Privado"],
                                           ['Público y Privado','Público y Privado']])
    experience_yrs = models.IntegerField(label="¿Cuántos años de experiencia profesional tiene? (escriba un número -redondeado sin decimales- desde 0 si no tiene experiencia en negociación hasta el número total de años que pueda tener). Por ejemplo: si son dos años y medio, escriba: 3.")


    pass


# PAGES

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'nationality', 'education', 'education_field', 'experience_sector', 'experience_yrs']


page_sequence = [Demographics]
