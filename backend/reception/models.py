from django.db import models
from django.core.exceptions import ValidationError
import re
from django_jalali.db import models as jmodels
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
import uuid
class DigitField(models.CharField):
    default_error_messages = {
        'invalid': 'This field should contain only digits.',
    }

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 20)  # Default max_length if not provided
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if not re.match(r'^\d+$', value):
            raise ValidationError(self.error_messages['invalid'], code='invalid')

def get_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "passports/%s.%s" % (uuid.uuid4(), ext)
    return  filename

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    national_code = DigitField(validators = [RegexValidator(regex=r"[0-9]{10}",message="کد ملی وارد شده صحیح نمیباشد")])
    first_time_pilgrim = models.BooleanField()
    gender = models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')])
    passport = models.ImageField(upload_to=get_path, null=True, blank=True)

class Accommodation(models.Model):
    boss = models.ForeignKey(Person,on_delete=models.SET_NULL,null=True,related_name='accommodationrequest_boss')
    members = models.ManyToManyField(Person,related_name='accommodationrequest_members')
    city = models.CharField(choices={('Najaf','Najaf'),('Karbala','Karbala')})
    status = models.CharField(choices=[('accepted','accepted'),('pending','pending'),('rejected','rejected')])
    presented = models.BooleanField(default=True)
    created_date = jmodels.jDateTimeField(auto_now_add=True)
    arrival_date = jmodels.jDateTimeField()
    departure_date = jmodels.jDateTimeField()
