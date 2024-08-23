from django.db import models

# Create your models here.

class Comment(models.Model):
    text = models.CharField(max_length=100)
    imageRef = models.ForeignKey(
        "images.Image",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    createdBy = models.ForeignKey(
        "jwtAuth.User",
        on_delete=models.CASCADE,
        related_name="userComments"
    )