from django.db import models

# Create your models here.

UNIVERSITY_CHOICES = (
    ("Zeus University", "Zeus University"),
    ("Apollo University", "Apollo University"),
    ("Nike University", "Nike University"),
    ("Hermes University", "Hermes University"),
)

class team(models.Model):
    name = models.CharField(
        max_length = 30,
    )
    size = models.IntegerField(
        range(5, 26),
    )
    university = models.CharField(
        max_length = 20,
        choices = UNIVERSITY_CHOICES
    )
    boarding = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name