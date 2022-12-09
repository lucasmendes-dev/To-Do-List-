from django.db import models

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done'),
)

class Task(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.title