import psynet.experiment
from psynet.consent import MainConsent
from psynet.page import DebugResponsePage, InfoPage, SuccessfulEndPage
from psynet.timeline import Module, Timeline

from markupsafe import Markup

# Importing the different parts of the survey
from .tasks_parts.basic_demographics_questionaire.experiment import basic_demographics_questionaire
from .tasks_parts.musical_background_questionnaire.experiment import musical_background_questionnaire
from .tasks_parts.creative_achievement_questionnaire.experiment import creative_achievement_questionnaire
from .tasks_parts.swedish_musical_achievements_questionnaire.experiment import swedish_musical_achievements_questionnaire
from .tasks_parts.state_flow_questionnaire.experiment import state_flow_questionnaire
from .tasks_parts.divergent_association_task.experiment import divergent_association_task


# Assets loading
all_assets = {}


# Intermediate pages
welcome_page = InfoPage(
    Markup(
        """
        <h1> Welcome to the musical improvisation test! </h1> <br>
        In this task, you will be asked a few questions about yourself and your musical background.
        <br><br>
        In the next page, you will be asked to agree to a conscent form.
        <br>
        """
    ),
    time_estimate=5,
)

survey_part_info = InfoPage(
    Markup(
        """
        <h1> Welcome to the survey part of the experiment! </h1> <br>
        In this task, you will be asked a few questions about yourself and your musical background.
        <br><br>
        In the next page, you will start with a few questions to get to know you better.
        <br>
        """
    ),
    time_estimate=5,
)

survey_part_end_info = InfoPage(
    Markup(
        """
        <h1> The surveys are completed! </h1> <br>
        Thank you for your answers. This concludes the survey part of the experiment.
        <br><br>
        In the next page, we will introduce the musical improvisation task that you will complete.
        <br>
        """
    ),
    time_estimate=5,
)

music_part_info = InfoPage(
    Markup(
        """
        <h1> Welcome to the musical improvisation test! </h1> <br>
        In this task, you will be asked a few questions about yourself and your musical background.
        <br><br>
        In the next page, you will be go through the preparation steps to make sure that your setup is properly 
        set to complete the musical improvisation task.
        <br>
        """
    ),
    time_estimate=5,
)

task_to_come = InfoPage(
    Markup(
        """
        <h1> This will be the Musical Divergent Thinking Test part with the piano </h1> <br>
        """
    ),
    time_estimate=5,
)

music_part_end_info = InfoPage(
    Markup(
        """
        <h1> The musical improvidation test is completed! </h1> <br>
        <br>
        In the next page, we will ask you a few questions regarding your experience.
        <br>
        """
    ),
    time_estimate=5,
)

divergent_association_part_info = InfoPage(
    Markup(
        """
        <h1> Last task! </h1> <br>
        <br>
        We will now enter the last phase of the experiment.
        <br>
        In the next page, we will ask you to write write some words according to a specific instruction. You will have 
        a maximum of 10 minutes to complete the task. Please make sure you are ready to use your keyboard and then 
        proceed to the next final step. 
        """
    ),
    time_estimate=5,
)

divergent_association_end_info = InfoPage(
    Markup(
        """
        <h1> Thank you for your participation! </h1> <br>
        <br>
        This concludes today's experiment. Thank you for your participation! Please follow the instructions on the 
        next page to claim your compensation.
        """
    ),
    time_estimate=5,
)

# Definition of the experiment
class Exp(psynet.experiment.Experiment):
    label = "MDTT Project"
    initial_recruitment_size = 1

    timeline = Timeline(
        welcome_page,
        MainConsent(),
        Module(
            "MDTT Project Surveys",
            survey_part_info,
            basic_demographics_questionaire,
            musical_background_questionnaire,
            creative_achievement_questionnaire,
            swedish_musical_achievements_questionnaire,
            survey_part_end_info,
            assets=all_assets,
        ),
        Module(
            "MDTT Project Musical Improvidation",
            music_part_info,
            task_to_come,
            music_part_end_info,
            state_flow_questionnaire,
            assets=all_assets,
        ),
        Module(
            "MDTT Project Divergent Association Task",
            divergent_association_part_info,
            divergent_association_task,
            divergent_association_end_info,
            assets=all_assets,
        ),
        DebugResponsePage(),
        SuccessfulEndPage(),
    )
