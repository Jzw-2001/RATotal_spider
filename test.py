import requests
import re
import chardet
import codecs
from lxml import html


def solve_url(url__):
    try:
        #url__ = 'http://www.uc129.com/zhanshu/ra3/31400.html'
        
        
        #标题
        doc = html.parse(url__)
        #title = doc.find('.//title').text
        title = doc.findtext('.//title')[:-5]
        print (title)


        #内容
        fw = open("C:/Users/pc/Desktop/articles/test.txt", 'w+',encoding='gb18030')    
        r=requests.get(url__)
        r.encoding=('gb18030')
        text_pre = r.text
        text_nxt = re.sub(u"\\<.*?\\>", "", text_pre)

        #print(text_nxt)
        #print(type(text_nxt))
        #print(type(text_pre))

        begin = text_nxt.find('www.uc129.com')
        end = text_nxt.find('本类TOP10')
        #print(begin)
        #print(end)
        fw.write(text_nxt[begin+13:end])
        fw.flush()
    except:
        print("没有url为"+url__+"的文章")
        return

    try:
        #转码
        filename_in = 'C:/Users/pc/Desktop/articles/test.txt'
        filename_out = 'C:/Users/pc/Desktop/articles/'+re.sub(u"/", "_", title)+'.txt'

        # 输入文件的编码类型
        encode_in = 'gb18030'

        # 输出文件的编码类型
        encode_out = 'utf-8'

        with codecs.open(filename=filename_in, mode='r', encoding=encode_in) as fi:
            data = fi.read()
            with open(filename_out, mode='w', encoding=encode_out) as fo:
                fo.write(data)
                fo.close()

        with open(filename_out, 'rb') as f:
            data = f.read()
            print(chardet.detect(data))
        return
    except:
        print("出错了")

i = 0
while i < 40000:
    solve_url('http://www.uc129.com/zhanshu/ra3/' + str(i) + '.html')
    i = i + 1
