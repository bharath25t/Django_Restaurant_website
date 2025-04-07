from django.db import models # type: ignore
class student (models.Model):
    data=[("male","Male"),("female","Female"),("others","Others")]
    name=models.CharField(max_length=100)
    age=models.IntegerField
    email=models.EmailField
    gender=models.CharField(max_length=10,choices=data,null=False)
    class meta:
        verbose_name_plural="student table"
    def __str__(self):
        return self.name

