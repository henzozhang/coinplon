from django.db import models
from wagtail.snippets.models import register_snippet

# Create your models here.
class Temoignage(models.Model):
    quote = models.TextField(
        max_length=500,
        blank=False,
        null=False,
    )

    author = models.CharField(
        max_length = 50,
        blank=False,
        null=False
    )
    def __str__(self):
        return f"{self.quote} par {self.author}"
    
    class Meta :
        verbose_name = "temoignage"
        verbose_name_plural = "temoignages"