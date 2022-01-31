from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q

from .forms import IdForm, IdSearch, FindForm
from .models import IdModel


# Create your views here.
def index(request):
    params = {
        'title': "これはINDEX頁",
        'msg': "<h1>All Record !</h1>",
        'form': IdSearch(),
        'btn1': '検索',
        'data': [], }
    if request.method == 'POST':
        nametxt = request.POST['name']
        item = IdModel.objects.filter(Q(name__icontains=nametxt))
        params['title'] = 'お探しのName一致してますか？'
        params['msg'] = "<h2>your request is ...</h2>"
        params['data'] = item
        params['form'] = IdSearch(request.POST)
    else:
        params['data'] = IdModel.objects.all()
    return render(request, 'mydjangoSoen/index.html', params)


def create(request):
    params = {
        'title': "これはCREATE頁",
        'msg': "<h1>Let's Create !</h1>",
        'form': IdForm(), }
    if request.method == 'POST':
        obj = IdModel()
        record = IdForm(request.POST, instance=obj)
        record.save()
        return redirect(to='mydjangoSoen:index')
    return render(request, 'mydjangoSoen/create.html', params)

@login_required
def edit(request, number):
    record = IdModel.objects.get(id=number)
    obj = IdModel.objects.get(id=number)
    if request.method == 'POST':
        record = IdForm(request.POST, instance=obj)
        record.save()
        return redirect(to='mydjangoSoen:index')
    params = {
        'title': '編集頁っす',
        'msg': str(record) + '       編集中ね',
        'id': number,
        'obj': obj,
        'form': IdForm(), }
    return render(request, 'mydjangoSoen/edit.html', params)

@login_required
def delete(request, number):
    record = IdModel.objects.get(id=number)
    if request.method == 'POST':
        record.delete()
        return redirect(to='mydjangoSoen:index')
    params = {
        'title': '削除ぉぉぉぉぉ',
        'msg': '本当 だいじょうぶ？',
        'id': number,
        'obj': record, }
    return render(request, 'mydjangoSoen/delete.html', params)


def find(request):
    if request.method == 'POST':
        msg = '結果はっぴょー'
        form = FindForm()
        str1 = request.POST['findname']
        str2 = str(request.POST['finddate'])
        data = IdModel.objects.filter(Q(name__icontains=str1)|Q(date__icontains=str2))
    else:
        msg = 'さがそう'
        form = FindForm()
        data = IdModel.objects.all()
    params = {
        'title': 'ここは、検索頁',
        'msg': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'mydjangoSoen/find.html', params)


@login_required()
def main(request):
    params = {
        'title': "これはmain頁",
        'msg': 'main'}
    return render(request, 'mydjangoSoen/main.html', params)


@login_required()
def sub(request):
    params = {
        'title': "これはsub頁",
        'msg': 'sub'}
    return render(request, 'mydjangoSoen/sub.html', params)
