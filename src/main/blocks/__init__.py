from .blocks import (
    ArticleSection,
    ContactSection,
    FeatureSection,
    FeatureRowSection,
    FeatureCarouselSection,
    FAQSection,
    FAQImageSection,
    HeroSection,
    HeroCarouselSection,
    HeroSlideSection,
    LogoCloudSection,
    TeamSection,
    TestimonialSection,
)  # noqa
from wagtail.blocks import RichTextBlock

# noqa avoids "unused imports in __init__.py" error when using flake8


# Simply add this to any existing list of streamfield s in a content panel to enable creation of sections
section_blocks = [
    ("article_section", ArticleSection()),
    ("contact_section", ContactSection()),
    ("faq_section", FAQSection()),
    ("faq_image_section", FAQImageSection()),
    ("feature_section", FeatureSection()),
    ("feature_row_section", FeatureRowSection()),
    ("feature_carousel_section", FeatureCarouselSection()),
    ("hero_section", HeroSection()),
    ("hero_section_carousel", HeroSlideSection()),
    ("hero_slide_section", HeroCarouselSection()),
    ("logo_cloud_section", LogoCloudSection()),
    ("richtext_section", RichTextBlock()),
    ("team_section", TeamSection()),
    ("testimonial_section", TestimonialSection()),
]
