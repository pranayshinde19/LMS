from django.contrib import admin
from .models import BookModel
class BookModelAdmin(admin.ModelAdmin):
    list_display=['id' ,'book_name','author_name','price','type_of_book']
# Register your models here.
admin.site.register(BookModel,BookModelAdmin)