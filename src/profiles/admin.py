from django.contrib import admin

from .models import UserProfile

#Register your models here.
class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = UserProfile

admin.site.register(UserProfile, profileAdmin)