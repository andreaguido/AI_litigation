import random
import numbers

from otree.api import *


doc = """
Production and negotiation game 
"""


class Constants(BaseConstants):
    name_in_url = 'AI'
    players_per_group = 2
    num_rounds = 5
    endowment = 20


    ## P1
    task_1_costs_P1 = [
        dict(cost=round(0.99/2*100,1), labels = "A", task=1), #
        dict(cost=round(0.93/2*100,1), labels = "B", task=1),
        dict(cost=round(0.87/2*100,0), labels = "C", task=1),
        dict(cost=round(0.81/2*100,0), labels = "D", task=1),
        dict(cost=round(0.75/2*100,0), labels = "E", task=1), #
        dict(cost=round(0.69/2*100,0), labels = "F", task=1),
        dict(cost=round(0.63/2*100,0), labels = "G", task=1),
        dict(cost=round(0.57/2*100,0), labels = "H", task=1),
        dict(cost=round(0.51/2*100,0), labels = "I", task=1)
    ]
    task_2_costs_P1 = [
        dict(cost=round(0.51/2*100, 1), labels = "A", task=2), #
        dict(cost=round(0.53/2*100, 1), labels = "B", task=2),
        dict(cost=round(0.55/2*100, 0), labels = "C", task=2),
        dict(cost=round(0.57/2*100, 0), labels = "D", task=2),
        dict(cost=round(0.59/2*100, 0), labels = "E", task=2), #
        dict(cost=round(0.61/2*100, 0), labels = "F", task=2),
        dict(cost=round(0.63/2*100, 0), labels = "G", task=2),
        dict(cost=round(0.65/2*100, 0), labels = "H", task=2),
        dict(cost=round(0.67/2*100, 0), labels = "I", task=2)
    ]
    task_3_costs_P1 = [
        dict(cost=round(0.99/2*100, 0), labels = "A", task=3),
        dict(cost=round(0.91/2*100, 0), labels = "B", task=3),
        dict(cost=round(0.83/2*100, 0), labels = "C", task=3),
        dict(cost=round(0.75/2*100, 0), labels = "D", task=3),
        dict(cost=round(0.67/2*100, 0), labels = "E", task=3), #
        dict(cost=round(0.59/2*100, 0), labels = "F", task=3),
        dict(cost=round(0.51/2*100, 0), labels = "G", task=3),
        dict(cost=round(0.43/2*100, 0), labels = "H", task=3),
        dict(cost=round(0.35/2*100, 0), labels = "I", task=3)
    ]
    task_4_costs_P1 = [
        dict(cost=round(0.99/2*100, 0), labels = "A", task=4),
        dict(cost=round(0.93/2*100, 0), labels = "B", task=4),
        dict(cost=round(0.87/2*100, 0), labels = "C", task=4),
        dict(cost=round(0.81/2*100, 0), labels = "D", task=4),
        dict(cost=round(0.75/2*100, 0), labels = "E", task=4), #
        dict(cost=round(0.69/2*100, 0), labels = "F", task=4),
        dict(cost=round(0.63/2*100, 0), labels = "G", task=4),
        dict(cost=round(0.57/2*100, 0), labels = "H", task=4),
        dict(cost=round(0.51/2*100, 0), labels = "I", task=4)
    ]

    ## P2
    task_1_costs_P2 = [
        dict(cost=round(0.51/2*100, 1), labels = "A", task=1), #
        dict(cost=round(0.53/2*100, 1), labels = "B", task=1),
        dict(cost=round(0.55/2*100, 0), labels = "C", task=1),
        dict(cost=round(0.57/2*100, 0), labels = "D", task=1),
        dict(cost=round(0.59/2*100, 0), labels = "E", task=1), #
        dict(cost=round(0.61/2*100, 0), labels = "F", task=1),
        dict(cost=round(0.63/2*100, 0), labels = "G", task=1),
        dict(cost=round(0.65/2*100, 0), labels = "H", task=1),
        dict(cost=round(0.67/2*100, 0), labels = "I", task=1)
    ]
    task_2_costs_P2 = [
        dict(cost=round(0.99/2*100, 1), labels = "A", task=2),
        dict(cost=round(0.93/2*100, 1), labels = "B", task=2),
        dict(cost=round(0.87/2*100, 0), labels = "C", task=2),
        dict(cost=round(0.81/2*100, 0), labels = "D", task=2),
        dict(cost=round(0.75/2*100, 0), labels = "E", task=2), #
        dict(cost=round(0.69/2*100, 0), labels = "F", task=2),
        dict(cost=round(0.63/2*100, 0), labels = "G", task=2),
        dict(cost=round(0.57/2*100, 0), labels = "H", task=2),
        dict(cost=round(0.51/2*100, 0), labels = "I", task=2)
    ]
    task_3_costs_P2 = [
        dict(cost=round(0.35/2*100, 0), labels = "A", task=3),
        dict(cost=round(0.43/2*100, 0), labels = "B", task=3),
        dict(cost=round(0.51/2*100, 0), labels = "C", task=3),
        dict(cost=round(0.59/2*100, 0), labels = "D", task=3),
        dict(cost=round(0.67/2*100, 0), labels = "E", task=3), #
        dict(cost=round(0.75/2*100, 0), labels = "F", task=3),
        dict(cost=round(0.83/2*100, 0), labels = "G", task=3),
        dict(cost=round(0.91/2*100, 0), labels = "H", task=3),
        dict(cost=round(0.99/2*100, 0), labels = "I", task=3)
    ]
    task_4_costs_P2 = [
        dict(cost=round(0.51/2*100, 0), labels = "A", task=4),
        dict(cost=round(0.57/2*100, 0), labels = "B", task=4),
        dict(cost=round(0.63/2*100, 0), labels = "C", task=4),
        dict(cost=round(0.69/2*100, 0), labels = "D", task=4),
        dict(cost=round(0.75/2*100, 0), labels = "E", task=4), #
        dict(cost=round(0.81/2*100, 0), labels = "F", task=4),
        dict(cost=round(0.87/2*100, 0), labels = "G", task=4),
        dict(cost=round(0.93/2*100, 0), labels = "H", task=4),
        dict(cost=round(0.99/2*100, 0), labels = "I", task=4)
    ]

    P1_ROLE = "P1"
    P2_ROLE = "P2"

