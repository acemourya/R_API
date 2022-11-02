from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import RegisterSerializer

# Register API


class RegistrationApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User Created Successfully.  Now perform Login to get your token",
            })
        return Response({"Error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
