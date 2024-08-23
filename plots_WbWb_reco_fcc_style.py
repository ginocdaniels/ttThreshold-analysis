import ROOT, os,uproot
from datetime import date
# global parameters

from treemaker_WbWb_reco import available_ecm, all_branches as branchList
branchList.append('BDT_score')

ecm_scan = [340]#,345, 350, 355] # List of ecm values to scan
hadronic = False
channel = 'had' if hadronic else 'semihad'



intLumi = 1
intLumiLabel = "L = 5 ab^{-1}"
ana_tex = "e^{+}e^{-} #rightarrow WbWb #rightarrow "+channel
delphesVersion = "3.4.2"
collider = "FCC-ee"
formats = ["png","pdf"]
plotStatUnc = True
date = date.today() #.fromisoformat()
print("this is what i'm using",date)
eosdir="/eos/user/a/anmehta/www/FCC_top/"

colors = {}
colors["WbWb"] = ROOT.kRed
colors["WW"] = ROOT.kBlue

def if3(cond, iftrue, iffalse):
    return iftrue if cond else iffalse

def plot_signal_background(basedir,sig,bkg,ecm,channel,pf):
    energy = ecm
    print('making plots for',ecm)
    procs = {}
    procs["signal"] = {"WbWb": [sig.split('/events')[0]]}
    procs["backgrounds"] = {"WW": [bkg.split('/events')[0]]}

    inputDir=basedir
    legend = {}
    legend["WbWb"] = "WbWb"
    legend["WW"] = "WW"

    hists = {}
    odir = '{od}/{when}_{ecm}_{FS}_{pf}'.format(od=eosdir,when=date,FS=channel,ecm=ecm,pf=pf)
    
    if not os.path.exists(odir):
        os.makedirs(odir)
        os.system('cp ~anmehta/public/index.php {od}'.format(od=odir))
    outdir=odir

    hists["BDT_score"] = {
        "output": "BDT_score",
        "logy": True,
        "stack": False,
        "rebin": 1,
        "xmin": -1,
        "xmax": -1,
        "ymin": 1,
        "ymax": -1,
        "xtitle": "BDT_score",
        "ytitle": "Events",
    }
    
    for var in uproot.open(sig)['events'].keys():
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
        
        ##amhists[var] = {
        ##am    "output": var+"_AAAyields",
        ##am    "logy": logy,
        ##am    "stack": False,
        ##am    "rebin": 1,
        ##am    "xmin": -1,
        ##am    "xmax": -1,
        ##am    "ymin": 0 if not logy else 1,
        ##am    "ymax": -1,
        ##am    "xtitle": var,
        ##am    "ytitle": "Events",
        ##am}

        
        #hists['BDT_cut_'+var] = {
        #    "output": 'BDT_cut_'+var,
        #    "logy": logy,
        #    "stack": True,
        #    "rebin": 1,
        #    "xmin": -1,
        #    "xmax": -1,
        #    "ymin": 0 if not logy else 1,
        #    "ymax": -1,
        #    "xtitle": var,
        #    "ytitle": "Events",
    #}


        
    

        

for ecm in ecm_scan:
    for channel in ['semihad']: #,'had']:
        for useflav in [True, False]:
            for usebtagged in [True, False]:
                if useflav and usebtagged : continue
                else:
                    base_dir="/eos/cms/store/cmst3/group/dpsww/condor_WbWb/{}/".format(channel)
                    pf="%s"%if3(usebtagged,'withbtaggedJet',if3(useflav,'withflav','noflav'))
                    fname='events_combined.root'
                    sig="{0}/wzp6_ee_WbWb_{1}_ecm{2}/{3}/{4}".format(base_dir,channel,ecm,pf,fname)
                    bkg="{}/p8_ee_WW_ecm{}/{}/{}".format(base_dir,ecm,pf,fname)

                    plot_signal_background(base_dir,sig,bkg,ecm,channel,pf)
