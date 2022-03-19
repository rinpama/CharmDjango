from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import ActualSpotMo, AsSoenMo
from Soen.models import MemberMo
from .forms import ActualSpotF, AsSoenF, AsSearchF
from Soen.forms import MemberF


# Create your views here.
# *******************************************************************************************
def VsekoList(request):
    data = ActualSpotMo.objects.all()
    form = ActualSpotF()
    data2=AsSoenMo.objects.all()
    form2=AsSoenF()
    if request.method == 'POST':  # 簡易create
        rec = ActualSpotMo()
        obj = ActualSpotF(request.POST, instance=rec)
        rec2 = AsSoenMo(actualspot=rec)
        obj2 = AsSoenF(request.POST, instance=rec2)
        if obj.is_valid():
            obj.save()
        if obj.is_valid():
            obj2.save()
            return redirect(to='Show:VsekoList')
    # else:
    #     form = ActualSpotF()
    params = {
        'msg': 'リストページ',
        'data': data,
        'form': form,
        'data2': data2,
        'form2':form2,
        'form4': AsSearchF(),
    }
    return render(request, 'Show/sekoList.html', params)

# *******************************************************************************************
def VsekoListSearch(request):
    params = {
        'msg': '現場検索',
    }
    if request.method == 'POST':
        nametxt = request.POST['name']
        item = ActualSpotMo.objects.filter(Q(AsName__icontains=nametxt))
        params['finded'] = item
        params['form'] = ActualSpotF()
        params['form4'] = AsSearchF(request.POST)
    else:
        params['data'] = ActualSpotMo.objects.all()
        params['form4'] = AsSearchF()
    return render(request, 'Show/sekoList.html', params)


# *******************************************************************************************
def Vsekodetail(request, number):
    record = ActualSpotMo.objects.get(pk=number)
    form = ActualSpotF(instance=record)
    rec = AsSoenMo(actualspot=record)
    obj = AsSoenF(request.POST, instance=rec)
    params = {
        'title': '詳細頁',
        'msg': "<h1>Let's show me!</h1>",
        'data': record,
        'data2':rec,
    }
    return render(request, 'Show/sekodetail.html', params)
# *******************************************************************************************
def Vsekocreate(request):
    params = {
        'title': "これはCREATE頁",
        'msg': "<h1>Let's Create !</h1>",
        'form': ActualSpotF(),
    }
    if request.method == 'POST':
        obj = ActualSpotMo()
        record = ActualSpotF(request.POST, instance=obj)
        if record.is_valid():
            record.save()
            return redirect(to='Show:VsekoList')
    return render(request, 'Show/sekocreate.html', params)


# *******************************************************************************************
@login_required
def VlogsekoList(request):
    data = ActualSpotMo.objects.all()
    params = {
        'data': data
    }
    return render(request, 'Show/logsekoList.html', params)

    # *******************************************************************************************
def Vlogsekocreate(request):
    params = {
        'title': "これはCREATE頁",
        'msg': "<h1>Let's Create !</h1>",
        'form': ActualSpotF(),
    }
    if request.method == 'POST':
        obj = ActualSpotMo()
        record = ActualSpotF(request.POST, instance=obj)
        if record.is_valid():
            record.save()
            return redirect(to='Show:VlogsekoList')
    return render(request, 'Show/logsekocreate.html', params)

    # *******************************************************************************************
@login_required
def Vlogsekosmemcreate(request):
    params = {
        'title': "これはCREATE頁",
        'msg': "<h1>Let's Create !</h1>",
        'form2': AsSoenF(),
    }
    if request.method == 'POST':
        obj = AsSoenMo()
        record = AsSoenF(request.POST, instance=obj)
        if record.is_valid():
            record.save()
            return redirect(to='Show:VlogsekoList')
    return render(request, 'Show/logsekosmemcreate.html', params)

    # *******************************************************************************************
@login_required
def Vlogsekosmemlist(request):
    data = AsSoenMo.objects.all()
    params = {
        'data': data
    }
    return render(request, 'Show/logsekosmemlist.html', params)

    # *******************************************************************************************
@login_required
def Vlogsekoedit(request, number):
    obj = ActualSpotMo.objects.get(id=number)
    # if AsSoenMo.objects.get(actualspot=obj):
    #     obj2 = AsSoenMo.objects.get(actualspot=obj)
    # else:
    #     obj2=AsSoenMo()
    obj2=AsSoenMo()
    if request.method == 'POST':
        record = ActualSpotF(request.POST, instance=obj)
        record2 = AsSoenF(request.POST, instance=obj2)

        if record.is_valid():
            record.save()
        if record2.is_valid():
            record2.save()
        return redirect(to='Show:VlogsekoList')
    params = {
        'title': '編集頁っす',
        'msg': '編集中ね',
        'record': obj,
        'id': number,
        'form': ActualSpotF(instance=obj),
        'form2': AsSoenF(instance=obj2),
    }
    return render(request, 'Show/logsekoedit.html', params)


# *******************************************************************************************
@login_required
def Vlogsekodelete(request, number):
    record = ActualSpotMo.objects.get(pk=number)
    if request.method == 'POST':
        record.delete()
        return redirect(to='Show:VlogsekoList')
    params = {
        'title': '削除ぉぉぉぉぉ',
        'msg': '本当 だいじょうぶ？',
        'id': number,
        'obj': record, }
    return render(request, 'Show/logsekodelete.html', params)

    # *******************************************************************************************
@login_required
def Vlogsekosmemedit(request, number):
    obj2 = AsSoenMo.objects.get(id=number)
    obj = ActualSpotMo.objects.get(actualspot=obj2)
    # obj2 = AsSoenMo.objects.get(actualspot=obj)
    if request.method == 'POST':
        record = ActualSpotF(request.POST, instance=obj)
        record2 = AsSoenF(request.POST, instance=obj2)
        if record.is_valid():
            record.save()
        if record2.is_valid():
            record2.save()
        return redirect(to='Show:VlogsekoList')
    params = {
        'title': '編集頁っす',
        'msg': '編集中ね',
        'record': obj,
        'id': number,
        'form': ActualSpotF(instance=obj),
        'form2': AsSoenF(instance=obj2),
    }
    return render(request, 'Show/logsekosmemedit.html', params)


# *******************************************************************************************
@login_required
def Vlogsekosmemdelete(request, number):
    record = AsSoenMo.objects.get(pk=number)
    if request.method == 'POST':
        record.delete()
        return redirect(to='Show:VlogsekoList')
    params = {
        'title': '削除ぉぉぉぉぉ',
        'msg': '本当 だいじょうぶ？',
        'id': number,
        'obj': record, }
    return render(request, 'Show/logsekosmemdelete.html', params)
