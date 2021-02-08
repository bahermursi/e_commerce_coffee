# Create your views here.
from django.http import JsonResponse
from rest_framework import generics
from coffee.models.pod import Pod
from coffee.serializers.pod import PodSerializer
from coffee.serializers.pod import PodValidationSerializer

class PodView(generics.ListAPIView):
    http_method_names = ["get"]
    queryset = Pod.objects.all()
    serializer_class = PodValidationSerializer

    def get_queryset(self):
        product_type = self.request.query_params.get('product_type', None)
        coffee_flavor = self.request.query_params.get('coffee_flavor', None)
        pack_size = self.request.query_params.get('pack_size', None)

        kwargs = {}
        if product_type: kwargs.update({'{0}'.format('product_type'): product_type})
        if coffee_flavor: kwargs.update({'{0}'.format('coffee_flavor'): coffee_flavor})
        if pack_size: kwargs.update({'{0}'.format('pack_size'): pack_size})
        return self.queryset.filter(**kwargs)

    def get(self, request , *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.GET)
            if serializer.is_valid():
                queryset = self.get_queryset()
                pods = PodSerializer(queryset, many=True)
                return JsonResponse(pods.data, safe=False)
            else:
                return JsonResponse(serializer.errors, safe=False, status=400)
        except Exception as e:
            return JsonResponse({'message: Please make sure all the fields are valid.'}
                                                                    ,safe=False, status=400)
