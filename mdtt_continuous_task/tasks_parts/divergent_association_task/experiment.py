import psynet.experiment
from psynet.modular_page import ModularPage, SurveyJSControl


divergent_association_task = ModularPage(
    "divergent_association_task",
    "Divergent association",
    SurveyJSControl(
        {
            "logoPosition": "right",
            "pages": [
                {
                    "name": "page_1",
                    "elements": [
                        {
                            "type": "multipletext",
                            "name": "divergent_association_words",
                            "title": 
                                "Please write 10 nouns that are as unrelated to one another as possible, " \
                                "that is, nouns that would rarely or never be found in the same context.",
                            "items": [
                                { "name": "1", "isRequired": True },
                                { "name": "2", "isRequired": True },
                                { "name": "3", "isRequired": True },
                                { "name": "4", "isRequired": True },
                                { "name": "5", "isRequired": True },
                                { "name": "6", "isRequired": True },
                                { "name": "7", "isRequired": True },
                                { "name": "8", "isRequired": True },
                                { "name": "9", "isRequired": True },
                                { "name": "10", "isRequired": True },
                            ],
                            "colCount": 2,
                        }
                    ],
                },
            ],
        },
    ),
    time_estimate=300,
    bot_response=lambda: {},
)