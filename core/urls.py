from django.urls import path

from .views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
]
