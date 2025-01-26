from django.test import TestCase
from django.core.exceptions import ValidationError

from decimal import Decimal
from datetime import date, timedelta
from .models import TravelPackage, PricingRule, Booking

class TravelPackageTests(TestCase):
    def setUp(self):
        self.package = TravelPackage.objects.create(
            title="Test Package",
            category="Adventure",
            description="Test Description",
            base_price=Decimal("100.00"),
            duration_days=5
        )

    def test_travel_package_creation(self):
        self.assertEqual(self.package.title, "Test Package")
        self.assertEqual(self.package.category, "Adventure")
        self.assertEqual(self.package.base_price, Decimal("100.00"))
        self.assertEqual(self.package.duration_days, 5)

    def test_travel_package_str(self):
        self.assertEqual(str(self.package), "Test Package")

class PricingRuleTests(TestCase):
    def setUp(self):
        self.package = TravelPackage.objects.create(
            title="Test Package",
            category="Adventure",
            base_price=Decimal("100.00")
        )
        self.pricing_rule = PricingRule.objects.create(
            package=self.package,
            heading="Group Discount",
            min_people=2,
            max_people=5,
            days=3,
            price=Decimal("80.00")
        )

    def test_pricing_rule_creation(self):
        self.assertEqual(self.pricing_rule.min_people, 2)
        self.assertEqual(self.pricing_rule.max_people, 5)
        self.assertEqual(self.pricing_rule.price, Decimal("80.00"))
        self.assertEqual(self.pricing_rule.package, self.package)

    def test_pricing_rule_str(self):
        expected_str = "Test Package: 2-5 people, 3"
        self.assertEqual(str(self.pricing_rule), expected_str)

    def test_pricing_rule_str_without_days(self):
        rule = PricingRule.objects.create(
            package=self.package,
            min_people=2,
            max_people=5,
            price=Decimal("80.00")
        )
        expected_str = "Test Package: 2-5 people, any"
        self.assertEqual(str(rule), expected_str)

class BookingTests(TestCase):
    def setUp(self):
        self.package = TravelPackage.objects.create(
            title="Test Package",
            category="Adventure",
            base_price=Decimal("100.00")
        )
        self.today = date.today()
        self.booking = Booking.objects.create(
            package=self.package,
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            number_of_people=2,
            total_price=Decimal("200.00"),
            booking_start_date=self.today,
            booking_end_date=self.today + timedelta(days=5)
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.email, "john@example.com")
        self.assertEqual(self.booking.number_of_people, 2)
        self.assertEqual(self.booking.total_price, Decimal("200.00"))

    def test_booking_str(self):
        expected_str = "John Doe - Test Package (2 people)"
        self.assertEqual(str(self.booking), expected_str)

    def test_booking_dates_validation(self):
        # Test invalid dates (end date before start date)
        with self.assertRaises(ValidationError):
            invalid_booking = Booking(
                package=self.package,
                name="Jane Doe",
                email="jane@example.com",
                phone="0987654321",
                number_of_people=1,
                total_price=Decimal("100.00"),
                booking_start_date=self.today,
                booking_end_date=self.today - timedelta(days=1)
            )
            invalid_booking.full_clean()

    def test_booking_ordering(self):
        # Create another booking
        newer_booking = Booking.objects.create(
            package=self.package,
            name="Jane Doe",
            email="jane@example.com",
            phone="0987654321",
            number_of_people=1,
            total_price=Decimal("100.00"),
            booking_start_date=self.today,
            booking_end_date=self.today + timedelta(days=3)
        )
        
        # Get all bookings and check if they're ordered by created_at in descending order
        bookings = Booking.objects.all()
        self.assertEqual(bookings[0], newer_booking)
        self.assertEqual(bookings[1], self.booking)

class ModelRelationshipTests(TestCase):
    def setUp(self):
        self.package = TravelPackage.objects.create(
            title="Test Package",
            category="Adventure",
            base_price=Decimal("100.00")
        )

    def test_pricing_rule_relationship(self):
        rule = PricingRule.objects.create(
            package=self.package,
            min_people=2,
            max_people=5,
            price=Decimal("80.00")
        )
        self.assertEqual(self.package.pricing_rules.count(), 1)
        self.assertEqual(self.package.pricing_rules.first(), rule)

    def test_booking_relationship(self):
        booking = Booking.objects.create(
            package=self.package,
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            number_of_people=2,
            total_price=Decimal("200.00"),
            booking_start_date=date.today(),
            booking_end_date=date.today() + timedelta(days=5)
        )
        self.assertEqual(self.package.bookings.count(), 1)
        self.assertEqual(self.package.bookings.first(), booking)
