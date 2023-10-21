from fastai.vision import *
from fastai.learner import load_learner
import pathlib
import os
import pickle
import platform 

path= os.getcwd()
EXPORT_PATH = pathlib.Path(os.path.join(path,'models', 'kidneystone_ml_improved'))
posix_backup = pathlib.PosixPath

def check_kidney_stone(xrayImageOfKidney):
    try:
        plt = platform.system()
        if plt == 'Linux':
            pathlib.PosixPath = posix_backup
        else:
            pathlib.PosixPath = pathlib.WindowsPath
        learn_inf = load_learner(EXPORT_PATH)
        r =learn_inf.predict(xrayImageOfKidney)
        return r[0]
    finally:
       pathlib.PosixPath = posix_backup
       
def check_cdk(array_of_values):
    modelpath=os.path.join(path, "dtc_ckd.pkl")
    dtc = pickle.load(open(modelpath, 'rb'))
    r = dtc.predict([array_of_values])
    return r [0]



