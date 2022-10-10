from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("tolga",views.tolga,name="tolga")
]

