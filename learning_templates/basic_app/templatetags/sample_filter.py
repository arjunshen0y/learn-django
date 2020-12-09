from django import template

register = template.Library()

@register.filter(name = 'cutt')
def cut(value,arg):
    # its a function to replace passed value with empty character

    return value.replace(arg ,'')