from .models import ContactUs
from django.forms import ModelForm

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"