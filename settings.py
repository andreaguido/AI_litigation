from os import environ

SESSION_CONFIGS = [
     dict(
         name='AI',
         app_sequence=['AI'],
         num_demo_participants=2,
         treatment = 'A',
         doc = """A = algo treatment; M = manager treatment;"""
     ),
     dict(
         name='Social_Preferences',
         app_sequence=['dg_social_preferences'],
         num_demo_participants=2,
     ),
    dict(
        name='All',
        app_sequence=['AI', 'dg_social_preferences', 'demographics', 'results'],
        num_demo_participants=2,
        treatment='A',
        doc="""A = algo treatment; M = manager treatment;"""

    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['ai_payoff_r1','ai_payoff_r2','ai_payoff_r3','ai_payoff_r4','ai_payoff_r5','dg_payoff', 'ai_quiz_payoff']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1790370492338'
