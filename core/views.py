from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def django_hash_make_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hashed_password = make_password(password)
        return JsonResponse({'message':f'{hashed_password}', 'message_hint':'hash_generated'})
    else:
        return JsonResponse({'message':'Methods not allowed'}, status=400)
    
@csrf_exempt
def django_hash_check_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hashed_password = request.POST.get('hashed_password')
        is_valid = check_password(password, hashed_password)
        return JsonResponse({'message':f'{is_valid}', 'message_hint':'password_verified'})
    else:
        return JsonResponse({'message':'Methods not allowed'}, status=400)