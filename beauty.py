
# coding: utf-8

# In[4]:

from pyquery import PyQuery as pq
from IPython.display import Image
import urllib
import os
N = 20
num = 0
testfile = urllib.URLopener()
gogogo = []
q = pq(url="https://www.ptt.cc/bbs/Beauty/index.html")
jizz = q("a.wide").text()
jizz = q("a.wide").filter(lambda i, this: pq(this).text().encode("utf8")  == "‹ 上頁")
ji = int(jizz.attr['href'][-9:-5])
for page in range(ji-N, ji):    
    q = pq(url="https://www.ptt.cc/bbs/Beauty/index"+str(page)+".html")
    jizz = q("div.r-ent").filter(lambda i, this: pq(this)("div.nrec").find("span").text().encode("utf8")  == "爆")
    if(jizz("div.title")("a").attr['href']):
        os.mkdir("./" + jizz("div.title")("a").text());
        num = 0
        print jizz("div.title")("a").text()," https://www.ptt.cc"+jizz("div.title")("a").attr['href']
        qq = "https://www.ptt.cc"+jizz("div.title")("a").attr['href'].encode("utf8")
        h = pq(url = qq)
        for i in h("div#main-content")("div.richcontent")("img"):
            image = str(pq(i).attr["src"].encode("utf8"))
            if image[0:4]!="http":
                image = "http:" + image
                if(image):
                    #testfile.retrieve(image, str(jizz("div.title")("a").text().encode("utf8")) + "/" + str(num) + ".jpg")
                    testfile.retrieve(image,  "./" + jizz("div.title")("a").text() + "/" + str(num) + ".jpg")
                    print image
                    num+=1


# In[6]:



