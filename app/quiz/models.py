from django.db import models
from course.models import Module
from lessons.models import Lesson

# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    # module = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    test_count = models.IntagerField()
    test_vaqti = models.IntagerField()


    def __str__(self):
        return self.title


class Questions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f"Sabol:-->{self.body[20]}"


class Answer(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    title = models.TextField()
    is_correct = models.BoolenField(default=False)
    def __str__(self):
        return f"Sabol:-->{self.title[20]}"
