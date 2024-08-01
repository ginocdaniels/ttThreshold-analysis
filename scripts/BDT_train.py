import uproot
import pandas as pd
import numpy as np
import os

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

ecm = 345
max_entries = 1E05
hadronic = True
channel = 'had' if hadronic else 'semihad'

infile_s = 'outputs/treemaker/WbWb/{0}/wzp6_ee_WbWb_{0}_ecm{1}.root'.format(channel,ecm)
infile_b = 'outputs/treemaker/WbWb/{}/p8_ee_WW_ecm{}.root'.format(channel,ecm)

tree_s = uproot.open(infile_s)["events"]
tree_b = uproot.open(infile_b)["events"]

pd_s = tree_s.arrays(tree_s.keys(),library="pd",entry_stop=max_entries)
pd_b = tree_b.arrays(tree_b.keys(),library="pd",entry_stop=max_entries)

pd_s['target'] = 1.
pd_b['target'] = 0.

pd_all = pd.concat([pd_s, pd_b])

X_train, X_test, y_train, y_test = train_test_split(pd_all.drop(columns=['target']), pd_all['target'], test_size=0.2)

bst = XGBClassifier(n_estimators=100, max_depth=10, learning_rate=0.1, verbosity=0, objective='binary:logistic')
bst.fit(X_train, y_train)
preds = bst.predict_proba(X_test)

pd_preds = pd.DataFrame()
pd_preds['target'] = y_test
pd_preds['preds'] = preds[:,1]


import matplotlib.pyplot as plt

# Plot signal and background predictions
plt.hist(pd_preds[pd_preds['target'] == 1]['preds'], bins=50, label='Signal', alpha=0.5, log=True)
plt.hist(pd_preds[pd_preds['target'] == 0]['preds'], bins=50, label='Background', alpha=0.5, log=True)
plt.xlabel('Prediction')
plt.ylabel('Count')
plt.legend()
print('Saving model')
outdir = 'BDT_model'
if not os.path.exists(outdir):
    os.makedirs(outdir)
bst.save_model('{}/model_{}.json'.format(outdir,channel))
plt.savefig('{}/preds_{}.png'.format(outdir,channel))
plt.close()