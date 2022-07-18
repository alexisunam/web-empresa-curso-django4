from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def category(request, category_id):
    # Match reverse, usar template category.html para ejemplo
    category = get_object_or_404(Category, id=category_id)
    # Reutilizamos el template Blog, mejor Practica, usamos el template blog.html
    posts = Post.objects.filter(categories=category_id)
    # Aqui se devuelve una lista de posts si usamos la mejor practica |#{'category': category}
    return render(request, 'blog/blog.html', {'posts': posts})