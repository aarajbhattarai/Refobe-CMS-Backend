from django.utils.encoding import force_str
from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from wagtail.admin.widgets import AdminTagWidget
from wagtail.blocks import (
    StructBlock,
    CharBlock,

    TextBlock,
    URLBlock,
    ChoiceBlock,
    FieldBlock,
)
from main.blocks.helper_blocks import APIImageChooserBlock, APIPageChooserBlock



class ButtonBlock(StructBlock):
    text = CharBlock(required=False, max_length=100, label="Text",)
    link = URLBlock(
        required=False,
        label="Link",
        null=True,
        blank=True,
        help_text="If provided, the button will be a link to this URL",
    )
    page = APIPageChooserBlock(required=False)
    button_type = ChoiceBlock(
        required=False,
        choices=[("primary", "Primary"), ("secondary", "Secondary")],
        default="primary",
    )

    def clean(self, value):
        cleaned_data = super().clean(value)
        link = cleaned_data.get("link")
        page = cleaned_data.get("page")

        if link and page:
            raise ValidationError('Please provide either "Link" or "Page", not both.')
        if (link or page) and not cleaned_data.get("text"):
            raise ValidationError('Please provide a "Text" for the button.')
        return cleaned_data

    class Meta:
        icon = "placeholder"


class TagsBlock(FieldBlock):
    """
    Basic Stream Block that will use the Wagtail tags system.
    Stores the tags as simple strings only.
    """

    def __init__(self, required=False, help_text=None, **kwargs):
        self.field = forms.CharField(
            widget=AdminTagWidget,
            required=False,
        )
        super().__init__(**kwargs)


class CardBlock(StructBlock):
    heading = TextBlock(
        required=False,
        default="Debugging Tech and Staffing Glitches",
    )
    description = TextBlock(
        required=False,
        label="Description",
        default="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
    )
    image = APIImageChooserBlock(required=False, label="Hero image")

    button = ButtonBlock(required=False, label="Call To Action")


class SectionBlock(StructBlock):
    tag = TagsBlock(label="Tag")
    title = TextBlock(
        required=False,
        default="We are the best",
    )
    description = TextBlock(
        required=False,
        label="Description",
        default="Experience the best of both worlds. Enjoy comfortable accommodations paired with thrilling outdoor activities in a breathtaking natural setting.",
    )


class HashBlock(FieldBlock):
    """Hash values which will allow sections to be automatically linked to using URL hashes
    e.g. link to a page at a particular section could be https://your-site.com/your-page-slug/#your-section-hash
    specifically to be used to in page section rensering throught url

    Can be blank, in which case no hash should be generated for the section.

    This Block is essentially a CharBlock with a custom clean() method.
    """

    def __init__(
        self, required=True, help_text=None, max_length=None, min_length=None, **kwargs
    ):
        self.field = forms.CharField(
            required=required,
            help_text=help_text,
            max_length=max_length,
            min_length=min_length,
        )
        super().__init__(**kwargs)

    def get_searchable_content(self, value):
        return [force_str(value)]

    def clean(self, value):
        if value:
            return slugify("section-" + force_str(value), allow_unicode=False)
        return value


class VideoBlock(StructBlock):
    heading = CharBlock(required=False, max_length=200, label="Video Title")
    video_url = URLBlock(required=True, label="Video URL")
    description = TextBlock(required=False, label="Description")

    class Meta:
        icon = "media"
        label = "Video"
