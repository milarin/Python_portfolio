from django.db import models



# Create your models here.
class WorkModel(models.Model):
  title = models.CharField(max_length=100, blank=True, null=True)
  time = models.CharField(max_length=100, blank=True, null=True)
  skill = models.TextField(blank=True, null=True)
  comment = models.TextField(blank=True, null=True)
  date = models.CharField(max_length=100, blank=True, null=True)
  img1 = models.ImageField(upload_to='', blank=True)
  img2 = models.ImageField(upload_to='', blank=True)
  url = models.URLField(blank=True)

  def __str__(self):
    return self.title