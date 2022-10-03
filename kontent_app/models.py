from django.db import models

class Content(models.Model):
    id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    module = models.CharField()
    students = models.IntegerField()
    description = models.CharField(blank=True)
    is_active = models.BooleanField(default=False)

    def __repr__ (self):
       return f'<[{self.id}] {self.title} - {self.module}>'

"""   def __init__ (self, id, module, students, description, is_active, title):
        self.id = id
        self.title = title
        self.module = module
        self.students = students
        self.description = description
        self.is_active = is_active """


new_content = {
    "id": 1,
    "title": "Python",
    "module": "M5",
    "description": "Python Fundamental",
    "students": 90,
    "is_active": True,
}