class Subsession(BaseSubsession):
    # treatment
    treatment = models.StringField()
    pass

class Group(BaseGroup):
    # XXX random draw for percentages when overriding negotiation
    random_draw_max_diff_1 = models.IntegerField()

    #
    group_payoff_round_1 = models.FloatField()
    group_payoff_round_2 = models.FloatField()
    group_payoff_round_3 = models.FloatField()
    group_payoff_round_4 = models.FloatField()
    #production_cost = models.FloatField(initial=1)

    # agreement on tasks
    agree_1 = models.IntegerField(initial= 0 )
    agree_2 = models.IntegerField(initial= 0 )
    agree_3 = models.IntegerField(initial= 0 )
    agree_4 = models.IntegerField(initial= 0 )

    final_agree = models.IntegerField(initial = 0 )
    pass

class Player(BasePlayer):
    # amounts produced
    prod_round_1 = models.IntegerField(choices=range(0,21), label = "")
    prod_round_2 = models.IntegerField(choices=range(0,21), label = "")
    prod_round_3 = models.IntegerField(choices=range(0,21), label = "")
    prod_round_4 = models.IntegerField(choices=range(0,21), label = "")
    # payoffs per task
    payoff_round_1 = models.FloatField()
    payoff_round_2 = models.FloatField()
    payoff_round_3 = models.FloatField()
    payoff_round_4 = models.FloatField()
    # vote
    vote_1 = models.StringField()
    vote_2 = models.StringField()
    vote_3 = models.StringField()
    vote_4 = models.StringField()
    # production cost
    production_cost_1 = models.FloatField(initial=50)
    production_cost_2 = models.FloatField(initial=45)
    production_cost_3 = models.FloatField(initial=40)
    production_cost_4 = models.FloatField(initial=35)
    # survey variables
    joyful = models.IntegerField(label = "Joyful", choices=range(1, 10), widget=widgets.RadioSelectHorizontal)
    afraid = models.IntegerField(label = "Afraid", choices=range(1, 10), widget=widgets.RadioSelectHorizontal)
    elated = models.IntegerField(label = "Elated", choices=range(1, 10), widget=widgets.RadioSelectHorizontal)
    scared = models.IntegerField(label = "Scared", choices=range(1, 10), widget=widgets.RadioSelectHorizontal)
    delighted = models.IntegerField(label = "Delighted", choices=range(1, 10), widget=widgets.RadioSelectHorizontal)
    nervous = models.IntegerField(label = "Nervous", choices=range(1, 10), widget=widgets.RadioSelectHorizontal)
    happy = models.IntegerField(label = "Happy", choices=range(1, 10), widget=widgets.RadioSelectHorizontal)
    # quiz variables
    ## Quiz part I
    quiz1 = models.IntegerField(
        label="<b>Question 1:</b> How many parts does the experiment consist of?",
        choices=[[1, '1'],
                 [2, '2'],
                 [0, '3'],
                 [3, '4'],
                 ], widget=widgets.RadioSelect)
    quiz2 = models.IntegerField(
        label="<b>Question 2:</b> With how many participants are you matched with in Part I of the study?”",
        choices=[[1, '1 worker'],
                 [0, '1 worker and 1 manager'],
                 [2, '1 manager'],
                 [3, 'No one'],
                 ], widget=widgets.RadioSelect)
    quiz3 = models.IntegerField(
        label="<b>Question 3:</b> If you and your matched worker decide to allocate all the 20 points to the group account, and you get 40% of the group account, what are your final earnings?",
        choices=[[1, '17 points'],
                 [2, '0 points'],
                 [0, '32 points'],
                 [3, '40 points'],
                 ], widget=widgets.RadioSelect)
    quiz4 = models.IntegerField(
        label="<b>Question 4:</b> You will know the percentage of your matched worker and manager:",
        choices=[[1, 'True'],
                 [0, 'False'],
                 ], widget=widgets.RadioSelect)
    ## Quiz part II
    quiz5 = models.IntegerField(
        label="<b>Question 1:</b> In the Negotiation-Production game, you and the other worker in your group will go through:",
        choices=[[0, 'A negotiation stage first and then a production stage'],
                 [2, 'A production stage and then a negotiation stage'],
                 [1, 'Two production stages and then a negotiation stage'],
                 [3, 'A negotiation stage only'],
                 ], widget=widgets.RadioSelect)
    quiz6 = models.IntegerField(
        label="<b>Question 2:</b> How many repetitions (periods) will you play in the Negotiation-Production?",
        choices=[[1, '1'],
                 [2, '2'],
                 [0, '3'],
                 [3, '4'],
                 ], widget=widgets.RadioSelect)
    quiz7 = models.IntegerField(
        label="<b>Question 3:</b> In the Negotiation Stage, how are percentages determined for the Production Stage?",
        choices=[[1, 'The manager decides the percentages always.'],
                 [2, 'Workers select their own percentages individually without any agreement.'],
                 [3, 'Percentages are predetermined and cannot be changed.'],
                 [0, 'If workers agree on a possible alternative, those percentages will be implemented.'],
                 ], widget=widgets.RadioSelect)
    quiz8_manager = models.IntegerField(
        label="<b>Question 4:</b> What happens if you and the other worker in your group do not reach an agreement during the Negotiation Stage?",
        choices=[[1, 'You and the other worker in your group will earn 0 points and the manager will earn 100 points.'],
                 [0, 'The manager will decide the percentages.'],
                 [2, 'Both workers will be expelled from the experiment.'],
                 [3, 'Participants will have to restart the negotiation.'],
                 ], widget=widgets.RadioSelect)
    quiz8_algo = models.IntegerField(
        label="<b>Question 4:</b> What happens if you and the other worker in your group do not reach an agreement during the Negotiation Stage?",
        choices=[[0, 'The percentages will be predetermined by an algorithm that mimics managers decisions.'],
                 [1, 'You and the other worker in your group will earn 0 points and the manager will earn 100 points.'],
                 [2, 'Both workers will be expelled from the experiment.'],
                 [3, 'You and the other worker in your group will have to restart the negotiation.'],
                 ], widget=widgets.RadioSelect)

    quiz_attempts_1 = models.IntegerField(initial=0)
    timeout_quiz_1 = models.IntegerField(initial = 0)
    quiz_attempts_2 = models.IntegerField(initial=0)
    timeout_quiz_2 = models.IntegerField(initial = 0)

    # demographics
    age = models.IntegerField(label="¿Cuál es su edad actual? (Escriba un número, por ejemplo: 27)")
    gender = models.StringField(label="¿Cuál es su sexo? Seleccione una opción.",
                                 choices=[['Male','Hombre'],
                                          ['Female','Mujer'],
                                          ['Not disclosed','Prefiero no decirlo']],
                                widget=widgets.RadioSelectHorizontal)
    education = models.StringField(label="¿Cuál es el nivel máximo de estudios terminados? Seleccione una opción.",
                                 choices= [["Primaria", "Primaria"], ["Secundaria", "Secundaria"],
                                           ["Formación Profesional", "Formación Profesional"],
                                           ['Graduado o Licenciado Master/ Postgrado','Graduado o Licenciado Master/ Postgrado'],
                                           ['Doctorado','Doctorado'],['Otros','Otros']])
    campo_estudio = models.StringField(label="¿Qué campo de estudios universitarios tiene? Seleccione una opción",
                                 choices= [["Ninguno", "Ninguno"], ["Derecho", "Derecho"],
                                           ["Economía/ Empresa/ Gestión", "Economía/ Empresa/ Gestión"],
                                           ['STEM (Ciencia, Tecnología. Ingeniería o Matemáticas)','STEM (Ciencia, Tecnología. Ingeniería o Matemáticas)'],
                                           ['Otros','Otros']])
    experience_sector = models.StringField(label="¿En qué sector tiene experiencia profesional? Seleccione una opción.",
                                 choices= [["Ninguno", "Ninguno"], ["Público", "Público"],
                                           ["Privado", "Privado"],
                                           ['Público y Privado','Público y Privado']])
    experience_yrs = models.IntegerField(label="¿Cuántos años de experiencia profesional tiene? (escriba un número -redondeado sin decimales- desde 0 si no tiene experiencia en negociación hasta el número total de años que pueda tener). Por ejemplo: si son dos años y medio, escriba: 3.")

    # SAM
    SAM_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5,6,7,8,9])
    SAM_2 = models.IntegerField()
    SAM_3 = models.IntegerField()

    # Distributive Justice
    distributive_j_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Sus recompensas/ resultados* reflejan el esfuerzo que has puesto en su trabajo?")
    distributive_j_2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Sus recompensas son apropiadas para el trabajo que ha terminado?")
    distributive_j_3 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Sus recompensas reflejan que ha contribuido al grupo?")
    distributive_j_4 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Sus recompensas son justas teniendo en cuenta su desempeño?")

    # Perceived Justice
    perceived_j_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Ha sido capaz de expresar sus puntos de vista y sentimientos ante los procedimientos utilizados para dar recompensas? ")
    perceived_j_2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Ha tenido influencia sobre las recompensas obtenidas a partir de dichos procedimientos?")
    perceived_j_3 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Los procedimientos para dar recompensas han sido aplicados consistentemente (de la misma manera a todos los empleados)?")
    perceived_j_4 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Los procedimientos para dar recompensas han sido aplicados de manera neutral (sin prejuicios)?")
    perceived_j_5 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Los procedimientos para dar recompensas se han basado en información precisa?")
    perceived_j_6 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Ha sido capaz de solicitar las recompensas que merece según dichos procedimientos?")
    perceived_j_7 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1,2,3,4,5], label="¿Los procedimientos para dar recompensas se han basado en estándares éticos y morales?")

    # Algo Aversion
    algo_aversion_1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Para transacciones rutinarias, prefiero interactuar con un sistema artificialmente inteligente que con un humano.")
    algo_aversion_2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="La inteligencia artificial puede proporcionar nuevas oportunidades económicas para este país.")
    algo_aversion_3 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Las organizaciones usan la Inteligencia Artificial de manera poco ética.")
    algo_aversion_4 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Los sistemas artificialmente inteligentes pueden ayudar a las personas a sentirse más felices.")
    algo_aversion_5 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Estoy impresionado por lo que la inteligencia artificial puede hacer.")
    algo_aversion_6 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Creo que los sistemas artificialmente inteligentes cometen muchos errores.")
    algo_aversion_7 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Me interesa usar sistemas artificialmente inteligentes en mi vida diaria.")
    algo_aversion_8 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="La inteligencia artificial me parece siniestra.")
    algo_aversion_9 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="La inteligencia artificial podría tomar el control de la gente.")
    algo_aversion_10 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Creo que la inteligencia artificial es peligrosa.")
    algo_aversion_11 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="La inteligencia artificial puede tener impactos positivos en el bienestar de las personas.")
    algo_aversion_12 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="La inteligencia artificial es emocionante.")
    algo_aversion_13 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Un agente artificialmente inteligente sería mejor que un empleado en muchos trabajos rutinarios.")
    algo_aversion_14 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Hay muchas aplicaciones beneficiosas de la Inteligencia Artificial.")
    algo_aversion_15 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Tiemblo de incomodidad cuando pienso en futuros usos de la Inteligencia Artificial.")
    algo_aversion_16 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Los sistemas artificialmente inteligentes pueden funcionar mejor que los humanos.")
    algo_aversion_17 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Gran parte de la sociedad se beneficiará de un futuro lleno de Inteligencia Artificial.")
    algo_aversion_18 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="Me gustaría usar la Inteligencia Artificial en mi propio trabajo.")
    algo_aversion_19 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="La gente como yo sufrirá si la Inteligencia Artificial se utiliza cada vez más.")
    algo_aversion_20 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[1,"Totalmente en desacuerdo"],
                                                                                         [2,"En desacuerdo"],
                                                                                         [3,"Neutral"],
                                                                                         [4,"De acuerdo"],
                                                                                         [5,"Totalmente de acuerdo"]],
                                                                                         label="La inteligencia artificial se utiliza para espiar a las personas.")
    algo_aversion_attention = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[0,"Yes"],[1,"No"]],
                                                  label="This is an attention check. Press the button No")

    # CRT
    crt_1 = models.IntegerField(label='Una mesa y una silla cuestan 150 dólares en total. La mesa cuesta 100 '
                                      'dólares más que la silla. ¿Cuánto cuesta la silla? '
                                      '(contesta abajo en dólares. Si necesita escribir decimales, utiliza "." y no ",").')
    crt_2 = models.IntegerField(label='Si 10 mecánicos tardan 10 horas en arreglar 10 coches, ¿cuánto tardarían 80 mecánicos en arreglar 80 coches? (contesta abajo en horas. Si necesita escribir decimales, utiliza "." y no ",").')
    crt_3 = models.IntegerField(label='Una nueva biblioteca está comprando libros para su colección. Cada semana se duplica el número de libros adquiridos. Si tardan 36 semanas en comprar todos los libros que necesitan, ¿cuánto tardaría la biblioteca en comprar la mitad de los libros que necesita? (contesta abajo en semanas. Si necesita escribir decimales, utiliza "." y no ",").')
    crt_4 = models.IntegerField(label='En el zoo, los leones comen una tonelada de carne cada 6 semanas, y los tigres comen otra tonelada de carne cada 12 semanas, ¿cuánto tiempo tardarían (leones y tigres) en comer una tonelada de carne juntos? (responde a continuación en semanas. Si necesita escribir decimales, utiliza "." y no ",").')
    crt_5 = models.IntegerField(label='Juan obtuvo la 25ª marca más rápida y la 25ª más lenta en una carrera. ¿Cuántas personas participaron en la carrera? (responde a continuación. Si necesita escribir decimales, utiliza "." y no ",".)')
    crt_6 = models.IntegerField(label='Un coleccionista de arte adquiere un cuadro famoso por 50 millones y lo vende por 60 millones. Unos años más tarde, el coleccionista vuelve a comprarlo por 70 millones, y finalmente lo vende por 80 millones. ¿Cuánto ha ganado en total el coleccionista? (contesta abajo en millones. Si necesita escribir decimales, utiliza "." y no ",").')
    crt_7 = models.IntegerField(label='María invirtió 12.000 dólares en bolsa en noviembre de 2013. Seis meses después, en mayo de 2014, las acciones que había comprado habían bajado un 50%. Afortunadamente para Mary, de mayo de 2014 a agosto de 2014, las acciones que había comprado subieron un 75%. En ese momento, Mary:',
                                choices = [
                                    [1, "ha ganado dinero"],
                                    [2, "ha perdido dinero"],
                                    [3, "no ha ganado ni perdido dinero"],
                                           ],
                                widget=widgets.RadioSelect)
    socialpreferences_1=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 10 puntos para usted; 6 puntos para el otro participante"]
        ], widget=widgets.RadioSelectHorizontal, label=""
    )
    socialpreferences_2=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 16 puntos para usted; 4 puntos para el otro participante"]
        ], widget=widgets.RadioSelectHorizontal, label=""
    )
    socialpreferences_3=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 10 puntos para usted; 18 puntos para el otro participante"]
        ], widget=widgets.RadioSelectHorizontal, label=""
    )
    socialpreferences_4=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 11 puntos para usted; 19 puntos para el otro participante"]
        ], widget=widgets.RadioSelectHorizontal, label=""
    )
    socialpreferences_5=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 12 puntos para usted; 4 puntos para el otro participante"]
        ], widget=widgets.RadioSelectHorizontal, label=""
    )
    socialpreferences_6=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 8 puntos para usted; 16 puntos para el otro participante"]
        ], widget=widgets.RadioSelectHorizontal, label=""
    )

    # Personality
    perso_1 = models.IntegerField(label="Extravertida, entusiasta", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])
    perso_2 = models.IntegerField(label="Que critica a los demás, conflictiva", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])
    perso_3 = models.IntegerField(label="Fiable, autodisciplinada", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])
    perso_4 = models.IntegerField(label="Ansiosa, que fácilmente se altera", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])
    perso_5 = models.IntegerField(label="Abierta a nuevas experiencias, compleja", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])
    perso_6 = models.IntegerField(label="Reservada, callada", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])
    perso_7 = models.IntegerField(label="Considerada, afectuosa", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])
    perso_8 = models.IntegerField(label="Desorganizada, descuidada", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])
    perso_9 = models.IntegerField(label="Tranquila, emocionalmente estable", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])
    perso_10 = models.IntegerField(label="Convencional, poco creativa", choices=[
        [1, "1. Totalmente en descuerdo"],
        [2, "2. Muy en  descuerdo"],
        [3, "3.	Algo en descuerdo"],
        [4, "4.	Ni de acuerdo ni en desacuerdo"],
        [5, "5.	Algo de acuerdo"],
        [6, "6.	Muy de acuerdo"],
        [7, "7.	Totalmente de acuerdo"],
    ])

    ## Computed personalities
    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    openness = models.FloatField()
    emotional_stability = models.FloatField()
    conscientiousness = models.FloatField()
    pass

