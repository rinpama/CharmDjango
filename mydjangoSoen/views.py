from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import IdForm, IdSearch
from .models import IdModel
from django.shortcuts import redirect


# Create your views here.
def index(request):
    # alldata = IdpwModel.objects.all()
    params = {
        'title': "これはINDEX頁",
        'msg': "<h1>All Record !</h1>",
        'form': IdSearch(),  # idpwForm(),
        'data': [], }
    if (request.method == 'POST'):
        nametxt = request.POST['name']
        item = IdModel.objects.get(name=nametxt)
        params['title'] = 'お探しのName一致してますか？'
        params['msg'] = "<h2>your request is ...</h2>"
        params['data'] = [item]
        params['form'] = IdForm(request.POST)
    else:
        params['data'] = IdModel.objects.all()  # model.objects.values('name','pw')
    return render(request, 'mydjangoSoen/index.html', params)


def create(request):
    params = {
        'title': "これはCREATE頁",
        'msg': "<h1>Let's Create !</h1>",
        'form': IdForm(), }
    if (request.method == 'POST'):
        # name = request.POST['name']
        # pw = request.POST['pw']
        # record = IdpwModel(name=name, pw=pw)
        obj = IdModel()
        record = IdForm(request.POST, instance=obj)
        record.save()
        return redirect(to='mydjangoSoen:index')
    return render(request, 'mydjangoSoen/create.html', params)


def edit(request, number):
    obj = IdModel.objects.get(id=number)
    if (request.method == 'POST'):
        record = IdForm(request.POST, instance=obj)
        record.save()
        return redirect(to='mydjangoSoen:edit')
    params = {
        'title': '編集頁っす',
        'msg': str(obj) + '       編集中ね' ,
        'form': IdForm()
    }
    return render(request, 'mydjangoSoen/index.html', params)


def delete(request, number):
    record = IdModel.objects.get(id=number)
    if (request.method == 'POST'):
        record.delete()
        return redirect(to='mydjangoSoen:index')
    params = {
        'title': '削除ぉぉぉぉぉ',
        'msg': '本当 だいじょうぶ？',
        'id': number,
        'obj': record,
    }
    return render(request, 'mydjangoSoen/delete.html', params)


# @login_required()
def main(request):
    params = {
        'title': "これはmain頁",
        'msg': 'main'}
    return render(request, 'mydjangoSoen/main.html', params)


# @login_required()
def sub(request):
    params = {
        'title': "これはsub頁",
        'msg': 'sub'}
    return render(request, 'mydjangoSoen/sub.html', params)
