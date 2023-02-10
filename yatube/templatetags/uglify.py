from django import template
register = template.Library()


@register.filter
def uglify(filed):
    a = ''
    i = 0
    for letter in filed:
        i += 1
        if i % 2 == 0:
            a += letter.upper()
        else:
            a += letter.lower()
    return a
