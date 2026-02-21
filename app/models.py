from django.db import models

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    bio = models.TextField()
    image = models.ImageField(upload_to='profile/')
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.full_name
    
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.company
    
    
class Education(models.Model):
    institute = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_yaer = models.IntegerField()
    
    def __str__(self):
        return self.institute
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    