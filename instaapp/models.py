from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = HTMLField()
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'images/')



    def save_image(self):
        self.save()
   
    def delete_image(self):
        self.delete()

    def update_image():
        self.update()

    @classmethod
    def update_caption(cls,caption):
        caption=cls.objects.filter(caption=caption).update(caption=caption)
        return caption


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    comment = models.CharField(max_length=80, blank=True)


    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def update_comment(self):
        self.update()
