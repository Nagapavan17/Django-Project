from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField(null=False,unique=True)
    password=models.CharField(max_length=250)

    def isexist(self):
        if(Employee.objects.filter(email=self.email)):
            return True
        return False
    
    @staticmethod
    def isuser(username1):
        try:
            return Employee.objects.get(username=username1)
        except:
            return False

        
        