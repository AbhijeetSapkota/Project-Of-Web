from django.conf import settings
from django.db import models


class Post(models.Model):
    CATEGORY_LOST = 'LOST'
    CATEGORY_FOUND = 'FOUND'
    CATEGORY_CONFESSION = 'CONFESSION'

    CATEGORY_CHOICES = [
        (CATEGORY_LOST, 'Lost'),
        (CATEGORY_FOUND, 'Found'),
        (CATEGORY_CONFESSION, 'Confession'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=120, blank=True)
    contact_info = models.CharField(max_length=120, blank=True)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.get_category_display()}: {self.title}"

# Create your models here.
