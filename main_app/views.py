from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog, Comment
from .forms import CommentForm
from datetime import date

def home(request):
    return render(request, 'home.html')

def blogs_index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})

def blogs_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comment_form = CommentForm()
    return render(request, 'blogs/detail.html', {
        'blog': blog, 'comment_form': comment_form
        })

class BlogCreate(CreateView):
    model = Blog
    fields = '__all__'
    success_url = '/blogs/'

class BlogUpdate(UpdateView):
    model = Blog
    fields = '__all__'

class BlogDelete(DeleteView):
    model = Blog
    success_url = '/blogs/'

def add_comment(request, blog_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.blog_id = blog_id
        new_comment.save()
    return redirect('detail', blog_id=blog_id)

class CommentDelete(DeleteView):
    model = Comment
