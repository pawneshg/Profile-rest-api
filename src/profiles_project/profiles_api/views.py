from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methos as function (get,put,posst, patch,delete)',
            'It is similar to a traditiona; Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in req."""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delete and object"""
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """test API viewsets."""

    serializer_class = serializers.HelloSerializer

    def list(Self, request):
        """Return a Hello message."""

        a_viewset = [
            'Usees actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'provides more functionality with less code.'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def  create(self, request):
        """Create a new Hello message."""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getiing an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http-method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http-method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http-method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handels creating, and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    