# FUNCTIONS
def creating_session(subsession):
    subsession.group_randomly()
    print(subsession.get_group_matrix())
    subsession.treatment = subsession.session.config['treatment']
pass

def final_earnings(player):
    payoff_sum = player.payoff_round_1 + player.payoff_round_2 + player.payoff_round_3 + player.payoff_round_4
    player.payoff = payoff_sum
pass

def set_payoffs(group: Group):
    for p in group.get_players():
        for k in p.get_others_in_group():
            p.payoff_round_1 = Constants.endowment - p.prod_round_1 + p.production_cost_1*0.02*(p.prod_round_1 + k.prod_round_1)
            p.payoff_round_2 = Constants.endowment - p.prod_round_2 + p.production_cost_2*0.02*(p.prod_round_2 + k.prod_round_2)
            p.payoff_round_3 = Constants.endowment - p.prod_round_3 + p.production_cost_3*0.02*(p.prod_round_3 + k.prod_round_3)
            p.payoff_round_4 = Constants.endowment - p.prod_round_4 + p.production_cost_4*0.02*(p.prod_round_4 + k.prod_round_4)
            # compute sum of payoffs in a given round
            final_earnings(p)

pass


def set_production_cost(group: Group):
    def get_cost(label, tasks):
        for task in tasks:
            #print(task)
            if task['labels'] == label:
                return task['cost']
        return None

    if group.final_agree == 1:
        for p in group.get_players():
            if p.role == "P1":
                p.production_cost_1 = get_cost(p.vote_1, Constants.task_1_costs_P1) # Constants.task_1_costs_P1['labels'==p.vote_1]['cost']
                p.production_cost_2 = get_cost(p.vote_2, Constants.task_2_costs_P1) # Constants.task_1_costs_P1['labels'==p.vote_1]['cost']
            else:
                p.production_cost_1 = get_cost(p.vote_1, Constants.task_1_costs_P2) #Constants.task_1_costs_P2['labels'==p.vote_1]['cost']
                p.production_cost_2 = get_cost(p.vote_2, Constants.task_2_costs_P2) #Constants.task_1_costs_P2['labels'==p.vote_1]['cost']
    else:
        temp = random.sample([0, 1], 1)[0]
        print("This is temp ", temp)
        group.random_draw_max_diff_1 = temp
        print("RANDOM DRAW : ", group.random_draw_max_diff_1)
        for p in group.get_players():
                if p.role == "P1" and group.random_draw_max_diff_1 == 1:
                    p.production_cost_1 = round(99/2, 2)
                    p.production_cost_2 = round(51/2, 2)
                elif p.role == "P2" and p.group.random_draw_max_diff_1 == 1:
                    p.production_cost_1 = round(51/2, 2)
                    p.production_cost_2 = round(99/2, 2)
                else:
                    p.production_cost_1 = round(63/2, 2)
                    p.production_cost_2 = round(63/2, 2)


