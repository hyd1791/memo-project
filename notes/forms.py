from django import forms
from .models import Note
#아래 구조는 정해진 규칙입니다.
class NoteForm(forms.ModelForm):
    class Meta:
        #내가 사용할 데이터베이스
        model = Note
        #데이터 베이스에서 사용할 요소(사용자에게 입력받는)
        fields = ['title', 'context',]