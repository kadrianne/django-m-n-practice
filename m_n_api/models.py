from django.db import models

# Create your models here.
class Actor(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return f'{self.id}: {self.name}'

class Director(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return f'{self.id}: {self.name}'

class Movie(models.Model):
  title = models.CharField(max_length=50)
  actor = models.ForeignKey(Actor, related_name='movies', on_delete=models.CASCADE)
  director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.id}: {self.title}'