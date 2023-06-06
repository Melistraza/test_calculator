from rest_framework.views import APIView
from rest_framework.response import Response

from test_calculator.apps.calculator.serializers import CalculatorSerializer
from test_calculator.apps.calculator.utils import BoringCalculator


class CalculatorView(APIView):
    """
    CalculatorView[POST] accept JSON
    Current Api point support 4 type of operation - + * /
    For two arguments a & b

    :argument int first: first argument
    :argument int secont: secont argument
    :argument str operator: calculation operator
    :return: result of calculation
    """

    def post(self, request):
        serializer = CalculatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        result = BoringCalculator().calculate(data['first'], data['second'], data['operation'])
        return Response({'result': result})
