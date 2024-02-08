from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import * 
from django.http import HttpResponse 
# Create your views here.


class TemplateHtml(TemplateView): 
    template_name='TemplateHtml.html'  
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs) 
        ECDO['name']='ganesh'
        ECDO['age']='22'
        return ECDO 

class insertSchoolByTV(TemplateView):
    template_name='insertSchoolByTV.html' 
    def get_context_data(self, **kwargs): 
        ECDO=super().get_context_data(**kwargs) 
        ECDO['SFO']=SchoolForm 
        return ECDO  
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByTV is done') 


class InsertSchoolByFV(FormView):
    template_name='InsertSchoolByFV.html' 

    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('InsertSchoolByFV is done')

    