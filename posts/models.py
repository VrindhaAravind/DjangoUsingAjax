from django.db import models
from django.contrib.auth.models import User


class Userpost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post_content=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='blog_post')


    def total_likes(self):
        return self.likes.all().count()

    def __str__(self):
        return str(self.author)

LIKE_CHOICES=(
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Userpost,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.post)