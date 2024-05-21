import ROOT

# global parameters
intLumi = 1
intLumiLabel = "L = 5 ab^{-1}"
ana_tex = "e^{+}e^{-} #rightarrow WbWb #rightarrow #mu + jets"
delphesVersion = "3.4.2"
energy = 240.0
collider = "FCC-ee"
formats = ["png"]

outdir         = './outputs/plots/WbWb/semilept/' 
inputDir       = './outputs/histmaker/WbWb/semilept/' 

plotStatUnc = True

colors = {}
colors["WbWb"] = ROOT.kRed
colors["WW"] = ROOT.kBlue

procs = {}
procs["signal"] = {"WbWb": ["wzp6_ee_WbWb_semihad_ecm345"]}
procs["backgrounds"] = {"WW": ["p8_ee_WW_ecm345"]}

legend = {}
legend["WbWb"] = "WbWb"
legend["WW"] = "WW"

hists = {}

branchList = [
    "lep_p", 'lep_theta', 'lep_phi',
    "jet1_p", "jet2_p", "jet3_p","jet4_p",
    "jet1_theta", "jet2_theta", "jet3_theta","jet4_theta",
    "jet1_phi", "jet2_phi", "jet3_phi","jet4_phi",
    "missing_p", "missing_p_theta", "missing_p_phi",
    "d_12","d_23","d_34",
    "jet1_isB", "jet2_isB", "jet3_isB", "jet4_isB",
    "jet1_isG", "jet2_isG", "jet3_isG", "jet4_isG",
    "jet1_isQ", "jet2_isQ", "jet3_isQ", "jet4_isQ",
    "jet1_isS", "jet2_isS", "jet3_isS", "jet4_isS",
    "jet1_isC", "jet2_isC", "jet3_isC", "jet4_isC",
]


for var in branchList:
    logy = False
    if var.endswith("_isB") or var.endswith("_isG") or var.endswith("_isQ") or var.endswith("_isS") or var.endswith("_isC"):
        logy = True
    if var == "d_12" or var == "d_23" or var == "d_34":
        logy = True
    hists[var] = {
        "output": var,
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

