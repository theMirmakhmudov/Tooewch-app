from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from drf_spectacular.utils import OpenApiResponse, extend_schema


class PatientCreateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    @extend_schema(
        summary="Create a patient APIView",
        description="Create a patient with required fields",
        request=PatientSerializer,
        responses={
            200: OpenApiResponse(
                response=PatientSerializer,
                description="Patient has been created successfully"
            ),
            400: OpenApiResponse(
                description="Something went wrong during creation process"
            )
        },
        tags=["User Authentication API"]
    )
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientListReadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    @extend_schema(
        summary="Get a list of patients APIView",
        description="Read a list of patients",
        request=PatientSerializer,
        responses={
            200: OpenApiResponse(
                response=PatientSerializer,
                description="Patient has been read successfully"
            ),
            400: OpenApiResponse(
                description="Something went wrong during reading process"
            )
        },
        tags=["User Authentication API"]
    )
    def get(self, request):
        patients = Patient.objects.all().order_by('-created_at')
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)


class PatientReadDetailAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    @extend_schema(
        summary="Get a patient detail APIView",
        description="Read a patient detail",
        request=PatientSerializer,
        responses={
            200: OpenApiResponse(
                response=PatientSerializer,
                description="Patient has been read successfully"
            ),
            400: OpenApiResponse(
                description="Something went wrong during reading process"
            )
        },
        tags=["User Authentication API"]
    )
    def get(self, request, user_id):
        try:
            patients = Patient.objects.get(user_id=user_id)
            serializer = PatientSerializer(patients)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
