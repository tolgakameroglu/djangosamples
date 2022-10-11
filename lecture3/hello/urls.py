from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("tolga",views.tolga,name="tolga"),
    path("<str:name>",views.greet,name="greet")
]

