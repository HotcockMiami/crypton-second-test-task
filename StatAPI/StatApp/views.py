from StatAPI.StatApp.timeconverter import ts_to_date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StatModel
from .serializers import StatSerializer
from datetime import datetime

# Create your views here.

class StatList(APIView):
    "Класс для поведения API модели StatModel"

    def get(self, request):
        #Смотрим есть ли что-то в запросе, если нет - возвращаем всё
        if request.data == {}:
            queryset = StatModel.objects.all()
        else:
            startdate = ts_to_date(request.data)
            if startdate['error_code'] == 1:
                return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            queryset = StatModel.objects.filter(timestamp__gte=startdate['timestamp'],
                                                timestamp__lte=datetime.now())
        serializer = StatSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        converted_data = ts_to_date(request.data)
        if converted_data['error_code'] == 1:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StatSerializer(data=converted_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
