from django.views.generic.list_detail import object_list
from aaacec.apps.blog.models import Post

def index(request):
        return object_list(request,
                template_name='teste.html',
                queryset = Post.objects.all().order_by("-pub_date"),
                paginate_by = 2)
