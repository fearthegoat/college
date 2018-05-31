from django.contrib import admin
from .models import Comment, College, Player, Offer, HighSchool
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(Comment)
admin.site.register(College)
admin.site.register(Player)
admin.site.register(Offer)
admin.site.register(HighSchool)

# class CollegeInline(admin.StackedInline):
#     model = College
#     can_delete = False
#     verbose_name_plural = 'college'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (CollegeInline, )

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)