from django.db import models
# from django.apps import apps
import re, datetime
import bcrypt

# Message = apps.get_model('wallApp', 'Message')
# Comment = apps.get_model('wallApp', 'Comment')

class CheckUser(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['fName']) < 2 or str(postData['fName']).isalpha() != True:
            errors['fName'] = "Name must be at least 2 non-numeric characters."
        if len(postData['lName']) < 2 or str(postData['lName']).isalpha() != True:
            errors['lName'] = "Name must be at least 2 non-numeric characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("The Email address entered is invalid.")
        if len(postData['passwd']) < 8:
            errors['passwd'] = "Password must be at least 8 characters."
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['exists'] = "This email already exists in our system."        
        return errors

    def checkLogin(self, postData):
        errors = {}
        passwd = postData['passwd2']
        if len(User.objects.filter(email=postData['email2'])) == 0:
            errors['email'] = "This email doesn't exist in our system."
        else:
            usr = User.objects.get(email=postData['email2'])
            if not bcrypt.checkpw(passwd.encode(), usr.password.encode()):
                errors['passwd'] = "Incorrect password!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CheckUser()

    @property
    def full_name(self):
            return f"{self.first_name} {self.last_name}"
