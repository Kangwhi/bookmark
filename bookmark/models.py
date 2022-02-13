from django.db import models
# models에 대한 작업에서는 reverse, views에 대한 작업에서는 reverse_lazy 사용
from django.urls import reverse


# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