# PAGES
class Instruction(Page):
    timeout_seconds = 60*15
    timer_text = 'Time left to finish reading instructions:'
    def is_displayed(player: Player):
        return player.round_number == 1
    pass

class Instruction_2(Page):
    timeout_seconds = 60*15
    timer_text = 'Time left to finish reading instructions:'
    def is_displayed(player: Player):
        return player.round_number == 1
    pass

class Quiz(Page):

    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz1=0, quiz2=0, quiz3=0, quiz4=0)

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'

        if values != solutions:
            player.quiz_attempts_1 += 1
            #return "One or more answers were incorrect. Please, try again."
        return error_messages

    def is_displayed(player: Player):
        return player.round_number == 1

    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.timeout_quiz_1 = 1
    pass

class Quiz_2(Page):

    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        print("SUCAAAAAAAAAAAAAAAAA", player.subsession.treatment)
        if player.subsession.treatment == "A":
            temp = ['quiz5', 'quiz6', 'quiz7', 'quiz8_algo']
        else:
            temp = ['quiz5', 'quiz6', 'quiz7', 'quiz8_manager']
        return temp
    def error_message(player: Player, values):
        if player.subsession.treatment == "A":
            solutions = dict(quiz5=0, quiz6=0, quiz7=0, quiz8_algo=0)
        else:
            solutions = dict(quiz5=0, quiz6=0, quiz7=0, quiz8_manager=0)

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'

        if values != solutions:
            player.quiz_attempts_2 += 1
            #return "One or more answers were incorrect. Please, try again."
        return error_messages

    def is_displayed(player: Player):
        return player.round_number == 1

    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.timeout_quiz_2 = 1
    pass

