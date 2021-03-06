
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework_gis.filters import DistanceToPointFilter

from multco_permits_api.models import CurrentPermits, ArchivedPermits
from multco_permits_api.serializers import CurrentPermitsSerializer, ArchivedPermitsSerializer

import coreapi



class CurrentPermitsGeoFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into schema.
    """

    class Meta:
        model = CurrentPermits
        fields = []

    def get_schema_fields(self, view):
        fields = []
        dist = coreapi.Field(
            name="dist",
            location="query",
            description="Distance in Meters (Use with point)",
            type="number"
            )
        point = coreapi.Field(
            name="point",
            location="query",
            description="Example: -122.276,45.5162",
            type="string"
            )
        fields.append(dist)
        fields.append(point)

        return fields



class CurrentPermitsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Current Multnomah County Work Permits
    """

    queryset = CurrentPermits.objects.all()
    serializer_class = CurrentPermitsSerializer
    filter_backends = (SearchFilter, OrderingFilter, DistanceToPointFilter, CurrentPermitsGeoFilter)
    search_fields = ('city', 'city_state', 'comments', 'cross_street', 'direction', 'district', 'effect_date', 'entry_date', 'expiration_date', 'final_date', 'issue_date', 'location', 'permit_category', 'permit_id', 'state', 'street', 'street_number', 'street_type', 'type', 'zip_code')
    ordering_fields = ('city', 'city_state', 'comments', 'cross_street', 'direction', 'district', 'effect_date', 'entry_date', 'expiration_date', 'final_date', 'issue_date', 'location', 'permit_category', 'permit_id', 'state', 'street', 'street_number', 'street_type', 'type', 'zip_code')
    distance_filter_field = 'geom_point'
    bbox_filter_include_overlapping = True # Optional
    distance_filter_convert_meters = True

class ArchivedPermitsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Historical Multnomah County Work Permits
    """

    queryset = ArchivedPermits.objects.all()
    serializer_class = ArchivedPermitsSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('applic_title', 'bond_expiration_date', 'bond_number', 'comments', 'commodity', 'daily_posting_date', 'duplicate', 'effect_date', 'entry_date', 'expiration_date', 'final_date', 'id', 'issue_date', 'jurisdiction', 'location', 'permit_count', 'permit_effect_date', 'permit_number', 'pkey')
    ordering_fields = ('applic_title', 'bond_expiration_date', 'bond_number', 'comments', 'commodity', 'daily_posting_date', 'duplicate', 'effect_date', 'entry_date', 'expiration_date', 'final_date', 'id', 'issue_date', 'jurisdiction', 'location', 'permit_count', 'permit_effect_date', 'permit_number', 'pkey')
