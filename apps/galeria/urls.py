from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns("",
    url(r"^$", "apps.galeria.views.index"),
    url(r"^callback/$", "apps.galeria.views.callback"),
    #url(r"^albuns/$", "apps.galeria.views.getPhotosets"),
    url(r"^albuns/(\d)", "apps.galeria.views.listarFotos"),
)