class Intro_to_New_Round(Page):
    @staticmethod
    def vars_for_template(player:Player):
        return dict(round=player.round_number - 1)

    def is_displayed(player: Player):
        return player.round_number > 1
    pass

class Intro_to_negotiation(Page):
    @staticmethod
    def vars_for_template(player:Player):
        return dict(round=player.round_number - 1)

    def is_displayed(player: Player):
        return player.round_number > 1
    pass

class WaitNegotiation(WaitPage):

    pass
class Production(Page):
    form_model = 'player'
    form_fields = ["prod_round_1", "prod_round_2", "prod_round_3", "prod_round_4"]

    @staticmethod
    def vars_for_template(player:Player):
        return dict(round=player.round_number - 1)
    pass

class Feedback_production(Page):
    def vars_for_template(player: Player):
        for p in player.get_others_in_group():
            # points in the group account
            a1 = p.prod_round_1
            a2 = p.prod_round_2
            a3 = p.prod_round_3
            a4 = p.prod_round_4
        # total points in the group account (both players)
        g1 = a1 + player.prod_round_1
        g2 = a2 + player.prod_round_2
        g3 = a3 + player.prod_round_3
        g4 = a4 + player.prod_round_4
        return dict(
            other_contribution_1 = a1,
            other_contribution_2 = a2,
            other_contribution_3 = a3,
            other_contribution_4 = a4,
            g1 = g1,
            g2 = g2,
            g3 = g3,
            g4 = g4,
            p1 = 20 - player.prod_round_1,
            p2 = 20 - player.prod_round_2,
            p3 = 20 - player.prod_round_3,
            p4 = 20 - player.prod_round_4,
            c1 = g1*player.production_cost_1/100,
            c2 = g2*player.production_cost_2/100,
            c3 = g3*player.production_cost_3/100,
            c4 = g4*player.production_cost_4/100,
            round = player.round_number-1
        )

