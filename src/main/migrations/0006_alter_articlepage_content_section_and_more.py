# Generated by Django 5.1.4 on 2025-01-24 04:28

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_articlepage_content_section_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="content_section",
            field=wagtail.fields.StreamField(
                [
                    ("article_section", 2),
                    ("contact_section", 14),
                    ("faq_section", 22),
                    ("faq_image_section", 24),
                    ("feature_section", 27),
                    ("feature_row_section", 28),
                    ("hero_section", 30),
                    ("hero_section_carousel", 30),
                    ("hero_slide_section", 30),
                    ("logo_cloud_section", 37),
                    ("team_section", 46),
                    ("testimonial_section", 53),
                    ("richtext_section", 54),
                ],
                blank=True,
                block_lookup={
                    0: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "From the blog",
                            "help_text": "Add a title",
                            "label": "Title",
                            "required": False,
                        },
                    ),
                    1: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Learn how to grow your business with our expert advice",
                            "help_text": "Add a description",
                            "label": "Description",
                            "required": False,
                        },
                    ),
                    2: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 0), ("description", 1)]],
                        {},
                    ),
                    3: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Ready To Take The Next Step?",
                            "help_text": "Add a heading at the beginning of this page section",
                            "label": "Heading",
                            "required": False,
                        },
                    ),
                    4: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "This is the paragraph where you can write more details. Keep it meaningful!",
                            "label": "Description",
                            "required": False,
                        },
                    ),
                    5: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "Write your address",
                            "label": "Location 1",
                            "required": False,
                        },
                    ),
                    6: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "Write Country and district",
                            "label": "Location 2",
                            "required": False,
                        },
                    ),
                    7: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "Write Number",
                            "label": "Phone Number",
                            "required": False,
                        },
                    ),
                    8: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "Write email",
                            "label": "Email",
                            "required": False,
                        },
                    ),
                    9: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "default": "Learn More",
                            "label": "Text",
                            "max_length": 100,
                            "required": True,
                        },
                    ),
                    10: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "Link", "required": False},
                    ),
                    11: (
                        "main.blocks.helper_blocks.APIPageChooserBlock",
                        (),
                        {"required": False},
                    ),
                    12: (
                        "wagtail.blocks.ChoiceBlock",
                        [],
                        {
                            "choices": [
                                ("primary", "Primary"),
                                ("secondary", "Secondary"),
                            ],
                            "required": False,
                        },
                    ),
                    13: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("text", 9),
                                ("link", 10),
                                ("page", 11),
                                ("button_type", 12),
                            ]
                        ],
                        {"required": False},
                    ),
                    14: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("title", 3),
                                ("description", 4),
                                ("location1", 5),
                                ("location2", 6),
                                ("phone", 7),
                                ("email", 8),
                                ("button", 13),
                            ]
                        ],
                        {},
                    ),
                    15: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {"default": "We are the best", "required": False},
                    ),
                    16: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Experience the best of both worlds. Enjoy comfortable accommodations paired with thrilling outdoor activities in a breathtaking natural setting.",
                            "label": "Description",
                            "required": False,
                        },
                    ),
                    17: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {"default": "Lorem Ipsum Title", "required": False},
                    ),
                    18: (
                        "main.blocks.helper_blocks.APIImageChooserBlock",
                        (),
                        {"label": "Hero image", "required": False},
                    ),
                    19: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("text", 9),
                                ("link", 10),
                                ("page", 11),
                                ("button_type", 12),
                            ]
                        ],
                        {"label": "Call To Action", "required": False},
                    ),
                    20: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 17),
                                ("description", 16),
                                ("image", 18),
                                ("button", 19),
                            ]
                        ],
                        {},
                    ),
                    21: ("wagtail.blocks.ListBlock", (20,), {"label": "FAQs"}),
                    22: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 15), ("description", 16), ("faqs", 21)]],
                        {},
                    ),
                    23: (
                        "wagtail.blocks.ListBlock",
                        (20,),
                        {"label": "FAQs", "required": False},
                    ),
                    24: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 15), ("description", 16), ("faqs", 23)]],
                        {},
                    ),
                    25: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Why our product is best",
                            "help_text": "Add a heading at the beginning of this page section",
                            "label": "Heading",
                            "required": False,
                        },
                    ),
                    26: ("wagtail.blocks.ListBlock", (20,), {"label": "Features"}),
                    27: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 25), ("features", 26)]],
                        {},
                    ),
                    28: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 15), ("description", 16), ("features", 26)]],
                        {},
                    ),
                    29: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 17),
                                ("description", 16),
                                ("image", 18),
                                ("button", 19),
                            ]
                        ],
                        {"label": "Content", "required": True},
                    ),
                    30: ("wagtail.blocks.StructBlock", [[("content", 29)]], {}),
                    31: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "default": "Our Partners",
                            "help_text": "Add a country name",
                            "label": "Country Name",
                            "required": False,
                        },
                    ),
                    32: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "We serve in 17 countries",
                            "help_text": "Add a description",
                            "label": "Logo Cloud Description",
                            "required": False,
                        },
                    ),
                    33: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "default": "Nepal",
                            "help_text": "Add a country name",
                            "label": "Logo Title",
                            "required": False,
                        },
                    ),
                    34: (
                        "main.blocks.helper_blocks.APIImageChooserBlock",
                        (),
                        {
                            "help_text": "Pick an image for the country logo",
                            "label": "Image",
                            "required": False,
                        },
                    ),
                    35: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 33), ("image", 34)]],
                        {},
                    ),
                    36: ("wagtail.blocks.ListBlock", (35,), {"label": "Images"}),
                    37: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 31), ("description", 32), ("logos", 36)]],
                        {},
                    ),
                    38: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"label": "Name", "max_length": 255, "required": True},
                    ),
                    39: (
                        "main.blocks.helper_blocks.APIImageChooserBlock",
                        (),
                        {"label": "Photo", "required": False},
                    ),
                    40: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "label": "Role / Job Title",
                            "max_length": 255,
                            "required": True,
                        },
                    ),
                    41: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {"label": "Bio", "required": False},
                    ),
                    42: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "LinkedIn Page", "required": False},
                    ),
                    43: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "Twitter Page", "required": False},
                    ),
                    44: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("name", 38),
                                ("image", 39),
                                ("role", 40),
                                ("description", 41),
                                ("linkedin", 42),
                                ("twitter", 43),
                            ]
                        ],
                        {},
                    ),
                    45: (
                        "wagtail.blocks.ListBlock",
                        (44,),
                        {"label": "Team Members", "required": False},
                    ),
                    46: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 15), ("description", 16), ("members", 45)]],
                        {},
                    ),
                    47: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Testimonials",
                            "help_text": "Add a heading at the beginning of this page section",
                            "label": "Heading",
                            "required": False,
                        },
                    ),
                    48: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Our users love us. Look at these rave reviews...",
                            "label": "Description",
                            "required": False,
                        },
                    ),
                    49: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "deafult": "Traveller,CEO",
                            "help_text": "Any subtitle realted to the person",
                            "label": "Role",
                            "max_length": 255,
                            "required": False,
                        },
                    ),
                    50: (
                        "wagtail.blocks.ChoiceBlock",
                        [],
                        {
                            "choices": [
                                (None, "No rating"),
                                (0, "0 Stars"),
                                (1, "1 Star"),
                                (2, "2 Stars"),
                                (3, "3 Stars"),
                                (4, "4 Stars"),
                                (5, "5 Stars"),
                            ],
                            "icon": "pick",
                            "required": False,
                        },
                    ),
                    51: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 17),
                                ("description", 16),
                                ("image", 18),
                                ("button", 19),
                                ("role", 49),
                                ("stars", 50),
                            ]
                        ],
                        {},
                    ),
                    52: ("wagtail.blocks.ListBlock", (51,), {}),
                    53: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 47), ("description", 48), ("testimonials", 52)]],
                        {},
                    ),
                    54: ("wagtail.blocks.RichTextBlock", (), {}),
                },
                null=True,
                verbose_name="Content Section",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="content_section",
            field=wagtail.fields.StreamField(
                [
                    ("article_section", 2),
                    ("contact_section", 14),
                    ("faq_section", 22),
                    ("faq_image_section", 24),
                    ("feature_section", 27),
                    ("feature_row_section", 28),
                    ("hero_section", 30),
                    ("hero_section_carousel", 30),
                    ("hero_slide_section", 30),
                    ("logo_cloud_section", 37),
                    ("team_section", 46),
                    ("testimonial_section", 53),
                    ("richtext_section", 54),
                ],
                blank=True,
                block_lookup={
                    0: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "From the blog",
                            "help_text": "Add a title",
                            "label": "Title",
                            "required": False,
                        },
                    ),
                    1: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Learn how to grow your business with our expert advice",
                            "help_text": "Add a description",
                            "label": "Description",
                            "required": False,
                        },
                    ),
                    2: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 0), ("description", 1)]],
                        {},
                    ),
                    3: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Ready To Take The Next Step?",
                            "help_text": "Add a heading at the beginning of this page section",
                            "label": "Heading",
                            "required": False,
                        },
                    ),
                    4: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "This is the paragraph where you can write more details. Keep it meaningful!",
                            "label": "Description",
                            "required": False,
                        },
                    ),
                    5: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "Write your address",
                            "label": "Location 1",
                            "required": False,
                        },
                    ),
                    6: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "Write Country and district",
                            "label": "Location 2",
                            "required": False,
                        },
                    ),
                    7: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "Write Number",
                            "label": "Phone Number",
                            "required": False,
                        },
                    ),
                    8: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "Write email",
                            "label": "Email",
                            "required": False,
                        },
                    ),
                    9: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "default": "Learn More",
                            "label": "Text",
                            "max_length": 100,
                            "required": True,
                        },
                    ),
                    10: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "Link", "required": False},
                    ),
                    11: (
                        "main.blocks.helper_blocks.APIPageChooserBlock",
                        (),
                        {"required": False},
                    ),
                    12: (
                        "wagtail.blocks.ChoiceBlock",
                        [],
                        {
                            "choices": [
                                ("primary", "Primary"),
                                ("secondary", "Secondary"),
                            ],
                            "required": False,
                        },
                    ),
                    13: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("text", 9),
                                ("link", 10),
                                ("page", 11),
                                ("button_type", 12),
                            ]
                        ],
                        {"required": False},
                    ),
                    14: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("title", 3),
                                ("description", 4),
                                ("location1", 5),
                                ("location2", 6),
                                ("phone", 7),
                                ("email", 8),
                                ("button", 13),
                            ]
                        ],
                        {},
                    ),
                    15: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {"default": "We are the best", "required": False},
                    ),
                    16: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Experience the best of both worlds. Enjoy comfortable accommodations paired with thrilling outdoor activities in a breathtaking natural setting.",
                            "label": "Description",
                            "required": False,
                        },
                    ),
                    17: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {"default": "Lorem Ipsum Title", "required": False},
                    ),
                    18: (
                        "main.blocks.helper_blocks.APIImageChooserBlock",
                        (),
                        {"label": "Hero image", "required": False},
                    ),
                    19: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("text", 9),
                                ("link", 10),
                                ("page", 11),
                                ("button_type", 12),
                            ]
                        ],
                        {"label": "Call To Action", "required": False},
                    ),
                    20: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 17),
                                ("description", 16),
                                ("image", 18),
                                ("button", 19),
                            ]
                        ],
                        {},
                    ),
                    21: ("wagtail.blocks.ListBlock", (20,), {"label": "FAQs"}),
                    22: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 15), ("description", 16), ("faqs", 21)]],
                        {},
                    ),
                    23: (
                        "wagtail.blocks.ListBlock",
                        (20,),
                        {"label": "FAQs", "required": False},
                    ),
                    24: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 15), ("description", 16), ("faqs", 23)]],
                        {},
                    ),
                    25: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Why our product is best",
                            "help_text": "Add a heading at the beginning of this page section",
                            "label": "Heading",
                            "required": False,
                        },
                    ),
                    26: ("wagtail.blocks.ListBlock", (20,), {"label": "Features"}),
                    27: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 25), ("features", 26)]],
                        {},
                    ),
                    28: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 15), ("description", 16), ("features", 26)]],
                        {},
                    ),
                    29: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 17),
                                ("description", 16),
                                ("image", 18),
                                ("button", 19),
                            ]
                        ],
                        {"label": "Content", "required": True},
                    ),
                    30: ("wagtail.blocks.StructBlock", [[("content", 29)]], {}),
                    31: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "default": "Our Partners",
                            "help_text": "Add a country name",
                            "label": "Country Name",
                            "required": False,
                        },
                    ),
                    32: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "We serve in 17 countries",
                            "help_text": "Add a description",
                            "label": "Logo Cloud Description",
                            "required": False,
                        },
                    ),
                    33: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "default": "Nepal",
                            "help_text": "Add a country name",
                            "label": "Logo Title",
                            "required": False,
                        },
                    ),
                    34: (
                        "main.blocks.helper_blocks.APIImageChooserBlock",
                        (),
                        {
                            "help_text": "Pick an image for the country logo",
                            "label": "Image",
                            "required": False,
                        },
                    ),
                    35: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 33), ("image", 34)]],
                        {},
                    ),
                    36: ("wagtail.blocks.ListBlock", (35,), {"label": "Images"}),
                    37: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 31), ("description", 32), ("logos", 36)]],
                        {},
                    ),
                    38: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"label": "Name", "max_length": 255, "required": True},
                    ),
                    39: (
                        "main.blocks.helper_blocks.APIImageChooserBlock",
                        (),
                        {"label": "Photo", "required": False},
                    ),
                    40: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "label": "Role / Job Title",
                            "max_length": 255,
                            "required": True,
                        },
                    ),
                    41: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {"label": "Bio", "required": False},
                    ),
                    42: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "LinkedIn Page", "required": False},
                    ),
                    43: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "Twitter Page", "required": False},
                    ),
                    44: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("name", 38),
                                ("image", 39),
                                ("role", 40),
                                ("description", 41),
                                ("linkedin", 42),
                                ("twitter", 43),
                            ]
                        ],
                        {},
                    ),
                    45: (
                        "wagtail.blocks.ListBlock",
                        (44,),
                        {"label": "Team Members", "required": False},
                    ),
                    46: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 15), ("description", 16), ("members", 45)]],
                        {},
                    ),
                    47: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Testimonials",
                            "help_text": "Add a heading at the beginning of this page section",
                            "label": "Heading",
                            "required": False,
                        },
                    ),
                    48: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "default": "Our users love us. Look at these rave reviews...",
                            "label": "Description",
                            "required": False,
                        },
                    ),
                    49: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "deafult": "Traveller,CEO",
                            "help_text": "Any subtitle realted to the person",
                            "label": "Role",
                            "max_length": 255,
                            "required": False,
                        },
                    ),
                    50: (
                        "wagtail.blocks.ChoiceBlock",
                        [],
                        {
                            "choices": [
                                (None, "No rating"),
                                (0, "0 Stars"),
                                (1, "1 Star"),
                                (2, "2 Stars"),
                                (3, "3 Stars"),
                                (4, "4 Stars"),
                                (5, "5 Stars"),
                            ],
                            "icon": "pick",
                            "required": False,
                        },
                    ),
                    51: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 17),
                                ("description", 16),
                                ("image", 18),
                                ("button", 19),
                                ("role", 49),
                                ("stars", 50),
                            ]
                        ],
                        {},
                    ),
                    52: ("wagtail.blocks.ListBlock", (51,), {}),
                    53: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 47), ("description", 48), ("testimonials", 52)]],
                        {},
                    ),
                    54: ("wagtail.blocks.RichTextBlock", (), {}),
                },
                null=True,
                verbose_name="Content Section",
            ),
        ),
    ]