from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    module = models.TextField(blank=False, null=False)
    students = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False, null=True)

    def __repr__ (self):
       return f'<[{self.pk}] {self.title} - {self.module}>'
