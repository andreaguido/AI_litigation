from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'results'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

# PAGES

class WaitingPage(WaitPage):
    print("SUCAAAAA")
    pass

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(payoff1=player.participant.ai_payoff_r1,
                    payoff2=player.participant.ai_payoff_r2,
                    payoff3=player.participant.ai_payoff_r3,
                    payoff4=player.participant.ai_payoff_r4,
                    payoff5=player.participant.ai_payoff_r5,
                    dg=player.participant.dg_payoff,
                    quiz=player.participant.ai_quiz_payoff,
                    total=player.participant.payoff
                            )
    pass


page_sequence = [WaitingPage,Results]
