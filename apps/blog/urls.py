from django.conf.urls.defaults import *
from aaacec.apps.blog.models import Post
urlpatterns = patterns("",
    url(r"^$", "django.views.generic.date_based.archive_index",
        {'queryset': Post.objects.all(), 'date_field': 'time'}),
)
