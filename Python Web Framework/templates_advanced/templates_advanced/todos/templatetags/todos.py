from django import template

from templates_advanced.todos.models import Todo

register = template.Library()


@register.simple_tag()
def todos_count(value):
    return Todo.objects.count() + value


@register.inclusion_tag(
    'shared/templatetags/todos_preview.html',
    takes_context=True)
def todos_preview(context):
    print(context)
    return {
        'count': Todo.objects.count(),
    }
