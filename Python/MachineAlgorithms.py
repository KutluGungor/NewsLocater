# -*- coding: utf-8 -*-

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.svm import LinearSVC
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

class machineAlgorithms(object):
    
    
    
    def __init__(self,daf,label):

        msg_train, msg_test, label_train, label_test = \
        train_test_split(daf, label, test_size=0.2)
        
    
        print("\n")
        print("\n")
        print("Message Train :",len(msg_train), "Message Test : ",len(msg_test), "Sum Data : ",len(msg_train) + len(msg_test))

        svc = Pipeline([('vect', TfidfVectorizer(lowercase=False)), ('svm', LinearSVC())])
        svc.fit(msg_train, label_train)

        # model save

        filename = 'news1150model.sav'
        pickle.dump(svc, open(filename, 'wb'))
        y_pred_class = svc.predict(msg_test) #Test işlemi yapılıyor.

        print("\n")
        print("\n")
        print('SVM Clasification: \n', classification_report(label_test, y_pred_class))
        print('SVM Confussion matrix: \n', confusion_matrix(label_test, y_pred_class))

        print("\n")
        print("\n")
        scores = cross_val_score(svc, daf, label, cv=10)
        print("SVM Scores : \n", scores)
        print("\n")
        print("\n")
        print("SVM Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))



    
