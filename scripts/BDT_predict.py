import uproot
import pandas as pd
import numpy as np
import os,sys,re
import ROOT
from xgboost import XGBClassifier
def if3(cond, iftrue, iffalse):
    return iftrue if cond else iffalse

sys.path.insert(0, "/afs/cern.ch/work/a/anmehta/public/FCC/ttThreshold-analysis/") #os.getcwd()+'../')
from treemaker_WbWb_reco import all_branches

outdir = '/eos/user/a/anmehta/www/FCC_top/BDT_model'



ecm_model='345'
hadronic = False

branches_toTrain=[]
branches_toTrain=all_branches


channel = 'had' if hadronic else 'semihad'
channel_model = 'semihad'
base_dir="/eos/cms/store/cmst3/group/top/anmehta/FCC/condor_WbWb/{}/".format(channel)

def calcsumW(proc):
    sumW=0
    nfiles=[os.path.join(base_dir,proc,f) for f in os.listdir(os.path.join(base_dir,proc)) if re.search('^events_\d*.root',f)]
    for i in nfiles:
        if re.search('events_\d*.root',i):
            fIn=ROOT.TFile.Open(i,"read")
            #print(i,fIn.Get("eventsProcessed").GetVal())
            sumW+=fIn.Get("eventsProcessed").GetVal();
            fIn.Close();
    return sumW

def evaluate(proc,ecm,useflav,usebtagged):

    infiles =  uproot.concatenate([os.path.join(base_dir,proc,f)+':events' for f in os.listdir(os.path.join(base_dir,proc)) if re.search('^events_\d*.root',f)],branches_toTrain ,library="pd")
    flavor_branches=[v for v in all_branches if '_is' in v]
    
    nbjets= np.where(infiles["jet1_isB"] > 0.5,1,0) + np.where(infiles["jet2_isB"] > 0.5 ,1,0) + np.where(infiles["jet3_isB"] > 0.5,1,0) + np.where(infiles["jet4_isB"] > 0.5,1,0) + np.where(infiles["jet5_isB"] > 0.5,1,0)   
    if usebtagged:
        #print('in here')
        infiles["jet1_btagged"] =np.where(infiles["jet1_isB"] > 0.5,1, 0)
        infiles["jet2_btagged"] =np.where(infiles["jet2_isB"] > 0.5,1, 0)
        infiles["jet3_btagged"] =np.where(infiles["jet3_isB"] > 0.5,1, 0)
        infiles["jet4_btagged"] =np.where(infiles["jet4_isB"] > 0.5,1, 0)
        infiles["jet5_btagged"] =np.where(infiles["jet5_isB"] > 0.5,1, 0)
        infiles["jet6_btagged"] =np.where(infiles["jet6_isB"] > 0.5,1, 0)
        infiles=infiles.drop(columns=flavor_branches, axis=1)
    if not usebtagged and not useflav:
        infiles=infiles.drop(columns=flavor_branches, axis=1)
        
    ##load model 
    pf="%s"%if3(usebtagged,'withbtaggedJet',if3(useflav,'withflav','noflav'))
    print('runnning for %s'%pf)
    bst = XGBClassifier()
    bst.load_model('{}/model_{}_{}_{}.json'.format(outdir,channel_model,ecm_model,pf))
    preds = bst.predict_proba(infiles)
    pd = (infiles)
    pd['BDT_score'] = preds[:,1]
    pd['BDT_score'] = pd['BDT_score'].astype('float32')
    pd["nbjets"] = nbjets #np.where(infiles["jet1_isB"] > 0.5,1,0) + np.where(infiles["jet2_isB"] > 0.5 ,1,0) + np.where(infiles["jet3_isB"] > 0.5,1,0) + np.where(infiles["jet4_isB"] > 0.5,1,0) + np.where(infiles["jet5_isB"] > 0.5,1,0)
    #print((infiles["jet1_isB"]).shape)
    #print(np.where(infiles["jet1_isB"] > 0.5,1,0) + np.where(infiles["jet2_isB"] > 0.5 ,1,0) + np.where(infiles["jet3_isB"] > 0.5,1,0) + np.where(infiles["jet4_isB"] > 0.5,1,0) + np.where(infiles["jet5_isB"] > 0.5,1,0))
    #print((np.where(infiles["jet1_isB"] > 0.5,1,0) + np.where(infiles["jet2_isB"] > 0.5 ,1,0) + np.where(infiles["jet3_isB"] > 0.5,1,0) + np.where(infiles["jet4_isB"] > 0.5,1,0) + np.where(infiles["jet5_isB"] > 0.5,1,0)).shape)

    data_dict = {name: pd[name].values for name in pd.columns}
    odir=os.path.join(base_dir,pf,proc)
    if not os.path.exists(odir):
        os.makedirs(odir)
    fname_new = os.path.join(odir,'events_combined.root')
    if os.path.exists(fname_new):
        os.remove(fname_new)
    print ('this is the name of the output file',fname_new)
    rdf = ROOT.RDF.MakeNumpyDataFrame(data_dict)
    rdf.Snapshot('events', fname_new,  pd.columns)
    fname=ROOT.TFile.Open(fname_new,"update")
    sumW=calcsumW(proc)
    fname.cd();
    p = ROOT.TParameter(int)("eventsProcessed", sumW)
    #print(sumW,p.GetVal())
    p.Write();
    fname.Write();fname.Close();
for ecm in ['340','345','350','355']:
    sig="wzp6_ee_WbWb_{0}_ecm{1}".format(channel,ecm)
    bkg="p8_ee_WW_ecm{}".format(ecm)
    
    evaluate(sig,ecm,True,False)
    evaluate(bkg,ecm,True,False)
    evaluate(sig,ecm,False,True)
    evaluate(bkg,ecm,False,True)
    evaluate(sig,ecm,False,False)
    evaluate(bkg,ecm,False,False)
