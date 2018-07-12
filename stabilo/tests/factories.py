from factory import Faker, fuzzy, SubFactory
from factory.django import DjangoModelFactory

from ..models import Category, Keyword


class CategoryFactory(DjangoModelFactory):

    class Meta:
        model = Category

    label = Faker('word')
    slug = Faker('word')


class KeywordFactory(DjangoModelFactory):

    class Meta:
        model = Keyword

    keyword = Faker('word')
    category = SubFactory(CategoryFactory)
