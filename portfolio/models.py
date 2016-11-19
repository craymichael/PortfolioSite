from django.db import models


class Page(models.Model):
    """"""
    name = models.CharField(max_length=50, primary_key=True, blank=True, unique=True)

    def __str__(self):
        """The page's name."""
        return self.name


def default_page():
    return Page.objects.get_or_create(name='')[0]


class Section(models.Model):
    """Base section. Uses self for sub-sections."""
    section_title = models.CharField(max_length=100)
    sub_section = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    order = models.PositiveIntegerField(default=0)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, default=default_page)

    class Meta:
        """Metadata for Section."""
        unique_together = (
            ('page', 'section_title'),  # Unique title for each section in page
            ('sub_section', 'section_title'),  # Unique title for each subsection in section
        )
        ordering = ['order', 'section_title']  # Order by ascending order (starting at 0), then by title

    def __str__(self):
        """The section's title."""
        return self.section_title


class SectionItem(models.Model):
    """Base section item. Contains text to be displayed, a section can have multiple SectionItems."""
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    section_text = models.TextField(max_length=10000)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        """Metadata for SectionItem."""
        ordering = ['order', 'section_text']  # Order by ascending order (starting at 0), then by text

    def __str__(self):
        """The section item's text."""
        return self.section_text
