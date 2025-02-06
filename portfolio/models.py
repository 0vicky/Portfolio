from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    cv = models.FileField(upload_to='cvs/', blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50)  # For FontAwesome or other icon libraries

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title