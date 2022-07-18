from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag
def getPageList():
    pages = Page.objects.all()
    return pages