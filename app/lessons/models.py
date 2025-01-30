from django.db import models
from course.models import Module
# Create your models here.
   
class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug= models.SlugField(blank=True, null=True)
    lesson_type = models.CharField(max_length=50, choices=[("darslik","darslik"), ("problems","problems")])
    lesson_ochiq = models.BooleanField(default=False)
    cerated = models.DateTimeField(auto_now=True)
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Language(models.Model):
    name = models.CharField(max_length=250)
    cerated = models.DateTimeField(auto_now=True)
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Problems(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language)
    title = models.CharField(max_length=250)
    slug= models.SlugField(blank=True, null=True)
    body = models.TextField()
    cerated = models.DateTimeField(auto_now=True)
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Defaultfunctions(models.Model):
    problems = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    body = models.TextField()
    cerated = models.DateTimeField(auto_now=True)
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"language : { self.language.name}"
    
class Algoritm(models.Model):
    problems = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    aloritm = models.TextField()
    cerated = models.DateTimeField(auto_now=True)
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Testcase(models.Model):
    algoritm = models.ForeignKey(Algoritm, on_delete=models.CASCADE)
    input_data = models.CharField(max_length=250)
    output_data = models.CharField(max_length=250)

    def __str__(self):
        return self.title