from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from datetime import datetime

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        print(request.method)
        print(request.GET)
        print(request.COOKIES)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # by default it returns an empty dictionary
        context['key1'] = 'value1'
        context['key2'] = 'value2'
        context['title'] = 'Hello World'
        context['first'] = [1, 2, 3]
        context['second'] = [4, 5, 6]
        context['today'] = datetime.now()
        context['notes'] = "<strong>Note:</strong> Always learn something new!"
        context['js_inject'] = "<script>alert('Hello World')</script>"
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"

def home_func_view(request):
    print(request.method) # GET
    print(request.GET) # GET 
    print(request.COOKIES)
    context = {
        'key1': 'value1',
        'key2': 'value2',
        'title': 'Hello World',
        'first': [1, 2, 3],
        'second': [4, 5, 6],
        'today': datetime.now(),
        'notes': "<strong>Note:</strong> Always learn something new!",
        'js_inject':"<script>alert('Hello World')</script>"
    }

    return render(request, 'home2.html', context)
    # response_obj = render(request, 'home2.html', context)
    # response_obj.write('<h1>Hello</h1>')
    # return response_obj

    another_response = HttpResponse('<h1>bla</h1>')
    another_response.write('<div>Hello World</div>')
    another_response.set_cookie('another_cookie', 'value3')
    return another_response




