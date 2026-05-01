from .models import (Signals)
from rest_framework.response import Response
from .serializers import (SignalSerializer)

def get_signals():
    signals = Signals.objects.all()
    serializers = SignalSerializer(signals, many=True)
    return Response(serializers.data)

def post_signal(request):
    serializers = SignalSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=201)
    return Response(serializers.errors, status=400)

def delete_signal(request, signal_id = None):
    if not signal_id:
        return Response({"error":"Id required"})
    signal = Signals.objects.get(id=signal_id)
    if signal.DoesNotExist:
        return Response({"message":"signal not found"}, status=404)
    signal.delete()
    return Response({"message":"signal deleted"}, status=200)