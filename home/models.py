from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page, Site
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailadmin.edit_handlers import FieldPanel

class HomePage(Page):
    def get_template(self, request):
        # Retrieve the current site based on the request
        current_site = Site.find_for_request(request)

        # If no site is found, return a default template
        if not current_site:
            return 'home/default_home_page.html'

        # Retrieve the site branding settings for the current site
        branding = SiteBranding.for_site(current_site)

        # Use the specified template if it exists, otherwise fallback to a default
        if branding and branding.template:
            return branding.template
        return 'home/default_home_page.html'
        
    body = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
