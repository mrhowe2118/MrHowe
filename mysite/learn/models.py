from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']

class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='questions')
    sf_id = models.CharField(max_length=16, default='0')  #加上这个可以记住问题在sf的位置，方便以后更新或者其他操作
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    content = models.TextField()

    def __str__(self):
        return 'To question %s' % self.question.title		

		
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

# Create your models here.




