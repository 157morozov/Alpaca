from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Test
from .serializers import TestSerializer


class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        primary_key = kwargs.get('pk', None)
        if not primary_key:
            queryset = Test.objects.all()
            values = queryset.values()
            return Response({
                'content': list(values),
            })

        instance = Test.objects.get(pk=primary_key)
        serializer = TestSerializer(instance)

        return Response({
            'content': serializer.data,
        })

    def post(self, request, *args, **kwargs):
        # COM: For self-control data process
        # request_data = request.data.dict()
        # title = request_data['title']
        # description = request_data['description'] if 'description' in request_data else ''

        serializer = TestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'content': serializer.data,
        })

    def delete(self, request, *args, **kwargs):
        primary_key = kwargs.get('pk', None)
        if not primary_key:
            return Response({
                'error': 'Method DELETE not allowed'
            })

        try:
            instance = Test.objects.get(pk=primary_key)
        except:
            return Response({
                'error': 'Object does not exists'
            })

        instance.delete()

        return Response({
            'content': 'Object deleted'
        })

    def put(self, request, *args, **kwargs):
        primary_key = kwargs.get('pk', None)
        if not primary_key:
            return Response({
                'error': 'Method PUT not allowed'
            })

        try:
            instance = Test.objects.get(pk=primary_key)
        except:
            return Response({
                'error': 'Object does not exists'
            })

        serializer = TestSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'content': serializer.data
        })

    def patch(self, request, *args, **kwargs):
        return Response({
            'content': 'Patch'
        })


class Reports(APIView):
    pass
