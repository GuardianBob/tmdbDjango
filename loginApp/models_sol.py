from django.db import models
import re

class UserManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 1:
            errors['name'] = 'User name is too short.'
        if len(User.objects.filter(alias = post_data['alias'])) > 0:
            errors['alias'] = 'This user alias is already in use.'
        if len(post_data['alias']) < 1:
            errors['alias'] = 'User alias must be at least one character long.'
        if len(post_data['alias']) > 50:
            errors['alias'] = 'User alias must be 50 characters or less.'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):        
            errors['email'] = "Invalid email address."
        if len(post_data['email']) > 384:
            errors['email'] = 'Email address is too long.'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long.'
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = 'Passwords do not match.'
        try:
            user = User.objects.get(email = post_data['email'])
            errors['email_in_use'] = 'This email is already associated with an account.'
        except:
            pass
        return errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 50)
    email = models.CharField(max_length = 384)
    password = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()