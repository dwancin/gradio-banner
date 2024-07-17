# Banner - A Gradio Custom Component
# Created by Daniel Ialcin Misser Westergaard
# https://huggingface.co/dwancin
# https://github.com/dwancin
# (c) 2024

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

from gradio.components.base import Component, FormComponent
from gradio.events import Events

if TYPE_CHECKING:
    from gradio.components import Timer


class Banner(FormComponent):
    """
    Creates a banner component for displaying important information, alerts, notifications, and messages.
    """

    EVENTS = [
        Events.change,
        Events.input,
        Events.submit,
    ]

    def __init__(
        self,
        value: str | Callable | None = None,
        *,
        variant: str = "info",
        label: str | None = None,
        icon: str | None = None,
        size: Literal["sm", "lg"] | None = "lg",
        show_close_button: bool = False,
        show_icon: bool = True,
        every: Timer | float | None = None,
        inputs: Component | list[Component] | set[Component] | None = None,
        show_label: bool | None = None,
        scale: int | None = None,
        min_width: int = 160,
        visible: bool = True,
        rtl: bool = False,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        key: int | str | None = None,
    ):
        """
        Parameters:
            value: 
                The main text of the banner. Supports markdown formatting. 
                If a callable, will be executed to get the value.
            variant: 
                Type of banner to display. Options are 'info', 'warning', 'error', and 'success'.
            label: 
                The headline of the banner. Supports markdown formatting.
            icon: 
                URL or path to the icon file to display within the banner. If None, default icon will be used.
            size: 
                Size of the banner. Can be "sm" (small) or "lg" (large). Defaults to "lg".
            show_close_button: 
                If True, shows a close button to hide the banner.
            show_icon: 
                If True, displays the icon specified in the icon parameter. Defaults to True.
            every: 
                Continuously calls `value` to recalculate it if `value` is a function (has no effect otherwise). 
                Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.
            inputs: 
                Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). 
                `value` is recalculated any time the inputs change.
            show_label: 
                If True, will display the label. Defaults to None.
            scale: 
                Relative size compared to adjacent Components. For example, if Components A and B are in a Row, and A has scale=2, 
                and B has scale=1, A will be twice as wide as B. Should be an integer. Scale applies in Rows, and to top-level Components 
                in Blocks where fill_height=True.
            min_width: 
                Minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value 
                results in this Component being narrower than min_width, the min_width parameter will be respected first.
            visible: 
                If False, the component will be hidden. Defaults to True.
            rtl: 
                If True, sets the direction of the text to right-to-left (cursor appears on the left of the text). 
                Default is False, which renders cursor on the right.
            elem_id: 
                An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: 
                An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: 
                If False, the component will not be rendered in the Blocks context. Should be used if the intention is to assign 
                event listeners now but render the component later. Defaults to True.
            key: 
                If assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render 
                will have their value preserved.
        """
        self.variant = variant
        self.icon = icon
        self.size = size
        self.show_close_button = show_close_button
        self.show_icon = show_icon
        self.rtl = rtl
        super().__init__(
            label=label,
            every=every,
            inputs=inputs,
            show_label=show_label,
            scale=scale,
            min_width=min_width,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            render=render,
            key=key,
        )

    def preprocess(self, payload: str | None) -> str | None:
        """
        Parameters:
            payload: the text entered in the textarea.
        Returns:
            Passes text value as a {str} into the function.
        """
        return None if payload is None else str(payload)

    def postprocess(self, value: str | None) -> str | None:
        """
        Parameters:
            value: Expects a {str} returned from function and sets textarea value to it.
        Returns:
            The value to display in the textarea.
        """
        return None if value is None else str(value)

    def api_info(self) -> dict[str, Any]:
        return {"type": "string"}

    def example_payload(self) -> Any:
        return "This is a specific status text example."

    def example_value(self) -> Any:
        return "This is a specific status text example."
