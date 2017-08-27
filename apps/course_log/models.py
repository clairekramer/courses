from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Name must be longer than 5 Characters'
        if len(postData['desc']) < 15:
            erros['desc'] = 'Description must be longer than 15 Characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    def __repr__(self):
        return 'Course: {}'.format(self.name)
