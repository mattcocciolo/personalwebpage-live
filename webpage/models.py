from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(max_length=2000, null=False, blank=False)

    def __str__(self):
        return self.name
