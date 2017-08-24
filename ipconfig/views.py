from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
        if v=='HTTP_X_REAL_IP':
            return HttpResponse('Your ip is: %s' % (v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
