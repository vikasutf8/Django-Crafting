from django.db import models
from django.contrib.auth.models  import User
# this is 'User' comes from admin panel 


class Tweet(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    text =models.TextField(max_length=250)
    photo =models.ImageField(upload_to='photo/',blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f'{self.user.username} -{self.text[:10]}'
# this dender function is how shows in admin route/panel as like username-text upto 10 char


