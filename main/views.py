from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .forms import ContactUsForm

class HomeListView(ListView):
    template_name = 'index.html'



    def get(self, request):
        intro = Intro.objects.get()
        menu = Menu.objects.all()
        about = AboutUs.objects.get()
        contact = Contact.objects.get()

        context = {
            'intro' : intro,
            'menu' : menu,
            'about' : about,
            'contact' : contact,
        }
        

        return render(request, self.template_name, context = context)
    
    def post(self,request):
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = ContactUsForm()
            
        intro = Intro.objects.get()
        menu = Menu.objects.all()
        about = AboutUs.objects.get()
        contact = Contact.objects.get()

        context = {
            'intro' : intro,
            'menu' : menu,
            'about' : about,
            'contact' : contact,
        }
        

        return render(request, self.template_name, context = context)
