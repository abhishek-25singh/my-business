
from rest_framework import viewsets
from rest_framework.response import Response
from accounts.models import User, Customer
from .serializers import UserSerializer, CustomerSerializer
from django.core.mail import send_mail
import threading
from rest_framework import generics, status, permissions


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    # def send_email(self, message, subject, recipient_list):
    #     from_email = 'codes.environment@gmail.com'
    #     send_mail(subject, message,from_email,recipient_list, fail_silently=False)


    def get_queryset(self):
        customer = Customer.objects.all()
        return customer


    def create(self, request, *args, **kwargs):
        custom_data = request.data
        print(custom_data)

        user = custom_data['user']
        print(user)
        print(user.get('first_name'))
        if not Customer.objects.filter(profile_number=custom_data["profile_number"]).exists():
            if not User.objects.filter(email=user["email"]).exists():
                if not User.objects.filter(mobile_no=user["mobile_no"]).exists():


                    new_user = User.objects.create(first_name=user["first_name"], last_name=user["last_name"],
                     email=user["email"], mobile_no=user["mobile_no"])
                    new_user.set_password(user['password'])
                    new_user.save()

                    new_customer = Customer.objects.create(profile_number=custom_data["profile_number"], user=new_user)
                    new_customer.save()
                    # self.send_email("this a notification", "Notification",['codes.environment@gmail.com',])
                    # HandleNotifications("this a notification", "Notification",['codes.environment@gmail.com',]).start()
                    serializer = CustomerSerializer(new_customer)

                    return Response(serializer.data)
                else:
                    return Response({"Error": "This Mobile Number already exists"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"Error": "This Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "This Profile Number already exists"}, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.all()
        return user



