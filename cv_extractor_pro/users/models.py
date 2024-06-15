from django.db import models

# Create your models here.
"""class Folder(models.Model):
    name = models.CharField(max_length = 400)
    upload_date = models.DateTimeField(auto_now_add=True)
    """

class CV(models.Model):
    #folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    filename  = models.CharField(max_length=255)
    email = models.TextField()
    contact_number = models.TextField()
    text = models.TextField()


