from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404

from .forms import wagesF,steelPartsF,upPercentF
from .models import wagesM,steelPartsM
# Create your views here.
def topView(request):#Number トップページ
    params={
        'title':'ScriptsAppだす',
    }
    return render(request,'Number/numberTop.html',params)

def calcDescriptionNumber(request):
    params={
        'title':'計算番号検索⇒[ctrl]+[F]？',
    }
    return render(request,'Number/calcDescriptionNumber.html',params)

def InputWages(request):
    params={
        'title':'Input Wages',
        'form':wagesF(),
    }
    if request.method=='POST':
        obj=wagesM()
        rec=wagesF(request.POST,instance=obj)
        rec.is_valid()
        rec.save()
        return redirect(to='Number:topView')
    return render(request,'Number/inputDataForm.html',params)


def InputSteelParts(request):#Number 軽鉄部材　単価表の作成
    params={
        'title':'Input steelPartsPrice',
        'form':steelPartsF(),
    }
    if request.method=='POST':
        obj=steelPartsM()
        rec=steelPartsF(request.POST,instance=obj)
        rec.is_valid()
        rec.save()
        return redirect(to='Number:topView')
    return render(request,'Number/inputDataForm.html',params)

def ListPartsList(request):#Number 材料別Listの目次
    data=steelPartsM.objects.all().order_by('-firstDay')
    params={
        'title':'過去LIST',
        'data':data,

    }
    return render(request, 'Number/listPartsList.html', params)


from .application.priceScripts import MakeBasePrice_module
def ListSteelParts(request,number):#ListListからのdetail
    data=steelPartsM.objects.get(id=number)
    data2 = wagesM.objects.all().latest("id")
    form=upPercentF()
    params={
        'titile':'軽鉄部品価格表',
        'form':form,
        'data':data,
        'data2': data2,
    }
    if request.method=='POST':
        wagesUp=request.POST['wagesUp']
        partsUp = request.POST['partsUp']
        data=data
        data2=data2

        X=MakeBasePrice_module.func(data,data2,wagesUp,partsUp)
        print(X)
        return render(request,'Number/scriptAnswer.html',X)
    return render(request,'Number/listParts.html',params)
