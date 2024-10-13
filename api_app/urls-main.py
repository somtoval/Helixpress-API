from django.urls import path
from .views import *

urlpatterns = [
    # Base URL
    path("", getRoutes),

    # Journal URLs
    path('journals/', journal_list, name='journal-list'),
    path('journals/<int:pk>/', journal_detail, name='journal-detail'),

    # Volume URLs
    path('volumes/', volume_list, name='volume-list'),
    path('volumes/<int:pk>/', volume_detail, name='volume-detail'),

    # Issue URLs
    path('issues/', issue_list, name='issue-list'),
    path('issues/<int:pk>/', issue_detail, name='issue-detail'),

    # Paper URLs
    path('papers/', paper_list, name='paper-list'),
    path('papers/<int:pk>/', paper_detail, name='paper-detail'),

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
    path('newsletters/<int:pk>/', newsletter_detail, name='newsletter-detail'),

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
