from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import CustomUser, Trip
from .serializers import UserSerializer, TripSerializer

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        user = CustomUser.objects.create_user(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            full_name=data.get('full_name')
        )
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UserSerializer(user).data})
        return Response({'error': 'Invalid credentials'}, status=400)

class TripView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trips = Trip.objects.filter(user=request.user)
        return Response(TripSerializer(trips, many=True).data)

    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
