from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
    )
    summary = models.CharField(max_length=300, default='Qisqa matn qoshildi!1')
    body = models.TextField()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])


