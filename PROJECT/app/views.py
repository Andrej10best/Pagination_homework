from django.shortcuts import render
from django.core.paginator import Paginator
from .models import User, Post

# Create your views here.


def base_page(request):
    return render(request, 'base_page.html')


def all_users(request):
    users = User.objects.all()
    
    selected_choice = request.GET.get('choice', '3')
    
    paginator = Paginator(users, selected_choice)
    page_number = request.GET.get('page')
    page_users = paginator.get_page(page_number)

    pages = paginator.num_pages
    all_pages = [i for i in range(1, pages + 1)]
    
    context = {
        'users': users,
        'selected_choice': selected_choice,
        'paginator': paginator,
        'page_number': page_number,
        'page_users': page_users,
        'all_pages': all_pages
    }
    return render(request, 'list_users.html', context)


def all_posts(request):
    posts = Post.objects.all().order_by('-date_published')
    
    selected_choice = request.GET.get('choice', '3')
    
    paginator = Paginator(posts, selected_choice)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    pages = paginator.num_pages
    all_pages = [i for i in range(1, pages + 1)]
    
    context = {
        'posts': posts,
        'selected_choice': selected_choice,
        'paginator': paginator,
        'page_number': page_number,
        'page_posts': page_posts,
        'all_pages': all_pages
    }
    return render(request, 'list_posts.html', context)
