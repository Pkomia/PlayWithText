from django.contrib import admin
from django.urls import path
# from django.conf.urls import url

from playwithText import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('Toupper/', views.Toupper, name='Toupper'),
    # path('Tolower/', views.Tolower, name='Tolower'),
    # path('RemovePunc/', views.RemovePunc, name="RemovePunc")
]
