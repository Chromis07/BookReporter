from django.contrib import admin
from django.utils.safestring import mark_safe
from bookreporter.models import Genre, Book, Review, Quote

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'author', 'image',
                    'publisher', 'genre', 'book_url']

    def book_image(self, book : Book) : # 이미지가 안뜬다!!
        html = f'<img src="{book.image.url}" style="width: 100px;" />'
        return mark_safe(html)
        
    def book_url_link(self, book : Book) -> str: # 클릭이 안되네...
        html = f'<a href="{book.book_url}" target="_blank">바로가기</a>'
        return mark_safe(html)
    
    
@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    pass

@admin.register(Quote)
class AdminQuote(admin.ModelAdmin):
    pass