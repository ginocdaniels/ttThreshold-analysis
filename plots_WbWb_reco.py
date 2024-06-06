import ROOT

# global parameters

from treemaker_WbWb_reco import available_ecm, all_branches as branchList
branchList.append('BDT_score')

hadronic = True
channel = 'had' if hadronic else 'semihad'

ecm = 345
if not ecm in available_ecm:
    raise ValueError("ecm value not in available_ecm")


intLumi = 1
intLumiLabel = "L = 5 ab^{-1}"
ana_tex = "e^{+}e^{-} #rightarrow WbWb #rightarrow "+channel
delphesVersion = "3.4.2"
energy = ecm
collider = "FCC-ee"
formats = ["png"]

outdir         = './outputs/plots/WbWb/{}/'.format(channel) 
inputDir       = './outputs/histmaker/WbWb/{}/'.format(channel) 

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


for var in branchList:
    logy = False
    if var.endswith("_isB") or var.endswith("_isG") or var.endswith("_isQ") or var.endswith("_isS") or var.endswith("_isC"):
        logy = True
    if var.endswith('d_12') or var.endswith('d_23') or var.endswith('d_34') or var.endswith('d_45') or var.endswith('d_56'):
        logy = True
    if 'BDT_score' in var:
        logy = True
    hists[var] = {
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
        "output": 'BDT_cut_'+var,
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
    
    

