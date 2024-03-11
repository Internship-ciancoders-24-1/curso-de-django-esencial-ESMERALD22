from typing import Any
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError

from users.forms import ProfileForm, SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,DetailView, FormView, UpdateView
from django.urls import reverse
from posts.models import Post
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        print('*'*10)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return  redirect('posts:feed')
        else: 
            return  render(request, 'users/login.html',{'error':'Invalid username and password'})
        

        print (username, ':', password)
        print('*'*10)

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

def signup_view(request):
    """if request.method == 'POST':
        username= request.POST["username"]
        password = request.POST["password"]
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation:
            return  render(request, 'users/signup.html',{'error':'Passwords do not match'})
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return  render(request, 'users/signup.html',{'error':'Username is already in user'})

        user.first_name= request.POST['first_name']
        user.last_name= request.POST['last_name']
        user.email= request.POST["email"]
        user.save()
        profile = Profile(user= user)
        profile.save()
        return redirect('login')

    return render(request, 'users/signup.html')
@login_required"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
            request=request,
            template_name='users/signup.html',
            context={
                'form':form,
            }
        )

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
    

def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()
            print(form.cleaned_data)
            url = reverse('users:detail', kwargs={'username':request.user.username})
            return redirect(url)  
    else:
        form = ProfileForm()
                
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form,
        }
    )


class UserDetailView(LoginRequiredMixin, DetailView):

    """User detail view."""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        user= self.get_object()
        context['posts'] = Post.objects.filter(user= user).order_by('-created')
        return context
    
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})
    
class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/login.html'