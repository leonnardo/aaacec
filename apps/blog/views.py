from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from aaacec.apps.blog.models import Post

def main(request):
    posts = Post.objects.all().order_by("-pub_date")
    paginator = Paginator(posts, 2)
    
    try: 
        page = int(request.GET.get("page", '1'))
    except ValueError: 
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("post_archive.html", dict(posts=posts, user=request.user))



