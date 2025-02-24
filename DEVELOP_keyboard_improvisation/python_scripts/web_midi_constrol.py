from psynet.modular_page import Control
from psynet.utils import NoArgumentProvided

class WebMidiControl(Control):
    """
    Records MIDI keyboard input from a participant.

    # Parameters
    # ----------

    # personal
    #     Whether the recording should be marked as 'personal' and hence excluded from 'scrubbed' data exports.
    #     Default: `True`.

    **kwargs
        Further arguments passed to :class:`~psynet.modular_page.WebMidiControl`
    """

    external_template = "web_midi_control.html"
    macro = "web_midi"

    def __init__(
        self,
        *,
        personal=True,
        is_sound_enabled=True,
        has_reinitialize_connection_button=False,
        bot_response=NoArgumentProvided,
        **kwargs,
    ):
        super().__init__(bot_response, **kwargs)

        self.personal = personal
        self.is_sound_enabled = is_sound_enabled
        self.has_reinitialize_connection_button = has_reinitialize_connection_button


    def get_bot_response(self, experiment, bot, page, prompt):
        raise NotImplementedError
