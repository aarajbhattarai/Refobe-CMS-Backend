from rest_framework import serializers

from sitesettings.models import SiteSetting


class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = ["gtm_id", "cookie_content","facebook","instagram","linkedin","x_twitter"]
