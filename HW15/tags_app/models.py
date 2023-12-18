from django.db import models


class Tag(models.Model):
    tag_label = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.id}: {self.tag_label}"
