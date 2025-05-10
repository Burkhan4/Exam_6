from django.db import models

class Poet(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    biography = models.TextField()
    works = models.TextField()

    def __str__(self):
        return self.name
