from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
MALE = "MALE"
FEMALE = "MALE"
GENDER = (
    (MALE,MALE),
    (FEMALE,FEMALE),
)
class User(AbstractUser):
    is_member = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=15, choices=GENDER, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def get_full_name(self):
        return "{}, {}".format(self.first_name,self.last_name)

    def get_name_is_empty(self):
        if not self.first_name or not self.last_name:
            return False
        return True
