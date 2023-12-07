from django.db import models

# Create your models here.

class task(models.Model):
    sno = models.IntegerField()
    task_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def save(self):
        self.task_name = self.task_name.capitalize()
        self.status = self.status.capitalize()
        super().save()
        