# -*- coding: utf-8 -*-
import requests # requests��Ϊ���ǵ�html�ͻ���
from pyquery import PyQuery as Pq # pyquery������dom


class SegmentfaultQuestionSpider(object):

    def __init__(self, segmentfault_id): # ����Ϊ��segmentfault�ϵ�id
        self.url = 'http://segmentfault.com/q/{0}'.format(segmentfault_id)
        self._dom = None # Ū������������ȡ����html���ݣ�һ��֩��Ӧ��֮����һ��

    @property
    def dom(self): # ��ȡhtml����
        if not self._dom:
            document = requests.get(self.url)
            document.encoding = 'utf-8'
            self._dom = Pq(document.text)
        return self._dom

    @property 
    def title(self): # �÷�������ͨ��s.title�ķ�ʽ���� �����ٴ������
        return self.dom('h1#questionTitle').text() # ����ѡ�������Բο�css selector����jquery selector, ������pyquery�¼���������ʹ��

    @property
    def content(self):
        return self.dom('.question.fmt').html() # ֱ�ӻ�ȡhtml ���Ӿ��Ǵ� �Ժ���������

    @property
    def answers(self):
        return list(answer.html() for answer in self.dom('.answer.fmt').items()) # ��ס��Pqʵ����items�����Ǻ����õ�

    @property
    def tags(self):
        return self.dom('ul.taglist--inline > li').text().split() # ��ȡtags������ֱ����text���������з־����ˡ�һ��ֻҪ���������ݣ��������������Լ�û�пո�,���ŵȣ�����������Ū��ʡ�¡�

class SegmentfaultTagSpider(object):

    def __init__(self, tag_name, page=1):
        self.url = 'http://segmentfault.com/t/%s?type=newest&page=%s' % (tag_name, page)
        self.tag_name = tag_name
        self.page = page
        self._dom = None

    @property
    def dom(self):
        if not self._dom:
            document = requests.get(self.url)
            document.encoding = 'utf-8'
            self._dom = Pq(document.text)
            self._dom.make_links_absolute(base_url="http://segmentfault.com/") # ������ӱ�ɾ������� ˬ
        return self._dom


    @property
    def questions(self):
        return [question.attr('href') for question in self.dom('h2.title > a').items()]

    @property
    def has_next_page(self): # ��������û����һҳ������б�Ҫ
        return bool(self.dom('ul.pagination > li.next')) # ������ľ����һҳ

    def next_page(self): # �����֩��ɱ�ˣ� ����һ���µ�֩�� ץȡ��һҳ�� ��������������Ǹ����ʣ����ԾͲ���@property��
        if self.has_next_page:
            self.__init__(tag_name=self.tag_name ,page=self.page+1)
        else:
            return None

