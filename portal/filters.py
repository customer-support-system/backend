
from django_filters import rest_framework as filters
from .models import Issues

class LevelFilterBackend(filters.DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        try:
            if request.user.is_authenticated:
                staff_level_id = request.user.staff.level
                queryset = queryset.filter(level=staff_level_id)
            else:
                # If user is not authenticated, return an empty queryset
                queryset = queryset.none()
        except Exception as e:
            raise e
        
        return queryset