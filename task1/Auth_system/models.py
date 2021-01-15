from django.db import models

# Create your models here.
"""class category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class subcategory(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    subcategory=models.CharField(max_length=50)

    def __str__(self):
        return self.subcategory"""

class userInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=50)


class item(models.Model):
    username=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    prce = models.IntegerField()
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)






