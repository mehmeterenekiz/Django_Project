from django.shortcuts import render, get_object_or_404
from . models import Post
from django.core.paginator import Paginator

# Create your views here.
def post_list(request):
    posts = Post.objects.all();

    paginator = Paginator(posts, 2)  # Show 2 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'post/post_list.html', {'posts': posts, 'page_obj': page_obj })


def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'post/post_detail.html', {'post': post})