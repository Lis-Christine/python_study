from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Categoryクラス
class Category(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

# Boardクラス
class Board(models.Model):
    title = models.TextField(max_length=100)
    main_text = models.TextField()
    good_cnt = models.IntegerField(default=0)
    read_cnt = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('create_date',)

# Goodクラス
class Good(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.board) + ':' + str(self.user)



