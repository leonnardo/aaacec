from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns("",
    url(r"^$", "apps.loja.views.index"),
    url(r"^encomendas/fazer/(\d)", "apps.loja.views.fazer_encomenda"),
    url(r"^encomendas/cancelar/(\d)", "apps.loja.views.cancelar_encomenda"),
    url(r"^encomendas/checar/(\d)", "apps.loja.views.checar_encomenda"),
    url(r"^encomendas/", "apps.loja.views.listar_encomendas"),
)
