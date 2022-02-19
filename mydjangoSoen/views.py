from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic import DetailView

from .forms import IdSearch, FindForm, IdForm, IddetailForm, BlogForm
from .models import IdModel, Iddetail, BlogModel


# Create your views here.
def index(request):
    params = {
        'title': "これはINDEX頁",
        'msg': "<h1>All Soen Member !</h1>",
        'form': IdSearch(),
        'btn1': '検索',
        'data': [], }
    if request.method == 'POST':
        nametxt = request.POST['name']
        item = IdModel.objects.filter(Q(name__icontains=nametxt))
        params['title'] = 'お探しのName一致してますか？'
        params['msg'] = "<h2>your request is ...</h2>"
        params['finded'] = item
        params['form'] = IdSearch(request.POST)
    else:
        params['data'] = IdModel.objects.all()
    return render(request, 'mydjangoSoen/index.html', params)


def VIddetail(request, pk):
    record = IdModel.objects.get(pk=pk)
    params = {
        'title': '詳細頁',
        'msg': "<h1>Let's show me!</h1>",
        # 'form': IdForm(instance=record),
        'record': record,
    }
    return render(request, 'mydjangoSoen/detail.html', params)


# class IdModelDetail(DetailView):
#     model = IdModel  # ,Iddetail,BlogModel
#     context_object_name = 'idmodel'
#     template_name = 'mydjangoSoen/detail.html'


def create(request):
    params = {
        'title': "これはCREATE頁",
        'msg': "<h1>Let's Create !</h1>",
        'form': IdForm(),
    }
    if request.method == 'POST':
        obj = IdModel()
        record = IdForm(request.POST, instance=obj)
        if record.is_valid():
            record.save()
            return redirect(to='mydjangoSoen:index')
    return render(request, 'mydjangoSoen/create.html', params)


@login_required
def edit(request, number):
    obj = IdModel.objects.get(id=number)
    # var = obj.details  #Iddetails

    params = {
        'title': '編集頁っす',
        'msg': '編集中ね',
        'record': obj,
        'id': number,
        'form': IdForm(instance=obj)}
    if request.method == 'POST':
        record = IdForm(request.POST, instance=obj)
        if record.is_valid():
            record.save()
            detai=Iddetail(request.POST,IdModel=obj)
            detai.save()
        return redirect(to='mydjangoSoen:main')
    return render(request, 'mydjangoSoen/edit.html', params)


@login_required
def delete(request, number):
    record = IdModel.objects.get(id=number)
    if request.method == 'POST':
        record.delete()
        return redirect(to='mydjangoSoen:main')
    params = {
        'title': '削除ぉぉぉぉぉ',
        'msg': '本当 だいじょうぶ？',
        'id': number,
        'obj': record, }
    return render(request, 'mydjangoSoen/delete.html', params)


@login_required()
def main(request):
    if request.method == 'POST':
        msg = '結果はっぴょー'
        form = FindForm()
        str1 = request.POST['findname']
        str2 = str(request.POST['findadd'])
        data = IdModel.objects.filter(Q(name__icontains=str1) | Q(date__icontains=str2))
    else:
        msg = 'ココからはログインしてます<br><h3>社員一覧</h3>'
        form = FindForm()
        data = IdModel.objects.all()
    params = {
        'title': 'ここは、検索頁',
        'msg': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'mydjangoSoen/main.html', params)


@login_required()
def sub(request):
    params = {
        'title': "これはsub頁",
        'msg': 'sub'}
    return render(request, 'mydjangoSoen/sub.html', params)
