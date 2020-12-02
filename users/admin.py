from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class RegularUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username', 'email', 'phone_number', 'age', 'salary_amount', 'is_staff'
    ]


admin.site.register(CustomUser, RegularUserAdmin)
