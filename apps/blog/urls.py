from django.conf.urls.defaults import patterns, url 
#from django.views.generic import ListView
from aaacec.apps.blog.models import Post


urlpatterns = patterns("",
    url(r"^$", "django.views.generic.date_based.archive_index",
        {'queryset': Post.objects.all(), 'date_field': 'pub_date'}),
    #url(r"^$", ListView.as_view(
    #                            queryset=Post.objects.all().order_by("-pub_date")[:3],
    #                           template_name="index.html")),
)
