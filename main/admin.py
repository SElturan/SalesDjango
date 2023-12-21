from django.contrib import admin
from .models import User, CodeGenerate, Branch, RegularUser

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','nickname', 'user_id', 'first_name', 'last_name', 'phone_number', 'phone_number2', 'age', 'date','points','age_check',  'is_admin', 'date_joined')
    list_display_links = ('nickname',)
    search_fields = ('nickname', 'user_id', 'first_name', 'last_name', 'phone_number', 'phone_number2', )
    list_filter = ('is_admin', 'date_joined','age_check',)
    list_editable = ('age_check',)
    ordering = ('-date_joined',)

@admin.register(CodeGenerate)
class CodeGenerateAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'code', 'summ', 'discount', 'confirmed_presence', 'created_at')
    search_fields = ('user__nickname', 'code', 'user__phone_number')
    list_display_links = ('user',)
    list_filter = ('discount', 'created_at', 'confirmed_presence',)
    ordering = ('-created_at',)
    list_editable = ('confirmed_presence',)
    autocomplete_fields = ('user',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'location','opening_time', 'closing_time', )
    search_fields = ('name', 'location')


@admin.register(RegularUser)
class RegularAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'summ', 'visits', 'discount', 'date_joined', )
    list_display_links = ('user',)
    search_fields = ('user__nickname', 'summ', 'user__phone_number')

