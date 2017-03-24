from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50,default='First Name', blank=False)
    last_name = models.CharField(max_length=50,default='Last Name', blank=False)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=False)
    birth_date = models.DateField(null=True, blank=False,help_text='Enter date in YYYY-MM-DD format')
    birth_location = models.CharField(max_length=30, blank=False)
    personal_email = models.EmailField(max_length=50, default='@mail.com', blank=False)
    joining_date =  models.DateField(null=True, blank=False,help_text='Enter date in YYYY-MM-DD format')
    work_location = models.CharField(max_length=30, blank=False)
    work_email = models.EmailField(max_length=50,default='@fulcrum.net', blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15,validators=[phone_regex], blank=True)  # validators should be a list
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


