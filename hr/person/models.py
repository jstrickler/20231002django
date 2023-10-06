import uuid
from django.db import models

# Create your models here.

class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    editable=False, help_text="Unique ID of this city")
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'
#        verbose_name = "metropolis"
        verbose_name_plural = "cities"

class Complaint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    editable=False, help_text="Unique ID of this complaint")
    text = models.CharField(max_length=128)

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    editable=False, help_text="Unique ID of this user")
    first_name = models.CharField(max_length=32, verbose_name="First Name")
    last_name = models.CharField(max_length=32)
    email_address = models.EmailField(max_length=64)
    salary = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Annual Pay")
    position = models.CharField(max_length=32)
    start_date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["last_name", "first_name"]