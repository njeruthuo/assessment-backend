from django.db.models import Count
from .models import Status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello")


class VehicleStatusSummary(APIView):

    """ Handling the get request"""

    def get(self, request, format=None):
        """Aggregate the number of vehicles for each status"""
        summary = Status.objects.values('status').annotate(
            total=Count('status')).order_by('status')

        """Create a response dictionary"""
        response_data = {item['status']: item['total'] for item in summary}

        return Response(response_data)
