from datetime import datetime
from this import d
from time import time
from traceback import print_tb
from warnings import catch_warnings
from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from sqlalchemy import false
from .serializer import FileUploadSerializer, SaveFileSerializer
from .models import File
from rest_framework.decorators import api_view


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            temp=row['id']
            # print(temp)
            # print("##############################################################")
            new_file = File(
                       id=temp[3:],   
                    #    id = row[3:],
                       institution_name = temp[:3]
                       
                    #  institution_name= row["School Name"]
                       )
            new_file.save()
        return Response({"status": "success"},
                        status=200)

@api_view(['GET'])
def check_user(request,pk):
    if File.objects.filter(id=pk).exists():
        if request.method == 'GET':
    
            for e in File.objects.filter(id=pk):
                vis = e.visited
                t=e.timing


        # vis = File.objects.filter(id=pk).values('visited')
        # print(vis)
            print('##############################################################################')
            print(t)
            if vis==False:
                File.objects.filter(id=pk).update(visited=True)
                File.objects.filter(id=pk).update(date_now=datetime.now())
                File.objects.filter(id=pk).update(timing=datetime.now().time())
                return Response({"status": "success"},status=200)
            else:
                return Response({"status": "already visited at "+str(t)},status=200)
    else:
        return Response({"status": "id does not exist"},status=200)
        
        