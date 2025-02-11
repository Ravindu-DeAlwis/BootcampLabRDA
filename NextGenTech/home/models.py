from django.db import models

from wagtail.models import Page  # ✅ Correct import
from wagtail.fields import RichTextField  # ✅ Correct import
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultiFieldPanel  # ✅ Correct import
from wagtail.images.models import Image  # ✅ Use models.Image directly instead



class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], default="Welcome to our site!")
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
   )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
        PageChooserPanel("banner_cta")
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


# from django.db import models

# from wagtail.models import Page


# class HomePage(Page):
#     pass
