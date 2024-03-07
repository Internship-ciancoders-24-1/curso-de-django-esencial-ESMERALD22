"""Platzigram middleware catalog"""

from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware():
    """
     Ensure every user that us interacting with  the platfomr
      have their profile , picture and biography
    """
    
    def __init__(self,get_response) :
        """middleware initialization"""
        self.get_response = get_response
    
    def __call__(self,request):
        """COde to be executed for each request before the view is called"""
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_response(request)
        return response