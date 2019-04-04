# -*- coding: utf-8 -*-

import FileLoad
import PropertyFunctions
import MachineAlgorithms

class Classifier(object):
    
    
    def __init__(self):
        
        
        f = FileLoad.fileLoad()
        daf = f.load2()                                #daf = DataFrame
        sp = PropertyFunctions.propertyFunctions()

        #first function (word stemmer operations (tf-idf))
        
        print("\n")
        print("\n")      
        print("WORD STEMMER PROCESS (TF-IDF)")
        print("\n")
        print("\n")

        message = daf["message"].apply(sp.split_into_stem)

        new_message = []
        for i in message:
            new_message.append(" ".join(i))

        MachineAlgorithms.machineAlgorithms(new_message,daf["label"])

Classifier()
