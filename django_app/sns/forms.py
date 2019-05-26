from django import forms
from.models import Message,Group, Friend, Good
from django.contrib.auth.models import User

# Messageのフォーム(未使用)
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['owner', 'group', 'content']

#  Groupのフォーム(未使用)
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['owner', 'title']

# Friendのフォーム(未使用)
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['owner', 'user', 'group']

# Goodのフォーム(未使用)
class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['owner', 'message']

# 検索フォーム
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)

# Groupのチェックボックスフォーム
class GroupCheckForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(GroupCheckForm, self).__init__(*args, **kwargs)