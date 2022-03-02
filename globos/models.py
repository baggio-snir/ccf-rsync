from django.db import models


class Proof(models.Model):
    content = models.TextField()
    def __str__(self):
        return self.content
