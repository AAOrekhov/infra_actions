from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Я не могу в это поверить')


def second_page(request):
    return HttpResponse('А это вторая страница! не работает(((')
