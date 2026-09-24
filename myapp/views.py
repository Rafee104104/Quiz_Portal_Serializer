from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.db.models import Q
# Create your views here.

class StudentData(APIView):

    def get(self,request):
        students = Student.objects.all()
        
        search = request.query_params.get('search')
        if search:
            students = Student.objects.filter(
                Q(name__icontains = search)
            )
        serializer = StudentSerializer(students,many = True)
        return Response(
            data = serializer.data,
            status = status.HTTP_200_OK
        )
    
    def post(self,request):

        data = request.data
        
        serializer = StudentSerializer(data =data)
    
        if serializer.is_valid():
            serializer.save()

            return Response(
                data = serializer.data,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

class StudentDetail(APIView):

    def get(self,request,id):

        student = Student.objects.get(id=id)

        serializer = StudentSerializer(student)

        return Response(
            data = serializer.data,
            status = status.HTTP_200_OK
        )
    
    def put(self,request,id):

        data = request.data

        student = Student.objects.get(id=id)  

        serializer = StudentSerializer(student,data=data)
    
        if serializer.is_valid():
            serializer.save()

            return Response(
                data = serializer.data,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

    def delete(self,request,id):

        student = Student.objects.get(id=id)
        student.delete()

        return Response(
            data= {
                'msg' : 'Delete Operation Success'
            },
            status= status.HTTP_200_OK
        )

class QuizAPI(APIView):
    def get(self,request):
        quiz = Quiz.objects.all()
        serializer = QuizSerializer(quiz,many = True)
        return Response(
            data = serializer.data,
            status = status.HTTP_200_OK
        )
    
    def post(self,request):

        data = request.data
        
        serializer = QuizSerializer(data =data)
    
        if serializer.is_valid():
            serializer.save()

            return Response(
                data = serializer.data,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

class QuestionAPI(APIView):
    def get(self,request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question,many = True)
        return Response(
            data = serializer.data,
            status = status.HTTP_200_OK
        )
    
    def post(self,request):
    
        data = request.data
    
        serializer = QuestionSerializer(data =data)
    
        if serializer.is_valid():
            serializer.save()
    
            return Response(
                data = serializer.data,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

class OptionAPI(APIView):
    def get(self,request):
        option = Option.objects.all()
        serializer = OptionSerializer(option,many = True)
        return Response(
            data = serializer.data,
            status = status.HTTP_200_OK
        )
    
    def post(self,request):
    
        data = request.data
    
        serializer = OptionSerializer(data =data)
    
        if serializer.is_valid():
            serializer.save()
    
            return Response(
                data = serializer.data,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

class ParticipantAPI(APIView):
    def get(self,request):
        participant = Participant.objects.all()
        serializer = ParticipantSerializer(participant,many = True)
        return Response(
            data = serializer.data,
            status = status.HTTP_200_OK
        )
    
    def post(self,request):
    
        data = request.data
    
        serializer = ParticipantSerializer(data =data)
    
        if serializer.is_valid():
            serializer.save()
    
            return Response(
                data = serializer.data,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

class QuizResultAPI(APIView):
    def get(self,request):
        quizResult = QuizResult.objects.all()
        serializer = QuizResultSerializer(quizResult,many = True)
        return Response(
            data = serializer.data,
            status = status.HTTP_200_OK
        )
    
    def post(self,request):
    
        data = request.data
    
        serializer = QuizResultSerializer(data =data)
    
        if serializer.is_valid():
            serializer.save()
    
            return Response(
                data = serializer.data,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )