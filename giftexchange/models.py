from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    
    class Meta:
        pass    

class Exchange(models.Model):
    participants = models.ManyToManyField(Participant)
    
    class Meta:
        pass