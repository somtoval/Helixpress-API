from rest_framework import status
from rest_framework.response import Response

# Helper function for CRUD operations
def crud_operations(request, model, serializer_class, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                instance = model.objects.get(pk=pk)
            except model.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = serializer_class(instance)
            return Response(serializer.data)
        else:
            print('This place ran')
            instances = model.objects.all()
            serializer = serializer_class(instances, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        try:
            instance = model.objects.get(pk=pk)
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            instance = model.objects.get(pk=pk)
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
