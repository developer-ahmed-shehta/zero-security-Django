from django.db import models

class XSSComment(models.Model):
    username = models.CharField(max_length=50)
    message = models.TextField()  # NO SANITIZATION
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username