from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Intro(models.Model):
    img = models.ImageField(("img"), upload_to='media')
    title = models.CharField('title', max_length=50)
    text1 = models.TextField('text1')
    text2 = models.TextField('text2')

    def __str__(self) -> str:
        return self.title
    
class Menu(models.Model):
    big_img = models.ImageField(("img"), upload_to='media', null=True)
    img = models.ImageField(("img"), upload_to='media')
    title = models.CharField('title', max_length=50)
    price1 = models.DecimalField(("price1"), max_digits=5, decimal_places=2)
    price2 = models.DecimalField(("price2"), max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.title

class AboutUs(models.Model):
    img = models.ImageField(("img"), upload_to='media')
    title = models.CharField('title', max_length=50)
    text = models.TextField('text')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'

class Contact(models.Model):
    img = models.ImageField(("img"), upload_to='media')
    phone = PhoneNumberField('phone', null = True)
    email = models.EmailField('email', null = True)
    title = models.CharField('title', max_length=50)
    text = models.TextField('text')

    def __str__(self) -> str:
        return self.title

class ContactUs(models.Model):
    name = models.CharField('name', max_length=50)
    email = models.EmailField('email')
    message = models.TextField('message')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'






    

