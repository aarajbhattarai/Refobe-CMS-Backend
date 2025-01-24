from django.utils.translation import gettext_lazy as _
from customimage.models import CustomImage
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import PageManager
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail.fields import RichTextField, StreamField

from .base import BasePage
from main.blocks import section_blocks


class ArticlePage(HeadlessPreviewMixin, BasePage):
    cover_image = models.ForeignKey(
        CustomImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Cover Image"),
    )
    category = models.CharField(max_length=255, blank=True, null=True)
    content_section = StreamField(
        section_blocks,
        use_json_field=True,
        blank=True,
        null=True,
        verbose_name=_("Content Section"),
    )
    summary = models.TextField(blank=True, null=True)

    content_panels = BasePage.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("content_section"),
    ]

    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.ArticlePageSerializer"

    objects: PageManager

    class Meta:
        verbose_name = _("Article Page")
