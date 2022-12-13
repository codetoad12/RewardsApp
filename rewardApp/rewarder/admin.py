from django.contrib import admin
from .models import AdminFacing,SignUp,Task,Profile
# Register your models here.
admin.site.register(AdminFacing)
admin.site.register(SignUp)
admin.site.register(Task)
admin.site.register(Profile)