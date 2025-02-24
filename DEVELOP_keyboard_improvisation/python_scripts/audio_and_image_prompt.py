from typing import List, Optional, Union

from markupsafe import Markup
from psynet.asset import Asset
from psynet.modular_page import AudioPrompt
from psynet.timeline import Event


class AudioAndImagePrompt(AudioPrompt):
    """
    Displays an image to the participant.

    Parameters
    ----------

    url
        URL of the image to show.

    text
        Text to display to the participant. This can either be a string
        for plain text, or an HTML specification from ``markupsafe.Markup``.

    width
        CSS width specification for the image (e.g. ``'50%'``).

    height
        CSS height specification for the image (e.g. ``'50%'``).
        ``'auto'`` will choose the height automatically to match the width;
        the disadvantage of this is that other page content may move
        once the image loads.

    show_after
        Specifies the time in seconds when the image will be displayed, calculated relative to the start of the trial.
        Defaults to 0.0.

    hide_after
        If not ``None``, specifies a time in seconds after which the image should be hidden.

    margin_top
        CSS specification of the image's top margin.

    margin_bottom
        CSS specification of the image's bottom margin.

    text_align
        CSS alignment of the text.

    """

    def __init__(
        self,
        audio,
        image_url: str,
        text: Union[str, Markup],
        width: str,
        height: str,
        image_url_2: str = None,
        show_after: float = 0.0,
        hide_after: Optional[float] = None,
        margin_top: str = "0px",
        margin_bottom: str = "0px",
        text_align: str = "left",

        loop: bool = False,
        play_window: Optional[List] = None,
        controls: bool = False,
        fade_in: float = 0.0,
        fade_out: float = 0.0,
        **kwargs,
    ): 
        super().__init__(
            audio=audio,
            text=text,
            text_align=text_align,
            loop=loop, 
            play_window=play_window, 
            controls=controls, 
            fade_in=fade_in, 
            fade_out=fade_out,
            **kwargs,
        )

        if isinstance(image_url, Asset):
            image_url = image_url.url
        self.image_url = image_url

        self.has_post_prompt_image = False
        if isinstance(image_url_2, Asset):
            image_url_2 = image_url_2.url

        if image_url_2:
            self.image_url_2 = image_url_2
            self.has_post_prompt_image = True

        self.width = width
        self.height = height
        self.show_after = show_after
        self.hide_after = hide_after
        self.margin_top = margin_top
        self.margin_bottom = margin_bottom

    external_template = "audio_and_image_prompt.html"
    macro = "audio_and_image"

    @property
    def metadata(self):
        return {
            "text": str(self.text),
            "image_url": self.image_url,
            "show_after": self.show_after,
            "hide_after": self.hide_after,
            "audio_url": self.url,
            "play_window": self.play_window,
        }

    def update_events(self, events):
        super().update_events(events)

        events["promptStart"] = Event(
            is_triggered_by="trialStart", delay=self.show_after
        )

        if self.hide_after is not None:
            events["promptEnd"] = Event(
                is_triggered_by="promptStart", delay=self.hide_after
            )
