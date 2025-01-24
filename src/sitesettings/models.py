from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField


@register_setting
class SiteSetting(BaseSiteSetting):
    gtm_id = models.CharField(max_length=50, blank=True)
    google_site_verification = models.CharField(max_length=255, blank=True)
    facebook = models.URLField(blank=True, null=True)
    facebook_pixel = models.CharField(max_length=255, blank=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    linkedin_pixel= models.CharField(max_length=255, blank=True)
    x_twitter = models.URLField(blank=True, null=True)

    cookie_content = RichTextField(
        blank=True, null=True, verbose_name=_("Cookie bar content"), features=[]
    )

    panels = [FieldPanel("gtm_id"), FieldPanel("cookie_content"),FieldPanel("facebook"),
              FieldPanel("facebook_pixel"),
              FieldPanel("instagram"),
              FieldPanel("linkedin"),
              FieldPanel("linkedin_pixel"),
              FieldPanel("x_twitter"),
              FieldPanel("google_site_verification"),
              ]

    def __str__(self):
        return str(self.site)

    class Meta:
        verbose_name = _("Site setting")
        verbose_name_plural = _("Site settings")
