from rest_framework import viewsets, mixins
from .models import User, Ride
from .permissions import IsUserOrCreatingAccountOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, RideSerializer
import django_filters.rest_framework
from rest_framework.filters import OrderingFilter

class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrCreatingAccountOrReadOnly,)

    def get_serializer_class(self):
        is_creating_a_new_user = self.action == 'create'
        if is_creating_a_new_user:
            return CreateUserSerializer
        return self.serializer_class


class RideViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ride.objects.select_related("rider", "driver").prefetch_related("rideevent_set")
    serializer_class = RideSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'rider__email']
    ordering_fields = ['pickup_time']
