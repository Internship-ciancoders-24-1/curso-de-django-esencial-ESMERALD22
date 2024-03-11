from django.http import HttpResponse
# Create your views here.
from datetime import datetime
import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,DetailView, FormView, UpdateView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy
@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created')
    """List existing posts"""
    #content = []
    #for post in posts:
    #   content.append("""
    #        <p><strong>{name}</strong></p>
    #        <p><small>{user} - <i>{timestamp}</i></small></p>
    #        <figure><img src="{picture}"/></figure>
    #   """.format(**post))
    #return HttpResponse('<br>'.join(content))

    return render(request, 'posts/feed.html',{'posts':posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm() 

    return render(
        request = request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile,
        }
    )

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
    
class PostsFeedView(LoginRequiredMixin, ListView):
    template_name= 'posts/feed.html'
    model = Post
    ordering =('-created')
    paginate_by = 2
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'