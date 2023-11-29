from django.http import JsonResponse


def index(request, *args, **kwargs):
    return JsonResponse({'message':"hello this is msgs", 'name': 'Prince'})
