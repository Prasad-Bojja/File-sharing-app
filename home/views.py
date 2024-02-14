from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from .serializers import *
from django.http import FileResponse
from django.conf import settings
import os
import shutil
from django.shortcuts import render


class UploadFiles(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        serializer = FileListSerializer(data=request.data)
        if serializer.is_valid():
            uid = serializer.save()['folder']
            url = f'http://127.0.0.1:8000/download_file/{uid}/'

            context={'url':url}
            
            return render(request, 'home.html',context)
        return render(request, 'home.html', {'errors': serializer.errors})



def Download(request , uid):
    return render(request , 'download.html' , context = {'uid' : uid})


class DownloadFolder(APIView):
    def get(self, request, folder_uid):
        # Convert folder_uid from UUID to string
        folder_uid_str = str(folder_uid)
        
        # Construct folder path
        folder_path = os.path.join(settings.MEDIA_ROOT, folder_uid_str)
        
        # Construct zip file path
        zip_file_path = os.path.join(settings.MEDIA_ROOT, f'{folder_uid_str}.zip')
        
        # Create a zip file from the folder
        shutil.make_archive(zip_file_path[:-4], 'zip', folder_path)
        
        # Prepare the response with the zip file
        response = FileResponse(open(zip_file_path, 'rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{folder_uid_str}.zip"'
        
        return response