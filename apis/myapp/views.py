from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView

# Create your views here.
def Hello(request):
    return HttpResponse("Hello")

# @api_view(["GET","POST"])
# def listAll(request):

#     print("In function ListAll")

#     e = Employee.objects.all()
#     if request.method == "GET":
#         ser = EmployeeSerializer(e, many = True)
#         return JsonResponse({"Employees" : ser.data})
    
#     elif request.method == "POST":
#         ser = EmployeeSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             print("hello")
#             return JsonResponse({"Employee" : ser.data})
#         return ser.error_messages

# @api_view(["GET","PUT","DELETE"])
# def useAPI(request,id):
    
#     print("In function useAPI")
#     e = Employee.objects.filter(pk = id) 
#     print(request.method)
#     print(id)

#     if request.method == "GET":
#         ser = EmployeeSerializer(e,many=True)
#         return JsonResponse({"Employee" : ser.data})
    
#     elif request.method == "PUT":
#         ser = EmployeeSerializer(e,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return ser.error_messages
    
#     elif request.method == "DELETE":
#         e.delete()
#         return HttpResponse(status=204)

class listAll(APIView):

    def get(self,request,format = None):
        e = Employee.objects.all()
        ser = EmployeeSerializer(e, many = True)
        return JsonResponse({"Employees" : ser.data})
    
    def post(self,request,format=None):
        ser = EmployeeSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            print("hello")
            return JsonResponse({"Employee" : ser.data})
        return ser.error_messages
    
class useAPI(APIView):

    def get_object(self,id):
        try:
            e = Employee.objects.filter(pk = id)
            return e
        except e.DoesNotExist:
            raise Http404
        
    def get(self,request,id,format = None):
        e = self.get_object(id)
        ser = EmployeeSerializer(e,many=True)
        return JsonResponse({"Data":ser.data})
    
    def put(self,request,id,format = None):
        e = self.get_object(id)
        ser = EmployeeSerializer(e,data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"Data":ser.data})
        return JsonResponse(ser.errors)
    
    def delete(self,request,id,format=None):
        e = self.get_object(id)
        e.delete()
        return HttpResponse(status=204)

