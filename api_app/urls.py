from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Base URL
    path("get_routes", get_routes),
    
    # Journal URLs
    path("journals", journals), # returns all journals
    path("journal/<int:pk>", journal), # returns a specific journal

    path("journal/<int:pk>/volumes", journal_volumes), # returns all volumes of a specific journal
    path("journal/<int:pk>/papers", journal_papers), # returns all papers of a specific journal


    # Volume URLs
    path("volume/<int:pk>", volume), # returns a specific journal
    path("volume/<int:pk>/issues", volume_issues), # returns all issues of a specific volume


    # Issue URLs
    path("issue/<int:pk>", issue), # returns a specific issue
    path("issue/<int:pk>/papers", issue_papers), # returns all papers of a specific issue


    # Paper URLs
    path("paper/<int:pk>", paper), # returns a specific paper

    # Authentication URLs
    path("login", login_view), # logout endpoint
    path("logout", logout_view), # logout endpoint
    path('api-token-auth', obtain_auth_token), # obtaining user token endpoint
    path('create_user', create_user_view), # user creation endpoint

    ## OTHER URLs
    # News URLs
    path('news/', news_list, name='news-list'),
    path('news/<int:pk>/', news_detail, name='news-detail'),

    # HomeSlider URLs
    path('home-sliders/', home_slider_list, name='home-slider-list'),
    path('home-sliders/<int:pk>/', home_slider_detail, name='home-slider-detail'),

    # Submission URLs
    path('submissions/', submission_list, name='submission-list'),
    path('submissions/<int:pk>/', submission_detail, name='submission-detail'),

    # Newsletter URLs
    path('newsletters/', newsletter_list, name='newsletter-list'),
    path('newsletters/<str:pk>/', newsletter_detail, name='newsletter-detail'),

    # About URLs
    path('about/', about_list, name='about-list'),
    path('about/<int:pk>/', about_detail, name='about-detail'),

    # Contact URLs
    path('contacts/', contact_list, name='contact-list'),
    path('contacts/<int:pk>/', contact_detail, name='contact-detail'),

    # Author URLs
    path('authors/', author_list, name='author-list'),
    path('authors/<int:pk>/', author_detail, name='author-detail'),

    # Reviewer URLs
    path('reviewers/', reviewer_list, name='reviewer-list'),
    path('reviewers/<int:pk>/', reviewer_detail, name='reviewer-detail'),

    # Editor URLs
    path('editors/', editor_list, name='editor-list'),
    path('editors/<int:pk>/', editor_detail, name='editor-detail'),

    # OpenAccess URLs
    path('open-access/', open_access_list, name='open-access-list'),
    path('open-access/<int:pk>/', open_access_detail, name='open-access-detail'),

    # EditorialProcess URLs
    path('editorial-processes/', editorial_process_list, name='editorial-process-list'),
    path('editorial-processes/<int:pk>/', editorial_process_detail, name='editorial-process-detail'),

    # Ethics URLs
    path('ethics/', ethics_list, name='ethics-list'),
    path('ethics/<int:pk>/', ethics_detail, name='ethics-detail'),

    # Charges URLs
    path('charges/', charges_list, name='charges-list'),
    path('charges/<int:pk>/', charges_detail, name='charges-detail'),

    # VisibilityStatement URLs
    path('visibility-statements/', visibility_statement_list, name='visibility-statement-list'),
    path('visibility-statements/<int:pk>/', visibility_statement_detail, name='visibility-statement-detail'),

]

##################### USING ROUTERS ###################
# Special Configuration for viewsets which is the router
from rest_framework.routers import DefaultRouter
from .views_with_viewsets import *

# Our URL Mapping
# You can give it anyname but here we will call it router
router = DefaultRouter()
# "my_journals" here is the prefix
router.register("my_journals", JournalsViewSet)
router.register("my_volumes", VolumeViewSet)

urlpatterns += router.urls # You can also add "path("", include(router.urls))" and it will work

# With this we can access /api/my_journals and see all journals, we can send post, delete and so on
# We can also do /api/my_journals/1 and it automatically gets the journal with id of 1
# To see all the router endpoints we go to /api

