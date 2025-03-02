from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import IdeaSerializer
from .models import Idea, Category

@api_view(['GET'])
def api_overview(request):
    return Response({"message": "Welcome to the API!"})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def idea_list_create(request):
    if request.method == 'GET':
        ideas = Idea.objects.all()
        serializer = IdeaSerializer(ideas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IdeaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def idea_detail(request, idea_id):
    try:
        idea = Idea.objects.get(id=idea_id)
    except Idea.DoesNotExist:
        return Response({"error": "Idea not found"}, status=status.HTTP_404_NOT_FOUND)

    # Ensure only the author can modify/delete the idea
    if request.user != idea.author:
        return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = IdeaSerializer(idea)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IdeaSerializer(idea, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        idea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
