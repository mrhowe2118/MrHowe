__author__ = 'MrHowe'
# -*- coding: utf-8 -*-
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"#该网页中全是单独成行的单词
WORDS = []

PHRASES = { #编写脚本时应该写的代码为key，其解释为value
    "class %%%(%%%):": #%%%表示类名
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False #False表示先打印key，按下任意键后再打印value
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True #True表示先打印value，按下任意键后再打印key


# load up the words from the website
for word in urlopen(WORD_URL).readlines(): #一行一行从网页中读取数据
    WORDS.append(word.strip()) #删除每一行开始和结尾的空格，只留下单词并加入到words列表中

#先从下面的try开始看，调用到该函数时再看回来
def convert(snippet, phrase): #我们以传入的具体参数来分析
    class_names = [w.capitalize() for w in #从WORDS序列中随机取出1个单词首字母大写后赋值给class_names，此处假设为"Actor"
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***")) #从WORDS序列中随机取出一个单词赋值给other_names，此处假设为"dinner"
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")): #只循环一次
        param_count = random.randint(1,3) #假设随机到了2
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        #从WORDS中随机取出2个单词用逗号和空格连接起来，放在param_names中，假设为"cook, donkey"

    for sentence in snippet, phrase: #循环两次，只讲解第一次循环
        result = sentence[:] #浅拷贝，result = "class %%%(object):\n\tdef ***(self, @@@)"

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word.decode(), 1) #result = "class Actor(object):\n\tdef ***(self, @@@)"

        # fake other names
        for word in other_names:
            result = result.replace("***", word.decode(), 1) #result = "class Actor(object):\n\tdef dinner(self, @@@)"

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word.decode(), 1) #result = "class Actor(object):\n\tdef dinner(self, cook, donkey)"

        results.append(result) #添加到results序列中

    return results
    #results = ["class Actor(object):\n\tdef dinner(self, cook, donkey)", "class Actor has-a function named dinner that takes self and cook, donkey parameters."]


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES) #提取PHRASES中的键
        print(snippets)
        random.shuffle(snippets) #打乱snippets中元素（PHRASES中键）顺序

        for snippet in snippets: #取一个键来操作，假设取到"class %%%(object):\n\tdef ***(self, @@@)"
            phrase = PHRASES[snippet] #取出值"class %%% has-a function named *** that takes self and @@@ parameters."
            question, answer= convert(snippet, phrase) #现在去上面看这个函数的定义
            if PHRASE_FIRST: #先打印value，再打印key
                question, answer = answer, question
            print(question)
            input("> ")
            print("ANSWER:  %s\n\n" % answer)
except EOFError:
    print("\nBye")