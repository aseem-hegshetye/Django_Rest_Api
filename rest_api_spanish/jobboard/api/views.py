from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from rest_framework.generics import get_object_or_404


class JobBoardList(APIView):
    def get(self, request):
        jobs = JobBoard.objects.all()
        serializer = JobBoardSerializer(jobs, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobBoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobBoardDetails(APIView):
    def get_object(self, pk):
        job = get_object_or_404(JobBoard, pk=pk)
        return job

    def get(self, request, pk):
        job = self.get_object(pk=pk)
        serializer = JobBoardSerializer(job)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, pk):
        job = self.get_object(pk=pk)
        serializer = JobBoardSerializer(job,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk):
        job = self.get_object(pk=pk)
        serializer = JobBoardSerializer(job,data=request.data,
                                        partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        job = self.get_object(pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
