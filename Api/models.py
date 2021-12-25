from django.db import models 

# Create your models here.
class Sample_Details(models.Model):
    name=models.CharField(max_length=70)
    description=models.CharField(max_length=70)
    email=models.EmailField()
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name