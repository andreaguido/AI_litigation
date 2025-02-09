from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'dg_social_preferences'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    P1_ROLE = "Dictator"
    P2_ROLE = "Receiver"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Social Preferences settings

    # pick one dictator
    #chosen_dictator = models.StringField(initial=random.sample(["P1", "P2"], 1)[0])
    # pick one question out of the six
    chosen_question = models.IntegerField(initial=0)
    answer_dictator = models.StringField()

    pass


class Player(BasePlayer):
    socialpreferences_1=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 10 puntos para usted; 6 puntos para el otro participante"]
        ], widget=widgets.RadioSelect, label=""
    )
    socialpreferences_2=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 16 puntos para usted; 4 puntos para el otro participante"]
        ], widget=widgets.RadioSelect, label=""
    )
    socialpreferences_3=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 10 puntos para usted; 18 puntos para el otro participante"]
        ], widget=widgets.RadioSelect, label=""
    )
    socialpreferences_4=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 11 puntos para usted; 19 puntos para el otro participante"]
        ], widget=widgets.RadioSelect, label=""
    )
    socialpreferences_5=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 12 puntos para usted; 4 puntos para el otro participante"]
        ], widget=widgets.RadioSelect, label=""
    )
    socialpreferences_6=models.StringField(choices=[
        ["A","Opción A: 10 puntos para usted; 10 puntos para el otro participante"],
        ["B","Opción B: 8 puntos para usted; 16 puntos para el otro participante"]
        ], widget=widgets.RadioSelect, label=""
    )
    earnings_social_preferences = models.IntegerField()

    pass

# Functions

def creating_session(subsession):
    subsession.group_randomly()
    print(subsession.get_group_matrix())

    # get a question for each group
    for g in subsession.get_groups():
        g.chosen_question = random.randint(1, 6)

pass


# PAGES

class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group:Group):

        d = group.get_player_by_role("Dictator")
        r = group.get_player_by_role("Receiver")

        # vector of payoffs for Dictator and Receiver
        dictator_payoffs = [10, 16, 10, 11, 12, 8]
        receiver_payoffs = [6, 4, 18, 19, 4, 16]

        # store responses to social preferences questions and pick the one randomly chosen
        s1 = d.socialpreferences_1
        s2 = d.socialpreferences_2
        s3 = d.socialpreferences_3
        s4 = d.socialpreferences_4
        s5 = d.socialpreferences_5
        s6 = d.socialpreferences_6
        list_responses = [s1, s2, s3, s4, s5, s6]
        group.answer_dictator = list_responses[group.chosen_question - 1]

        if group.answer_dictator == "A":
            d.earnings_social_preferences = 10
            r.earnings_social_preferences = 10
        else:
            d.earnings_social_preferences = dictator_payoffs[group.chosen_question - 1]
            r.earnings_social_preferences = receiver_payoffs[group.chosen_question - 1]

        for p in group.get_players():
            p.participant.dg_payoff = p.earnings_social_preferences
            # Moved to results app p.participant.payoff = p.participant.dg_payoff + p.participant.ai_payoff_r1 + p.participant.ai_quiz_payoff + p.participant.ai_payoff_r2 + p.participant.ai_payoff_r3 + p.participant.ai_payoff_r4 + p.participant.ai_payoff_r5
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
    pass

class Results(Page):
    pass

page_sequence = [SocialPreferences, ResultsWaitPage]
