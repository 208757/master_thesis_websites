from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Operation
from django.views import View
from .forms import LoginForm, ChooseForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests
from .constants import AUTH_TOKEN
from .models import User

# Create your views here.
class LogPageView(View):

    def get(self, request):
        return render(request, 'log_form.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None and user.is_active:
                login(request, user)
                return redirect('/web/mainpage')
        return render(request, "log_form.html")


class MainPageView(View):

    def get(self, request):
        form = ChooseForm()
        return render(request, "main.html", {
            "form": form
        })

    def post(self, request):
        form = ChooseForm(request.POST)
        user = request.user
        cd = form.data
        id = len(Operation.objects.all())
        operation = Operation(user=user, state="waiting", operation_number=id, operation_type=cd['widget'])
        operation.save()
        operation_msg = ""
        if cd['widget'] == "delete_id":
            operation_msg = "account deletion"
        elif cd['widget'] == "transfer_id":
            operation_msg = "transfer cash"
        elif cd['widget'] == "change_phone_id":
            operation_msg = "change phone number"

        content = {
            "username": user.username,
            "operation_id": id,
            "operation_msg": operation_msg
        }
        headers = {"Authorization": AUTH_TOKEN}
        r = requests.post('http://127.0.0.1:8001/api/notify/', headers=headers, data=content)
        return render(request, "waiting.html", {
            "operation_id": id,
            "operation_msg": operation_msg
        })

def end_session(request):
    logout(request)
    return redirect("/")
