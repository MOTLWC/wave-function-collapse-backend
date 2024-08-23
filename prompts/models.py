from django.db import models

# Create your models here.

class Prompt(models.Model):
    promptName = models.CharField(max_length=20)
    promptBitmapAsBinary = models.BinaryField()
    createdBy = models.ForeignKey(
        "jwtAuth.User",
        on_delete=models.DO_NOTHING,
        related_name="prompts"
    )

    def __str__(self):
        return self.promptName