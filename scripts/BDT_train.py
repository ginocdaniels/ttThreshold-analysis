import uproot
import pandas as pd
import numpy as np
import os,sys

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
sys.path.insert(0, "/afs/cern.ch/work/a/anmehta/public/FCC/ttThreshold-analysis/") #os.getcwd()+'../')
from treemaker_WbWb_reco import all_branches

def if3(cond, iftrue, iffalse):
    return iftrue if cond else iffalse




useflav=True 
usebtagged=False if useflav else True
noflav=False
if noflav:
    usebtagged=False
    useflav=False



branches_toTrain=[]

branches_toTrain=all_branches


ecm = '345'

max_entries = 1E05
hadronic = False
channel = 'had' if hadronic else 'semihad'
base_dir="/eos/user/m/mdefranc/condor_WbWb/{}/".format(channel)
sig="wzp6_ee_WbWb_{0}_ecm{1}".format(channel,ecm)
bkg="p8_ee_WW_ecm{}".format(ecm)




infile_s =  uproot.concatenate([os.path.join(base_dir,sig,f)+':events' for f in os.listdir(os.path.join(base_dir,sig)) if f.endswith(".root")],branches_toTrain ,library="pd")
infile_b =  uproot.concatenate([os.path.join(base_dir,bkg,f)+':events' for f in os.listdir(os.path.join(base_dir,bkg)) if f.endswith(".root")],branches_toTrain ,library="pd")

flavor_branches=[v for v in all_branches if '_is' in v]
pf="%s"%if3(usebtagged,'_withbtaggedJet',if3(useflav,'_withflav','_noflav'))

if usebtagged:
    
    infile_s["jet1_btagged"] =np.where(infile_s["jet1_isB"] > 0.5,1, 0)
    infile_b["jet1_btagged"] =np.where(infile_b["jet1_isB"] > 0.5,1, 0)
    infile_s["jet2_btagged"] =np.where(infile_s["jet2_isB"] > 0.5,1, 0)
    infile_b["jet2_btagged"] =np.where(infile_b["jet2_isB"] > 0.5,1, 0)
    infile_s["jet3_btagged"] =np.where(infile_s["jet3_isB"] > 0.5,1, 0)
    infile_b["jet3_btagged"] =np.where(infile_b["jet3_isB"] > 0.5,1, 0)
    infile_s["jet4_btagged"] =np.where(infile_s["jet4_isB"] > 0.5,1, 0)
    infile_b["jet4_btagged"] =np.where(infile_b["jet4_isB"] > 0.5,1, 0)
    infile_s["jet5_btagged"] =np.where(infile_s["jet5_isB"] > 0.5,1, 0)
    infile_b["jet5_btagged"] =np.where(infile_b["jet5_isB"] > 0.5,1, 0)
    infile_s["jet6_btagged"] =np.where(infile_s["jet6_isB"] > 0.5,1, 0)
    infile_b["jet6_btagged"] =np.where(infile_b["jet6_isB"] > 0.5,1, 0)

    infile_s=infile_s.drop(columns=flavor_branches, axis=1)
    infile_b=infile_b.drop(columns=flavor_branches, axis=1)

if noflav:
        infile_s=infile_s.drop(columns=flavor_branches, axis=1)
        infile_b=infile_b.drop(columns=flavor_branches, axis=1)

    
#branches_toTrain.append('')
print(infile_s)


#print(type(infile_b))
pd_s = (infile_s)
pd_b = (infile_b)


pd_s['target'] = 1.
pd_b['target'] = 0.

pd_all = pd.concat([pd_s, pd_b])


print('starting to train')
X_train, X_test, y_train, y_test = train_test_split(pd_all.drop(columns=['target']), pd_all['target'], test_size=0.5) #train_test_split
print('defined splits')
bst = XGBClassifier(n_estimators=50, max_depth=5, learning_rate=0.1, verbosity=0, objective='binary:logistic')
print('created model instance ')
bst.fit(X_train, y_train)
print('fitted the model')
preds = bst.predict_proba(X_test)
print('predictions')
pd_preds = pd.DataFrame()
pd_preds['target'] = y_test
pd_preds['preds'] = preds[:,1]


train_preds = bst.predict_proba(X_train)
pd_train_preds = pd.DataFrame()
pd_train_preds['target']  = y_train
pd_train_preds['preds'] = train_preds[:,1]


import matplotlib.pyplot as plt

# Plot signal and background predictions
plt.hist(pd_preds[pd_preds['target'] == 1]['preds'], bins=50, label='Signal-test', histtype='step',color='tab:red',alpha=0.5, log=True)
plt.hist(pd_preds[pd_preds['target'] == 0]['preds'], bins=50, label='Background-test', histtype='step',color='tab:blue',alpha=0.5, log=True)
plt.hist(pd_train_preds[pd_train_preds['target'] == 1]['preds'], bins=50, label='Signal-train', histtype='step',color='tab:green',alpha=0.5, log=True)
plt.hist(pd_train_preds[pd_train_preds['target'] == 0]['preds'], bins=50, label='Background-train',  histtype='step',color='tab:orange',alpha=0.5, log=True)



plt.xlabel('Prediction')
plt.ylabel('Count')
plt.legend()
print('Saving model')
outdir = '/eos/user/a/anmehta/www/FCC_top/BDT_model'
if not os.path.exists(outdir):
    os.makedirs(outdir)

bst.save_model('{}/model_{}_{}{}.json'.format(outdir,channel,ecm,pf))
plt.savefig('{}/preds_{}_{}{}.png'.format(outdir,channel,ecm,pf))
plt.savefig('{}/preds_{}_{}{}.pdf'.format(outdir,channel,ecm,pf))
plt.close()
