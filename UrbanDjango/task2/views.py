from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ClassTemplate(TemplateView):
    template_name = 'class_template.html'


def func(request):
    return render(request, 'func_template.html')