import os, sys

debug = False
### to be customized by user

## analysis script
script = "../examples/FCCee/weaver/analysis_inference_zh_vvjj_v2.py"
# script = "../examples/FCCee/weaver/analysis_inference.py"

## name/tag of the physics analysis
# analysis_name = "zh_vvss_test"

analysis_name = "zh_vvjj_var"

## run nev_per_job = -1 to run on all event in input root files
# queue = "microcentury"
queue = "testmatch"
queue = "nextweek"

nev_per_job = 100000

## list of samples to run on training jets
samples = [
    "wzp6_ee_nunuH_Hbb_ecm240",
    "wzp6_ee_nunuH_Hcc_ecm240",
    "wzp6_ee_nunuH_Hgg_ecm240",
    "wzp6_ee_nunuH_Hss_ecm240",
    "wzp6_ee_nunuH_Hqq_ecm240",
    # "wzp6_ee_nunuH_Htautau_ecm240",
    # "p8_ee_ZH_Znunu_Hbb_ecm240",
    # "p8_ee_ZH_Znunu_Hcc_ecm240",
    # "p8_ee_ZH_Znunu_Hgg_ecm240",
    # "p8_ee_ZH_Znunu_Hss_ecm240",
    # "p8_ee_WW_ecm240",
    # "p8_ee_ZZ_ecm240",
    # "p8_ee_Zqq_ecm240",
]

"""
samples = [
    "wzp6_ee_nunuH_Huu_ecm240",
    "wzp6_ee_nunuH_Hdd_ecm240",
    "p8_ee_ZH_Znunu_Huu_ecm240",
    "p8_ee_ZH_Znunu_Hdd_ecm240",
]
"""


## list of samples to run on
samples = [
    # "wzp6_ee_ZnunuHnonhad_ecm240",
    "wzp6_ee_nunuH_Hbb_ecm240",
    "wzp6_ee_nunuH_Hcc_ecm240",
    "wzp6_ee_nunuH_Hgg_ecm240",
    "wzp6_ee_nunuH_Hss_ecm240",
    "wzp6_ee_nunuH_Htautau_ecm240",
    "wzp6_ee_nunuH_HWW_ecm240",
    "wzp6_ee_nunuH_HZZ_ecm240",
    "wzp6_ee_qqH_ecm240",
    # "p8_ee_ZH_Znunu_Hbb_ecm240",
    # "p8_ee_ZH_Znunu_Hcc_ecm240",
    # "p8_ee_ZH_Znunu_Hgg_ecm240",
    # "p8_ee_ZH_Znunu_Hss_ecm240",
    # "p8_ee_ZH_Znunu_Htautau_ecm240",
    "p8_ee_WW_ecm240",
    "p8_ee_ZZ_ecm240",
    "p8_ee_Zqq_ecm240",
]

# indir = "/eos/experiment/fcc/ee/generation/DelphesStandalone/Edm4Hep/pre_winter2023_tests_v2/"

indir = "/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/IDEA/"
outdir = "/eos/experiment/fcc/ee/analyses/case-studies/higgs/flat_trees/{}/".format(analysis_name)

# outdir = "/eos/experiment/fcc/ee/jet_flavour_tagging/winter2023/wc_pt_13_01_2022/"

### run condor jobs
os.system("rm -rf std/*")
for s in samples:
    cmd = "python submitAnalysisJobs.py --indir {}/{} ".format(indir, s)
    cmd += "--outdir {}/{} ".format(outdir, s)
    cmd += "--queue {} --script {} --nev {} ".format(queue, script, nev_per_job)
    if debug:
        cmd += "--dry"
    print(cmd)
    #os.system(cmd)
