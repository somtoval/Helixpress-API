# serializers.py
from rest_framework import serializers
from .models import *

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ['number', 'journal']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['number', 'volume', 'journal']

class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['title', 'author', 'issue', 'volume', 'journal', 'description', 'institution', 'keywords', 'document', 'date_created', 'doi', 'editorsChoice']



# OTHER SERIALIZERS
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class HomeSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSlider
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = '__all__'

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = '__all__'

class OpenAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenAccess
        fields = '__all__'

class EditorialProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorialProcess
        fields = '__all__'

class EthicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethics
        fields = '__all__'

class ChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charges
        fields = '__all__'

class VisibilityStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisibilityStatement
        fields = '__all__'