class ResultsWaitPage(WaitPage):
    # define here group payoffs
    after_all_players_arrive = 'set_payoffs'
    pass

class Intro_to_production(Page):
    @staticmethod
    def vars_for_template(player:Player):
        return dict(round=player.round_number - 1)
    pass

class Negotiation_2(Page):
    form_model = 'player'
    form_fields = []
    #timeout_seconds = 120 # XXX

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 1

    @staticmethod
    def vars_for_template(player: Player):
        import random
        if player.role == "P1":
            loop_task_1 = Constants.task_1_costs_P1.copy()
            loop_task_2 = Constants.task_2_costs_P1.copy()
            #loop_task_3 = Constants.task_3_costs_P1.copy()
            #loop_task_4 = Constants.task_4_costs_P1.copy()
        else:
            loop_task_1 = Constants.task_1_costs_P2.copy()
            loop_task_2 = Constants.task_2_costs_P2.copy()
            #loop_task_3 = Constants.task_3_costs_P2.copy()
            #loop_task_4 = Constants.task_4_costs_P2.copy()

        loop_task_1_sorted_ascending = sorted(loop_task_1, key=lambda x:x['labels'])
        loop_task_2_sorted_ascending = sorted(loop_task_2, key=lambda x:x['labels'])

        return dict(
            loop_task_1=(loop_task_1_sorted_ascending),
            loop_task_2=(loop_task_2_sorted_ascending),
            #loop_task_3=(loop_task_3),
            #loop_task_4=(loop_task_4),
            round=player.round_number - 1
        )
    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)

    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        players = group.get_players()

        # task 1
        if 'vote_1' in data:
            ## if client sends vote in task 1
            try:
                vote_1 = (data['vote_1'])
            except Exception:
                print('Invalid message received 1', data['task'])
                return

            ## check if vote is in costs (labels), if so assign to vote_1 (server)
            if player.role == "P1":
                task_costs = Constants.task_1_costs_P1
            else:
                task_costs = Constants.task_1_costs_P2
            costs = [d['labels'] for d in task_costs]
            if not vote_1 in costs:
                print('Invalid message received 2', vote_1, costs)
                return
            player.vote_1 = vote_1

        # task 2
        if 'vote_2' in data:
            try:
                vote_2 = (data['vote_2'])
            except Exception:
                print('Invalid message received 1', data['task'])
                return
            ## check if vote is in costs (labels), if so assign to vote_1 (server)
            if player.role == "P1":
                task_costs = Constants.task_2_costs_P1
            else:
                task_costs = Constants.task_2_costs_P2
            costs = [d['labels'] for d in task_costs]
            if not vote_2 in costs:
                print('Invalid message received 2', vote_2, costs)
                return
            player.vote_2 = vote_2

        # task 3
