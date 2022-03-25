from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy, reverse
# Create your views here.
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic import ListView, CreateView, DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
# Create your views here.
from .models import Aspot, mostRecent, gContractor,Vehicle
from .forms import AspotForm, MostRecentForm, gContractorForm,VehicleForm

class aspotList(ListView,LoginRequiredMixin):
    model= Aspot
    queryset= Aspot.objects.all().prefetch_related('gContractor') 
    template_name= 'actualSpot/spotList.html'

class actualSpotDetailView(DetailView,LoginRequiredMixin):
    model= Aspot
    context_object_name='spot_detail'
    template_name='actualSpot/spotdetail.html'
    form_class= AspotForm

class actualSpotCreateView(CreateView,LoginRequiredMixin):
    model= Aspot
    template_name='actualSpot/spotcreate.html'
    form_class=AspotForm
    def get_success_url(self):
        # return reverse('reimex:spotdetail',kwargs={'pk':self.object.pk})
        return reverse('actualSpot:spotlist')
    
class actualSpotUpdateView(UpdateView,LoginRequiredMixin):
    model= Aspot
    template_name='actualSpot/spotupdate.html'
    form_class=AspotForm
    def get_success_url(self):
        # return reverse('reimex:spotdetail',kwargs={'pk':self.object.pk})
        return reverse('actualSpot:spotlist')

class actualSpotDeleteView(DeleteView,LoginRequiredMixin):
    template_name = 'actualSpot/spotdelete.html'
    model = Aspot
    success_url = reverse_lazy('actualSpot:spotlist')
    # form_class= Actual_spotForm
    context_object_name='spot_delete'

#*************************************************************************************************
class mostRecentList(ListView,LoginRequiredMixin):
    # model= SoenModel  #=== queryset= SoenModel.objects.all()
    queryset= mostRecent.objects.order_by('-recentName')   #=== def get_queryset()self  return SoenModel.objects.all()
    template_name= 'actualSpot/mostRecentList.html'
    # paginate_by= 20 #ﾍﾟｰｼﾞﾈｰｼｮﾝで利用
    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = mostRecent.objects.filter(
                Q(recentName__icontains=q_word) | Q(Xx__icontains=q_word))
        else:
            object_list = mostRecent.objects.order_by('recentName')
        return object_list


class mostRecentCreateView(CreateView,LoginRequiredMixin):
    model= mostRecent
    template_name='actualSpot/mostRecentCreate.html'
    form_class=MostRecentForm
    def get_success_url(self):
        return reverse('actualSpot:spotlist')
    
class mostRecentUpdateView(UpdateView,LoginRequiredMixin):
    model= mostRecent
    template_name='actualSpot/mostRecentUpdate.html'
    form_class=MostRecentForm
    def get_success_url(self):
        return reverse('actualSpot:spotlist')

class mostRecentDeleteView(DeleteView,LoginRequiredMixin):
    template_name = 'actualSpot/mostRecentDelete.html'
    model = mostRecent
    success_url = reverse_lazy('actualSpot:spotlist')
    
    context_object_name='mostRecent_delete'
#*************************************************************************************************
class gconList(ListView,LoginRequiredMixin):
    # model= SoenModel  #=== queryset= SoenModel.objects.all()
    queryset= gContractor.objects.order_by('-gName')   #=== def get_queryset()self  return SoenModel.objects.all()
    template_name= 'actualSpot/gconList.html'
    # paginate_by= 20 #ﾍﾟｰｼﾞﾈｰｼｮﾝで利用
    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = gContractor.objects.filter(
                Q(gName__icontains=q_word) | Q(gName__icontains=q_word))
        else:
            object_list = gContractor.objects.order_by('gName')
        return object_list


class gconCreateView(CreateView,LoginRequiredMixin):
    model= gContractor
    template_name='actualSpot/gconCreate.html'
    form_class=gContractorForm
    def get_success_url(self):
        return reverse('actualSpot:spotlist')
    
class gconUpdateView(UpdateView,LoginRequiredMixin):
    model= gContractor
    template_name='actualSpot/gconUpdate.html'
    form_class=gContractorForm
    def get_success_url(self):
        return reverse('actualSpot:spotlist')

class gconDeleteView(DeleteView,LoginRequiredMixin):
    template_name = 'actualSpot/gconDelete.html'
    model = gContractor
    success_url = reverse_lazy('actualSpot:spotlist')
    context_object_name='gcon_delete'
    
#*************************************************************************************************
class vehicleList(ListView,LoginRequiredMixin):
    # model= SoenModel  #=== queryset= SoenModel.objects.all()
    queryset= Vehicle.objects.order_by('vehicleNumber')   #=== def get_queryset()self  return SoenModel.objects.all()
    template_name= 'actualSpot/vehicleList.html'
    # paginate_by= 20 #ﾍﾟｰｼﾞﾈｰｼｮﾝで利用
    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = Vehicle.objects.filter(
                Q(gName__icontains=q_word) | Q(gName__icontains=q_word))
        else:
            object_list = Vehicle.objects.order_by('vehicleNumber')
        return object_list


class vehicleCreateView(CreateView,LoginRequiredMixin):
    model= Vehicle
    template_name='actualSpot/vehicleCreate.html'
    form_class=VehicleForm
    def get_success_url(self):
        return reverse('actualSpot:spotlist')
    
class vehicleUpdateView(UpdateView,LoginRequiredMixin):
    model= Vehicle
    template_name='actualSpot/vehicleUpdate.html'
    form_class=VehicleForm
    def get_success_url(self):
        return reverse('actualSpot:spotlist')

class vehicleDeleteView(DeleteView,LoginRequiredMixin):
    template_name = 'actualSpot/vehicleDelete.html'
    model = Vehicle
    success_url = reverse_lazy('actualSpot:spotlist')
    context_object_name='vehicle_delete'

from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError    
@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)