from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.BinaryField()
    createdBy = models.ForeignKey(
        "jwtAuth.User",
        on_delete=models.CASCADE,
        related_name="userImages"
        )

    def __str__(self):
        return self.name