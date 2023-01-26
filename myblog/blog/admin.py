from django.contrib import admin
from .models import PostOn, Comments, Example_Models

@admin.register(PostOn)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")


    # @admin.register(<Модель>)
    # class <Имя класса>(admin.ModelAdmin):
    #     <Параметры>


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("name", "post")


@admin.register(Example_Models)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("name", "posts", "slug")



