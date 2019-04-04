import pickle
import PropertyFunctions

def main(news):

    filename = 'news1150model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    sp = PropertyFunctions.propertyFunctions().split_into_stem(news['content'])
    sp = " ".join(sp)
    value_list = []
    value_list.append(sp)
    predict = loaded_model.predict(value_list)
    data = {'content': predict[0]}
    return data


#news =["istanbul'un trafiği ve artmaya devam edecek. Çözüm nerede? Çözüm toplu ulaşımda. Asıl çözümü oluşturan segment raylı sistem. Şu anda mevcut uzunluk 170 km. Mart'ın 10'unda Gebze Halkalı banliyö hattı devreye girecek. Onunla birlikte 238 km'ye çıkmış olacak. Hedefimiz 5 yıl içinde 518 km'ye çıkartmak. 518'e çıktığı zaman Tokyo'yu da Paris'i de geçiyoruz. O zaman ne olacak? Raylı sistemin toplu taşımadaki payı yüzde 48'e çıkacak. Yüzde 30 artacak."]
#print(news,"\n")
#value = main(news)
#print(value)