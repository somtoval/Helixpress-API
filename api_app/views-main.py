from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from .route_list import routes

@api_view(['GET'])
def getRoutes(request):
    return Response(routes)

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

# Journal API views
@api_view(['GET', 'POST'])
def journal_list(request):
    return crud_operations(request, Journal, JournalSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def journal_detail(request, pk):
    return crud_operations(request, Journal, JournalSerializer, pk)

# Repeat the pattern for other models
@api_view(['GET', 'POST'])
def volume_list(request):
    return crud_operations(request, Volume, VolumeSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def volume_detail(request, pk):
    return crud_operations(request, Volume, VolumeSerializer, pk)

@api_view(['GET', 'POST'])
def issue_list(request):
    return crud_operations(request, Issue, IssueSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def issue_detail(request, pk):
    return crud_operations(request, Issue, IssueSerializer, pk)

@api_view(['GET', 'POST'])
def paper_list(request):
    return crud_operations(request, Paper, PaperSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def paper_detail(request, pk):
    return crud_operations(request, Paper, PaperSerializer, pk)

@api_view(['GET', 'POST'])
def news_list(request):
    return crud_operations(request, News, NewsSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def news_detail(request, pk):
    return crud_operations(request, News, NewsSerializer, pk)

@api_view(['GET', 'POST'])
def home_slider_list(request):
    return crud_operations(request, HomeSlider, HomeSliderSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def home_slider_detail(request, pk):
    return crud_operations(request, HomeSlider, HomeSliderSerializer, pk)

@api_view(['GET', 'POST'])
def submission_list(request):
    return crud_operations(request, Submission, SubmissionSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def submission_detail(request, pk):
    return crud_operations(request, Submission, SubmissionSerializer, pk)

@api_view(['GET', 'POST'])
def newsletter_list(request):
    return crud_operations(request, Newsletter, NewsletterSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def newsletter_detail(request, pk):
    return crud_operations(request, Newsletter, NewsletterSerializer, pk)

@api_view(['GET', 'POST'])
def about_list(request):
    return crud_operations(request, About, AboutSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def about_detail(request, pk):
    return crud_operations(request, About, AboutSerializer, pk)

@api_view(['GET', 'POST'])
def contact_list(request):
    return crud_operations(request, Contact, ContactSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    return crud_operations(request, Contact, ContactSerializer, pk)

@api_view(['GET', 'POST'])
def author_list(request):
    return crud_operations(request, Author, AuthorSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    return crud_operations(request, Author, AuthorSerializer, pk)

@api_view(['GET', 'POST'])
def reviewer_list(request):
    return crud_operations(request, Reviewer, ReviewerSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def reviewer_detail(request, pk):
    return crud_operations(request, Reviewer, ReviewerSerializer, pk)

@api_view(['GET', 'POST'])
def editor_list(request):
    return crud_operations(request, Editor, EditorSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def editor_detail(request, pk):
    return crud_operations(request, Editor, EditorSerializer, pk)

@api_view(['GET', 'POST'])
def open_access_list(request):
    return crud_operations(request, OpenAccess, OpenAccessSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def open_access_detail(request, pk):
    return crud_operations(request, OpenAccess, OpenAccessSerializer, pk)

@api_view(['GET', 'POST'])
def editorial_process_list(request):
    return crud_operations(request, EditorialProcess, EditorialProcessSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def editorial_process_detail(request, pk):
    return crud_operations(request, EditorialProcess, EditorialProcessSerializer, pk)

@api_view(['GET', 'POST'])
def ethics_list(request):
    return crud_operations(request, Ethics, EthicsSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def ethics_detail(request, pk):
    return crud_operations(request, Ethics, EthicsSerializer, pk)

@api_view(['GET', 'POST'])
def charges_list(request):
    return crud_operations(request, Charges, ChargesSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def charges_detail(request, pk):
    return crud_operations(request, Charges, ChargesSerializer, pk)

@api_view(['GET', 'POST'])
def visibility_statement_list(request):
    return crud_operations(request, VisibilityStatement, VisibilityStatementSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def visibility_statement_detail(request, pk):
    return crud_operations(request, VisibilityStatement, VisibilityStatementSerializer, pk)
