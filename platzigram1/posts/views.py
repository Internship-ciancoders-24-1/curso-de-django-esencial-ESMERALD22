from django.http import HttpResponse
# Create your views here.
from datetime import datetime
import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.forms import PostForm


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