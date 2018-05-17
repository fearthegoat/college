from django.contrib import admin

from .models import Comment, College, Player, Offer, HighSchool

admin.site.register(Comment)
admin.site.register(College)
admin.site.register(Player)
admin.site.register(Offer)
admin.site.register(HighSchool)
