from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import new_user_oauth, login, all_users, root_redirect

urlpatterns = [
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('edit-profile/', new_user_oauth, name='new_user_oauth'),
    path('login/', login, name='login-user'),
    path('all/', all_users, name='all_users')
]
