# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import Post

class PostAdmin(admin.ModelAdmin):
    exclude = ('author',)
    list_display = ('title', 'pub_date', 'author')
    search_fields = ['title', 'author']
    
    # Set the post's author based on the logged user
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    # Limit the post's list to his owner, unless he is a superuser 
    def queryset(self, request):
        if request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author=request.user)

    # Just to check permissions
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(PostAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True

admin.site.register(Post,PostAdmin)
