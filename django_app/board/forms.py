from django import forms
from.models import Category, Board
from django.contrib.auth.models import User

# 検索フォーム
class SearchForm(forms.Form):
    search = forms.CharField(label='search', required=False)


# 投稿フォーム
class BoardForm(forms.Form):
    data=[
        ('勉強', '勉強'),
        ('ゲーム', 'ゲーム'),
        ('グルメ', 'グルメ'),
        ('旅行', '旅行'),
    ]
    category = forms.ChoiceField(choices=data)
    title = forms.CharField(max_length=100, initial="",)
    main_text = forms.CharField(max_length=500, widget=forms.Textarea, initial="",)

