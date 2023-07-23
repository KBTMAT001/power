from django.db import models

# Create your models here.
class Enquiry(models.Model):
    company = models.CharField(max_length=200)
    date_sent = models.DateTimeField('date_sent')
    person = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.company