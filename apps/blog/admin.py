from django.contrib import admin
from models import Post

class PostAdmin(admin.ModelAdmin):
    exclude = ('author',)
    list_display = ('title', 'pub_date', 'author')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Post,PostAdmin)
