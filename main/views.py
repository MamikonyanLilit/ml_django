from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from .forms import ContactUsForm

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        home = Home.objects.all()
        about = AboutUs.objects.get()
        blog = Blog.objects.all()
        contact = ContactUs.objects.all()
        furniture = Furniture.objects.all()
        client = Client.objects.all()[1:]
        client_active = Client.objects.first()


        context = {
            'home':home,
            'about' : about,
            'blog' :blog,
            'contact' : contact,
            'furniture' : furniture,
            'client' : client,
            "client_active":client_active,
        }
        return render(request, self.template_name, context = context)

class AboutListView(ListView):
    template_name = 'about.html'
    
    def get(self, request):
        about = AboutUs.objects.get()

        context = {
            'about' : about,

        }
        return render(request, self.template_name, context = context)
    

class BlogListView(ListView):
    template_name = 'blog.html'

    def get(self, request):
        blog = Blog.objects.all()
        context = {
            'blog' :blog,
        }
        return render(request, self.template_name, context = context)

    
class FurnitureListView(ListView):
    template_name = 'furniture.html'

    def get(self, request):
        furniture = Furniture.objects.all()

        context = {
            'furniture' : furniture
        }
        return render(request, self.template_name, context = context)
    
class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        contact = ContactUs.objects.all()

        context = {
            'contact' : contact,
        }
        return render(request, self.template_name, context = context)
    
    def post(self,request):
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = ContactUsForm()

        furniture = Furniture.objects.all()
        blog = Blog.objects.all()
        about = AboutUs.objects.get()
        home = Home.objects.all()
        contact = ContactUs.objects.all()


        context = {
            'furniture' : furniture,
            'blog' :blog,
            'about' : about,
            'home':home,
            'contact' : contact,
            'form' : form,

        }

        return render(request, self.template_name, context=context)



    

    






