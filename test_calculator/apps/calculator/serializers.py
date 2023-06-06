from rest_framework import serializers


class CalculatorSerializer(serializers.Serializer):
    first = serializers.IntegerField(required=True)
    second = serializers.IntegerField(required=True)
    operation = serializers.CharField(required=True, max_length=1)

    def validate_operation(self, value):
        if value not in '+-/*':
            raise serializers.ValidationError("Operation field should contain only math operation symbol +-/*")
        return value

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['operation'] == '/' and data['second'] == 0:
            raise serializers.ValidationError("Сan`t be divided by zero!")
        return data
