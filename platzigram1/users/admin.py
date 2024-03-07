
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile


#muestra los perfiles
@admin.register(Profile)
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    """profile admin"""
    list_display = ('user', 'website', 'biography', 'phone_number', 'picture', 'created_at','modified_at')  
    #para agregar links a los atributos
    list_display_links= ('user', 'phone_number')
    #para editar datos en el listado
    list_editable = ('website', 'biography', 'picture')
    #buscar
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number', 'user__username')


    list_filter= ('created_at', 'modified_at','user__is_active', 'user__is_staff')

    fieldsets = (
        # titulo, dict
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            ),
        }),
        ('Extra information',{
            'fields':(
                ('website', 'phone_number', ),
                ( 'biography',)

            )
        }),

        ('Metadata',{
            'fields':(
                ('created_at', ),
                ( 'modified_at',)

            )
        })

    )



    readonly_fields = ('created_at','modified_at')

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural='profiles'
    
class UserAdmin(BaseUserAdmin):
    #add profile admin  to base user admin
    inlines = (ProfileInLine,)
    list_display = ('username','email', 'first_name', 'last_name', 'is_active', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """profile admin"""
    list_display = ('user', 'profile', 'title', 'photo', 'created','modified')  
    #para agregar links a los atributos
    list_display_links= ('user', 'profile')
    #para editar datos en el listado
    list_editable = ('title', 'photo')
    #buscar
    search_fields = ('title', 'user__first_name', 'user__username')


    list_filter= ('created', 'modified')

    fieldsets = (
        # titulo, dict
        ('Information', {
            'fields': (
                ('title', 'photo'),
            ),
        }),
        ('User', {
            'fields': (
                ('user'),
            ),
        }),
        ('Profile', {
            'fields': (
                ('profile'),
            ),
        }),
        ('Metadata',{
            'fields':(
                ('created', ),
                ( 'modified',)

            )
        })

    )



    readonly_fields = ('created','modified')

