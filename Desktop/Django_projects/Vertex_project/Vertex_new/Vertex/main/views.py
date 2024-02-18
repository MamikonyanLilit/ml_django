from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from .forms import ContactUsForm


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        blogs = Blog.objects.all()
        service = Service.objects.get()
        galleries = Gallery.objects.all()

        context = {
            "blogs" : blogs,
            "service" : service,
            "galleries" : galleries,
        }

        return render(request, self.template_name, context = context)

    def post(self, request):
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = ContactUsForm()


        blogs = Blog.objects.all()
        service = Service.objects.get()
        galleries = Gallery.objects.all()

        context = {
            "blogs" : blogs,
            "service" : service,
            "galleries" : galleries,
            "form" : form,
        }

        return render(request, self.template_name, context = context)

