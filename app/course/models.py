from django.db import models

# Create your models here.



class Course(models.Model):
    title  = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, unique=True)
    body = models.TextField()
    price = models.PositiveIntegerField()
    lesson_count = models.PositiveIntegerField(blank=True, null=True)
    image = models.URLField()
    unlisted = models.BooleanField(default=False)
    cerated = models.DateTimeField(auto_now=True)
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug= models.SlugField(blank=True, null=True)
    body = models.TextField()
    cerated = models.DateTimeField(auto_now=True)
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
 