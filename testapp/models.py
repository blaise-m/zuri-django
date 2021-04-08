from django.db import models


class Client(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
