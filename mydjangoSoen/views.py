from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import IdpwForm, IdSearch
from .models import IdpwModel
from django.shortcuts import redirect


# Create your views here.
def index(request):
    # alldata = IdpwModel.objects.all()
    params = {
        'title': "これはINDEX頁",
        'msg': "<h1>All Record !</h1>",
        'form': IdSearch(),  # idpwForm(),
        'data': [],}
    if (request.method == 'POST'):
        number = request.POST['id']
        item = IdpwModel.objects.get(id=number)
        params['title'] = 'お探しのName一致してますか？'
        params['msg'] = "<h2>your request is ...</h2>"
        params['data'] = [item]
        params['form'] = IdSearch(request.POST)
    else:
        params['data'] = IdpwModel.objects.all()  # model.objects.values('name','pw')
    return render(request, 'mydjangoSoen/index.html', params)


def create(request):
    params = {
        'title': "これはCREATE頁",
        'msg': "<h1>Let's Create !</h1>",
        'form': IdpwForm(),}
    if (request.method == 'POST'):
        # name = request.POST['name']
        # pw = request.POST['pw']
        # record = IdpwModel(name=name, pw=pw)
        obj= IdpwModel()
        record= IdpwForm(request.POSt,instance= obj)
        record.save()
        return redirect(to='mydjangoSoen:index')
    return render(request, 'mydjangoSoen/create.html', params)

def edit(request, number):
    obj = IdpwModel.objects.get(id=number)
    if (request.method == 'POST'):
        record=IdpwForm(request.POST,instance= obj)
        record.save()
        return redirect(to='mydjangoSoen:index')
    params={
        'title': '編集頁っす',
        'msg': '編集中ね',
        'form': 'IdpwModel'
    }
    return render(request, 'mydjangoSoen/index.html',params)

def delete(request,number):
    record= IdpwModel.objects.get(id= number)
    if (request.method == 'POST'):
        record.delete()
        return redirect(to='mydjangoSoen:index')
    params={
        'title': '削除ぉぉぉぉぉ',
        'msg': '本当 だいじょうぶ？',
        'id': number,
        'obj': record,
    }
    return render(request,'mydjangoSoen/delete.html', params)

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
