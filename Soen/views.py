from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q
from django.views.generic import DetailView

from .models import MemberMo, MemberDetailMo, BlogMo
from .forms import IdSearch, FindForm, MemberF, MemberDetailF, BlogF  # NewMemberF,


# Create your views here.
#***************************************************************************************
def Vindex(request):
    params = {
        'title': "これはINDEX頁",
        'msg': "<h1> Soen Member !</h1>",
        'form': IdSearch(),
        'btn1': '検索',
        'data': [], }
    if request.method == 'POST':
        nametxt = request.POST['name']
        item = MemberMo.objects.filter(Q(name__icontains=nametxt))
        params['title'] = 'お探しのName一致してますか？'
        params['msg'] = "<h2>your request is ...</h2>"
        params['finded'] = item
        params['form'] = IdSearch(request.POST)
    else:
        params['data'] = MemberMo.objects.all()
    return render(request, 'Soen/index.html', params)
#***************************************************************************************
def Vdetail(request, number):
    record = MemberMo.objects.get(id=number)
    form=MemberF(instance=record)
    params = {
        'title': '詳細頁',
        'msg': "<h1>Let's show me!</h1>",
        'record': record,
        'form':form,
    }
    return render(request, 'Soen/detail.html', params)

#***************************************************************************************
def Vcreate(request):
    params = {
        'title': "これはCREATE頁",
        'msg': "<h1>Let's Create !</h1>",
        'form': MemberF(),
    }
    if request.method == 'POST':
        obj = MemberMo()
        obj2 = MemberDetailMo(memberm=obj)
        obj3 = BlogMo(memberm=obj)
        record = MemberF(request.POST, instance=obj)
        record2 = MemberDetailF(request.POST, instance=obj2)  # *******************
        record3 = BlogF(request.POST, instance=obj3)
        if record.is_valid():
            record.save()
            record2.save()
            record3.save()
            return redirect(to='Soen:Vindex')
    return render(request, 'Soen/create.html', params)

#***************************************************************************************
@login_required()
def Vlogsmemlist(request):
    if request.method == 'POST':
        msg = '結果はっぴょー'
        form = FindForm()
        str1 = str(request.POST['findname'])
        str2 = str(request.POST['findadd'])
        finded = MemberMo.objects.filter(Q(name__icontains=str1) | Q(add__icontains=str2))
        data = []
    else:
        msg = '<h3>SoenMember</h3>'
        form = FindForm()
        data = MemberMo.objects.all()
        finded = []
    params = {
        'title': 'ここは、検索頁',
        'msg': msg,
        'form': form,
        'data': data,
        'finded': finded,
    }
    return render(request, 'Soen/logSmemList.html', params)

#***************************************************************************************
@login_required
def Vlogsmemcreatemore(request):
    params = {
        'title': "これはNEWCREATE頁",
        'msg': "<h1>Let's NewCreate !</h1>",
        'form': MemberF(),
        'form2': MemberDetailF(),
        'form3': BlogF(),
    }
    if request.method == 'POST':
        obj = MemberMo()
        obj2 = MemberDetailMo(memberm=obj)
        obj3 = BlogMo(memberm=obj)
        record = MemberF(request.POST, instance=obj)
        record2 = MemberDetailF(request.POST, instance=obj2)
        record3 = BlogF(request.POST, instance=obj3)
        # if record.is_valid():
        record.save()
        record2.save()
        record3.save()
        return redirect(to='Soen:Vlogsmemlist')
    return render(request, 'Soen/logCreateMore.html', params)

#***************************************************************************************
@login_required
def Vlogsmemedit(request, number):
    obj = MemberMo.objects.get(id=number)
    obj2 = MemberDetailMo.objects.get(memberm=obj)
    obj3 = BlogMo.objects.get(memberm=obj)
    params = {
        'title': '編集頁っす',
        'msg': '編集中ね',
        'record': obj,
        'id': number,
        'form': MemberF(instance=obj),
        'form2': MemberDetailF(instance=obj2),
        'form3': BlogF(instance=obj3),
    }
    if request.method == 'POST':
        record = MemberF(request.POST, instance=obj)
        record2 = MemberDetailF(request.POST, instance=obj2)
        record3 = BlogF(request.POST, instance=obj3)
        if record.is_valid():
            record.save()
        if record2.is_valid():
            record2.save()
        if record3.is_valid():
            record3.save()
        return redirect(to='Soen:Vlogsmemlist')
    return render(request, 'Soen/logSmemEdit.html', params)

#***************************************************************************************
@login_required
def Vlogsmemdelete(request, number):
    record = MemberMo.objects.get(id=number)
    if request.method == 'POST':
        record.delete()
        return redirect(to='Soen:Vlogsmemlist')
    params = {
        'title': '削除ぉぉぉぉぉ',
        'msg': '本当 だいじょうぶ？',
        'id': number,
        'obj': record, }
    return render(request, 'Soen/logSmemDelete.html', params)

#***************************************************************************************
@login_required()
def Vlogmain(request):
    params = {
        'title': "これはmain頁",
        'msg': 'main'}
    return render(request, 'Soen/logMain.html', params)

#***************************************************************************************
@login_required()
def Vlogmainsub(request):
    params = {
        'title': "これはsub頁",
        'msg': 'sub'}
    return render(request, 'Soen/logMainsub.html', params)

#***************************************************************************************
@login_required()
def Vlogsmemdetail(request):
    if request.method == 'POST':
        msg = '結果はっぴょー'
        form = FindForm()
        str1 = str(request.POST['findname'])
        str2 = str(request.POST['findadd'])
        data = MemberMo.objects.filter(Q(name__icontains=str1) | Q(add__icontains=str2))
    else:
        msg = '<h3>SoenMember</h3>'
        form = FindForm()
        data = MemberMo.objects.all()
    params = {
        'title': 'ここは、検索頁',
        'msg': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'Soen/logSmemList.html', params)
#***************************************************************************************