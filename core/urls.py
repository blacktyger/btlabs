# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path("", include("apps.authentication.urls")),  # Auth routes - login / register

    # Leave `Home.Urls` as last the last line
    path("projects/", include("apps.projects.urls")),
    path("tipbot/", include("apps.funding.urls")),
    path("epicweb/", include("apps.epicweb.urls")),
    path("easyminer/", include("apps.easyminer.urls")),
    path("epicradar/", include("apps.epicradar.urls")),
    path("miningcalc/", include("apps.miningcalc.urls")),
    path("giverofepic/", include("apps.giverofepic.urls")),

    path("", include("apps.home.urls"))
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
