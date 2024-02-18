from django.db import models

class Home(models.Model):
    title = models.CharField(("title"), max_length=50)
    text = models.TextField("text")
    img = models.ImageField("img", upload_to='media')

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'


    def __str__(self) -> str:
        return 'Home'
    

class AboutUs(models.Model):
    title = models.CharField(("title"), max_length=50)
    text = models.TextField("text")
    img = models.ImageField("img", upload_to='media')

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'

    def __str__(self) -> str:
        return self.title
    
class Furniture(models.Model):
    title = models.CharField('title', max_length=100)
    img = models.ImageField('img', upload_to='media')
    price = models.DecimalField('price', max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.title
    
class Blog(models.Model):
    title = models.CharField(("title"), max_length=50)
    text = models.TextField("text")
    img = models.ImageField("img", upload_to='media')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self) -> str:
        return self.title


class ContactUs(models.Model):
    name = models.CharField('name', max_length=50)
    email = models.EmailField('email')
    message = models.TextField('message')

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

class Client(models.Model):
    name = models.CharField('client name', max_length=50)
    img = models.ImageField('img', upload_to='media')
    review = models.TextField('text')

    def __str__(self) -> str:
        return self.name
    
    

