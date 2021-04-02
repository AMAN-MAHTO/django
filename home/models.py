from django.db import models

# Create your models here.
# it creat table
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    message = models.TextField()
    date = models.DateField()
    
    # to get mail sender name on her mail otherwise it name as object1,2,3..
    def __str__(self):
        return self.name, self.email
    