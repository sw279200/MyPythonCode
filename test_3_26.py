import re
with open('article.txt', 'r', encoding='utf-8') as file:
    #1.1.读取txt文本文件内容
    file_txt = file.read()
    #2.文本预处理，去掉英文符号
    word_text=re.sub(r'[?.!,;""/\[\]]', ' ', file_txt) #特殊字符替换成空格
    word_texts=re.sub(r"-", ' ', word_text) #替换单独的-，不是同一单词里的连字符
    #3.分割获得单词列表
    wordlist=word_texts.split()
    #4.获得单词频次字典
    word_dict={}
    for word in wordlist:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]=word_dict.get(word)+1
    #5.对字典进行排序
    dict_order = dict(sorted(word_dict.items(), key=lambda x:x[1], reverse=True))#reverse为True，降序
    #6.显示字典前10项
    print(list(dict_order.items())[:10])

