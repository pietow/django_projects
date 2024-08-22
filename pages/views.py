from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

def home_func_view(request):
    print(request.method) # GET
    print(request.COOKIES)
    context = {
        'key1': 'value1',
        'key2': 'value2',
        'title': 'Hello World',
    }

    return render(request, 'home2.html', context)
    # response_obj = render(request, 'home2.html', context)
    # response_obj.write('<h1>Hello</h1>')
    # return response_obj

    another_response = HttpResponse('<h1>bla</h1>')
    another_response.write('<div>Hello World</div>')
    another_response.set_cookie('another_cookie', 'value3')
    return another_response




