"""
Coffee Machines ListAPIView for querying and listing . 
"""

from django.http import JsonResponse
from rest_framework import generics
from coffee.models.machine import Machine
from coffee.serializers.machine import MachineSerializer
from coffee.serializers.machine import MachineValidationSerializer

class MachineView(generics.ListAPIView):
    """
    A Machine View class for implementing a GET API for listing the available machines in the database

    ...
    Methods
    -------
    get_queryset()
        fetches the machines query parameters if available in the request to filter the Machine queryset
    get(request)
        returns a JSON response with filtered data as a list of objects or an error message
    """


    http_method_names = ["get"]
    queryset = Machine.objects.all()
    serializer_class = MachineValidationSerializer
    
    def get_queryset(self):
        """
        Returns
        ------
        django.db.models.query.QuerySet 
            Machine Model queryset
        """
        product_type = self.request.query_params.get('product_type', None)
        water_line_compatible = self.request.query_params.get('water_line_compatible', None)
        kwargs = {}
        if product_type: kwargs.update({'{0}'.format('product_type'): product_type})
        if water_line_compatible: kwargs.update({
                                    '{0}'.format('water_line_compatible'): water_line_compatible
                                    })
        return self.queryset.filter(**kwargs)
    
    def get(self, request):
        """
        Parameters
        ----------
        request: Requets
            a GET Http request

        Returns
        -------
            A JSON response with filtered data as a list of objects or an error message
        """
        try:
            serializer = self.serializer_class(data=request.GET)
            if serializer.is_valid():
                queryset = self.get_queryset()
                machines = MachineSerializer(queryset, many=True)
                machines = machines.data
                return JsonResponse(machines, safe=False)
            else:
                return JsonResponse(serializer.errors, safe=False, status=400)
        except Exception as e:
            return JsonResponse({'message: Please make sure all the fields are valid.'}
                                                                    ,safe=False, status=400)