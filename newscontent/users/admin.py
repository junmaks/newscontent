# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
#
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]
#
# admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]
#
# admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm, RegisterForm
from .models import Account

# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'admin')
#     list_filter = ('admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ()}),
#         ('Permissions', {'fields': ('admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()
#
#
# admin.site.register(Account, UserAdmin)
#
#
#
# # Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)


from django.contrib import admin

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    add_form = UserAdminCreationForm
    add_form_ac = RegisterForm
    form = UserAdminChangeForm
    model = Account
    list_display = ['email', 'username', 'is_active', 'is_admin', ]

admin.site.register(Account, UserAdmin)

