from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def django_hash_make_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if not password:
            return JsonResponse({'message': 'Password is required'}, status=400)
        
        hashed_password = make_password(password)
        if hashed_password:
            return JsonResponse({'message': f'{hashed_password}', 'message_hint':'hash_generated'}, status=201)
        else:
            return JsonResponse({'message': 'Error while generating hash please try again'}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@csrf_exempt
def django_hash_check_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hashed_password = request.POST.get('hashed_password')
        
        if not password or not hashed_password:
            return JsonResponse({'message': 'Both password and hashed_password are required'}, status=400)
        
        if check_password(password, hashed_password):
            return JsonResponse({'message': 'Password Verified', 'message_hint':'password_verified'}, status=200)
        else:
            return JsonResponse({'message': 'Password Mismatch'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
    
def home_page(request):
    return JsonResponse({'message': 'Welcome to Django Hasher API'})
