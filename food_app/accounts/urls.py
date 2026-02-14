from django.urls import path
from .views import login_view,signup_view,logout

urlpatterns = [
    path("login/",login_view,name='login'),
    path("",signup_view,name='signup'),
    path("logout/",logout,name="logout"),
]