from django.db import models

# crud_studentdjango
# Create your models here.
class Student(models.Model):
    # id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=25, blank=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25, blank=False,null=False)
    def __str__(self):
        return self.name # according to name table display