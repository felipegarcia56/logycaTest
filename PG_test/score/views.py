import django_filters
from django.db import IntegrityError
from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import filters
from professor.models import Professor
from student.models import Student
from .models import Score
from .serializers import ScoreSerializers


# Create your views here.
class ScoreViews(ListAPIView):
    serializer_class = ScoreSerializers
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ordering_fields = ["id","value","name","professor","student"]
    ordering = ["name"]

    def get_queryset(self):
        return Score.objects.all()

    def post(self,request):
        try:
            data = request.data
            print(data)
            if "name" in data.keys() and "value" in data.keys() and "professor" in data.keys() and "student" in data.keys():
                if data["name"] == "" or str(data["name"]).isnumeric() or data["value"] == "" or  data["professor"] == "" or not str(data["professor"]).isnumeric() or data["student"] == "" or not str(data["student"]).isnumeric():
                    raise ValueError

                professor = Professor.objects.filter(id = data["professor"])
                student = Student.objects.filter(id = data["student"])
                if len(professor)>0 and len(student) > 0:
                    score = Score(name=data["name"],value=data["value"],professor=professor[0], student=student[0])
                    score.save()
                    return Response({"response":"ok","message":"score created"},200)
                else:
                    resp = {"response":"ok","message":"professor id: {} or student id: {} doesn't exist".format(data["professor"],data["student"])}
                    return Response(resp,404)
            else:
                return Response({"response":"ok","message":"all data is required"},400)
        except ValueError:
            return Response({"resposne": "fail",
                             "message": "name can't be numeric or empty and value, professor, student must be numeric and not empty"},
                            500)
        except Exception as e:
            return Response({"resposne":"fail","message":"error {}".format(e)},500)

    def put(self,request):
        try:
            data = request.data
            if "id" in data.keys() and "name" in data.keys() and "value" in data.keys() and "professor" in data.keys() and "student" in data.keys():

                if data["name"] == "" or str(data["name"]).isnumeric() or data["value"] == "" or data["professor"] == "" or not str(data["professor"]).isnumeric() or data["student"] == "" or not str(data["student"]).isnumeric():
                    raise ValueError

                resultSet = Score.objects.filter(id=data["id"])
                resultProfessor = Professor.objects.filter(id = data["professor"])
                resultStudent = Student.objects.filter(id=data["student"])

                if len(resultSet)>0 and len(resultProfessor)>0 and len(resultStudent)>0:
                    professor = resultProfessor[0]
                    student = resultStudent[0]
                    score = Score(id=data["id"],name=data["name"],value=data["value"],professor=professor,student=student)
                    score.save()
                    return Response({"response":"ok","message":"score updated"},200)
                else:
                    return Response({"response":"ok","message":"no there data for score selected or professor or student doesn't exist"},404)
            else:
                return Response({"response":"ok","message":"all data is required"},400)
        except ValueError:
            return Response({"resposne":"fail","message":"name can't be numeric or empty and value, professor, student must be numeric and not empty"},500)
        except Exception as e:
            return Response({"resposne":"fail","message":"error {}".format(e)},500)

    def delete(self,request):
        try:
            id = request.query_params.get("id",None)
            if id is not None:
                resultSet = Score.objects.filter(id = id)
                if len(resultSet)>0:
                    score = resultSet[0]
                    score.delete()
                    return Response({"response":"ok","message":"erased"},200)
                else:
                    return Response({"response":"ok","message":"score not found"},404)
            else:
                return Response({"response":"ok","message":"all data is required"},400)
        except IntegrityError:
            return Response({"error": "error de integridad, verifique los recursos creaos"}, 500)
        except Exception as e:
            return Response({"resposne":"fail","message":"error {}".format(e)},500)
