import psynet.experiment
from psynet.consent import NoConsent
from psynet.modular_page import ModularPage, SurveyJSControl
from psynet.page import DebugResponsePage, SuccessfulEndPage
from psynet.timeline import Timeline


def generate_count_question(name, title, choices_category):
    
    choices = []
    if choices_category == 'small':
        choices = [
            "0",
            "1",
            "2",
            "3",
            "4-5",
            "6-9",
            "10 or more",
        ]
    elif choices_category == 'medium':
        choices = [
            "0",
            "1-2",
            "3-5",
            "6-9",
            "10-14",
            "15-24",
            "25-40",
            "41 or more",
        ]
    else:
        choices = [
            "0",
            "1-3",
            "4-10",
            "11-32",
            "33-100",
            "101-302",
            "321-1000",
            "1001 or more",
        ]

    return {
        "type": "radiogroup",
        "name": name,
        "title": title,
        "isRequired": True,
        "choices": choices,
    }


swedish_musical_achievements_questionnaire = ModularPage(
    "swedish_musical_achievements_questionnaire",
    "This questionnaire will ask you a few questions to better understand your achievements in music.",
    SurveyJSControl(
        {
            "logoPosition": "right",
            "pages": [
                {
                    "name": "page_1",
                    "elements": [
                        {
                            "type": "radiogroup",
                            "name": "stage_in_music",
                            "title": "At what stage do you find yourself as a musician?",
                            "isRequired": True,
                            "choices": [
                                "Still studying at a music academy/conservatory",
                                "Graduated and professionally active",
                            ]
                        },
                        {
                            "type": "text",
                            "name": "main_genre",
                            "title": "In what genre are you mainly active as a musician?",
                            "isRequired": True,
                        },
                        {
                            "type": "radiogroup",
                            "name": "main_occupation",
                            "title": "Within this genre, what is your main occupation as a musician?",
                            "isRequired": True,
                            "choices": [
                                "Instrumentalist: Soloist and member of small ensembles " \
                                "(chamber music groups, bands, etc.)",
                                "Instrumentalist: orchestral musician",
                                "Singer: Soloist",
                                "Singer: Vocal ensemble/choir",
                                "Composer",
                                "Music teacher",
                            ],
                            "showOtherItem": True,
                        },
                    ],
                },
                {
                    "name": "page_2",
                    "elements": [
                        generate_count_question(
                            name="musics_composed_count", 
                            title="How many music pieces have you composed?",
                            choices_category="large"
                        ),
                        generate_count_question(
                            name="works_as_orchestral_musician_count", 
                            title="How many different works have you performed as an orchestral musician?",
                            choices_category="large"
                        ),
                        generate_count_question(
                            name="works_as_singer_or_instrumentalist_count", 
                            title=
                                "How many different works have you performed in concert as a singer or " \
                                "instrumentalist (counting only solo works and works for small ensembles)?",
                            choices_category="large"
                        ),
                        generate_count_question(
                            name="students_count", 
                            title=
                                "How many pupils/students have you had in individual tuition as a music " \
                                "teacher?",
                            choices_category="large"
                        ),
                        generate_count_question(
                            name="albums_as_composer_count", 
                            title=
                                "On how many album recordings are you represented as a composer or with " \
                                "your own improvisations?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="radio_television_as_composer_count", 
                            title=
                                "On how many radio or television recordings are you represented as a " \
                                "composer or with your own improvisations?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="albums_as_orchestral_musician_count", 
                            title="On how many albums are you represented as an orchestral musician?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="radio_television_as_orchestral_musician_count", 
                            title=
                                "On how many radio or television recordings are you represented as an " \
                                "orchestral musician?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="albums_as_instrumentalist_count", 
                            title=
                                "On how many album recordings are you represented as an instrumentalist " \
                                "(counting only solo works and works for small ensembles)?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="radio_television_as_instrumentalist_count", 
                            title=
                                "On how many radio or television recordings are you represented as an " \
                                "instrumentalist (counting only solo works and works for small ensembles)?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="albums_as_signer_count", 
                            title=
                                "On how many album recordings are you represented as a singer (counting only " \
                                "solo works and works for small ensembles)?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="radio_television_as_signer_count", 
                            title=
                                "On how many radio or television recordings are you represented as a singer " \
                                "(counting only solo works and works for small ensembles)?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="reviewed_as_musician_in_newspaper_count", 
                            title=
                                "How many times have you been reviewed individually as a musician " \
                                "(composer/instrumentalist/singer) in nationwide newspapers in Sweden " \
                                "or abroad?",
                            choices_category="large"
                        ),
                        generate_count_question(
                            name="reviewed_as_musician_in_journals_count", 
                            title=
                                "How many times have you been reviewed individually as a musician in " \
                                "international professional journals (Gramophone, FonoForum, Diapason etc.)?",
                            choices_category="large"
                        ),
                        generate_count_question(
                            name="received_award_for_journal_count", 
                            title=
                                "How many times have you received an award (e.g. Diapason d'or, Recording of " \
                                "the Month/Year etc.) for a recording or a concert in an international " \
                                "professional journal (counting only solo works and works for small " \
                                "ensembles)?",
                            choices_category="small"
                        ),
                        generate_count_question(
                            name="junior_competition_awards_count", 
                            title=
                                "How many times have you won a prize as a musician in an international " \
                                "competition for juniors (< 18 years of age)?",
                            choices_category="small"
                        ),
                        generate_count_question(
                            name="adult_competition_awards_count", 
                            title=
                                "How many times have you won a prize as a musician in an international " \
                                "competition for adults (> 18 years of age)?",
                            choices_category="small"
                        ),
                        generate_count_question(
                            name="jury_as_junior_count", 
                            title=
                                "How many times have you been invited to participate as a member of the jury " \
                                "at an international music competition for juniors (< 18 years of age)?",
                            choices_category="small"
                        ),
                        generate_count_question(
                            name="jury_as_adult_count", 
                            title=
                                "How many times have you been invited to participate as a member of the jury " \
                                "at an international music competition for adults (> 18 years of age)?",
                            choices_category="small"
                        ),
                        generate_count_question(
                            name="awards_for_work_as_musician_count", 
                            title=
                                "How many awards, medals or other awards for your work as a musician have " \
                                "you received? Include membership or honorary membership of academies and " \
                                "the like.",
                            choices_category="small"
                        ),
                        generate_count_question(
                            name="students_becoming_musicians_count", 
                            title=
                                "How many of your pupils/students are now studying to become professional " \
                                "musicians or are working as professional musicians?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="students_won_junior_competition_count",
                            title=
                                "How many of your students have won a prize in an international music " \
                                "competition for juniors (< 18 years of age)?",
                            choices_category="medium"
                        ),
                        generate_count_question(
                            name="students_won_adult_competition_count",
                            title=
                                "How many of your students have won a prize in an international music "
                                "competition for adults (> 18 years of age)?",
                            choices_category="medium"
                        ),
                    ],
                },
            ],
        },
    ),
    time_estimate=5,
    bot_response=lambda: {},
)