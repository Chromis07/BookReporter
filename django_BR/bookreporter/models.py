from django.db import models


# 장르
class Genre(models.Model):
    name = models.CharField(max_length = 20)
    
    class Meta :
        verbose_name = "장르"
        verbose_name_plural = "장르 목록"
    
    def __str__(self):
        return self.name


# 책 정보
class Book(models.Model):
    title = models.CharField(max_length = 30, db_index=True, verbose_name = "제목")
    author = models.CharField(max_length = 20, verbose_name = "작가")
    publisher = models.CharField(max_length = 20, verbose_name = "출판사")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="장르")
    image = models.ImageField(verbose_name= "표지")
    book_url = models.URLField(verbose_name="구매 링크")
    desc = models.TextField(verbose_name="소개")
    # published_date 적으려면?? (날짜 형식)
    
    class Meta :
        verbose_name = "책"
        verbose_name_plural = "책 목록"

    def __str__(self):
        return self.title


# 책 리뷰
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    message = models.TextField(verbose_name="리뷰")
    # review objects 구분은 어쩌지...


# 책 인용구
class Quote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.IntegerField() # 페이지 숫자형, 순차별로 출력하기 위해 interger 사용
    phrase = models.TextField(verbose_name="인용구")

    def __str__(self):
        return f"{self.book}, p.{self.page}"