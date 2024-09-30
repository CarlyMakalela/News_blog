from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Q

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    related_posts = Post.objects.filter(category=post.category).exclude(pk=pk)[:3]
    return render(request, 'blog/post_detail.html', {'post': post, 'related_posts': related_posts})

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})
