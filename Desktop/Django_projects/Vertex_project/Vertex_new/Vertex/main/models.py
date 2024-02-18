from django.db import models

class Blog(models.Model):
    img = models.ImageField("Blog image", upload_to='media')
    title = models.CharField("Blog title", max_length=150)
    text = models.TextField("About blog")
    date = models.DateField("Post date")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class Service(models.Model):
    title = models.CharField('title', max_length=155)
    text1 = models.TextField('text1', max_length=255)
    text2 = models.TextField('text2', max_length=255)

    def __str__(self):
        return 'Service'
    
class Gallery(models.Model):
    img = models.ImageField('Image', upload_to='media')
    img_open = models.ImageField('Drop down image', upload_to='media')
    title = models.CharField('title', max_length=100)
    text = models.CharField('text', max_length=120)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


class ContactUs(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    message = models.TextField('Message')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'
