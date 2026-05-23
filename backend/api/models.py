from django.db import models


class Application(models.Model):

    ROLE_CHOICES = [
        ('web-development', 'Web Development'),
        ('python', 'Python Development'),
        ('data-analyst', 'Data Analyst'),
        ('ui-ux', 'UI/UX Design'),
    ]

    DURATION_CHOICES = [
        ('30', '30 Days'),
        ('45', '45 Days'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    duration = models.CharField(max_length=10, choices=DURATION_CHOICES)
    college = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return self.name

    #interns schema

class Intern(models.Model):

    DURATION_CHOICES = [
        ("30 Days", "30 Days"),
        ("45 Days", "45 Days"),
        
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=100)

    college_name = models.CharField(max_length=200)

    course = models.CharField(max_length=100)

    internship_field = models.CharField(max_length=100)

    duration = models.CharField(
        max_length=20,
        choices=DURATION_CHOICES
    )

    start_date = models.DateField()

    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name