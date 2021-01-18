from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings

register = template.Library()
 
@register.filter
@stringfilter
def switch_rating(count):
    output = ''
    count_all  = 3
    for _ in range(int(count)) :
        output += '<i class = "fa fa-star fa-fw" style = "color : gold;font-size:15px"></i>'
        count_all -= 1
    for _ in range(int(count_all)) :        
        output += '<i class = "fa fa-star fa-fw"></i>'
    return output
@register.filter
@stringfilter
def number_convertor(number_string):
    lis=[]
    dic = {
        '0': '۰',
        '1': '١',
        '2': '٢',
        '3': '۳',
        '4': '٤',
        '5': '۵',
        '6': '٦',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }
    for char in number_string:
        if char in dic:
            lis.append(dic[char])
        else:
            lis.append(char)
    return "".join(lis)