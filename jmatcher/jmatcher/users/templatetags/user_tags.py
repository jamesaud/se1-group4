from django import template

register = template.Library()


@register.filter(name='connections')
def connect(first_user, second_user):
    return set.intersection(set(first_user.connections.all()), set(second_user.connections.all()))
