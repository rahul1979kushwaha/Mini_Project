from django.http import JsonResponse


def index(request, *args, **kwargs):
    m = 'abcdef'
    return JsonResponse({'message':"hello this is msg", 'm':m})
