from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name