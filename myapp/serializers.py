from rest_framework import serializers
from .models import *
import datetime

class StudentSerializer(serializers.ModelSerializer):

    request_time = serializers.SerializerMethodField()

    class Meta:
        model = Student
        # fields = ('__all__')
        fields = ['name','dept','roll', 'request_time']

        extrat_kwargs = {
            'name' : {'required': False},
            'dept' : {'required': False},
            'roll' : {'required': False}
        }

    def get_request_time(self,obj):
        time = datetime.datetime.now()
        return time

class CustomUserSerializer(serializers.ModelSerializer):
    request_time = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        # fields = ('__all__')
        fields = ['username','email','password','request_time']

        extrat_kwargs = {
            'username' : {'required': True},
            'email' : {'required': True},
            'password' : {'required': True}
        }

    def get_request_time(self,obj):
        time = datetime.datetime.now()
        return time

class QuizSerializer(serializers.ModelSerializer):
    request_time = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        # fields = ('__all__')
        fields = ['title','description','request_time']

        extra_kwargs = {
            'title' : {'required': False},
            'description' : {'required': False}
        }

    def get_request_time(self,obj):
        time = datetime.datetime.now()
        return time

class QuestionSerializer(serializers.ModelSerializer):
    request_time = serializers.SerializerMethodField()

    class Meta:
        model = Question
        # fields = ('__all__')
        fields = ['quiz','question','request_time']

        extrat_kwargs = {
            'quiz' : {'required': False},
            'question' : {'required': False}
        }

    def get_request_time(self,obj):
        time = datetime.datetime.now()
        return time

class OptionSerializer(serializers.ModelSerializer):
    request_time = serializers.SerializerMethodField()

    class Meta:
        model = Option
        # fields = ('__all__')
        fields = ['question','option','is_correct','request_time']

        extrat_kwargs = {
            'question' : {'required': False},
            'option' : {'required': False},
            'is_correct' : {'required': False}
        }

    def get_request_time(self,obj):
        time = datetime.datetime.now()
        return time

class ParticipantSerializer(serializers.ModelSerializer):
    request_time = serializers.SerializerMethodField()

    class Meta:
        model = Participant
        # fields = ('__all__')
        fields = ['Name','Class','Age','Institution','request_time']

        extrat_kwargs = {
            'Name' : {'required': False},
            'Class' : {'required': False},
            'Age' : {'required': False},
            'Institution' : {'required': False}
        }

    def get_request_time(self,obj):
        time = datetime.datetime.now()
        return time

class QuizResultSerializer(serializers.ModelSerializer):
    request_time = serializers.SerializerMethodField()

    class Meta:
        model = QuizResult
        # fields = ('__all__')
        fields = ['participant','quiz','score','submitted_at','request_time']

        extrat_kwargs = {
            'participant' : {'required': False},
            'quiz' : {'required': False},
            'score' : {'required': False},
            'submitted_at' : {'required': False}
        }

    def get_request_time(self,obj):
        time = datetime.datetime.now()
        return time