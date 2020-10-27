from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = HTMLField()
    likes = models.IntegerField(default=0)
    image = CloudinaryField('image')



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

    @classmethod
    def search_user(cls,search_term):
        images = cls.objects.filter(user__username=search_term)
        return images


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
