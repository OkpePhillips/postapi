from django.db import models

# Create your models here.
from django.db import models

from enum import Enum
class Operations(Enum):
    addition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"

class Task(models.Model):
    operation_type = models.CharField(max_length=250, choices =[(tag.name,tag.value) for tag in Operations])
    x =  models.IntegerField()
    y = models.IntegerField()