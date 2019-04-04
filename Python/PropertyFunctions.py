# -*- coding: utf-8 -*-

#from nltk.corpus import stopwords
import re
from zemberek import main_libs as ml


class propertyFunctions(object):

    def __init__(self):

        global stop_words
        #stop_words = set(stopwords.words("turkish"))  # stopwords words

        stop_words = {'o', 'eğer', 'nasıl', 'biz', 'bu', 'çünkü', 'bazı', 'ya', 've', 'defa', 'ne', 'niçin', 'şu', 'siz', 'yani', 'sanki', 'hem', 'kez', 'nereye', 'az', 'ama', 'birkaç', 'ile', 'hepsi', 'ise', 'nerde', 'de', 'diye', 'kim', 'neden', 'birşey', 'mu', 'aslında', 'şey', 'acaba', 'hep', 'gibi', 'en', 'için', 'daha', 'hiç', 'mü', 'biri', 'belki', 'da', 'veya', 'çok', 'tüm', 'mı', 'her', 'ki', 'nerede', 'niye'}


        # jvm.dll path location
        self.zemberek_api = ml.zemberek_api(libjvmpath="/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so",
                                       zemberekJarpath="./zemberek/zemberek-tum-2.0.jar").zemberek()

        # jvmDLLpath = r"C:\Program Files\Java\jdk1.7.0\jre\bin\server\jvm.dll"               # for windows

    # word root operations
    def split_into_stem(self, message):
        message = message.lower()
        words = re.sub(r'[^\w\s]', '', message) #Noktalama işaretleri kaldırıldı.
        words = words.split() #Kelimeler boşluklardan ayrıldı.
        words = [w2 for w2 in words if not w2 in stop_words]  # Stop wordsler kaldırıldı.
        return  ml.ZemberekTool(self.zemberek_api).metinde_gecen_kokleri_bul(words)

