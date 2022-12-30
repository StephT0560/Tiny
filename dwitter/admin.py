from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Profile,Dweet


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    filter_horizontal = ['follows']

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Dweet)