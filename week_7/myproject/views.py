from django.http import JsonResponse


def say_something(request):
    return JsonResponse({"message": "Hello from the sever side"})
