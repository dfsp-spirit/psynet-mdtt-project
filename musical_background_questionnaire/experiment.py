import psynet.experiment
from psynet.consent import NoConsent
from psynet.modular_page import ModularPage, SurveyJSControl
from psynet.page import DebugResponsePage, SuccessfulEndPage
from psynet.timeline import Timeline


class Exp(psynet.experiment.Experiment):
    label = "Musical Background Questionnaire"
    initial_recruitment_size = 1

    timeline = Timeline(
        NoConsent(),
        ModularPage(
            "musical_background_questionnaire",
            "This questionnaire asks you a few questions regarding your background in music.",
            SurveyJSControl(
                {
                    "logoPosition": "right",
                    "pages": [
                        {
                            "name": "page1",
                            "elements": [

                                {
                                    "type": "text",
                                    "name": "age_start_playing",
                                    "inputType": "number",
                                    "title": "How old were you when you started playing a musical instrument?",
                                    "isRequired": True,
                                    "validators": [{
                                        "type": "numeric",
                                        "text": "Value must be within the range of 0 to 125",
                                        "minValue": 0,
                                        "maxValue": 125,
                                    }]
                                },
                                {
                                    "type": "paneldynamic",
                                    "name": "musical_instruments",
                                    "title": "Which musical instruments do you play?",
                                    "description": 
                                        "Please start with your main instrument! Please mind to spell correctly.",
                                    "panelCount": 1,
                                    "maxPanelCount": 10,
                                    "isRequired": True,
                                    "templateElements": [
                                        {
                                            "type": "text",
                                            "name": "instrument",
                                            "title": "Instrument",
                                        },
                                    ],
                                    "panelAddText": "Add instrument",
                                    "panelRemoveText": "Remove instrument",
                                },
                                {
                                    "type": "paneldynamic",
                                    "name": "musical_genres",
                                    "title": "Which musical genres do you play?",
                                    "description": 
                                        "Please start with your main genre! Please mind to spell correctly.",
                                    "panelCount": 1,
                                    "maxPanelCount": 10,
                                    "isRequired": True,
                                    "templateElements": [
                                        {
                                            "type": "text",
                                            "name": "genre",
                                            "title": "Genre",
                                        },
                                    ],
                                    "panelAddText": "Add genre",
                                    "panelRemoveText": "Remove genre",
                                },
                                {
                                    "type": "panel",
                                    "name": "age_0_to_5_questions",
                                    "visibleIf": "{age_start_playing} <= 5",
                                    "elements": [
                                        {
                                            "name": "practice_time_0_to_5",
                                            "type": "text",
                                            "inputType": "number",
                                            "title": 
                                                "Please estimate how many hours a week you spent practicing a " \
                                                "musical instrument in the age period 0-5.",
                                            "isRequired": True,
                                            "validators": [{
                                                "type": "numeric",
                                                "text": "Value must be within the range of 0 to 140",
                                                "minValue": 0,
                                                "maxValue": 140,
                                            }]
                                        },
                                        {
                                            "name": "improvisation_ratio_0_to_5",
                                            "type": "text",
                                            "inputType": "number",
                                            "title": 
                                                "Please estimate how much of that time was spent on improvisation.",
                                            "description": 
                                                "Insert a number corresponding to the percentage (%) of time spent " \
                                                "on improvisation.",
                                            "isRequired": True,
                                            "validators": [{
                                                "type": "numeric",
                                                "text": "Value must be within the range of 0% to 100%",
                                                "minValue": 0,
                                                "maxValue": 100,
                                            }]
                                        },
                                    ]
                                },
                                {
                                    "type": "panel",
                                    "name": "age_6_to_11_questions",
                                    "visibleIf": "{age_start_playing} <= 11",
                                    "elements": [
                                        {
                                            "name": "practice_time_6_to_11",
                                            "type": "text",
                                            "inputType": "number",
                                            "title": 
                                                "Please estimate how many hours a week you spent practicing a " \
                                                "musical instrument in the age period 6-11.",
                                            "isRequired": True,
                                            "validators": [{
                                                "type": "numeric",
                                                "text": "Value must be within the range of 0 to 140",
                                                "minValue": 0,
                                                "maxValue": 140,
                                            }]
                                        },
                                        {
                                            "name": "improvisation_ratio_6_to_11",
                                            "type": "text",
                                            "inputType": "number",
                                            "title": 
                                                "Please estimate how much of that time was spent on improvisation.",
                                            "description": 
                                                "Insert a number corresponding to the percentage (%) of time spent " \
                                                "on improvisation.",
                                            "isRequired": True,
                                            "validators": [{
                                                "type": "numeric",
                                                "text": "Value must be within the range of 0% to 100%",
                                                "minValue": 0,
                                                "maxValue": 100,
                                            }]
                                        },
                                    ]
                                },
                                {
                                    "type": "panel",
                                    "name": "age_12_to_18_questions",
                                    "visibleIf": "{age_start_playing} <= 18",
                                    "elements": [
                                        {
                                            "name": "practice_time_12_to_18",
                                            "type": "text",
                                            "inputType": "number",
                                            "title": 
                                                "Please estimate how many hours a week you spent practicing a " \
                                                "musical instrument in the age period 12-18.",
                                            "isRequired": True,
                                            "validators": [{
                                                "type": "numeric",
                                                "text": "Value must be within the range of 0 to 140",
                                                "minValue": 0,
                                                "maxValue": 140,
                                            }]
                                        },
                                        {
                                            "name": "improvisation_ratio_12_to_18",
                                            "type": "text",
                                            "inputType": "number",
                                            "title": 
                                                "Please estimate how much of that time was spent on improvisation.",
                                            "description": 
                                                "Insert a number corresponding to the percentage (%) of time spent " \
                                                "on improvisation.",
                                            "isRequired": True,
                                            "validators": [{
                                                "type": "numeric",
                                                "text": "Value must be within the range of 0% to 100%",
                                                "minValue": 0,
                                                "maxValue": 100,
                                            }]
                                        },
                                    ]
                                },
                                {
                                    "type": "panel",
                                    "name": "age_18_and_above_questions",
                                    "elements": [
                                        {
                                            "name": "practice_time_18_and_above",
                                            "type": "text",
                                            "inputType": "number",
                                            "title": 
                                                "Please estimate how many hours a week you spent practicing a " \
                                                "musical instrument in the age period from 18 to now.",
                                            "isRequired": True,
                                            "validators": [{
                                                "type": "numeric",
                                                "text": "Value must be within the range of 0 to 140",
                                                "minValue": 0,
                                                "maxValue": 140,
                                            }]
                                        },
                                        {
                                            "name": "improvisation_ratio_18_and_above",
                                            "type": "text",
                                            "inputType": "number",
                                            "title": 
                                                "Please estimate how much of that time was spent on improvisation.",
                                            "description": 
                                                "Insert a number corresponding to the percentage (%) of time spent " \
                                                "on improvisation.",
                                            "isRequired": True,
                                            "validators": [{
                                                "type": "numeric",
                                                "text": "Value must be within the range of 0% to 100%",
                                                "minValue": 0,
                                                "maxValue": 100,
                                            }]
                                        },
                                    ]
                                }
                            ],
                        },
                    ],
                },
            ),
            time_estimate=50,
            bot_response=lambda: {},
        ),
        DebugResponsePage(),
        SuccessfulEndPage(),
    )
