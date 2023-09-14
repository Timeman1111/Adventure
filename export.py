import pickle
import npc
import scene





def export_as_pickle(object,filename):
    with open(filename,'wb') as f:
        pickle.dump(object,f)
        f.close()
        return True
    
