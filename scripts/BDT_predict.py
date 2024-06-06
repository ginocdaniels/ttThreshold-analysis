import uproot
import pandas as pd
import numpy as np
import os
import ROOT
from xgboost import XGBClassifier


ecm = 345
hadronic = True
channel = 'had' if hadronic else 'semihad'

infile_s = 'outputs/treemaker/WbWb/{0}/wzp6_ee_WbWb_{0}_ecm{1}.root'.format(channel,ecm)
infile_b = 'outputs/treemaker/WbWb/{}/p8_ee_WW_ecm{}.root'.format(channel,ecm)

infiles = [infile_s, infile_b]

bst = XGBClassifier()
bst.load_model('BDT_model/model_{}.json'.format(channel))

def evaluateBDT(infile):
    f = uproot.open(infile)
    tree = f["events"]
    pd = tree.arrays(tree.keys(),library="pd")

    preds = bst.predict_proba(pd)
    pd['BDT_score'] = preds[:,1]
    pd['BDT_score'] = pd['BDT_score'].astype('float32')

    dirs = infile.split('/')
    dirs[-2] = dirs[-2]+'_BDT'
    outfile = '/'.join(dirs)
    if not os.path.exists('/'.join(dirs[:-1])):
        os.makedirs('/'.join(dirs[:-1]))

    data_dict = {name: pd[name].values for name in pd.columns}
    file = uproot.recreate(outfile) 
    file["events"] = data_dict

    f.close()
    file.close()

    f = ROOT.TFile.Open(infile,'read')
    eventsProcessed = f.Get('eventsProcessed')
    eventsSelected = f.Get('eventsSelected')
    f.Close()

    out = ROOT.TFile.Open(outfile,'update')
    eventsProcessed.Write()
    eventsSelected.Write()
    out.Write()
    out.Close()

for infile in infiles:
    if not os.path.exists(infile):
        raise IOError('File not found: {}'.format(infile))
    print('Evaluating BDT for {}'.format(infile))
    evaluateBDT(infile)
    