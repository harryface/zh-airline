from rest_framework import views, response

from .serializers import AeroplaneSerializer

# Create your views here.


class AeroplaneApiView(views.APIView):

    def post(self, request):
        if isinstance(request.data, list):
            serializer = AeroplaneSerializer(data=request.data, many=True)
        else:
            serializer = AeroplaneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data)
