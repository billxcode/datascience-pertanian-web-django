from django import template

register = template.Library()
# Register your models here.

def index(l, i):
    return l[i]

register.filter('index', index)