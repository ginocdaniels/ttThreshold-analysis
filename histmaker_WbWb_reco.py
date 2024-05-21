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
inputDir    = "./outputs/treemaker/WbWb/semilept/"

# Optional: output directory, default is local running directory
outputDir = "./outputs/histmaker/WbWb/semilept/"


# optional: ncpus, default is 4, -1 uses all cores available
nCPUS = -1

# scale the histograms with the cross-section and integrated luminosity
doScale = True
intLumi = 5000000  # 5 /ab


# define some binning for various histograms
bins_phi = (100,-6.3,6.3)
bins_theta = (100,0,3.2)
bins_p = (100,0,200)
bins_tagger = (100,0,1)
bins_dij = {
    "d_12": (100,0,100000),
    "d_23": (100,0,10000),
    "d_34": (100,0,5000),
}


# build_graph function that contains the analysis logic, cuts and histograms (mandatory)
def build_graph(df, dataset):

    column_names = df.GetColumnNames()

    results = []

    df = df.Define("weight", "1.0")
    weightsum = df.Sum("weight")

    for var in column_names:
        var = str(var)
        if var.endswith("_phi"):
            results.append(df.Histo1D((var, "", *bins_phi), var))
        elif var.endswith("_theta"):
            results.append(df.Histo1D((var, "", *bins_theta),var))
        elif var.endswith("_p"):
            results.append(df.Histo1D((var, "", *bins_p),var))
        elif var in ['nlep', 'njets'] or 'jet5' in var or var == 'd_45':
            pass
        elif var.endswith("_isB") or var.endswith("_isG") or var.endswith("_isQ") or var.endswith("_isS") or var.endswith("_isC"):
            results.append(df.Histo1D((var, "", *bins_tagger),var))
        else:
            results.append(df.Histo1D((var, "", *bins_dij[var]),var))

    return results, weightsum