# from rest_framework.request import Request
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.generics import get_object_or_404
# from rest_framework.permissions import IsAuthenticated,AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView
# from django.contrib.auth import authenticate, get_user_model
# from rest_framework.authtoken.models import Token
# from .models import Issues, Levels, Solution, Staff
# from .serializers import ComplaintSerializer, LevelSerializer, SolutionSerializer, StaffSerializer

# class ComplaintView(APIView):
#     permission_classes=[AllowAny]
#     def get(self, request):
#         complaints = Issues.objects.all()
#         serializer = ComplaintSerializer(instance=complaints, many=True)
#         response = {"message": "complaints", "data": serializer.data}
#         return Response(data=response, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = request.data
#         serializer = ComplaintSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ComplaintDetailView(APIView):
#     def get(self, request, complaint_id):
#         complaint = get_object_or_404(Issues, pk=complaint_id)
#         serializer = ComplaintSerializer(instance=complaint)
#         response = {"message": "complaint details", "data": serializer.data}

#         return Response(data=response, status=status.HTTP_200_OK)

#     def put(self, request, complaint_id):
#         complaint = get_object_or_404(Issues, pk=complaint_id)
#         serializer = ComplaintSerializer(instance=complaint, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             response = {"message": "issue updated successfully", "data": serializer.data}
#             return Response(data=response, status=status.HTTP_200_OK)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, complaint_id):
#         complaint = get_object_or_404(Issues, pk=complaint_id)
#         complaint.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class LevelView(APIView):
#     def get(self, request):
#         levels = Levels.objects.all()
#         serializer = LevelSerializer(instance=levels, many=True)
#         response = {"message": "levels", "data": serializer.data}
#         return Response(data=response, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = request.data
#         serializer = LevelSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             response = {"message": "level created successfully", "data": serializer.data}
#             return Response(data=response, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LevelDetailView(APIView):
#     def get(self, request, level_id):
#         level = get_object_or_404(Levels, pk=level_id)
#         serializer = LevelSerializer(instance=level)
#         response = {"message": "levels", "data": serializer.data}
#         return Response(data=response, status=status.HTTP_200_OK)

#     def put(self, request, level_id):
#         level = get_object_or_404(Levels, pk=level_id)
#         serializer = LevelSerializer(instance=level, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             response = {"message": "level updated successfully", "data": serializer.data}
#             return Response(data=response, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, level_id):
#         level = get_object_or_404(Levels, pk=level_id)
#         level.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


# class SolutionView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         data = request.data
#         issue_id = data.get('issue_id', None)

#         if issue_id is None:
#             return Response({"error": "Please provide 'issue_id' in the request data."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             issue = Issues.objects.get(pk=issue_id)
#         except Issues.DoesNotExist:
#             return Response({"error": f"Issue with ID {issue_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

#         data['issue'] = issue_id
#         serializer = SolutionSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             response = {"message": "Solution for the issue created successfully", "data": serializer.data}
#             return Response(data=response, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SolutionDetailView(APIView):
#     def get(self, request, solution_id):
#         solution = get_object_or_404(Solution, pk=solution_id)
#         serializer = SolutionSerializer(instance=solution)

#         response_data = {"message": "solution details", "data": serializer.data}
#         return Response(data=response_data, status=status.HTTP_200_OK)

#     def put(self, request, solution_id):
#         solution = get_object_or_404(Solution, pk=solution_id)
#         serializer = SolutionSerializer(instance=solution, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             response_data = {"message": "solution updated successfully", "data": serializer.data}
#             return Response(data=response_data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, solution_id):
#         solution = get_object_or_404(Solution, pk=solution_id)
#         solution.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class StaffView(APIView):
    

#     def get(self, request, staff_id=None):
#         if staff_id is not None:
#             staff = get_object_or_404(Staff, pk=staff_id)
#             serializer = StaffSerializer(instance=staff)
#             response = {"message": "staff details", "data": serializer.data}
#         else:
#             staffs = Staff.objects.all()
#             serializer = StaffSerializer(instance=staffs, many=True)
#             response = {"message": "list of staff members", "data": serializer.data}

#         return Response(data=response, status=status.HTTP_200_OK)

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         level_id = request.data.get('level')

#         user = get_user_model().objects.create_user(username=username, password=password)
#         staff = Staff.objects.create(user=user)

#         if level_id:
#             staff.level_id = level_id
#             staff.save()

#         serializer = StaffSerializer(staff)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def delete(self, request, staff_id):
#         staff = get_object_or_404(Staff, pk=staff_id)
#         staff.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self, request, staff_id):
#         staff = get_object_or_404(Staff, pk=staff_id)
#         serializer = StaffSerializer(instance=staff, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             response_data = {"message": "staff updated successfully", "data": serializer.data}
#             return Response(data=response_data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(TokenObtainPairView):


#     def post(self, request: Request, *args, **kwargs) -> Response:
#         response=super().post(request, *args, **kwargs)
#         if response.status_code==status.HTTP_200_OK:
#             response.data['message']='logged in successfully'

#             return response

# using viewsets

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.request import Request
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


from .models import Issues, Levels, Solution, Staff
from .serializers import (
    ComplaintSerializer, LevelSerializer, SolutionSerializer, StaffSerializer
)
from rest_framework.pagination import PageNumberPagination




class CustomPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 1000  




class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter complaints by status
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset



    @action(detail=False)
    def without_solutions(self, request):
        queryset = Issues.objects.filter(status__in=['pending', 'answered']).exclude(solution__isnull=False)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False)
    def pending(self, request):
        queryset = Issues.objects.filter(status='pending')
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Levels.objects.all()
    serializer_class = LevelSerializer


class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class=CustomPagination


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class=CustomPagination


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    


    


