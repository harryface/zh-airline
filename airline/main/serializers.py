import math
from rest_framework import serializers
from collections import OrderedDict


class AeroplaneSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    passenger = serializers.IntegerField(default=1)

    def tank_capacity(self, id: int) -> float:
        return id * 200

    def fuel_consumed_per_minute(self, id: int, passenger: int) -> float:
        return (math.log(id) * 0.8) + (passenger * 0.002)

    def max_min_to_fly(self, tank_capacity: float, fuel_consumed_per_minute: float) -> float:
        return tank_capacity / fuel_consumed_per_minute

    def to_representation(self, instance: OrderedDict) -> OrderedDict:
        serialized = super().to_representation(instance)

        tank = self.tank_capacity(serialized["id"])
        total_fuel_consumption_per_minute = self.fuel_consumed_per_minute(
            serialized["id"], serialized["passenger"])
        max_minute_able_to_fly = self.max_min_to_fly(
                                    tank, total_fuel_consumption_per_minute)

        serialized['total_fuel_consumption_per_minute'] = total_fuel_consumption_per_minute
        serialized['max_minute_able_to_fly'] = max_minute_able_to_fly
        return serialized
