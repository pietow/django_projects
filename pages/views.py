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
    # print(request.method) # GET
    print(request.GET) # GET 
    # print(request.COOKIES)
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

    another_response = HttpResponse('<h1>bla</h1>')
    another_response.write('<div>Hello World</div>')
    another_response.write('<div>Hello World</div>')
    another_response.writelines(['<h1>H</h1>', '<h1>H</h1>',
    '<p>Hello<span>Bla</span></p>'])
    another_response.writelines(['<h1>H</h1>', '<h1>H</h1>',
    '<span>Bla</span>', '<span>Bla</span>'])
    return another_response




def home_func_view(request):
    print(request.method) # GET
    print(request.GET) # GET 
    print(request.COOKIES)
    context = {
        'key1': 'value1',
        'key2': 'value2',
        'title': 'Hello World',
    }


class HomePageView2(TemplateView):
    template_name = "home2.html"

    def dispatch(self, request, *args, **kwargs):
        print(request.method) 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        cookies_dict = request.COOKIES
        if cookies_dict.get('my_cookie') == 'my_cookie_value':
            my_response = HttpResponse('With cookie')
            my_response.set_cookie('key', 'value')
            return my_response
        my_super_response = super().get(request, *args, **kwargs)
        my_super_response.set_cookie('super_key', 'super_value')
        return my_super_response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key1'] = 'value1'
        context['key2'] = 'value2'
        context['title'] = 'Hello World'
        return context









