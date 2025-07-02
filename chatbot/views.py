from django.shortcuts import render
from django.http import JsonResponse

def chatbot(request):
    user = request.user
    user_id = user.id if user.is_authenticated else None

    return render(request, 'chatbot/index.html', {'user_id': user_id})

def login(request):
    return JsonResponse({"message": "Login API"})

def register(request):
    return JsonResponse({"message": "Register API"})

def logout(request):
    return JsonResponse({"message": "Logout API"})

def health_check(request):
    return JsonResponse({"status": "OK"})

