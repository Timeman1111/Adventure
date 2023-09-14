import pickle
import npc
import scene





def export_as_pickle(object,filename,outputPath = ''):
    with open(filename,'wb') as f:
        pickle.dump(object,f)
        return True
    
