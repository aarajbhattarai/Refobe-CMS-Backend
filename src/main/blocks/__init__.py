from .blocks import (
    ArticleSection,
    ContactSection,
    FeatureSection,
    FeatureRowSection,
    FAQSection,
    FAQImageSection,
    HeroSection,
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
    ("hero_section", HeroSection()),
    ("hero_section_carousel", HeroSection()),
    ("hero_slide_section", HeroSection()),
    ("logo_cloud_section", LogoCloudSection()),
    ("richtext_section", RichTextBlock()),
    ("team_section", TeamSection()),
    ("testimonial_section", TestimonialSection()),
]
