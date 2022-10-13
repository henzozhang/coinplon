from django.db import models

from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core .models import Page

class FlexPage(Page):
    
    class Meta :
        verbose_name = "page divers"
        verbose_name_plural = "pages divers"
    
    
    text = models.TextField(
        
        blank = True,
        help_text = "A propos de coinPlon"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("text")]