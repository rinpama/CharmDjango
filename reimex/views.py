from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy, reverse
# Create your views here.
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic import ListView, CreateView, DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.decorators.http import require_POST　　# @require_POST:def
from django.db.models import Q

from .models import SoenModel
from .forms import SoenModelForm
from actualSpot.models import Aspot

def top(request):
    return render(request,'reimex/reimextop.html')

# class SoenModelList(ListView,LoginRequiredMixin):
#     # model= SoenModel  #=== queryset= SoenModel.objects.all()
#     queryset= SoenModel.objects.order_by('-checking') #=== def get_queryset()self  return SoenModel.objects.all()
#     template_name= 'reimex/list.html'
#     def get_context_data(self,**kwargs):
#         context=super().get_context_data(**kwargs)
#         context.update({
#             'actualSpot': Aspot.objects.order_by('spotName'),
#             'more_context':Aspot.objects.all()  
#         })
#         members_list=SoenModel.objects.order_by('-checking')
#         return context

class SoenMemberList(ListView,LoginRequiredMixin):
    queryset= SoenModel.objects.order_by('djgroup2')   
    template_name= 'reimex/memberlist.html'
    # paginate_by= 20 #ﾍﾟｰｼﾞﾈｰｼｮﾝで利用
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = SoenModel.objects.filter(
                Q(name__icontains=q_word) | Q(kanaName__icontains=q_word))
        else:
            object_list = SoenModel.objects.order_by('-code').order_by('djgroup2')
        return object_list
  
class SoenModelDetail(DetailView,LoginRequiredMixin):
    model= SoenModel
    context_object_name='soen'
    template_name='reimex/detail.html'
    
class SoenModelCreate(CreateView,LoginRequiredMixin):
    model= SoenModel
    template_name='reimex/create.html'
    form_class=SoenModelForm
    def get_success_url(self):
        return reverse('reimex:sdetail',kwargs={'pk':self.object.pk})
    
class SoenModelUpdate(UpdateView,LoginRequiredMixin):
    model= SoenModel
    template_name='reimex/update.html'
    form_class=SoenModelForm
    # fields=['name','code','age']
    def get_success_url(self):
        return reverse('reimex:mlist')

class SoenModelDelete(DeleteView,LoginRequiredMixin):
    template_name = 'reimex/delete.html'
    model = SoenModel
    success_url = reverse_lazy('reimex:mlist')

# ***********************************************************************
# -----作業員名簿　Checking_Scripts----
members=[]
def memFalse(self):
    for member in Aspot.objects.all():
        a=Aspot.objects.get(spotName= member.spotName)
        a.members.clear()
    return render(self,'templates/reimex/list.html')

def onlymemFalse(request):
    for selected_spot in Aspot.objects.filter(checking=True): 
        print(selected_spot.spotName)
        a=Aspot.objects.get(spotName=selected_spot.spotName)
        a.members.clear()
        return render(request,'templates/reimex/list.html')

spots=[]
def spotFalse(self):
    for spot in Aspot.objects.all():
        # print(spot.checking)
        spot.checking= False
        # print(spot.checking)
        spots.append(spot)
    Aspot.objects.bulk_update(spots,fields=['checking'])
    return render(self,'templates/reimex/list.html')


# ***********************************************************************
# **********************************************************************
# ***********************************************************************
# -----作業員名簿　職方記載用Scripts----
from django.template import loader
from .application import test_module                 
def testprint(self):
    test_module.func()
    # params= {}
    return render(self,'reimex/list.html')#,params)

# ***********************************************************************
# -----施工体制台帳用記載用Scripts----
from .application import Aspot_module
def aspot(self):
    Aspot_module.func(self)
    return redirect('actualSpot:spotlist')
# **********************************************************************
from .application import AspotToExcel_module
def aspotToExcel(self):
    AspotToExcel_module.func(self)
    # print(wb)
    return redirect('actualSpot:spotlist')
# **********************************************************************






#　↓　これは本番deploy後に消すように（デプロイ後用ERROR探査）ほかの場所にもあるからチャンと探して消してね
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError    
@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)