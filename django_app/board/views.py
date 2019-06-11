from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, Category, Good
from django.core.paginator import Paginator
from .forms import SearchForm, BoardForm
from django.shortcuts import redirect
from django.db.models import Count

# Create your views here.

def index(request, num=1):
    data = Board.objects.all()
    page = Paginator(data, 3)
    message = 'index'
    params = {
        'data' : page.get_page(num),
        'form' : SearchForm(),
        'message' : message,
    }
    return render(request, 'board/index.html', params)

def search(request, num=1):
    form = SearchForm(request.POST)
    str = request.POST['search']
    data = Board.objects.filter(title__contains=str)
    page = Paginator(data, 3)
    message = 'post'
    params = {
        'form' : form,
        'data' : page.get_page(num),
        'message' : message,
    }
    return render(request, 'board/index.html', params)

def board_main(request, num):
    board_main = Board.objects.get(id=num)
    board_good = Good.objects.filter(board_id=num, user_id=request.user.id).aggregate(Count('id'))
    params={
        'id' : num,
        'obj' : board_main,
        'message' : 'メイン'+str(num),
        'goodFlg' : board_good['id__count'],
    }
    return render(request, 'board/board_main.html', params)

def create(request):
    params={
        'form' : BoardForm(),
    }
    if (request.method == 'POST'):
        bd = Board()
        bd.category = Category.objects.filter(name=request.POST['category']).first()
        bd.title = request.POST['title']
        bd.main_text = request.POST['main_text']
        bd.user= request.user
        bd.save()
        return redirect(to='/board')
    return render(request, 'board/create.html', params)

def update(request, num):
#    board_update = Board.objects.get(id=num)
#    BoardForm.category.valid_value = Board.objects.get(id=num).category
#    BoardForm.title.__init__ = board_update.title
#    BoardForm.main_text = Board.objects.get(id=num).main_text

    if (request.method == 'POST'):
        board_update = Board.objects.get(id=num)
        board_update.category = Category.objects.filter(name=request.POST['category']).first()
        board_update.title = request.POST['title']
        board_update.main_text = request.POST['main_text']
        board_update.save()
        return redirect(to='/board')

    # data = Board.objects.filter(id=num).values('category', 'title', 'main_text')
    
    # params = {
    #     'title' : '変更画面',
    #     'id' : num,
    #     'form' : BoardForm(),
    #     'data' : data
    # }
    # return render(request, 'board/board_update.html', params)

def update_main(request, num):
    update_main = Board.objects.get(id=num)
    data = BoardForm(initial={
        "title":update_main.title, 
        "main_text":update_main.main_text, 
        "category":update_main.category
        })
    params = {
        'title' : '変更画面',
        'id' : num,
        'form' : data,
        'data' : update_main,
    }
    return render(request, 'board/board_update.html', params)

def delete(request, num):
    board_delete = Board.objects.get(id=num)
    board_delete.delete()
    return redirect(to='/board')


def goodUpdate(request, num):
    board = Board.objects.get(id=num)
    board.good_cnt += 1
    board.save()
    good = Good()
    good.board_id = num
    good.user_id = request.user.id
    good.save()
    return redirect(to='/board')
    

    