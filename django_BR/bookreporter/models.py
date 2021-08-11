from django.db import models


# 장르
class Genre(models.Model):
    name = models.CharField(max_length = 20)


# 책 정보
class Book(models.Model):
    title = models.CharField(max_length = 30, db_index=True)
    author = models.CharField(max_length = 20)
    publisher = models.CharField(max_length = 20)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField()
    book_url = models.URLField()
    desc = models.TextField()
    # published_date 적으려면?? (날짜 형식)


# 책 리뷰
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    message = models.TextField()


# 책 인용구
class Quote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    phrase = models.TextField()

