from parler.forms import TranslatableModelForm, TranslatedField
from app.models import Blog, Regions


class BlogAdminForm(TranslatableModelForm): # => form for admin panel
    title = TranslatedField()
    description = TranslatedField()

    class Meta:
        model = Blog
        fields = ('title', 'slug', 'description', 'image', 'region', 'category','hashtag',)


class RegionsAdminForm(TranslatableModelForm): # => form for admin panel
    name = TranslatedField()

    class Meta:
        model = Regions
        fields = ('name', 'slug',)