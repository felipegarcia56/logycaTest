import django_filters
from django.db import IntegrityError
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import filters
from .models import *
from .serializers import ProfessorSerializers
# Create your views here.


class ProfessorView(ListAPIView):
    serializer_class = ProfessorSerializers
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ordering_fields = ['id', 'name']
    ordering = ['id']

    def get_queryset(self):
        return Professor.objects.all()

    def post(self,request):
        try:
            data = request.data
            if "name" in data.keys():

                if data['name'] == "" or str(data['name']).isnumeric():
                    raise ValueError

                professor = Professor(name=data["name"])
                professor.save()
                return Response({"response": "ok","message":"result set"}, 200)
            else:
                return Response({"response": "ok","message":"all parameter are required"}, 400)
        except ValueError:
            return Response({"response":"fail","message":"name can't be empty and must be a text"},400)
        except Exception as e:
            return Response({"resposne":"fail","message":"error {}".format(e)},500)

    def put(self,request):
        try:
            data = request.data
            if "id" in data.keys() and "name" in data.keys():

                if data['name'] == "" or str(data['name']).isnumeric():
                    raise ValueError

                resultSet = Professor.objects.filter(id=data["id"])
                if len(resultSet)>0:
                    professor = resultSet[0]
                    professor.name = data["name"]
                    professor.save()
                    resp = {"response":"ok",
                            "message":"professor updated id: {}, name: {}".format(data["id"],data["name"])}
                    return Response(resp,200)
                else:
                    return Response({"return":"ok","message":"not there data for id {}".format(data["id"])},404)
            else:
                return Response({"response":"ok","message":"all data is required"},400)
        except ValueError:
            return Response({"response":"fail","message":"name can't be empty and must be a text"},400)
        except Exception as e:
            return Response({"resposne":"fail","message":"error {}".format(e)},500)

    def delete(self,request):
        try:
            id = request.query_params.get("id",None)
            if id is not None:
                resultSet = Professor.objects.filter(id=id)
                if len(resultSet) > 0:
                    professor = resultSet[0]
                    professor.delete()
                    return Response({"response":"ok","message":"erased {}".format(id)},200)
                else:
                    return Response({"response":"ok","message":"id: {} doesn't exist".format(id)},404)
            else:
                return Response({"response":"ok","message":"all data is required"},400)

        except IntegrityError:
            return Response({"error": "integrity error"}, 500)
        except Exception as e:
            return Response({"resposne":"fail","message":"error {}".format(e)},500)



