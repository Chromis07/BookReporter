from django.contrib import admin
from bookreporter.models import Genre, Book, Review, Quote

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass

@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    pass

@admin.register(Quote)
class AdminQuote(admin.ModelAdmin):
    pass