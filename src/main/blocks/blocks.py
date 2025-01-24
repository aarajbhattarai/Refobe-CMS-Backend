from main.blocks.common_blocks import ButtonBlock, CardBlock, VideoBlock, SectionBlock
from main.blocks.helper_blocks import APIImageChooserBlock
from wagtail.blocks import (
    StructBlock,
    ListBlock,
    CharBlock,
    TextBlock,
    URLBlock,
    ChoiceBlock,
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField


from wagtail.snippets.blocks import SnippetChooserBlock


class ArticleSection(StructBlock):
    title = TextBlock(
        required=False,
        label="Title",
        default="From the blog",
        help_text="Add a title",
    )

    description = TextBlock(
        required=False,
        label="Description",
        default="Learn how to grow your business with our expert advice",
        help_text="Add a description",
    )

    class Meta:
        icon = "pick"
        label = "Article Section"


class ContactSection(StructBlock):
    title = TextBlock(
        required=False,
        label="Heading",
        default="Ready To Take The Next Step?",
        help_text="Add a heading at the beginning of this page section",
    )
    description = TextBlock(
        required=False,
        label="Description",
        help_text="This is the paragraph where you can write more details. Keep it meaningful!",
    )
    location1 = TextBlock(
        required=False,
        label="Location 1",
        help_text="Write your address",
    )
    location2 = TextBlock(
        required=False,
        label="Location 2",
        help_text="Write Country and district",
    )
    phone = TextBlock(
        required=False,
        label="Phone Number",
        help_text="Write Number",
    )
    email = TextBlock(
        required=False,
        label="Email",
        help_text="Write email",
    )
    button = ButtonBlock(required=False)

    class Meta:
        icon = "user"
        label = "Contact Section"

class FAQBlock(StructBlock):
    question = TextBlock(
        required=True,
        label="Question",
        help_text="Add a simply worded question, like 'How much will it cost?'",
    )
    answer = TextBlock(
        required=True,
        label="Answer",
        help_text="Provide a short answer in no more than a few lines of text",
    )
    button = ButtonBlock(
        required=False,
        label="Button",
        help_text="Add a link to be followed for more information on that question, feature or product",
    )

    class Meta:
        icon = "help"
        label = "FAQ"


class FAQSection(SectionBlock):
    faqs = ListBlock(CardBlock(), label="FAQs")

    class Meta:
        icon = "help"
        label = "FAQs Section"


class FAQImageSection(SectionBlock):
    faqs = ListBlock(CardBlock(), required=False, label="FAQs")

    class Meta:
        icon = "help"
        label = "FAQs with Image Section"


class FeatureRowSection(SectionBlock):
    long_description = TextBlock(
        required=False,
        label="Long Description",
        help_text="This is the paragraph where you can write more details about your product. Keep it meaningful!",
    )
    image = APIImageChooserBlock(
        required=False,
        label="Image",
        help_text="Pick an image for the side panel of a feature list",
    )
    features = ListBlock(CardBlock(), label="Feature Rows")

    class Meta:
        icon = "list-ul"
        label = "Feature Row ImagesSection, Description, Image Cards"


class FeatureSection(SectionBlock):
    features = ListBlock(CardBlock(), label="Features")

    class Meta:
        icon = "list-ul"
        label = "Features"


class HeroSection(StructBlock):
    content = CardBlock(required=True, label="Content")


class HeroSectionCarousel(StructBlock):
    content = ListBlock(CardBlock(), label="Carousel Images")


class HeroSlideSection(StructBlock):
    title = TextBlock(
        required=False,
        label="Title",
        default="Unwind in Luxury, Explore the Wilderness",
    )
    description = TextBlock(
        required=False,
        label="Description",
        default="Experience the best of both worlds at our resort in Bardiya National Park. Enjoy comfortable accommodations paired with thrilling outdoor activities in a breathtaking natural setting.",
    )
    images = ListBlock(APIImageChooserBlock(), label="Images")
    button = ButtonBlock(required=False, label="Call To Action")


class TeamMemberBlock(StructBlock):
    name = CharBlock(required=True, max_length=255, label="Name")
    image = APIImageChooserBlock(required=False, label="Photo")
    role = CharBlock(required=True, max_length=255, label="Role / Job Title")
    description = TextBlock(required=False, label="Bio")
    linkedin = URLBlock(required=False, label="LinkedIn Page")
    twitter = URLBlock(required=False, label="Twitter Page")

    class Meta:
        icon = "user"
        label = "Team Member"


class TeamSection(SectionBlock):

    members = ListBlock(TeamMemberBlock(), required=False, label="Team Members")

    class Meta:
        icon = "group"
        label = "team"





class TestimonialBlock(CardBlock):
    role = CharBlock(
        required=False,
        max_length=255,
        label="Role",
        deafult="Traveller,CEO",
        help_text="Any subtitle realted to the person",
    )
    stars = ChoiceBlock(
        required=False,
        choices=[
            (None, "No rating"),
            (0, "0 Stars"),
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ],
        icon="pick",
    )

    class Meta:
        icon = "people"
        label = "Testimonials from People"


class TestimonialSection(SectionBlock):
    testimonials = ListBlock(TestimonialBlock())

    class Meta:
        icon = "pick"
        label = "Testimonials Section"



class LogoCloudBlock(SectionBlock):
    heading = CharBlock(
        required=False,
        label="Heading",
        default="Refobe LLC",
        help_text="Add a heading at the beginning of this page section",
    )
    image = APIImageChooserBlock(
        required=False,
        label="Image",
        help_text="Pick an image for the country logo",
    )

    class Meta:
        icon = "list-ul"
        label = "Logos"


class LogoCloudSection(SectionBlock):

    logos = ListBlock(LogoCloudBlock(), label="Images")

    class Meta:
        icon = "pick"
        label = "Logo Cloud Section"
