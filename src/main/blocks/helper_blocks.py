from wagtail.blocks import PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class APIImageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                "id": value.id,
                "url": value.file.url,
                "width": value.width,
                "height": value.height,
            }


class APIPageChooserBlock(PageChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                "id": value.id,
                "title": value.title,
                "url": value.url,
            }


class APIPackageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                "id": value.id,
                "title": value.title,
                "price": value.price,
                "location": value.location,
                "category": value.category,
            }
