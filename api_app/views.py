from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from .models import Journal, Volume, Issue, Paper
from .models import *
from .serializers import JournalSerializer, VolumeSerializer, IssueSerializer, PaperSerializer
from .serializers import *
from .route_list import routes
from .crud_helper import crud_operations

from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

# AUTH
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password # Used to hash password


############################################### AUTHENTICATION ###########################################
@api_view(['POST'])
@csrf_exempt
def login_view(request):
    print("CSRF Exempt Applied")
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'Successfully logged in','token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def logout_view(request):
    # logout(request)
    # request.user.auth_token.delete()
    # return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
     # Get the token from the request headers

    # try:
    #     token = request.auth
    #     if token:
    #         token.delete()  # Delete the token
    #     return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    # except AttributeError:
    #     return Response({'error': 'No token found for the user'}, status=status.HTTP_400_BAD_REQUEST)

    token_key = request.headers.get('Authorization')  # Assume token is passed in the header
    if token_key:
        try:
            token = Token.objects.get(key=token_key.split(' ')[1])  # Extract the token part
            token.delete()  # Delete the token
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user_view(request):
    if request.user.groups.filter(name="super admin").exists():
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        # first_name = request.data.get('first_name')
        # last_name = request.data.get('last_name')
        role = request.data.get('role')
        
        if username is None or email is None or password is None:
            return Response({'error': 'Please provide all the fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=make_password(password))  # Hash the password before saving it, first_name=first_name, last_name=last_name)
        
        # Add the user to a group based on the 'role'
        if role:
            try:
                group = Group.objects.get(name=role)
                user.groups.add(group)
            except Group.DoesNotExist:
                return Response({'error': 'Group does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
            
        user.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'Message': "You are not authorized"}, 403)


############################################### CORE CRUD ###########################################
@api_view(['GET'])
def get_routes(request):
    """
    Retrieve available API routes.
    """
    return Response(routes, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def journals(request):
    """
    Handle requests to retrieve all journals or create a new journal.
    """
    if request.method == 'GET':
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)
        # print('Serializer: ', serializer, 'Serialized data:', serializer.data)
        # print('Journal Query Set: ', journals, '\n Serializable: ', journals.values())
        # return Response({'All Journals': journals.values()})
        return Response({'All Journals': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = JournalSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'Message': 'New Journal Successfully Created'}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def journal(request, pk):
    """
    Handle requests to retrieve, update, or delete a specific journal by ID.
    """
    try:
        journal = Journal.objects.get(pk=pk)
    except Journal.DoesNotExist:
        raise NotFound(detail="Journal not found")

    if request.method == 'GET':
        serializer = JournalSerializer(journal)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        # If you don't pass in the argument of the specific journal instance you are passsing it will function as a post request and create new one
        serializer = JournalSerializer(journal, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        journal.delete()
        return Response({'Message': 'Journal was deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def journal_volumes(request, pk):
    """
    Handle requests to create and retrieve all volumes of a particular journal.
    """
    if request.method == 'GET':
        journal = Journal.objects.get(id=pk)
        volumes = journal.volume_set.all()
        serializer = VolumeSerializer(volumes, many=True)
        return Response({f'All Volumes of {journal}': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        data = request.data
        # We do this so that our client will just have to send the "number" attribute of the volume to be created in his request and then the journal attribute will be automatically gotten from the pk
        data['journal'] = pk
        serializer = VolumeSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def journal_papers(request, pk):
    """
    Handle requests tor retrieve all papers of a particular journal.
    """
    if request.method == 'GET':
        journal = Journal.objects.get(id=pk)
        papers = journal.paper_set.all()
        serializer = VolumeSerializer(papers, many=True)
        return Response({f'All Papers of {journal}': serializer.data}, status=status.HTTP_200_OK)
    

# VOLUMES
@api_view(['GET', 'PUT', 'DELETE'])
def volume(request, pk):
    volume = Volume.objects.get(id=pk)
    if request.method == 'GET':
        serializer = VolumeSerializer(volume, many=False)
        return Response({f'Volume': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = VolumeSerializer(volume, data=data, many=False)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        volume.delete()
        return Response({'Message': 'Volume was deleted'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def volume_issues(request, pk):
    volume = Volume.objects.get(id=pk)
    issue = volume.issue_set.all()

    if request.method == 'GET':
        serializer = IssueSerializer(issue, many=True)
        return Response({f'All Issues of {volume.number} of {volume.journal}': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        data['volume'] = pk
        data['journal'] = Volume.objects.get(id=pk).journal.id
        serializer = IssueSerializer(data=data, many=False)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# ISSUES
@api_view(['GET', 'PUT', 'DELETE'])
def issue(request, pk):
    issue = Issue.objects.get(id=pk)
    if request.method == 'GET':
        serializer = IssueSerializer(issue, many=False)
        return Response({f'Issue': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = IssueSerializer(issue, data=data, many=False)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        issue.delete()
        return Response({'Message': 'Issue was deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def issue_papers(request, pk):
    issue = Issue.objects.get(id=pk)
    papers = issue.paper_set.all()

    if request.method == 'GET':
        serializer = PaperSerializer(papers, many=True)
        return Response({f'All papers of {issue.number} of {issue.volume.journal}': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        data['issue'] = pk
        data['volume'] = Issue.objects.get(id=pk).volume.id
        print(f"The volume id is {data['volume']}")
        data['journal'] = Issue.objects.get(id=pk).journal.id
        print(f"The journal id is {data['journal']}")
        
        serializer = PaperSerializer(data=data, many=False)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

# PAPERS
@api_view(['GET', 'PUT', 'DELETE'])
def paper(request, pk):
    paper = Paper.objects.get(id=pk)
    if request.method == 'GET':
        serializer = PaperSerializer(paper, many=False)
        return Response({f'Paper': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = PaperSerializer(paper, data=data, many=False)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        paper.delete()
        return Response({'Message': 'Paper was deleted'}, status=status.HTTP_204_NO_CONTENT)
    


# OTHERS
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

