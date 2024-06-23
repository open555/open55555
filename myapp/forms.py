from django import forms
from .models import Review

# 후기 작성 폼을 정의하는 클래스
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # Review 모델을 기반으로 함
        fields = ['author', 'content']  # 작성자와 내용 필드를 포함

# 관리자 인증 폼을 정의하는 클래스
class AdminAuthForm(forms.Form):
    admin_id = forms.CharField(label='Admin ID', max_length=100)  # 관리자 ID 입력 필드
    password = forms.CharField(label='Password', widget=forms.PasswordInput)  # 비밀번호 입력 필드, 입력 시 숨김 처리
