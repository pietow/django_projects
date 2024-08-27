from django import template

register = template.Library()

@register.filter(name='custom_split')
def custom_split(s, delimiter=' '):
    s_list = s.split(delimiter)
    return s_list