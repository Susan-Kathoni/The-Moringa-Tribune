import datetime as dt
from django.test import TestCase
from .models import Editor,Article,tags
from .models import Photo

from cloudinary.forms import CloudinaryFileField 


# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.susan= Editor(first_name = 'Susan', last_name ='Kariuki', email ='karis041@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.susan,Editor))

    def test_save_method(self):
        self.susan.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)    

class ArticleTestClass(TestCase):

    #Creating a new editor and saving it
    def setUp(self):
        self.susan= Editor(first_name = 'Susan', last_name = 'Kariuki', email = 'karis041@gmail.com')
        self.susan.save_editor()

    #Creating a new tag and saving it
    
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.susan)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)
       

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)


    def test_get_news_by_date(self):
        test_date = '2019-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)


    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()



