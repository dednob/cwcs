from .models import Home
from .serializers import HomeSerializer, HomeExperienceSerializer, HomeToggleSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
import base64
from django.core.files.base import ContentFile
from areaofwork.models import Areaofwork
from projects.models import Projects
from rest_framework import status


@api_view(['GET'])
def home_details(request):
    try:
        home = Home.objects.get(active=True)
        serializer = HomeSerializer(home)
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Received Data Successfully",
            "data": serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })


@api_view(['GET'])
def home_list(request):
    try:
        home = Home.objects.all()
        serializer = HomeSerializer(home, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Received Data Successfully",
            "data": serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })


@api_view(['GET'])
def toggle_active_status(request, pk):
    try:
        home = Home.objects.get(id=pk)
        home.active = True
        home.save()
        home_list = Home.objects.exclude(id=pk)
        for home in home_list:
            home.active = False
            home.save()

        home1 = Home.objects.get(active=True)
        serializer = HomeSerializer(home1)

        return Response({
            'code': status.HTTP_200_OK,
            'response': "Received Data Successfully",
            "data": serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })


@api_view(['GET'])
def experience_details(request):
    try:
        home = Home.objects.get(active=True)
        serializer = HomeExperienceSerializer(home)
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Received Data Successfully",
            "data": serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_home(request):
    try:
        data = request.data
        if 'image' in data:
            fmt, img_str = str(data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['image'] = img_file

        slug = slugify(data['title'])
        suffix = 1

        if Home.objects.filter(title__exact=data['title']).exists():
            count = Home.objects.filter(title__exact=data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(data['title']), suffix)

        data['slug'] = slug
        serializer = HomeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received Data Successfully",
                "data": serializer.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })
    # return Response(serializer.errors)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, slugkey):
    try:
        data = request.data
        if 'image' in data:
            fmt, img_str = str(data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            data['image'] = img_file

        slug = slugify(data['title'])
        suffix = 1

        if Home.objects.filter(title__exact=data['title']).exists():
            print("yes")
            count = Home.objects.filter(title__exact=data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(data['title']), suffix)

        data['slug'] = slug

        home = Home.objects.get(slug=slugkey)
        serializer = HomeSerializer(home, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received Data Successfully",
                "data": serializer.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': serializer.errors
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })


# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def partial_update_home(request, pk=None):
#     id = pk
#     home = Home.objects.get(pk=id)
#     serializer = HomeSerializer(home, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'msg': 'Partial Data Updated'})
#     return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_home(request, slug):
    try:
        home = Home.objects.get(slug=slug)
        home.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Data Deleted"
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })
