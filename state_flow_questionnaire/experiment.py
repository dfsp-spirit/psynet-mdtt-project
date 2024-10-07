import psynet.experiment
from psynet.consent import NoConsent
from psynet.modular_page import ModularPage, SurveyJSControl
from psynet.page import DebugResponsePage, SuccessfulEndPage
from psynet.timeline import Timeline


class Exp(psynet.experiment.Experiment):
    label = "State Flow Questionnaire"
    initial_recruitment_size = 1

    timeline = Timeline(
        NoConsent(),
        ModularPage(
            "state_flow_questionnaire",
            "This questionnaire will ask you a few questions about your experience.",
            SurveyJSControl(
                {
                    "logoPosition": "right",
                    "pages": [
                        {
                            "name": "page_1",
                            "elements": [
                                {
                                    "type": "matrix",
                                    "name": "state_flow_questionnaire_matrix",
                                    "title": 
                                        "Please answer the following questions in relation to your experience in the " \
                                        "event or activity you have just completed.",
                                    "description":
                                        "These questions relate to the thoughts and feelings you may have " \
                                        "experienced while taking part. There are no right or wrong answers. Think " \
                                        "about how you felt during the event/activity and answer the questions using " \
                                        "the rating scale below. For each question circle the number that best " \
                                        "matches your experience.",
                                    "columns": [
                                        {
                                            "value": -2,
                                            "text": "Strongly disagree"
                                        },
                                        {
                                            "value": -1,
                                            "text": "Disagree"
                                        },
                                        {
                                            "value": 0,
                                            "text": "Neutral"
                                        },
                                        {
                                            "value": 1,
                                            "text": "Agree"
                                        },
                                        {
                                            "value": 2,
                                            "text": "Strongly agree"
                                        }
                                    ],
                                    "rows": [
                                        {
                                            "value": "adequately_challenged",
                                            "text": 
                                                "I was challenged, but I believed my skills would allow me to meet " \
                                                "the challenge."
                                        },
                                        {
                                            "value": "uncounsciously_correct",
                                            "text": 
                                                "I made the correct movements without thinking about trying to do so."
                                        },
                                        {
                                            "value": "knew_intentions",
                                            "text": "I knew clearly what I wanted to do."
                                        },
                                        {
                                            "value": "clear_performance",
                                            "text": "It was really clear to me how my performance was going."
                                        },
                                        {
                                            "value": "attention_focused",
                                            "text": "My attention was focused entirely on what I was doing."
                                        },
                                        {
                                            "value": "sense_of_control",
                                            "text": "I had a sense of control over what I was doing."
                                        },
                                        {
                                            "value": "not_concerned_of_others",
                                            "text": "I was not concerned with what others may have been thinking of me."
                                        },
                                        {
                                            "value": "time_seemed_altered",
                                            "text": "Time seemed to alter (either slowed down or speeded up)."
                                        },
                                        {
                                            "value": "enjoyed_experience",
                                            "text": "I really enjoyed the experience."
                                        },
                                        {
                                            "value": "abilities_matched_challenge",
                                            "text": "My abilities matched the high challenge of the situation."
                                        },
                                        {
                                            "value": "things_happened_automatically",
                                            "text": "Things just seemed to be happening automatically."
                                        },
                                        {
                                            "value": "strong_sense_of_intention",
                                            "text": "I had a strong sense of what I wanted to do."
                                        },
                                        {
                                            "value": "performance_awareness",
                                            "text": "I was aware of how well I was performing."
                                        },
                                        {
                                            "value": "easy_focus",
                                            "text": "It was no effort to keep my mind on what was happening."
                                        },
                                        {
                                            "value": "felt_in_control",
                                            "text": "I felt like I could control what I was doing."
                                        },
                                        {
                                            "value": "not_concerned_with_others_evaluation",
                                            "text": "I was not concerned with how others may have been evaluating me."
                                        },
                                        {
                                            "value": "time_seemed_different",
                                            "text": "The way time passed seemed to be different from normal."
                                        },
                                        {
                                            "value": "loved_the_feeling",
                                            "text": 
                                                "I loved the feeling of the performance and want to capture it again."
                                        },
                                        {
                                            "value": "felt_competent",
                                            "text": 
                                                "I felt I was competent enough to meet the high demands of the " \
                                                "situation."
                                        },
                                        {
                                            "value": "automatic_without_thinking",
                                            "text": "I performed automatically, without thinking too much."
                                        },
                                        {
                                            "value": "knew_my_intentions",
                                            "text": "I knew what I wanted to achieve."
                                        },
                                        {
                                            "value": "good_idea_while_performing",
                                            "text": 
                                                "I had a good idea while I was performing about how well I was doing."
                                        },
                                        {
                                            "value": "total_concentration",
                                            "text": "I had total concentration."
                                        },
                                        {
                                            "value": "feeling_of_total_control",
                                            "text": "I had a feeling of total control."
                                        },
                                        {
                                            "value": "no_concern_for_self_presentation",
                                            "text": "I was not concerned with how I was presenting myself."
                                        },
                                        {
                                            "value": "felt_time_went_quickly",
                                            "text": "It felt like time went by quickly."
                                        },
                                        {
                                            "value": "left_feeling_great",
                                            "text": "The experience left me feeling great."
                                        },
                                        {
                                            "value": "challenge_and_skill_are_equal",
                                            "text": "The challenge and my skills were at an equally high level."
                                        },
                                        {
                                            "value": "did_things_spontaneously",
                                            "text": 
                                                "I did things spontaneously and automatically without having to think."
                                        },
                                        {
                                            "value": "goals_clearly_defined",
                                            "text": "My goals were clearly defined."
                                        },
                                        {
                                            "value": "could_tell_how_well_was_doing",
                                            "text": "I could tell by the way I was performing how well I was doing."
                                        },
                                        {
                                            "value": "completely_focused",
                                            "text": "I was completely focused on the task at hand."
                                        },
                                        {
                                            "value": "felt_total_body_control",
                                            "text": "I felt in total control of my body."
                                        },
                                        {
                                            "value": "not_worried_about_what_others_think",
                                            "text": "I was not worried about what others may have been thinking of me."
                                        },
                                        {
                                            "value": "lost_normal_time_awareness",
                                            "text": "I lost my normal awareness of time."
                                        },
                                        {
                                            "value": "expreience_extremely_rewarding",
                                            "text": "I found the experience extremely rewarding."
                                        },
                                    ],
                                    "alternateRows": True,
                                    "isAllRowRequired": True
                                },
                            ],
                            "showQuestionNumbers": "on"
                        },
                    ],
                },
            ),
            time_estimate=5,
            bot_response=lambda: {},
        ),
        DebugResponsePage(),
        SuccessfulEndPage(),
    )
