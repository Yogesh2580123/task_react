from django.db import models
'''
  self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.username = username
        self.age = age
        self.hobbies = hobbies if hobbies is not None else []

'''
class User(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    hobby = models.JSONField(default=list)

    '''
     hobbies = models.ArrayField(models.CharField(max_length=255), default=list)

    '''


