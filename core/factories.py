import factory
from news.models import News

class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News

    title = factory.Sequence(lambda n: f'Title of post number {n}')
    short_description = factory.Sequence(lambda n: f'Short_description {n}')
    description = factory.Sequence(lambda n: f'Description {n}')