from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse

def django_hash_make_password(request):
    return JsonResponse({'message':'Make Password Called'})