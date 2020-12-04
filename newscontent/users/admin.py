from .forms import UserAdminCreationForm, UserAdminChangeForm, RegisterForm
from .models import Account

from django.contrib import admin

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    add_form = UserAdminCreationForm
    add_form_ac = RegisterForm
    form = UserAdminChangeForm
    model = Account
    list_display = ['email', 'username', 'is_active', 'is_admin', ]

admin.site.register(Account, UserAdmin)

