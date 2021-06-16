from django.http import JsonResponse


def sayhi(request):
    data = {"sayhi": "hihihi!!!"}
    return JsonResponse(data)
