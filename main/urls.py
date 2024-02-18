from django.urls import path
from .views import (HomeListView, AboutListView, BlogListView, ContactListView, FurnitureListView)

urlpatterns = [
    path('', HomeListView.as_view(), name = 'home'),
    path('about/', AboutListView.as_view(), name = 'about'),
    path('blog/', BlogListView.as_view(), name = 'blog'),
    path('contact/', ContactListView.as_view(), name = 'contact'),
    path('furniture/', FurnitureListView.as_view(), name = 'furniture')

]
