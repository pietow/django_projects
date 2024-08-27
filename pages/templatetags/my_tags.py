# from django import template
from django.template import Library

# register = template.Library()
register = Library()

@register.simple_tag
def hello_world():
    return 'Hello World'