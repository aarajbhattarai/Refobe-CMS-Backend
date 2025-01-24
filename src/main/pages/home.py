from django.utils.translation import gettext_lazy as _
from wagtail.models import PageManager
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from .base import BasePage
from main.blocks import section_blocks


class HomePage(HeadlessPreviewMixin, BasePage):
    content_section = StreamField(
        section_blocks,
        use_json_field=True,
        blank=True,
        null=True,
        verbose_name=_("Content Section"),
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("content_section"),
    ]
    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.HomePageSerializer"

    objects: PageManager

    class Meta:
        verbose_name = _("Home")