#        if 'vote_3' in data:
#            ## if client sends vote in task 3
#            try:
#                vote_3 = (data['vote_3'])
#            except Exception:
#                print('Invalid message received 1', data['task'])
#                return
#
#            ## check if vote is in costs (labels), if so assign to vote_1 (server)
#            if player.role == "P1":
#                task_costs = Constants.task_3_costs_P1
#            else:
#                task_costs = Constants.task_3_costs_P2
#            costs = [d['labels'] for d in task_costs]
#            if not vote_3 in costs:
#                print('Invalid message received 2', vote_3, costs)
#                return
#            player.vote_3 = vote_3

        # task 4
#        if 'vote_4' in data:
#            ## if client sends vote in task 3
#            try:
#                vote_4 = (data['vote_4'])
#            except Exception:
#                print('Invalid message received 1', data['task'])
#                return
#
#            ## check if vote is in costs (labels), if so assign to vote_1 (server)
#            if player.role == "P1":
#                task_costs = Constants.task_4_costs_P1
#            else:
#                task_costs = Constants.task_4_costs_P2
#            costs = [d['labels'] for d in task_costs]
#            if not vote_4 in costs:
#                print('Invalid message received 2', vote_4, costs)
#                return
#            player.vote_4 = vote_4

        # counting majority (notice that im using the same labels for all task in loops)
        tallies_1 = {vote: 0 for vote in [d['labels'] for d in Constants.task_1_costs_P1]}
        tallies_2 = {vote: 0 for vote in [d['labels'] for d in Constants.task_1_costs_P1]}
#        tallies_3 = {vote: 0 for vote in [d['labels'] for d in Constants.task_1_costs_P1]}
#        tallies_4 = {vote: 0 for vote in [d['labels'] for d in Constants.task_1_costs_P1]}
        votes = []
        for p in players:
            vote_1 = p.field_maybe_none('vote_1')
            vote_2 = p.field_maybe_none('vote_2')
#            vote_3 = p.field_maybe_none('vote_3')
#            vote_4 = p.field_maybe_none('vote_4')
            if vote_1 is not None:
                tallies_1[vote_1] += 1
                if tallies_1[vote_1] >= 2:
                    group.agree_1 = 1
                else:
                    group.agree_1 = 0
            if vote_2 is not None:
                tallies_2[vote_2] += 1
                if tallies_2[vote_2] >= 2:
                    group.agree_2 = 1
                else:
                    group.agree_2 = 0
#            if vote_3 is not None:
#                tallies_3[vote_3] += 1
#                if tallies_3[vote_3] >= 2:
#                    group.agree_3 = 1
#                else:
#                    group.agree_3 = 0
#            if vote_4 is not None:
#                tallies_4[vote_4] += 1
#                if tallies_4[vote_4] >= 2:
#                    group.agree_4 = 1
#                else:
#                    group.agree_4 = 0
            votes.append([p.id_in_group, vote_1, vote_2])#, vote_3, vote_4])
        print("Tallies :", votes, tallies_1, tallies_2)#, tallies_3, tallies_4)

