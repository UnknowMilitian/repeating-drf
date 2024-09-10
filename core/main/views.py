from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.forms import model_to_dict
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action


from .models import Category, Women
from .serializers import CategorySerializer, WomenSerializer


# Create your views here.

# ----------------------------------------------------------

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# ----------------------------------------------------------


# class WomenAPIView(APIView):
#     def get(self, request):
#         lst = Women.objects.all().values()
#         return Response({"post": lst})

#     def post(self, request):
#         post_new = Women.objects.create(
#             title=request.data["title"],
#             content=request.data["content"],
#             cat_id=request.data["cat_id"],
#         )
#         return Response({"post": model_to_dict(post_new)})


# ----------------------------------------------------------
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAdminUser]


# ----------------------------------------------------------


# class WomenViewSet(
#     mixins.CreateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.ListModelMixin,
#     GenericViewSet,
# ):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

#     @action(detail=False, methods=["get"], serializer_class=CategorySerializer)
#     def category(self, request, pk):
#         category = Category.objects.all()
#         serializer = self.get_serializer(category, many=True)
#         return Response(serializer.data)
