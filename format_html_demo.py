


from django.utils.html import format_html
from django.utils.safestring import mark_safe

print(format_html('{}', mark_safe('Пицца с <i>сыром</i>')), '-OK')
print(format_html('{}', mark_safe('Пицца с <i#>сыром')), '-OK')
print(format_html('{}', mark_safe('Пицца с <i>сыром')), '-BAD')
print(format_html(mark_safe('Пицца с <i>сыром')), '-BAD')

