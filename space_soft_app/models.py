from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 110)
    email = models.EmailField()
    contact = models.CharField(max_length = 110, null=True)
    address = models.CharField(max_length = 110, null=True)
    message = models.TextField()


class Course_Intrest(models.Model):
    name = models.CharField(max_length=110)
    email = models.EmailField()
    contact = models.CharField(max_length = 110, null=True)
    address = models.CharField(max_length = 110, null=True)
    course = models.CharField(max_length = 110, choices=[
        ('web', 'Web Development'),
        ('design', 'UI/UX Design'),
        ('android_dev', 'Android Development'),
        ('IOS_dev', 'IOS Development'),
        ('solar', 'Solar Installation'),
        ('electronics', 'Electronics'),
    ])
    message = models.TextField()


COURSES = [
        ('Web Development', 'Web Development'),
        ('UI/UX Design', 'UI/UX Design'),
        ('Android Development', 'Android Development'),
        ('IOS Development', 'IOS Development'),
        ('Solar Installation', 'Solar Installation'),
        ('Electronics', 'Electronics'),
    ]
CLASSES = [
    ('Onsite', 'Onsite'),
    ('Online', 'Online'),
]
class Student(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=10, choices=[("Single", "Single"), ("Married", "Married")])
    state_of_origin = models.CharField(max_length=100)
    lga = models.CharField(max_length=100, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)

    # Contact Information
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    residential_address = models.TextField()
    emergency_name = models.CharField(max_length=100)
    emergency_relationship = models.CharField(max_length=50)
    emergency_phone = models.CharField(max_length=20, null=True, blank=True)

    # Academic Background
    highest_qualification = models.CharField(max_length=50)
    institution = models.CharField(max_length=150, blank=True)
    graduation_year = models.CharField(max_length=14, blank=True)
    field_of_study = models.CharField(max_length=100)
    relevant_skills = models.TextField(blank=True)

    #Course section
    course = models.CharField(max_length = 110, choices=COURSES)
    class_mode = models.CharField(max_length = 110, choices=CLASSES, default = "Onsite")
    reason = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.full_name
