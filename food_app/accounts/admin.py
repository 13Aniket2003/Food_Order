from django.contrib import admin
from .models import LoginUser,SignupUser

admin.site.register(LoginUser)
admin.site.register(SignupUser)
