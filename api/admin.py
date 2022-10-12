from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User,roles,student,teacher




# class batchAdmin(admin.ModelAdmin):
#       list_display = ['year','std']
      
class teacherAdmin(admin.ModelAdmin):
      list_display = ['qualification']



class studentAdmin(admin.ModelAdmin):
      list_display = ['roll','div']



class rolesAdmin(admin.ModelAdmin):
      list_display = ['roleName','roleId']

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['email', 'first_name', 'last_name', 'is_staff','is_active','ID' ]

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )
    fieldsets = (
        (None, {'fields':('email', 'first_name', 'last_name','phone','username','password','roleId')}),
  
        
    )
    add_fieldsets = (
         (None, {
            'classes': ('wide',),
            
            # 'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','roleId','username','first_name', 'last_name','phone')}
              'fields': ('username','email', 'password1', 'password2','roleId'),
       }),
   )
  

admin.site.register(User, UserAdmin)
admin.site.register(roles,rolesAdmin)
admin.site.register(student,studentAdmin)
admin.site.register(teacher,teacherAdmin)
# admin.site.register(batch,batchAdmin)


