from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.name, name="name"),
    path('analyze', views.about, name="about"),
    # path('contactUs', views.contactUs, name="contactUs"),
    # path('skills', views.skills, name="skills"),
    # path('hobbies', views.hobbies, name="hobbies")

]
