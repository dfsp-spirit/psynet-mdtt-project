import psynet.experiment
from psynet.modular_page import ModularPage, SurveyJSControl

creative_achievement_questionnaire = ModularPage(
    "creative_achievement_questionnaire",
    "This questionnaire asks one questions to learn more about your musical creative achievements.",
    SurveyJSControl(
        {
            "logoPosition": "right",
            "pages": [
                {
                    "name": "page_1",
                    "elements": [
                        {
                            "type": "radiogroup",
                            "name": "level_of_engagement_in_music",
                            "title": "How engaged are you in music?",
                            "description":
                                "Mark the alternative that applies best to you. Here counts both if you play " \
                                "an instrument or sing, or if you compose music yourself.",
                            "choices": [
                                "I do not at all engage in music.", 
                                "I am self-taught and engage in music privately, but have never played, " \
                                "sung, or displayed my own music to others.",
                                "I have taken lessons in music, but have never played, sung, or showed my " \
                                "own music to others.",
                                "I have played or sung – or my music has been played – in public concerts in " \
                                "my home town but I have never been paid to do this.",
                                "I have played or sung – or my music has been played – in public concerts in " \
                                "my home town and I have been paid to do this.",
                                "I am professionally active as a musician.",
                                "I am professionally active as a musician, and have been reviewed or noted " \
                                "in national or international media, and/or have received at least one prize " \
                                "or award for my musical work."
                            ]
                        }
                    ],
                },
            ],
        },
    ),
    time_estimate=5,
    bot_response=lambda: {},
)