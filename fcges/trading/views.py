from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions

# from common.mixins.login_required import LoginRequiredMixin

from trading.serializers import OrderBlockSerializer
from trading.models import OrderBlock


class OrderBlockView(APIView):
    ''' Check user if authenticated, exception will tell the user to login using utility app(Postman...)
        Use endpoint /api/token/ to get the access/refresh token
    '''    
    permission_classes = (IsAuthenticated,) 

    def get(self, request):
        content = {'message': 'Welcome to FCGES Trading Bot'}
        return Response(content)

class OrderBlockViewSet(viewsets.ModelViewSet):
    ''' API endpoint for creating, updating and retrieving Trading orders.

        endpoint: api/orders
            - this will list all trading orders.
        api/orders/<order_id>
            - retrive order information using the order id 
    '''
    serializer_class = OrderBlockSerializer
    permission_classes = (IsAuthenticated,) 

    def get_queryset(self, pk=None):
        queryset = OrderBlock.objects.all()
        return queryset.order_by('created_at')

    def perform_update(self, serializer):
        serializer.save()
    
    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({
                'status': 0, 'message': serializer.errors
                })

        self.perform_create(serializer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderBlockSerializer(order, data=request.data)
        if serializer.is_valid():
            return Response({
                'status': 0, 'message': serializer.errors
            })

        self.perform_update(serializer)
        return Response(serializer.data)
        

    def retrieve(self, request, pk=None):
        qs = get_object_or_404(self.get_queryset(), id=pk)
        serializer = self.serializer_class(qs)
        return Response(serializer.data)
