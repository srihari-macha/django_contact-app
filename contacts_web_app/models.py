from django.db import models

class add_contact_mod(models.Model):
    name=models.CharField(max_length=30)
    phone_no=models.CharField(max_length=12)
    email=models.CharField(max_length=30)
    street=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=30)
    pin_code=models.IntegerField()


class provider(models.Model):
    prov_name=models.CharField(max_length=30)
    prov_list=models.CommaSeparatedIntegerField(max_length=50)