from django.db import models
from django.core.exceptions import ValidationError
from wagtail.admin.panels import FieldPanel,InlinePanel,MultiFieldPanel
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


class TravelPackage(ClusterableModel):
    """
    Represents a travel package as a snippet.
    """
    title = models.CharField(max_length=255, help_text="Name of the package")
    category= models.CharField(max_length=255, help_text="Category of the package")
    description = models.TextField(blank=True, help_text="Details about the package")
    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Base price for a single person"
    )
    duration_days = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Number of days for the package"
    )
    image = models.ImageField(upload_to='travel_packages', blank=True, null=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('base_price'),
        FieldPanel('duration_days'),
        FieldPanel('image'),
        InlinePanel('pricing_rules', label="Pricing Rules"),
    ]

    def __str__(self):
        return self.title


class PricingRule(models.Model):
    """
    Represents pricing rules for a travel package.
    """
    package = ParentalKey(
        TravelPackage,
        related_name='pricing_rules',
        on_delete=models.CASCADE
    )
    heading= models.CharField(null=True,blank=True)
    min_people = models.PositiveIntegerField(help_text="Minimum group size")
    max_people = models.PositiveIntegerField(help_text="Maximum group size")

    days = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Maximum duration in days (optional)"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price for the specified group size and duration"
    )

    panels = [
        FieldPanel('heading'),
        FieldPanel('min_people'),
        FieldPanel('max_people'),
        FieldPanel('days'),
        FieldPanel('price'),
    ]

    def __str__(self):
        return (
            f"{self.package.title}: {self.min_people}-{self.max_people} people, "
            f"{self.days or 'any'}"
        )


class Booking(models.Model):
    """
    Represents a booking for a travel package with date range.
    """
    package = models.ForeignKey(TravelPackage, related_name='bookings', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text="Name of the person booking")
    email = models.EmailField(help_text="Email address of the person booking")
    phone = models.CharField(max_length=15, help_text="Phone number of the person booking")
    number_of_people = models.PositiveIntegerField(help_text="Number of people in the booking")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total price for the booking")
    booking_start_date = models.DateField(help_text="Start date of the booking")
    booking_end_date = models.DateField(help_text="End date of the booking")
    created_at = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('package'),
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('number_of_people'),
        MultiFieldPanel(
            [
                FieldPanel('booking_start_date'),
                FieldPanel('booking_end_date'),
            ],
            heading="Booking Dates"
        ),
        FieldPanel('total_price'),
    ]

    def clean(self):
        """
        Ensure the booking start date is before the end date.
        """
        if self.booking_start_date > self.booking_end_date:
            raise ValidationError("Booking start date cannot be later than the end date.")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.package.title} ({self.number_of_people} people)"
