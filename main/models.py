from django.db import models


class Course(models.Model):
    title = models.CharField('Название курса', max_length=50)

    def __str__(self):
        return self.title


class Subcourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subtitle = models.CharField('Название подкурса', max_length=120)
    stats = models.IntegerField(default=0)

    def __str__(self):
        return self.subtitle