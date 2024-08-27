from django import template

register = template.Library()

@register.filter(name='custom_split')
def custom_split(???):
    pass