from django.shortcuts import render
from django.views.generic import TemplateView
import requests
# Create your views here.
# class IndexView(TemplateView):
#     template_name = "app_one/index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "App One"
#         return context

def index(request):
    responce = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    current = responce.get('rates')
    
    if request.method == 'GET':

        context = {
            'current': current,

        }
        return render(request, template_name='app_one/index.html', context=context)
    
    if request.method == 'POST':
        
        sum = request.POST.get('from-amount')
        from_nat = request.POST.get('from-curr')
        to_nat = request.POST.get('to-curr')

        converted_amount = round((current[to_nat] / current[from_nat]) * float(sum), 2)

        context = {
            'sum': sum,
            'from_nat': from_nat,
            'to_nat': to_nat,
            'current': current,
            'converted_amount':converted_amount,
        }

        # print(context['from_nat'])
        # print(context['to_nat'])
        # print(context['sum'])
        return render(request, template_name='app_one/index.html', context=context) 