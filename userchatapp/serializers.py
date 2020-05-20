from rest_framework import serializers,viewsets
from userchatapp.models import User,Chat,Auth

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import serializers,viewsets
from userchatapp.models import User,Chat,Auth,Blog

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response



class GetAllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class GetAllChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields='__all__'

class GetAllBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields='__all__'
   




# class CustomPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'count': self.page.paginator.count,
#             'page_size': self.page_size,
#             'results': data
#         })

# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # fields = ('name','age','created_date')
#         fields='__all__'

#     # def to_representation(self,instance):
#     #     data = super().to_representation(instance)
#     #     data['check'] = 1
#     #     return data

# class AuthSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Auth
#         # fields = ('name','age','created_date')
#         fields = ('id', 'uid', 'token', 'created_at')  
      

#     # def to_representation(self,instance):
#     #     data = super().to_representation(instance)
#     #     data['check'] = 1
#     #     return data

# class ValidateSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True)
#     token = serializers.CharField(required=True)

# class ChatSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = Chat
#         # fields = ('name','age','created_date')
#         fields='__all__'
#         depth = 1

# class DataSerializerAll(serializers.ModelSerializer):
#     # image_name  = serializers.PrimaryKeyRelatedField(many=True,)
#     class Meta:
#         model = Auth
#         # fields = ('name','age','created_date')
#         fields='__all__'
#         read_only_fields=['uid']
#         # fields = ['imageUrlLink', 'UserId', 'image_name']
#         depth = 1

# class JoinSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('id','username','created_at', 'authtokens')
#         # read_only_fields=['uid']

#     authtokens = AuthSerializer(many=True)



# # class JoinsInSameField(serializers.ModelSerializer):
# #     # my_field = serializers.SerializerMethodField('is_named_bar')
# #     username = serializers.SerializerMethodField()

# #     # def is_named_bar(self, obj):
# #     #     # data = User.objects.filter(id = auth.uid)
# #     #     return obj.user.username

# #     class Meta:
# #         model = Auth
# #         fields = ('uid', 'token', 'created_at','username')
# #         # fields = '__all__'
# #         read_only_fields=['uid']
# #         # depth =1

# #     def get_username(self, obj):
# #         return obj.user.username



# class AllAuthSerializer(serializers.ModelSerializer):
# #    pagination_class = CustomPagination

#     class Meta:
#         model = Auth
#         fields = '__all__'
#         # pagination_class = CustomPagination

    
    


class GetAllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class GetAllChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields='__all__'
   




# class CustomPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'count': self.page.paginator.count,
#             'page_size': self.page_size,
#             'results': data
#         })

# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # fields = ('name','age','created_date')
#         fields='__all__'

#     # def to_representation(self,instance):
#     #     data = super().to_representation(instance)
#     #     data['check'] = 1
#     #     return data

# class AuthSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Auth
#         # fields = ('name','age','created_date')
#         fields = ('id', 'uid', 'token', 'created_at')  
      

#     # def to_representation(self,instance):
#     #     data = super().to_representation(instance)
#     #     data['check'] = 1
#     #     return data

# class ValidateSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True)
#     token = serializers.CharField(required=True)

# class ChatSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = Chat
#         # fields = ('name','age','created_date')
#         fields='__all__'
#         depth = 1

# class DataSerializerAll(serializers.ModelSerializer):
#     # image_name  = serializers.PrimaryKeyRelatedField(many=True,)
#     class Meta:
#         model = Auth
#         # fields = ('name','age','created_date')
#         fields='__all__'
#         read_only_fields=['uid']
#         # fields = ['imageUrlLink', 'UserId', 'image_name']
#         depth = 1

# class JoinSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('id','username','created_at', 'authtokens')
#         # read_only_fields=['uid']

#     authtokens = AuthSerializer(many=True)



# # class JoinsInSameField(serializers.ModelSerializer):
# #     # my_field = serializers.SerializerMethodField('is_named_bar')
# #     username = serializers.SerializerMethodField()

# #     # def is_named_bar(self, obj):
# #     #     # data = User.objects.filter(id = auth.uid)
# #     #     return obj.user.username

# #     class Meta:
# #         model = Auth
# #         fields = ('uid', 'token', 'created_at','username')
# #         # fields = '__all__'
# #         read_only_fields=['uid']
# #         # depth =1

# #     def get_username(self, obj):
# #         return obj.user.username



# class AllAuthSerializer(serializers.ModelSerializer):
# #    pagination_class = CustomPagination

#     class Meta:
#         model = Auth
#         fields = '__all__'
#         # pagination_class = CustomPagination

    
    