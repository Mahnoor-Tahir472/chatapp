from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from rest_framework.permissions import IsAuthenticated
from .models import Room,Message,Profile
from .serializers import RoomSerializers,MessageSerializer


class SignupAPI(APIView):
    def post(self, request):
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')

        if not username or not password :
            return Response({"error": "username and password are required"}, status=400)
        
        if User.objects.filter(username=username).exists():
            return Response({"Message": "user name already exist"},status=400)
        
        if User.objects.filter(email=email).exists():
            return Response({"Message": "email already exist"},status=400)
        
        # If everything is valid, create the user  
        user=User.objects.create_user(username=username , password=password , email=email)
        return Response({"Message":"user created succesfully"},status=201)

class LogInAPI(APIView):
    def post(self,request):
        username_or_email=request.data.get('username')
        password=request.data.get('password')
         
        if not username_or_email or not password :
            return Response({"error": "username and password are required"}, status=400)
        
        if '@' in username_or_email:
            user_obj=User.objects.get(email=username_or_email)
            username=user_obj.username
        else:
            username=username_or_email
        
        user=authenticate(username=username , password=password)
        if user is not None :
            login(request , user)
            return Response({"Message : Succesfully User Login"} , status=200)
        return Response({"Error":"Invalid Credentials"} , status=401)
        
class LogoutAPI(APIView):
    permission_classes=[IsAuthenticated]  # check the user who logedin or hit the api.this api can hit only when the user gat login.means only login user can hit the api's
    def post(self,request): # class based api's
        logout(request)
        return Response("Successfully logout",status=200)
    

class CheckLogin(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            return Response({"Logged_in":True})
        return Response({"Logged_in":False})
    
class GetAllUsers(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user= User.objects.exclude(id=request.user.id).exclude(is_superuser=True)
        # we get data in the form of list
        data=[{"id":u.id , "username": u.username}for u in user]
        return Response(data)
        
# we can't sort username or email but we sort id
# when we sort so the result comes in the form of list


class CreatePrivateRoom(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request): # self is a reference of objects   # request is used to pick http requests
        other_user_id=request.data.get('user_id')
        if not other_user_id:
            return Response({"Error":"The user id not found"},status=400)
        
        users_id=sorted([request.user.id, other_user_id])
        room_name=f"{users_id[0]}_{users_id[1]}"

# create is used to create new room if it was not created
        room, created =Room.objects.get_or_create(
            name=room_name,
            defaults={'created_by': request.user}
        )
        return Response({"room":{"id": room.id , "room_name": room_name}}, status=201)
    
class PostMessage(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        room_id=request.data.get('room_id')
        text=request.data.get('text')    

        if not room_id or not text:
            return Response({"Error":"Room_id and text not available"},status=400) 
        room=Room.objects.get(id=room_id)
        data=Message.objects.create(room=room,sender=request.user,text=text)
        serializer=MessageSerializer(data)
        return Response(serializer.data) 
    

class GetMessage(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,roomid):
        if not roomid:
            return Response({"ERROR": "Id not given"}, status=400)
        message=Message.objects.filter(room=roomid).order_by('timestamp')
        serializers=MessageSerializer(message,many=True) # many=true to get all msgs of the room
        return Response(serializers.data)


                                #for practice

class NewSignupAPI(APIView):
    def post(self,request):
        username=request.data.get('username')
        phone_number=request.data.get('phone_number')
        password=request.data.get('password')

        if not username or not password:
            return Response({"Error": "No username and password"},status=400)
        if User.objects.filter(username=username).exists():
            return Response({"Error": "username already exist"},status=400)
        if Profile.objects.filter(phone_number=phone_number).exists():
            return Response({"Error": "Phone number already exist"},status=400)
        # user=User.objects.create_user(username=username,phone_number=phone_number,password=password)
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, phone_number=phone_number)
        return Response({"Message": "Signup successfully"},status=200)
    

class NewLoginAPI(APIView):
    def post(self,request):
        phone_number=request.data.get('phone_number')
        password=request.data.get('password')

        if not phone_number or not password:
            return Response({"Error":"no data found"},status=400)
        
        if phone_number:
            user_obj=Profile.objects.get(phone_number=phone_number)
            users=user_obj.user
            
            user = authenticate(request, username=users .username, password=password)
            # user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return Response({"Message": "Successfully login"},status=200)
            return Response({"Error": "wrong data"},status=400)
        else:
         return Response({"Message": " Please enter phone_number"})\
         
class GetAllUser(APIView):
    permissions_classes=[IsAuthenticated]
    def get(self, request):
        users=Profile.objects.exclude(id=request.user.id)
        data=[{"id":u.id , "phone_number": u.phone_number}for u in users]
        return Response (data)
    

class NewPrivateRoom(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        other_person_id=request.data.get('user_id')
        if not other_person_id:
            return Response({"Error":"id not found"}, status=400)
        
        users_ids=sorted([request.user.id , other_person_id])
        room_name=f"{users_ids[0]}_{users_ids[1]}"

        room , created = Room.objects.get_or_create(
        name=room_name,
        defaults={'created_by': request.user}
        )
        return Response({"room":{"id": room.id , "room_name": room_name}}, status=201)
       
