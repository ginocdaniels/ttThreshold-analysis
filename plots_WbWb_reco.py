import ROOT,uproot

# global parameters

from treemaker_WbWb_reco import available_ecm, all_branches as branchList
branchList.append('BDT_score')
def if3(cond, iftrue, iffalse):
    return iftrue if cond else iffalse

hadronic = False
channel = 'had' if hadronic else 'semihad'
useflav=False
usebtagged=False
pf="%s"%if3(usebtagged,'withbtaggedJet',if3(useflav,'withflav','noflav'))

ecm = 345


intLumi = 1
intLumiLabel = "L = 5 ab^{-1}"
ana_tex = "e^{+}e^{-} #rightarrow WbWb #rightarrow "+channel
delphesVersion = "3.4.2"
energy = ecm
collider = "FCC-ee"
formats = ["png","pdf"]

inputDir       = '/eos/cms/store/cmst3/group/top/anmehta/FCC/condor_WbWb/outputs/histmaker/WbWb/{}/{}/'.format(channel,pf) 
outdir         = '/eos/user/a/anmehta/www/FCC_top/{}/{}/{}/'.format(channel,pf,ecm)

plotStatUnc = True

colors = {}
colors["WbWb"] = ROOT.kRed
colors["WW"] = ROOT.kBlue

procs = {}
procs["signal"] = {"WbWb": ["wzp6_ee_WbWb_{}_ecm{}".format(channel,ecm)]}
procs["backgrounds"] = {"WW": ["p8_ee_WW_ecm{}".format(ecm)]}

legend = {}
legend["WbWb"] = "WbWb"
legend["WW"] = "WW"

hists = {}

#tree=uproot.open(inputDir+"/p8_ee_WW_ecm340.root")["events"]

#branchList=['lep_p','BDT_score','lep_theta','jet1_p']
for var in branchList:
 
    if "_is" in var: continue
    logy = False
    if var.endswith("_isB") or var.endswith("_isG") or var.endswith("_isQ") or var.endswith("_isS") or var.endswith("_isC"):
        logy = True
    if var.endswith('d_12') or var.endswith('d_23') or var.endswith('d_34') or var.endswith('d_45') or var.endswith('d_56'):
        logy = True
    if 'BDT_score' in var:
        logy = True
    hists['no_cut_'+var] = {
        "output": var+"_stack",
        "logy": logy,
        "stack": True,
        "rebin": 1,
        "xmin": -1,
        "xmax": -1,
        "ymin": 0 if not logy else 1,
        "ymax": -1,
        "xtitle": var,
        "ytitle": "Events",
    }

    hists['no_cut_'+var] = {
        "output": var,
        "logy": logy,
        "stack": False,
        "rebin": 1,
        "xmin": -1,
        "xmax": -1,
        "ymin": 0 if not logy else 1,
        "ymax": -1,
        "xtitle": var,
        "ytitle": "Events",
    }


    hists['BDT_cut_'+var] = {
        "output": 'BDT_cut_'+var+"_nostack",
        "logy": logy,
        "stack": True,
        "rebin": 1,
        "xmin": -1,
        "xmax": -1,
        "ymin": 0 if not logy else 1,
        "ymax": -1,
        "xtitle": var,
        "ytitle": "Events",
    }

    
    hists['BDT_cut_'+var] = {
        "output": 'BDT_cut_'+var,
        "logy": logy,
        "stack": False,
        "rebin": 1,
        "xmin": -1,
        "xmax": -1,
        "ymin": 0 if not logy else 1,
        "ymax": -1,
        "xtitle": var,
        "ytitle": "Events",
    }

    

