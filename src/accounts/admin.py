from django.contrib import admin

from accounts.models import Customer


# Register your models here.
@admin.register(Customer)
class UserModelAdmin(admin.ModelAdmin):
    list_filter = ("username", 'email',)
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff',
    )
    list_editable = ('first_name', 'last_name',)
    list_display_links = ('email',)
