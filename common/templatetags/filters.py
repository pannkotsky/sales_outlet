from django import template

register = template.Library()


@register.filter
def get_value(obj, key):
    return obj.get(key)
