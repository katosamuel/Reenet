# from .models import (Signals)
# from rest_framework.response import Response
# from apps.serializers import (SignalSerializer)

# def get_signals():
#     signals = Signals.objects.all()
#     serializers = SignalSerializer(signals, many=True)
#     return Response(serializers.data)

# def get_single_signal(signal_id):
#     if not signal_id:
#         return Response({"error": "Id required"})
#     try:
#         signal = Signals.objects.get(id=signal_id)
#         serializers = SignalSerializer(signal)
#         return Response(serializers.data)
#     except Signals.DoesNotExist:
#         return Response({"message": "post not found"})

