from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField('생성일시',auto_now_add=True)
    modified_at = models.DateTimeField('수정일시',auto_now=True)

    def __str__(self):
        return self.title