#        tallies_2 = {vote_2: 0 for vote_2 in costs}
#            print("CIAOOOOOOOOOooo", tallies_2)
#            votes = []
#            for p in players:
#                task = 2
#                if vote_2 is not None:
#                    tallies_2[vote_2] += 1
#                    if tallies_2[vote_2] >= 2:
#                        group.agree_2 = 1
#                        #return {0: dict(finished=True)}
#                    else:
#                        group.agree_2 = 0
#                votes.append([p.id_in_group, vote_2, task])
#            return {0: dict(votes=votes)}#, votes_2=votes_2, tallies_2=tallies_2)}

        if group.agree_1 == 1 and group.agree_2 ==1 : #and group.agree_3 == 1 and group.agree_4 == 1:
            group.final_agree = 1
            return {0: dict(finished=True)}

        return {0: dict(votes=votes)}#, votes_2=votes_2, tallies_2=tallies_2)}

    @staticmethod
    def error_message(player: Player, values):
        group = player.group
        # anti-cheating measure
        if group.field_maybe_none('final_agree') is None:
            return "Not done with this page"

#    @staticmethod
#    def before_next_page(player: Player, timeout_happened):
        # Here is the treatment XXX
    pass


class ComputeProductionCosts(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 1
    after_all_players_arrive = 'set_production_cost'


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(payoff1=player.in_round(1).payoff,
                    payoff2=player.in_round(2).payoff,
                    payoff3=player.in_round(3).payoff,
                    payoff4=player.in_round(4).payoff)
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    pass


class Survey_E(Page):
    form_model = 'player'
    form_fields = ['joyful', 'afraid',
                            'elated',
                            'scared',
                            'delighted',
                            'nervous',
                            'happy'
                   ]
    @staticmethod
    def is_displayed(player:Player):
        return player.round_number > 1
pass


class Feedback_Negotiation(Page):
    @staticmethod
    def is_displayed(player:Player):
        return player.round_number > 1
    pass


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    pass

class PerceivedJustice(Page): # XXX
    form_model = 'player'
    form_fields = ['perceived_j_1','perceived_j_2','perceived_j_3','perceived_j_4','perceived_j_5','perceived_j_6','perceived_j_7']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    pass

class SAM(Page):
    form_model = 'player'
    form_fields = ['SAM_1', 'SAM_2', 'SAM_3']
    pass

class DistributiveJustice(Page):
    form_model = 'player'
    form_fields = ['distributive_j_1','distributive_j_2','distributive_j_3','distributive_j_4']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    pass

class Personality(Page):
    form_model = 'player'
    form_fields = [
        'perso_1', 'perso_2', 'perso_3', 'perso_4', 'perso_5'
        'perso_6', 'perso_7', 'perso_8', 'perso_9', 'perso_10'
                   ]
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    pass

class CRT(Page):
    form_model='player'
    form_fields=['crt_1', 'crt_2', 'crt_3', 'crt_4', 'crt_5', 'crt_6', 'crt_7']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    pass

class AlgoAversion(Page):
    form_model='player'
    form_fields=['algo_aversion_1','algo_aversion_2','algo_aversion_3','algo_aversion_4','algo_aversion_5',
                 'algo_aversion_6','algo_aversion_7','algo_aversion_8','algo_aversion_9','algo_aversion_10',
                 'algo_aversion_11','algo_aversion_12','algo_aversion_attention','algo_aversion_13','algo_aversion_14','algo_aversion_15',
                 'algo_aversion_16','algo_aversion_17','algo_aversion_18','algo_aversion_19','algo_aversion_20',
                 ]
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    def before_next_page(player: Player, timeout_happened):
        player.extraversion = player.perso_1 + 8 - player.perso_6
        player.agreeableness = 8 - player.perso_2 + player.perso_7
        player.conscientiousness = player.perso_3 + 8 - player.perso_8
        player.emotional_stability = 8 - player.perso_4 + player.perso_9
        player.openness = player.perso_5 + 8 - player.perso_10
    pass

class SocialPreferences(Page):
    form_model='player'
    form_fields=[
        'socialpreferences_1',
        'socialpreferences_2',
        'socialpreferences_3',
        'socialpreferences_4',
        'socialpreferences_5',
        'socialpreferences_6',
                 ]
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    pass


page_sequence = [Instruction,                       # R =1
                 Quiz,                              # R =1
                 Intro_to_New_Round,                # R > 1 hence all
                 Intro_to_negotiation,              # R > 1 hence all
                 WaitNegotiation,                   # R > 1 hence all
                 Negotiation_2,                     # R > 1 hence all
                 ComputeProductionCosts,            # R > 1 hence all
                 Feedback_Negotiation,              # R all - treatment human
                 SAM,
                 Intro_to_production,               # R all
                 Production,                        # R all
                 ResultsWaitPage,                   # R all
                 Feedback_production,               # R all
                 Instruction_2,                     # R =1
                 Quiz_2,                            # R =1 XXX
                 DistributiveJustice,
                 PerceivedJustice,
                 Personality,
                 AlgoAversion,
                 CRT,
                 SocialPreferences,
                 Demographics,                      # R last round
                 Results
                ]
