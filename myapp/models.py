from django.db import models
import os
from django.db import models

# Django 설정 모듈을 설정합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Review 모델 정의
class Review(models.Model):
    author = models.CharField(max_length=100)  # 작성자 이름 필드
    content = models.TextField()  # 리뷰 내용 필드
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시각 필드, 자동으로 현재 시각이 저장됨

    def __str__(self):
        return self.author  # 객체를 문자열로 나타낼 때 작성자 이름을 반환
