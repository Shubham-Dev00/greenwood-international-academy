from django.db import models
from django.utils import timezone


class NewsEvent(models.Model):
    CATEGORY_CHOICES = [
        ('News', 'News'),
        ('Event', 'Event'),
        ('Announcement', 'Announcement'),
    ]
    title = models.CharField(max_length=180)
    excerpt = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='News')
    event_date = models.DateField()
    image_url = models.URLField()

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.role}"


class LeadershipMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    image_url = models.URLField()
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return f"{self.name} ({self.designation})"


class FacultyMember(models.Model):
    DEPARTMENT_CHOICES = [
        ('Science', 'Science'),
        ('Arts', 'Arts'),
        ('Commerce', 'Commerce'),
        ('Sports', 'Sports'),
        ('Administration', 'Administration'),
    ]
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    qualification = models.CharField(max_length=120)
    experience_years = models.PositiveIntegerField()
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    image_url = models.URLField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Notification(models.Model):
    CATEGORY_CHOICES = [
        ('Academic', 'Academic'),
        ('Events', 'Events'),
        ('Fees', 'Fees'),
        ('Exams', 'Exams'),
        ('General', 'General'),
    ]
    title = models.CharField(max_length=180)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=50, default='fa-solid fa-circle-info')
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class PaymentRecord(models.Model):
    FEE_TYPE_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annual', 'Annual'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('Card', 'Credit/Debit Card'),
        ('UPI', 'UPI'),
        ('NetBanking', 'Net Banking'),
        ('BankTransfer', 'Bank Transfer'),
    ]
    student_name = models.CharField(max_length=120)
    roll_number = models.CharField(max_length=40)
    class_section = models.CharField(max_length=50)
    fee_type = models.CharField(max_length=20, choices=FEE_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=40, unique=True)
    status = models.CharField(max_length=20, default='Paid')
    payment_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-payment_date']

    def __str__(self):
        return f"{self.student_name} - {self.transaction_id}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Enquiry(models.Model):
    student_name = models.CharField(max_length=120)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    applying_class = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    father_name = models.CharField(max_length=120)
    mother_name = models.CharField(max_length=120)
    occupation = models.CharField(max_length=120)
    income = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    documents = models.CharField(max_length=255)
    referral_source = models.CharField(max_length=100)
    preferred_session = models.CharField(max_length=30)
    special_requirements = models.TextField(blank=True)
    declaration = models.BooleanField(default=False)
    reference_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student_name} ({self.reference_number})"
