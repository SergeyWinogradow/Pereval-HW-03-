
from rest_framework import generics, permissions
from .models import Pereval_added
from .serializers import PerevalListSer, PerevalDetailSer, PerevalCreateSer

class submitDataList(generics.ListAPIView):
    """Все Данные о перевалах"""
    permission_classes = [permissions.AllowAny]
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalListSer

class submitDataDetail(generics.RetrieveAPIView):
    """Детально о перевале"""
    permission_classes = [permissions.AllowAny]
    queryset = Pereval_added.objects.all()
    lookup_field = 'slug'
    serializer_class = PerevalDetailSer

class submitDataCreate(generics.CreateAPIView):
    """Добавление нового перевала"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalCreateSer

class UserPerevalList(generics.ListAPIView):
    """Все перевалы пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PerevalListSer

    def get_queryset(self):
        return Pereval_added.objects.filter(user=self.request.user)


class UserPerevalUpdate(generics.UpdateAPIView):
    """Редактирование перевалов пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PerevalCreateSer

    def get_queryset(self):
        return Pereval_added.objects.filter(user=self.request.user)


class UserPerevalDelete(generics.DestroyAPIView):
    """Удаление перевала пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pereval_added.objects.filter(id=self.kwargs.get("pk"), user=self.request.user)

