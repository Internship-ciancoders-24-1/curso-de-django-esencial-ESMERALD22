#    path ('users/login/', users_views.login_view, name = 'login'),
 #   path ('users/logout/', users_views.logout_view, name = 'logout'),
 #   path ('users/signup/', users_views.signup_view, name = 'signup'),
 #   path ('users/me/profile', users_views.update_profile, name = 'update_profile'),


"""Users URLs."""

# Django
from django.urls import path

# View
from users import views
from django.views.generic import TemplateView

urlpatterns = [
    #Posts, perfil de usuario
    
    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
    ),
    path (
        route = '<str:username>/',
        view= views.UserDetailView.as_view(),
        name='detail'
    ),

]