from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import json
from uuid import uuid4
from decimal import Decimal
from userchatapp.models import Auth, Chat, User

from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from profanity_check import predict, predict_prob





class Login(APIView):
    def post(self, request):
        user_name = request.data.get("username")
        # u = User(username=request.data.get("username"))
        kk = User.objects.filter(username=user_name)
        authToken = 0
        uid = 0
        if kk.count() > 0:  # OLD user
            print("*****OLD USER******")
            rand_token = uuid4()

            auth = Auth()
            auth.uid = kk[0]
            auth.token = rand_token
            auth.save()

            authToken = rand_token
            uid = kk[0].id
            res = 1
        else:  # New user
            print("*****New USER******", kk)
            u = User(username=request.data.get("username"))
            u.save()

            kk = User.objects.filter(username=request.data.get("username"))
            # print("**",kk.values("username")[0].get("username"))

            rand_token = uuid4()

            auth = Auth()
            auth.uid = kk[0]
            auth.token = rand_token
            auth.save()

            authToken = rand_token
            uid = kk[0].id

            # print(kk.count())

        data = {
            "uid": uid,
            "token": authToken
        }
        # u.save()
        # serializer = UserSerializers(model,many=True)
        return Response(data, status=status.HTTP_201_CREATED)


class GetAllUsers(APIView):
    def post(self, request):
        model = User.objects.filter().exclude(id=request.data.get("uid"))
        serializer = GetAllUserSerializer(model, many=True)
        data = {
            "data" : serializer.data,
            "status":status.HTTP_200_OK
        }
        return Response(serializer.data, status=status.HTTP_200_OK)




class GetAllChat(APIView):
    def post(self, request):

        senderId = request.data.get("yourUserId")
        receiverId = request.data.get("otherUserId")
        model1 = Chat.objects.filter(senderId=senderId, receiverId=receiverId)|Chat.objects.filter(senderId=receiverId, receiverId=senderId)
        model = model1.order_by('created_at')
        serializer = GetAllChatSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddChat(APIView):
    def post(self, request):


        senderId = request.data.get("senderId")
        receiverId = request.data.get("receiverId")
        message = request.data.get("message")
        kp = predict_prob([message])
        print("LLLLL",kp[0])
        

        send_user = User.objects.get(id=senderId)
        recv_user = User.objects.get(id=receiverId)

        chat_obj = Chat()
        chat_obj.senderId = send_user
        chat_obj.receiverId = recv_user
        chat_obj.message = message
        chat_obj.save()
        sss = '0.500000000'
        if(Decimal(kp[0]).compare(Decimal(sss))<=0):
            stt = status.HTTP_200_OK
        else:
            stt = status.HTTP_308_PERMANENT_REDIRECT
        

        data = {
            "message" : "added chat",
            "status":stt
        }


        return Response(data, status=status.HTTP_200_OK)