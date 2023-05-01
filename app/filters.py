import django_filters
from .models import Record

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = ['reg_no']