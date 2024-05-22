# list of processes (mandatory)
processList = {
    "wzp6_ee_WbWb_semihad_ecm345": {
        "fraction": 1,
    },
    "p8_ee_WW_ecm345": {
       "fraction": 1,
    },
}

# Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics (mandatory)
#prodTag = "FCCee/winter2023/IDEA/"

# Link to the dictonary that contains all the cross section informations etc... (mandatory)
procDict = "FCCee_procDict_winter2023_IDEA.json"

# Define the input dir (optional)
inputDir    = "./outputs/treemaker/WbWb/semilept_BDT/"

# Optional: output directory, default is local running directory
outputDir = "./outputs/histmaker/WbWb/semilept/"


# optional: ncpus, default is 4, -1 uses all cores available
nCPUS = -1

# scale the histograms with the cross-section and integrated luminosity
doScale = True
intLumi = 5000000  # 5 /ab


# define some binning for various histograms
bins = {
    "phi": (100, -6.3, 6.3),
    "theta": (100, 0, 3.2),
    "p": (100, 0, 200),
    "tagger": (100, 0, 1),
    "dij": {
        "d_12": (100, 0, 100000),
        "d_23": (100, 0, 10000),
        "d_34": (100, 0, 5000),
    }
}


# build_graph function that contains the analysis logic, cuts and histograms (mandatory)
def build_graph(df, dataset):

    column_names = df.GetColumnNames()

    results = []

    df = df.Define("weight", "1.0")
    weightsum = df.Sum("weight")
    df_BDT = df.Filter("BDT_score > 0.5")

    for var in column_names:
        var = str(var)
        if var in ['nlep', 'njets'] or 'jet5' in var or var == 'd_45': continue
        elif var.endswith("_phi"): binning = bins["phi"]
        elif var.endswith("_theta"): binning = bins["theta"]
        elif var.endswith("_p"): binning = bins["p"]
        elif var.endswith("_isB") or var.endswith("_isG") or var.endswith("_isQ") or var.endswith("_isS") or var.endswith("_isC"): binning = bins["tagger"]
        elif var in ['d_12', 'd_23', 'd_34']: binning = bins["dij"][var]
        elif 'BDT_score' in var: binning = bins["tagger"]
        else: 
            print('Default binning for variable {}'.format(var))
            binning = (100, -1, 100)

        results.append(df.Histo1D((var, "", *binning), var))
        results.append(df_BDT.Histo1D(('BDT_cut_'+var, "", *binning), var))


    return results, weightsum