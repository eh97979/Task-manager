from django.db import models

# Create your models here.

class Tasks(models.Model):
    task_text = models.CharField(max_length=300)
    its_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_text


