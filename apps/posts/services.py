from .models import (Signals)
from rest_framework.response import Response
from .serializers import (SignalSerializer)

def get_signals():
    signals = Signals.objects.all()
    serializers = SignalSerializer(signals, many=True)
    return Response(serializers.data)

def get_single_signal(signal_id):
    if not signal_id:
        return Response({"error": "Id required"})
    try:
        signal = Signals.objects.get(id=signal_id)
        serializers = SignalSerializer(signal)
        return Response(serializers.data)
    except signal.DoesNotExist:
        return Response({"message": "post not found"})

def post_signal(request):
    serializers = SignalSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=201)
    return Response(serializers.errors, status=400)

def update_post(request, signal_id):
    if not signal_id:
        return Response({"error": "Id required"})
    signal = Signals.objects.get(id=signal_id)
    serializers = SignalSerializer(signal, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response({"message": "post edited"})

def delete_signal(signal_id):
    if not signal_id:
        return Response({"error":"Id required"})
    signal = Signals.objects.get(id=signal_id)
    
    try:
        signal.delete()
    except signal.DoesNotExist:
        return Response({"message":"signal not found"})
    return Response({"message":"signal deleted"})