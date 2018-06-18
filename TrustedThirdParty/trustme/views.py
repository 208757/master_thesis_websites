# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import ServiceProvider, Subscriber, Authentication, User
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated



class LoginView(ObtainAuthToken):

    def post(self, request):
        print(request.data)
        cd = request.data
        user = authenticate(username=cd["username"],
                            password=cd["password"])
        if user == None:
            return "Token None"
        token = Token.objects.get_or_create(user=user)
        if token[1]:
            token[0].save()
        return JsonResponse({'token': str(token[0])})



class NotifierView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        provider = ServiceProvider.objects.get(user=request.user)
        print(request.data)
        if provider == None:
            return JsonResponse({"error": True,
                                 "msg": "You are not provider"})
        state = "READY"
        print(request.data)
        #parsing notify request

        try:
            service_user = User.objects.get(username=request.data['username'])
            print("A")

            subscriber = Subscriber.objects.get(user=service_user)
            print("B")
            print(subscriber)
            print(provider.subscriptions.all())
            subscribers = provider.subscriptions.all()#(subscriber=subscriber)
            print("C")

            authentication = Authentication(user=subscribers, service=provider, process_id=request.data['operation_id'],
                                            content=request.data["operation_msg"])
            print("D")
            authentication.save()
            print("registered")
        except Exception as e:
            print("Error: ", e)

            return JsonResponse({"error": False,
                            "msg": "Wrong request"})

class CheckerView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass
