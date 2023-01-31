from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
import base64
from django.core.files.base import ContentFile
from rest_framework import status


# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def list(request):
    try:
        publicaitons = Publications.objects.all()
        serializer = PublicationsSerializer(publicaitons, many=True)
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
def publication_detail(request, pk):
    try:
        if pk is not None:
            publicaitons = Publications.objects.get(id=pk)
            serializer = PublicationsSerializer(publicaitons)
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


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def gallery_by_proj(request, slug):
#     try:
#         gallery = Gallery.objects.filter(project__slug=slug)
#         serializer = GallerySerializer(gallery, many=True)
#         return Response({
#             'code': status.HTTP_200_OK,
#             'response': "Received Data Successfully",
#             "data": serializer.data
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'response': "Data not Found",
#             'error': str(e)
#         })


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def gallery_by_camp_slider(request, slug):
#     try:
#         gallery = Gallery.objects.filter(project__slug=slug)
#         serializer = GallerySerializer_slider(gallery, many=True)
#         return Response({
#             'code': status.HTTP_200_OK,
#             'response': "Received Data Successfully",
#             "data": serializer.data
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'response': "Data not Found",
#             'error': str(e)
#         })


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def projects_by_aow(request, pk):
#     id = pk
#     project = Projects.objects.filter(areaofwork__id = id)
#     serializer = ProjectsSerializer(project, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload(request):
    try:
        pdf_data = request.data
        if 'pdf' in pdf_data and pdf_data['pdf'] != None:
            fmt, pdf_str = str(pdf_data['pdf']).split(';base64,')
            ext = fmt.split('/')[-1]
            pdf_file = ContentFile(base64.b64decode(pdf_str), name='temp.' + ext)
            pdf_data['pdf'] = pdf_file

        # # slug = slugify(gallery_data['title'])
        # suffix = 1
        # if Gallery.objects.filter(title__exact=gallery_data['title']).exists():
        #     count = Gallery.objects.filter(title__exact=gallery_data['title']).count()
        #     print(count)
        #     suffix += count
        #     print("yes")
        #     slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

        # else:
        #     slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

        # gallery_data['slug'] = slug

        serializer = PublicationsSerializer(data=pdf_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Created Data Successfully",
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


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    try:
        pdf_data = request.data
        publication = Publications.objects.get(id=pk)

        if ('pdf' in pdf_data and pdf_data['pdf'] == None) and publication.pdf != None:
            pdf_data.pop('pdf')

        
        if 'pdf' in pdf_data and pdf_data['pdf'] != None:
            fmt, pdf_str = str(pdf_data['pdf']).split(';base64,')
            ext = fmt.split('/')[-1]
            pdf_file = ContentFile(base64.b64decode(pdf_str), name='temp.' + ext)
            pdf_data['pdf'] = pdf_file

        # slug = slugify(gallery_data['title'])
        # suffix = 1
        # if Gallery.objects.filter(title__exact=gallery_data['title']).exists():
        #     count = Gallery.objects.filter(title__exact=gallery_data['title']).count()
        #     print(count)
        #     suffix += count
        #     print("yes")
        #     slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

        # else:
        #     slug = "%s-%s" % (slugify(gallery_data['title']), suffix)
        # gallery_data['slug'] = slug

        serializer = PublicationsSerializer(publication, data=pdf_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Updated Data Successfully",
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


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    try:
        project = Publications.objects.get(id=pk)
        project.delete()
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
