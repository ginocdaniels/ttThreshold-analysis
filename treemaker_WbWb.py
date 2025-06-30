import os, copy
import urllib
# list of processes
all_processes = {
    #  "p8_ee_ZZ_ecm365":{ "fraction": 1,},
#    "p8_ee_ZZ_ecm345":{ "fraction": 1,},
#    "p8_ee_ZZ_ecm340":{ "fraction": 1,},
#    "wzp6_ee_qq_PSdown_ecm340" :{ "fraction": 1,},
#    "wzp6_ee_qq_PSup_ecm345":{ "fractsion": 1,},
#    "wzp6_ee_qq_PSdown_ecm345":{ "fraction": 1,},
#    "wzp6_ee_qq_PSup_ecm365":{ "fraction": 1,},
#    "wzp6_ee_qq_PSdown_ecm365":{ "fraction": 1,},
#    "wzp6_ee_qq_PSup_ecm340":{ "fraction": 1,},

    # "p8_ee_Zbb_ecm91":{ "fraction": 1,},
    # "p8_ee_Zcc_ecm91":{ "fraction": 1,},
    # "p8_ee_Zss_ecm91":{ "fraction": 1,},
    # "p8_ee_Zud_ecm91":{ "fraction": 1,},

    # "wzp6_ee_nunuH_Hbb_ecm365":{ "fraction": 1,},

#    "wzp6_ee_WWZ_Zbb_ecm340": {
#        "fraction": 1,
#     },
#    "wzp6_ee_WWZ_Zbb_ecm345": {
#        "fraction": 1,
#     },
#    "wzp6_ee_WWZ_Zbb_ecm365": {
#        "fraction": 1,
#     },

#     "wzp6_ee_WbWb_ecm340": {
#         "fraction": 1,
#     },
#   "wzp6_ee_WbWb_ecm345": {
#       "fraction": 1,
#   },
#    "wzp6_ee_WbWb_ecm350": {
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_ecm355": {
#        "fraction": 1,
#    },
#
   "wzp6_ee_WbWb_ecm365": {
       "fraction": 1,
   },
    # "p8_ee_WW_ecm345": {
    #     "fraction": 1,
    # },
#    "p8_ee_WW_ecm365": {
#         "fraction": 1,
#    },    
#    "p8_ee_WW_ecm350": {
#       "fraction": 1,
#    },
#    "p8_ee_WW_ecm340": {
#       "fraction": 1,
#    },
#     "p8_ee_WW_ecm355": {
#        "fraction": 1,
#     },
#
#    "wzp6_ee_WbWb_PSup_ecm345":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_PSdown_ecm340":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_PSdown_ecm345":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_PSup_ecm365":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_PSdown_ecm365":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_PSup_ecm340":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_mtop171p5_ecm345":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_mtop171p5_ecm340":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_mtop173p5_ecm345":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_mtop171p5_ecm365":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_mtop173p5_ecm340":{
#        "fraction": 1,
#    },
#    "wzp6_ee_WbWb_mtop173p5_ecm365":{
#        "fraction": 1,
#    },
#    "wzp6_ee_qq_ecm365":{
#       "fraction": 1,
#    },    
#    "wzp6_ee_qq_ecm345": {
#       "fraction": 1,
#    },
#    "wzp6_ee_qq_ecm340": {
#        "fraction": 1,
#    },
#
#
###FOR foll WW background samples with PS variations xsec values are wrong in the database!! 
#   "p8_ee_WW_PSdown_ecm340":{ "fraction": 1,},
#   "p8_ee_WW_PSup_ecm340":{ "fraction": 1,},
#   "p8_ee_WW_PSdown_ecm345":{ "fraction": 1,},
#   "p8_ee_WW_PSup_ecm345":{ "fraction": 1,},
#   "p8_ee_WW_PSdown_ecm365":{ "fraction": 1,},
#   "p8_ee_WW_PSup_ecm365":{ "fraction": 1,},
    
###### following samples we don't use
##am     "wzp6_ee_WbWb_semihad_ecm345": {
##am         "fraction": 1,
##am     },
##am     "wzp6_ee_WbWb_had_ecm345": {
##am         "fraction": 1,
##am     },
##am    "wzp6_ee_WbWb_semihad_ecm350": {
##am       "fraction": 1,
##am    },
##am    "wzp6_ee_WbWb_had_ecm350": {
##am       "fraction": 1,
##am    },
##am    "wzp6_ee_WbWb_semihad_ecm355": {
##am        "fraction": 1,
##am    },
##am    "wzp6_ee_WbWb_had_ecm355": {
##am        "fraction": 1,
##am    },
##am    "wzp6_ee_WbWb_semihad_ecm340": {
##am        "fraction": 1,
##am    },
##am    "wzp6_ee_WbWb_had_ecm340": {
##am        "fraction": 1,
##am    },
##am    "wzp6_ee_WbWb_lep_ecm340": {
##am     "fraction": 1,
##am     },
##am    "wzp6_ee_WbWb_lep_ecm345": {
##am             "fraction": 1,
##am     },
##am    "wzp6_ee_WbWb_lep_ecm350": {
##am     "fraction": 1,
##am     },
##am    "wzp6_ee_WbWb_lep_ecm355": {
##am             "fraction": 1,
##am     },
##am    "wzp6_ee_WbWb_lep_ecm365": {
##am         "fraction": 1,
##am     },
##am    "wzp6_ee_WbWb_semihad_ecm365": {
##am        "fraction": 1,
##am     },
##am    "wzp6_ee_WbWb_had_ecm365": {
##am         "fraction": 1,
##am    },

##     "wzp6_ee_WbWb_had_ecm345": {
##         "fraction": 1,
##     },
##    "wzp6_ee_WbWb_semihad_ecm350": {
##       "fraction": 1,
##    },
##    "wzp6_ee_WbWb_had_ecm350": {
##       "fraction": 1,
##    },
##    "wzp6_ee_WbWb_semihad_ecm355": {
##        "fraction": 1,
##    },
##    "wzp6_ee_WbWb_had_ecm355": {
##        "fraction": 1,
##    },
##    "wzp6_ee_WbWb_semihad_ecm340": {
##        "fraction": 1,
##    },
##    "wzp6_ee_WbWb_had_ecm340": {
##        "fraction": 1,
##    },
##
##    "wzp6_ee_WbWb_lep_ecm340": {
##     "fraction": 1,
##     },
##    "wzp6_ee_WbWb_lep_ecm345": {
##             "fraction": 1,
##     },
##    "wzp6_ee_WbWb_lep_ecm350": {
##     "fraction": 1,
##     },
##    "wzp6_ee_WbWb_lep_ecm355": {
##             "fraction": 1,
##     },
    #"wzp6_ee_WbWb_lep_ecm365": {
    #     "fraction": 1,
    # },
    #"wzp6_ee_WbWb_semihad_ecm365": {
    #    "fraction": 1,
    # },
    #"wzp6_ee_WbWb_had_ecm365": {
    #     "fraction": 1,
    #},
    #"wzp6_ee_WbWb_semihad_mtop173p5_ecm365": {
    #     "fraction": 1,
    #},
    #
    #"wzp6_ee_WbWb_semihad_mtop171p5_ecm365": {
    #     "fraction": 1,
    #},


    
}


available_ecm = ['340','345', '350', '355','365', "91"]
ncpus=-1
hadronic  = False
#semihad  = False
#lep      = False
ecm       = 365
print(ecm)

saveExclJets = False

if not str(ecm) in available_ecm:
    raise ValueError("ecm value not in available_ecm")

channel = "CHANNELNAMEHERE"

if  channel not in ["lep","semihad","had"]:
    print("using defa channel settings")
    channel="semihad"
print(channel)    

processList={key: value for key, value in all_processes.items() if str(ecm) in available_ecm and str(ecm) in key } # (True if str('p8_ee_WW_ecm'+ecm) in key else str('wzp6_ee_WbWb_ecm'+ecm) in key)}  

print(processList)
# Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics (mandatory)
prodTag     = "FCCee/winter2023/IDEA/"

#Optional: output directory, default is local running directoryp
outputDir   = "/eos/user/g/gidaniel/outputs/treemaker/WbWb/{}test".format(channel)


# additional/costom C++ functions, defined in header files (optional)
includePaths = ["examples/functions.h", "examples/truth_matching.h", "examples/MCParticleUtils.h","examples/test_funcs.h"]

## latest particle transformer model, trained on 9M jets in winter2023 samples
model_name = "fccee_flavtagging_edm4hep_wc" #"fccee_flavtagging_edm4hep_wc_v1"

## model files locally stored on /eos
eos_dir ="/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/IDEA/"
model_dir = (
    "/eos/experiment/fcc/ee/jet_flavour_tagging/winter2023/wc_pt_7classes_12_04_2023/"    # "/eos/experiment/fcc/ee/jet_flavour_tagging/winter2023/wc_pt_13_25_2022/"
)
local_preproc = "{}/{}.json".format(model_dir, model_name)
local_model = "{}/{}.onnx".format(model_dir, model_name)

url_model_dir = "https://fccsw.web.cern.ch/fccsw/testsamples/jet_flavour_tagging/winter2023/wc_pt_13_25_2022/"
url_preproc = "{}/{}.json".format(url_model_dir, model_name)
url_model = "{}/{}.onnx".format(url_model_dir, model_name)

## get local file, else download from url
def get_file_path(url, filename):
    if os.path.exists(filename):
        return os.path.abspath(filename)
    else:
        urllib.request.urlretrieve(url, os.path.basename(url))
        return os.path.basename(url)

def get_files(eos_dir, proc):
    files=[]
    basepath=os.path.join(eos_dir,proc)
    if os.path.exists(basepath):
        files =  [os.path.join(basepath,x) for x in os.listdir(basepath) if os.path.isfile(os.path.join(basepath, x)) ]
    return files

weaver_preproc = get_file_path(url_preproc, local_preproc)
weaver_model = get_file_path(url_model, local_model)

#inputDir = eos_dir

from addons.ONNXRuntime.jetFlavourHelper import JetFlavourHelper
from addons.FastJet.jetClusteringHelper import (
    ExclusiveJetClusteringHelper,
    InclusiveJetClusteringHelper,
)

jetFlavourHelper = None
jetFlavourHelper_R5 = None
jetClusteringHelper = None
jetClusteringHelper_R5 = None


all_branches = [
    "njets_R5","jets_R5_pflavor", "jets_R5_p_unfiltered_size","jets_R5_p_size", "jets_R5_theta_unfiltered",
      "bjets_R5_true","ljets_R5_true","remaining_muons_deltaR","remaining_electrons_deltaR","jets_R5_tlv","jets_R5_p","jets_R5_theta",
      "jet_mother_pdg_id", "jet_daughter_stuff", "electrons_iso", "muons_iso", "electrons_sel","muons_all_p", "electrons_all_p","bjets_R5_true_theta",
      "jets_R5_isC","jets_R5_isU","jets_R5_isD","jets_R5_isB","jets_R5_isG","jets_R5_isS","jets_R5_isTAU","cjets_R5_true_theta","ljets_R5_true_theta","gjets_R5_true_theta",
      "all_thetas_merged", 
      "jets_R5_isB_true_b", "jets_R5_isC_true_b", "jets_R5_isU_true_b", "jets_R5_isD_true_b", "jets_R5_isG_true_b", "jets_R5_isS_true_b", "jets_R5_isTau_true_b",
      "jets_R5_isC_true_c", "jets_R5_isB_true_c", "jets_R5_isU_true_c", "jets_R5_isD_true_c", "jets_R5_isG_true_c", "jets_R5_isS_true_c", "jets_R5_isTau_true_c",
      "nbjets_R5_true", "ncjets_R5_true","nljets_R5_true","ngjets_R5_true","jets_R5_eta","jets_R5_phi",
      "bjets_R5_true_pt", "bjets_R5_true_m", "jets_R5_pt", "jets_R5_m", "jets_R5_e"
     
]
  
# all_branches = [
#     "njets_R5",  "jet1_R5_p", "jet2_R5_p", "jet3_R5_p", "jet4_R5_p", "jet5_R5_p", "jet6_R5_p",
#     "jet1_R5_theta",  "jet2_R5_theta",  "jet3_R5_theta",  "jet4_R5_theta", "jet5_R5_theta", "jet6_R5_theta",
#     "jet1_R5_pflavor", "jet2_R5_pflavor", "jet3_R5_pflavor", "jet4_R5_pflavor", "jet5_R5_pflavor","jet6_R5_pflavor",
#     "jet1_R5_isG","jet2_R5_isG","jet3_R5_isG","jet4_R5_isG","jet5_R5_isG","jet6_R5_isG",                
#     "jet1_R5_isU","jet2_R5_isU","jet3_R5_isU","jet4_R5_isU","jet5_R5_isU","jet6_R5_isU",                
#     "jet1_R5_isB","jet2_R5_isB","jet3_R5_isB","jet4_R5_isB","jet5_R5_isB","jet6_R5_isB",                
#     "jet1_R5_isS","jet2_R5_isS","jet3_R5_isS","jet4_R5_isS","jet5_R5_isS","jet6_R5_isS",                
#     "jet1_R5_isC","jet2_R5_isC","jet3_R5_isC","jet4_R5_isC","jet5_R5_isC","jet6_R5_isC",                
#     "jet1_R5_isD","jet2_R5_isD","jet3_R5_isD","jet4_R5_isD","jet5_R5_isD","jet6_R5_isD", "jets_R5_pflavor", "jets_R5_p_unfiltered_size","jets_R5_p_size", "jets_R5_theta_unfiltered",
#     "jet1_R5_isTAU","jet2_R5_isTAU","jet3_R5_isTAU","jet4_R5_isTAU","jet5_R5_isTAU","jet6_R5_isTAU", 
#       "bjets_R5_true","ljets_R5_true","remaining_muons_deltaR","remaining_electrons_deltaR","jets_R5_tlv","jets_R5_p","jets_R5_theta",
#       "jet_mother_pdg_id", "jet_daughter_stuff", "electrons_iso", "muons_iso", "electrons_sel","muons_all_p", "electrons_all_p","bjets_R5_true_theta",
#       "jets_R5_isC","jets_R5_isU","jets_R5_isD","jets_R5_isB","jets_R5_isG","jets_R5_isS","jets_R5_isTAU","cjets_R5_true_theta","ljets_R5_true_theta","gjets_R5_true_theta",
#       "all_thetas_merged", 
#       "jets_R5_isB_true_b", "jets_R5_isC_true_b", "jets_R5_isU_true_b", "jets_R5_isD_true_b", "jets_R5_isG_true_b", "jets_R5_isS_true_b", "jets_R5_isTau_true_b",
#       "jets_R5_isC_true_c", "jets_R5_isB_true_c", "jets_R5_isU_true_c", "jets_R5_isD_true_c", "jets_R5_isG_true_c", "jets_R5_isS_true_c", "jets_R5_isTau_true_c",
      
#       "nbjets_R5_true", "ncjets_R5_true","nljets_R5_true","ngjets_R5_true",
     
# ]





if saveExclJets: all_branches+=[ "njets", "jet1_p", "jet2_p", "jet3_p","jet4_p","jet5_p","jet6_p",
    "jet1_theta", "jet2_theta", "jet3_theta","jet4_theta","jet5_theta","jet6_theta",
    "jet1_phi", "jet2_phi", "jet3_phi","jet4_phi","jet5_phi","jet6_phi",
    "jet1_isTau", "jet2_isTau", "jet3_isTau","jet4_isTau","jet5_isTau","jet6_isTau",
    "nbjets_WPp5", "nbjets_WPp8",
    "nbjets_WPp85", "nbjets_WPp9",
    "d_12","d_23","d_34","d_45","d_56",
    "jet1_isB", "jet2_isB", "jet3_isB", "jet4_isB", "jet5_isB", "jet6_isB",
    "jet1_isG", "jet2_isG", "jet3_isG", "jet4_isG", "jet5_isG", "jet6_isG",
    "jet1_isQ", "jet2_isQ", "jet3_isQ", "jet4_isQ", "jet5_isQ", "jet6_isQ",
    "jet1_isS", "jet2_isS", "jet3_isS", "jet4_isS", "jet5_isS", "jet6_isS",
    "jet1_isC", "jet2_isC", "jet3_isC", "jet4_isC", "jet5_isC", "jet6_isC",
    "nbjets_R5_WPp5", "nbjets_R5_WPp8", "nbjets_R5_WPp85", "nbjets_R5_WPp9"]
#print('saving these branches',all_branches)
# Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis:

    # __________________________________________________________
    # Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):

        # __________________________________________________________
        # Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2

        # define some aliases to be used later on
        df = df.Alias("Muon0", "Muon#0.index")
        df = df.Alias("Electron0","Electron#0.index")
        
        
        ## Find fraction of ones taht are cut make the d value optimized and find the ineefciecy add the prompt nonprompt together and find the fraction of erach that u ose with that cut and try to optimize this
        # normalized them as well as well so u can add them together because otherwize we dont have same number of events and it doesnt work for the bins 
        #Then we can send in condor jobs do cd/condor 
        # all interesting proceses wz bb qq. files will be in eos/user/g/gidaniel
        # to send in jobs do python3 send_all.py condor_q to check whats going on condor rm gidaniel to remove everythign
        # ls std/condor.1231753 does something 
        df = df.Alias("Particle0",           "Particle#0.index");    
        df = df.Alias("Particle1",           "Particle#1.index");    
        df = df.Alias("MCParticles",         "Particle");     

        df = df.Alias("MCRecoAssociations0", "MCRecoAssociations#0.index"); 
        df = df.Alias("MCRecoAssociations1", "MCRecoAssociations#1.index");
       


 

    
    # plot the jet multiplicity as function of the d_iso values so we can see how many jets we have at each d iso value
    # plot jet multiplicity as function of efficiencies so how many jets we reconstruct at each efficiency
    # R5 clustering algorithm
       
        
        df = df.Define(
            "muons_all",
            "FCCAnalyses::ReconstructedParticle::get(Muon0, ReconstructedParticles)",
        )
        df = df.Define(
            "electrons_all",
            "FCCAnalyses::ReconstructedParticle::get(Electron0, ReconstructedParticles)",
        )
        df=df.Define("muons_all_p", "FCCAnalyses::ReconstructedParticle::get_p(muons_all)")
        df=df.Define("electrons_all_p", "FCCAnalyses::ReconstructedParticle::get_p(electrons_all)")
        df=df.Define("all_thetas_merged", "FCCAnalyses::MCParticle::get_theta(MCParticles)")
        
       
        df=df.Define("all_reco_leptons_merged", "FCCAnalyses::ReconstructedParticle::merge(muons_all, electrons_all)")
        df=df.Define("all_reco_leptons_merged_tlv", "FCCAnalyses::ReconstructedParticle::get_tlv(all_reco_leptons_merged)")
        

        #Test with taus
        # df=df.Define("all_status2_taus", "FCCAnalyses::MCParticle::sel_genleps(15,0, true)(MCParticles)")
        # df=df.Define("all_status2_taus_origins", "FCCAnalyses::MCParticle::get_leptons_origin(all_status2_taus,MCParticles,Particle0)")
        # df=df.Define("all_status2_taus_fromWs", "FCCAnalyses::MCParticle::sel_genlepsfromW()(all_status2_taus,all_status2_taus_origins)")
        # df=df.Define("all_status2_taus_fromWs_daughter1", "FCCAnalyses::myUtils::get_MCDaughter1(all_status2_taus_fromWs, Particle0)")
        # df=df.Define("Taus_pre_pdgId", "FCCAnalyses::MCParticle::get_pdg(all_status2_taus_fromWs)")
     
        # df = df.Define(
        #     "all_status2_taus_fromWs_e_mu_daughters",
        #     "FCCAnalyses::TestFuncs::get_MCElectronMuonDaughters(all_status2_taus_fromWs, MCParticles, DaughterIndices)"
        # )
        # # df=df.Define("all_status2_taus_fromWs_e_mu_daughters_pdgId", "FCCAnalyses::MCParticle::get_pdg(all_status2_taus_fromWs_e_mu_daughters)")


        # df = df.Define(
        #     "reco_leptons_from_taus_fromWs",
        #     "FCCAnalyses::ReconstructedParticle2MC::selRP_matched_to_list(all_status2_taus_fromWs_e_mu_daughters, MCRecoAssociations0, MCRecoAssociations1, all_reco_leptons_merged, MCParticles)"
        # )


        # df = df.Define(
        #     "reco_leptons_from_taus_fromWs_tlv",
        #     "FCCAnalyses::ReconstructedParticle::get_tlv(reco_leptons_from_taus_fromWs)"
        # )

        # df= df.Define("status1parts",           "FCCAnalyses::MCParticle::sel_genStatus(1)(MCParticles)")
        # df= df.Define("status1",       "FCCAnalyses::MCParticle::sel_genleps(13,11, true)(status1parts)")
        # df = df.Define("nstatus1",      "FCCAnalyses::MCParticle::get_n(status1)")
        # df=df.Define("W_bosons", "FCCAnalyses::MCParticle::sel_pdgID(24, true)(MCParticles)")
        # df=df.Define("W_bosons_pdgId", "FCCAnalyses::MCParticle::get_pdg(W_bosons)")
       


        # df=df.Define("W_boson_origin", "FCCAnalyses::TruthMatching::get_particles_origin(W_bosons,MCParticles,Particle0)")
       
        

        # ## MC Leps from W info  with right reco indicies and same size as mc particle list but with 0 or -1 in other spots i can use this get leptons orgin func with the reco indices and then only be selecting from reco particles 
        # df=df.Define("status1_from_94_origins", "FCCAnalyses::MCParticle::get_leptons_origin(status1,MCParticles,Particle0)")
        # df= df.Define("status1_from_94", "status1[abs(status1_from_94_origins) == 94]") #94 is the W boson pdgId
        # df=df.Define("momentum_from_94", "FCCAnalyses::MCParticle::get_p(status1_from_94)")


        # df= df.Define("status1_mother_pdgId_prompt", "FCCAnalyses::MCParticle::get_leptons_origin(status1,MCParticles,Particle0)")
        # df=df.Define("status1_fromW", "status1[abs(status1_mother_pdgId_prompt) == 24 || abs(status1_mother_pdgId_prompt) == 94]")
        # df = df.Define("nstatus1_fromW",      "FCCAnalyses::MCParticle::get_n(status1_fromW)")
        # df = df.Define("size_status1_fromW", "status1_fromW.size()")
     
        # df = df.Define("status1_p_W",      "FCCAnalyses::MCParticle::get_p(status1_fromW)")
        # df =df.Define("status1_fromW_vertex_xyz", "FCCAnalyses::MCParticle::get_vertex(status1_fromW)")
        # df= df.Define("tlv_fromW", "FCCAnalyses::MCParticle::get_tlv(status1_fromW)")
        # df = df.Define("status1_fromW_z0", "FCCAnalyses::TruthMatching::compute_z0(status1_fromW_vertex_xyz, tlv_fromW)")
        # df=df.Define("status1_fromW_z0_matched_indices", "FCCAnalyses::TruthMatching::match_leptons_with_z0(tlv_fromW, all_reco_leptons_merged_tlv,status1_fromW_vertex_xyz,0.01 )")
        
        # df=df.Define("status1_fromW_z0_matched_indices_z0", "status1_fromW_z0_matched_indices.second")
        # df=df.Define("status1_fromW_z0_matched_indices_z0_matched_indices", "status1_fromW_z0_matched_indices.first")
        
        # df = df.Define("matched_fromW_leptons_and_z0",
        #        "ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> particles;"
        #        "ROOT::VecOps::RVec<float> z0_values;"
        #        "for (size_t i = 0; i < status1_fromW_z0_matched_indices_z0_matched_indices.size(); ++i) {"
        #        "  int idx = status1_fromW_z0_matched_indices_z0_matched_indices[i];"
        #        "  if (idx >= 0) {"
        #        "    particles.push_back(all_reco_leptons_merged[idx]);"
        #        "    z0_values.push_back(status1_fromW_z0_matched_indices_z0[i]);"
        #        "  }"
        #        "} return std::make_pair(particles, z0_values);")
        
        # df = df.Define("matched_fromW_leptons_and_z0_p_cut", 
        #                "auto particles = FCCAnalyses::ReconstructedParticle::sel_p(12)(matched_fromW_leptons_and_z0.first); "
        #                "ROOT::VecOps::RVec<float> z0_filtered; "
        #                "for (size_t i = 0; i < particles.size(); ++i) { "
        #                "    z0_filtered.push_back(matched_fromW_leptons_and_z0.second[i]); "
        #                "} "
        #                "return std::make_pair(particles, z0_filtered);")

        # df = df.Define("matched_fromW_leptons_and_z0_p_cut_z0", "matched_fromW_leptons_and_z0_p_cut.second")
        # df = df.Define("matched_fromW_leptons_and_z0_p_cut_indices", "matched_fromW_leptons_and_z0_p_cut.first")
        # df = df.Define("D_Iso_Values_Prompt_and_z0_pair", 
        #                "auto iso_values = FCCAnalyses::ZHfunctions::coneIsolation(0.01, .3)(matched_fromW_leptons_and_z0_p_cut_indices, ReconstructedParticles);"
        #                "ROOT::VecOps::RVec<std::pair<float, float>> result;"
        #                "for (size_t i = 0; i < iso_values.size(); ++i) {"
        #                "    result.push_back(std::make_pair(iso_values[i], matched_fromW_leptons_and_z0_p_cut_z0[i]));"
        #                "}"
        #                "return result;")
        # df = df.Define("D_Iso_Values_Prompt_z0", "ROOT::VecOps::RVec<float> iso_vals; for (const auto& pair : D_Iso_Values_Prompt_and_z0_pair) { iso_vals.push_back(pair.first); } return iso_vals;")
        # df = df.Define("z0_Values_Prompt", "ROOT::VecOps::RVec<float> z0_vals; for (const auto& pair : D_Iso_Values_Prompt_and_z0_pair) { z0_vals.push_back(pair.second); } return z0_vals;")
        # Explanation of why this works:
        # The code defines a paired vector 'D_Iso_Values_Prompt_and_z0_pair' that stores both the D isolation values (iso_values) and the corresponding z0 values (matched_fromW_leptons_and_z0_p_cut_z0) for matched leptons from W bosons.
        # We use 'FCCAnalyses::ZHfunctions::coneIsolation' to compute the isolation values for the selected leptons with a cone size of 0.3 and a minimum deltaR of 0.01.
        # Then, two separate vectors are created: 'D_Iso_Values_Prompt' extracts just the isolation values (first element of each pair), and 'z0_Values_Prompt' extracts just the z0 values (second element of each pair).
        # This works because the paired structure ensures that the isolation and z0 values remain associated with the same lepton during the pairing process, and the subsequent extraction preserves this order in the individual vectors.



        # df = df.Define("status1_theta",  "FCCAnalyses::MCParticle::get_theta(status1_fromW)")
        # df = df.Define("status1_phi",    "FCCAnalyses::MCParticle::get_phi(status1_fromW)")
        # df = df.Define("status1_charge", "FCCAnalyses::MCParticle::get_charge(status1_fromW)")
        # df = df.Define("status1_pdgId",  "FCCAnalyses::MCParticle::get_pdg(status1_fromW)")
        # ### Start Of NonPrompt Leptons
        # df=df.Define("status1_mother_pdgId_non_prompt", "FCCAnalyses::MCParticle::get_leptons_origin(status1,MCParticles,Particle0)")
        # df = df.Define("status1_from_b", "status1[abs(status1_mother_pdgId_non_prompt) !=15 && abs(status1_mother_pdgId_non_prompt) != 24 && abs(status1_mother_pdgId_non_prompt) != 94]") #15 is the tau lepton pdgId, 24 is the W boson pdgId, 94 is the W boson pdgId
        # df = df.Define("nstatus1_from_b", "FCCAnalyses::MCParticle::get_n(status1_from_b)")
        # df=df.Define("size_status1_from_b", "status1_from_b.size()")
        # df= df.Define("status1_from_b_p", "FCCAnalyses::MCParticle::get_p(status1_from_b)")
        # df=df.Define("status1_from_b_vertex_xyz", "FCCAnalyses::MCParticle::get_vertex(status1_from_b)")
        # df=df.Define("tlv_from_b", "FCCAnalyses::MCParticle::get_tlv(status1_from_b)")



        # df= df.Define("status1_from_b_z0", "FCCAnalyses::TruthMatching::compute_z0(status1_from_b_vertex_xyz, tlv_from_b)")

        # df=df.Define("status1_from_b_z0_matched_indices", "FCCAnalyses::TruthMatching::match_leptons_with_z0(tlv_from_b, all_reco_leptons_merged_tlv,status1_from_b_vertex_xyz,0.01 )")
        # df=df.Define("status1_from_b_z0_matched_indices_z0", "status1_from_b_z0_matched_indices.second")
        # df=df.Define("status1_from_b_z0_matched_indices_z0_matched_indices", "status1_from_b_z0_matched_indices.first")

        # df = df.Define("matched_fromb_leptons_and_z0",
        #        "ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> particles;"
        #        "ROOT::VecOps::RVec<float> z0_values;"
        #        "for (size_t i = 0; i < status1_from_b_z0_matched_indices_z0_matched_indices.size(); ++i) {"
        #        "  int idx = status1_from_b_z0_matched_indices_z0_matched_indices[i];"
        #        "  if (idx >= 0) {"
        #        "    particles.push_back(all_reco_leptons_merged[idx]);"
        #        "    z0_values.push_back(status1_from_b_z0_matched_indices_z0[i]);"
        #        "  }"
        #        "} return std::make_pair(particles, z0_values);")
        # df =df.Define("matched_fromb_leptons_and_z0_check", "matched_fromb_leptons_and_z0.first")
        
        
        # df = df.Define("matched_fromb_leptons_and_z0_p_cut", 
        #                "auto particles = FCCAnalyses::ReconstructedParticle::sel_p(12)(matched_fromb_leptons_and_z0.first); "
        #                "ROOT::VecOps::RVec<float> z0_filtered; "
        #                "for (size_t i = 0; i < particles.size(); ++i) { "
        #                "    z0_filtered.push_back(matched_fromb_leptons_and_z0.second[i]); "
        #                "} "
        #                "return std::make_pair(particles, z0_filtered);")
        # df =df.Define("matched_fromb_leptons_and_z0_check_p", "FCCAnalyses::ReconstructedParticle::get_p(matched_fromb_leptons_and_z0_p_cut.first)")
        

        # df = df.Define("matched_fromb_leptons_and_z0_p_cut_z0", "matched_fromb_leptons_and_z0_p_cut.second")
        # df = df.Define("matched_fromb_leptons_and_z0_p_cut_indices", "matched_fromb_leptons_and_z0_p_cut.first")
        # df = df.Define("D_Iso_Values_NonPrompt_and_z0_pair", 
        #                "auto iso_values = FCCAnalyses::ZHfunctions::coneIsolation(0.01, .3)(matched_fromb_leptons_and_z0_p_cut_indices, ReconstructedParticles);"
        #                "ROOT::VecOps::RVec<std::pair<float, float>> result;"
        #                "for (size_t i = 0; i < iso_values.size(); ++i) {"
        #                "    result.push_back(std::make_pair(iso_values[i], matched_fromb_leptons_and_z0_p_cut_z0[i]));"
        #                "}"
        #                "return result;")
        # df = df.Define("D_Iso_Values_NonPrompt_z0", "ROOT::VecOps::RVec<float> iso_vals; for (const auto& pair : D_Iso_Values_NonPrompt_and_z0_pair) { iso_vals.push_back(pair.first); } return iso_vals;")
        # df = df.Define("z0_Values_NonPrompt", "ROOT::VecOps::RVec<float> z0_vals; for (const auto& pair : D_Iso_Values_NonPrompt_and_z0_pair) { z0_vals.push_back(pair.second); } return z0_vals;")





        # df= df.Define("status1_from_b_theta", "FCCAnalyses::MCParticle::get_theta(status1_from_b)")
        # df= df.Define("status1_from_b_phi", "FCCAnalyses::MCParticle::get_phi(status1_from_b)")
        # df= df.Define("status1_from_b_charge", "FCCAnalyses::MCParticle::get_charge(status1_from_b)")
        # df= df.Define("status1_from_b_pdgId", "FCCAnalyses::MCParticle::get_pdg(status1_from_b)")
        # #Truth Matching Prompt
        # df = df.Define("fromW_reco_indices",
        #        "FCCAnalyses::TruthMatching::match_leptons(tlv_fromW, all_reco_leptons_merged_tlv, 0.01)")
        # #Maybe remove the leptons that we truth match idk because it could be double counting with this and so we get an inflated portion with no
        
        # df = df.Define("matched_fromW_leptons",
        #        "ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;"
        #        "for (size_t i = 0; i < fromW_reco_indices.size(); ++i) {"
        #        "  int idx = fromW_reco_indices[i];"
        #        "  if (idx >= 0) result.push_back(all_reco_leptons_merged[idx]);"
        #        "} return result;")
        # # #Truth Matching Non-Prompt
        # df = df.Define("from_b_reco_indices",
        #        "FCCAnalyses::TruthMatching::match_leptons(tlv_from_b, all_reco_leptons_merged_tlv, 0.01)")
        # df = df.Define("matched_from_b_leptons",
        #        "ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;"
        #        "for (size_t i = 0; i < from_b_reco_indices.size(); ++i) {"
        #        "  int idx = from_b_reco_indices[i];"
        #        "  if (idx >= 0) result.push_back(all_reco_leptons_merged[idx]);"
        #        "} return result;")
        # #merge the lists so we can calculate the isolation on all of them
        # df=df.Define("matched_fromW_leptons_p_cut", "FCCAnalyses::ReconstructedParticle::sel_p(12)(matched_fromW_leptons)")
        # df=df.Define("matched_from_b_leptons_p_cut", "FCCAnalyses::ReconstructedParticle::sel_p(12)(matched_from_b_leptons)")
        # df=df.Define("merged_leptons_list_status1", "FCCAnalyses::ReconstructedParticle::merge(matched_fromW_leptons_p_cut, matched_from_b_leptons_p_cut)")
        # df= df.Define("D_Iso_Values_Prompt", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .3)(matched_fromW_leptons_p_cut, ReconstructedParticles)")
        # df= df.Define("D_Iso_Values_nonPrompt", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .3)(matched_from_b_leptons_p_cut, ReconstructedParticles)")
        # df=df.Define("D_Iso_Values_all_status1", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .3)(merged_leptons_list_status1, ReconstructedParticles)")



        
        # # All gen muons collection
        # df = df.Define("status1_from_b_muons", "FCCAnalyses::MCParticle::sel_genleps(13,0, true)(status1_from_b)")
        # df=df.Define("status1_from_b_muons_p", "FCCAnalyses::MCParticle::get_p(status1_from_b_muons)")
        # df = df.Define("status1_from_b_muons_tlv", "FCCAnalyses::MCParticle::get_tlv(status1_from_b_muons)")
        # df = df.Define("reco_leps_status1_from_b_muons_indcies", "FCCAnalyses::TruthMatching::match_leptons(status1_from_b_muons_tlv, all_reco_leptons_merged_tlv, 0.01)")
        # df =df.Define("matched_leps_status1_from_b_muons",  
        #         "ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;"
        #         "for (size_t i = 0; i < reco_leps_status1_from_b_muons_indcies.size(); ++i) {"
        #         "  int idx = reco_leps_status1_from_b_muons_indcies[i];"
        #         "  if (idx >= 0) result.push_back(all_reco_leptons_merged[idx]);"
        #         "} return result;")
        # df = df.Define("status1_fromW_muons", "FCCAnalyses::MCParticle::sel_genleps(13,0, true)(status1_fromW)")
        # df = df.Define("status1_fromW_muons_p", "FCCAnalyses::MCParticle::get_p(status1_fromW_muons)")
        # df = df.Define("status1_fromW_muons_tlv", "FCCAnalyses::MCParticle::get_tlv(status1_fromW_muons)")
        # df = df.Define("reco_leps_status1_fromW_muons_indcies", "FCCAnalyses::TruthMatching::match_leptons(status1_fromW_muons_tlv, all_reco_leptons_merged_tlv, 0.01)")
        # df =df.Define("matched_leps_status1_from_W_muons",  
        #         "ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;"
        #         "for (size_t i = 0; i < reco_leps_status1_fromW_muons_indcies.size(); ++i) {"
        #         "  int idx = reco_leps_status1_fromW_muons_indcies[i];"
        #         "  if (idx >= 0) result.push_back(all_reco_leptons_merged[idx]);"
        #         "} return result;")
        # # All gen electrons collection
        # df = df.Define("status1_from_b_electrons", "FCCAnalyses::MCParticle::sel_genleps(11,0, true)(status1_from_b)")
        # df = df.Define("status1_from_b_electrons_p", "FCCAnalyses::MCParticle::get_p(status1_from_b_electrons)")
        # df = df.Define("status1_from_b_electrons_tlv", "FCCAnalyses::MCParticle::get_tlv(status1_from_b_electrons)")
        # df = df.Define("reco_leps_status1_from_b_electrons_indcies", "FCCAnalyses::TruthMatching::match_leptons(status1_from_b_electrons_tlv, all_reco_leptons_merged_tlv, 0.01)")
        # df =df.Define("matched_leps_status1_from_b_electrons", 
        #         "ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;"
        #         "for (size_t i = 0; i < reco_leps_status1_from_b_electrons_indcies.size(); ++i) {"
        #         "  int idx = reco_leps_status1_from_b_electrons_indcies[i];"
        #         "  if (idx >= 0) result.push_back(all_reco_leptons_merged[idx]);"
        #         "} return result;") 
        
        # df = df.Define("status1_fromW_electrons", "FCCAnalyses::MCParticle::sel_genleps(11,0, true)(status1_fromW)")
        # df = df.Define("status1_fromW_electrons_p", "FCCAnalyses::MCParticle::get_p(status1_fromW_electrons)")
        # df = df.Define("status1_fromW_electrons_tlv", "FCCAnalyses::MCParticle::get_tlv(status1_fromW_electrons)")
        # df = df.Define("reco_leps_status1_fromW_electrons_indcies", "FCCAnalyses::TruthMatching::match_leptons(status1_fromW_electrons_tlv, all_reco_leptons_merged_tlv, 0.01)")
        # df =df.Define("matched_leps_status1_from_W_electrons", 
        #         "ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> result;"
        #         "for (size_t i = 0; i < reco_leps_status1_fromW_electrons_indcies.size(); ++i) {"
        #         "  int idx = reco_leps_status1_fromW_electrons_indcies[i];"
        #         "  if (idx >= 0) result.push_back(all_reco_leptons_merged[idx]);"
        #         "} return result;") 
        # df=df.Define("matched_leps_status1_from_b_muons_p_cut", "FCCAnalyses::ReconstructedParticle::sel_p(12)(matched_leps_status1_from_b_muons)")
        # df=df.Define("matched_leps_status1_from_b_electrons_p_cut", "FCCAnalyses::ReconstructedParticle::sel_p(12)(matched_leps_status1_from_b_electrons)")
        # df=df.Define("matched_leps_status1_from_W_muons_p_cut", "FCCAnalyses::ReconstructedParticle::sel_p(12)(matched_leps_status1_from_W_muons)")
        # df=df.Define("matched_leps_status1_from_W_electrons_p_cut", "FCCAnalyses::ReconstructedParticle::sel_p(12)(matched_leps_status1_from_W_electrons)")
        # ## non prompts e,mu
        # df =df.Define("matched_leps_status1_from_b_muons_p_cut_coneIso_2", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .2)(matched_leps_status1_from_b_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_b_muons_p_cut_coneIso_3", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .3)(matched_leps_status1_from_b_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_b_muons_p_cut_coneIso_4", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .4)(matched_leps_status1_from_b_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_b_muons_p_cut_coneIso_5", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .5)(matched_leps_status1_from_b_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_b_muons_p_cut_coneIso_6", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .6)(matched_leps_status1_from_b_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_b_electrons_p_cut_coneIso_2", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .2)(matched_leps_status1_from_b_electrons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_b_electrons_p_cut_coneIso_3", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .3)(matched_leps_status1_from_b_electrons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_b_electrons_p_cut_coneIso_4", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .4)(matched_leps_status1_from_b_electrons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_b_electrons_p_cut_coneIso_5", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .5)(matched_leps_status1_from_b_electrons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_b_electrons_p_cut_coneIso_6", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .6)(matched_leps_status1_from_b_electrons_p_cut, ReconstructedParticles)")       
        # # Prompts e,mu
        # df =df.Define("matched_leps_status1_from_W_muons_p_cut_coneIso_2", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .2)(matched_leps_status1_from_W_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_W_muons_p_cut_coneIso_3", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .3)(matched_leps_status1_from_W_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_W_muons_p_cut_coneIso_4", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .4)(matched_leps_status1_from_W_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_W_muons_p_cut_coneIso_5", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .5)(matched_leps_status1_from_W_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_W_muons_p_cut_coneIso_6", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .6)(matched_leps_status1_from_W_muons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_W_electrons_p_cut_coneIso_2", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .2)(matched_leps_status1_from_W_electrons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_W_electrons_p_cut_coneIso_3", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .3)(matched_leps_status1_from_W_electrons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_W_electrons_p_cut_coneIso_4", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .4)(matched_leps_status1_from_W_electrons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_W_electrons_p_cut_coneIso_5", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .5)(matched_leps_status1_from_W_electrons_p_cut, ReconstructedParticles)")
        # df =df.Define("matched_leps_status1_from_W_electrons_p_cut_coneIso_6", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .6)(matched_leps_status1_from_W_electrons_p_cut, ReconstructedParticles)")
        #   ## KEEP CHANGING THESE D VALS
        # # adding in cut and return particle data 
        # # df= df.Define("D_Iso_particles_leptons_cut_prompt", "FCCAnalyses::ZHfunctions::sel_iso(0.25)(matched_fromW_leptons_p_cut, D_Iso_Values_Prompt)")
        # # df= df.Define("D_Iso_particles_leptons_cut_nonPrompt", "FCCAnalyses::ZHfunctions::sel_iso(0.25)(matched_from_b_leptons_p_cut, D_Iso_Values_nonPrompt)")
        # # df= df.Define("D_Iso_particles_leptons_cut_all_status1", "FCCAnalyses::ZHfunctions::sel_iso(0.25)(merged_leptons_list_status1, D_Iso_Values_all_status1)")

        # # # number leps post cut 
        # # df= df.Defined_iso_postcut_prompt", "D_Iso_particles_leptons_cut_prompt.size()")
        # # df= df.Defined_iso_postcut_nonPrompt", "D_Iso_particles_leptons_cut_nonPrompt.size()")
        # # df= df.Defined_iso_postcut_all_status1", "D_Iso_particles_leptons_cut_all_status1.size()")
       


        # select leptons with momentum > 12 GeV
        df = df.Define(
            "muons_sel",
            "FCCAnalyses::ReconstructedParticle::sel_p(12)(muons_all)",
        )

        df = df.Define(
            "electrons_sel",
            "FCCAnalyses::ReconstructedParticle::sel_p(12)(electrons_all)",
        )
        
        




      

     




        df=df.Define("muon_size", "muons_sel.size()")
        df=df.Define("electron_size", "electrons_sel.size()")
        df= df.Define("nlep_total", "muon_size + electron_size")
        # df=df.Define("merged_leptons_list", "FCCAnalyses::ReconstructedParticle::merge(muons_sel, electrons_sel)")
        # df=df.Define("merged_leptons_list_coneIso", "FCCAnalyses::ZHfunctions::coneIsolation(0.01, .5)(merged_leptons_list, ReconstructedParticles)")

        # compute the muon isolation and store muons with an isolation cut of 0df = df.20 in a separate column muons_sel_iso
        df = df.Define(
            "muons_iso",
            "FCCAnalyses::ZHfunctions::coneIsolation(0.01, 0.3)(muons_sel, ReconstructedParticles)",
        )
        # compute the electron isolation and store electrons with an isolation cut of 0df = df.20 in a separate column electrons_sel_iso
        df = df.Define(
            "electrons_iso",
            "FCCAnalyses::ZHfunctions::coneIsolation(0.01, 0.3)(electrons_sel, ReconstructedParticles)",
        )



        df = df.Define(
            "muons_sel_iso",
            "FCCAnalyses::ZHfunctions::sel_iso(0.3)(muons_sel, muons_iso)",
        )

        df = df.Define(
            "electrons_sel_iso",
            "FCCAnalyses::ZHfunctions::sel_iso(0.3)(electrons_sel, electrons_iso)",
        )
        # df=df.Define("E_RP_TRK_Z0_pcut_iso_cut", "ReconstructedParticle2Track::getRP2TRK_Z0(electrons_sel_iso, EFlowTrack_1)")
        # df=df.Define("Mu_RP_TRK_Z0_pcut_iso_cut", "ReconstructedParticle2Track::getRP2TRK_Z0(muons_sel_iso, EFlowTrack_1)")

        # df=df.Define("combined_leptons_per_event", "muons_sel_iso.size() + electrons_sel_iso.size()")
        # df=df.Define("merged_sel_iso", "FCCAnalyses::ReconstructedParticle::merge(muons_sel_iso, electrons_sel_iso)")
     
        #Filter zz where z to two neutrinos and one z to two quakrs
     
        
        df = df.Filter("muons_sel_iso.size() + electrons_sel_iso.size() == 0")
        # df = df.Filter("muons_sel_iso.size() + electrons_sel_iso.size() == 1")
        # df = df.Filter("muons_sel_iso.size() + electrons_sel_iso.size() == 2")
        ## require opsite charges for zz not for the zbb and cc ss but for those just make sure the iso leptons are 0 
        # Function to filter events where the sum of charges of muons and electrons is 0
        # df = df.Define("muons_charge", "FCCAnalyses::ReconstructedParticle::get_charge(muons_sel_iso)")
        # df = df.Define("electrons_charge", "FCCAnalyses::ReconstructedParticle::get_charge(electrons_sel_iso)")
        # df = df.Define("total_lepton_charge", 
        #                "int sum_charge = 0; "
        #                "for(size_t i = 0; i < muons_charge.size(); ++i) { sum_charge += muons_charge[i]; } "
        #                "for(size_t i = 0; i < electrons_charge.size(); ++i) { sum_charge += electrons_charge[i]; } "
        #                "return sum_charge;")
        # df = df.Filter("total_lepton_charge == 0")
        
        # df=df.Define("merged_sel_iso_z", "FCCAnalyses::ReconstructedParticle::merge(muons_sel_iso, electrons_sel_iso)")
        # df=df.Define("z_mass_constraint", "FCCAnalyses::ReconstructedParticle::resonanceBuilder(91.2)(merged_sel_iso_z)")
        # df=df.Define("z_mass_constraint_mass", "FCCAnalyses::ReconstructedParticle::get_mass(z_mass_constraint)[0]")
       
        # df = df.Filter("z_mass_constraint_mass < 76.2 && z_mass_constraint_mass > 106.2")
        
    
        

        # if not (channel == "had"):
        #     df = df.Define(
        #         "muons_p", "FCCAnalyses::ReconstructedParticle::get_p(muons_sel_iso)"
        #     )
        #     df = df.Define(
        #         "electrons_p", "FCCAnalyses::ReconstructedParticle::get_p(electrons_sel_iso)"
        #     )

        #     df = df.Define(
        #         "muons_theta",
        #         "FCCAnalyses::ReconstructedParticle::get_theta(muons_sel_iso)",
        #     )
        #     df = df.Define(
        #         "muons_phi",
        #         "FCCAnalyses::ReconstructedParticle::get_phi(muons_sel_iso)",
        #     )
        #     df = df.Define(
        #         "muons_q",
        #         "FCCAnalyses::ReconstructedParticle::get_charge(muons_sel_iso)",
        #     )
        #     df = df.Define(
        #         "muons_n", "FCCAnalyses::ReconstructedParticle::get_n(muons_sel_iso)",
        #     )

        #     df = df.Define(
        #         "electrons_theta",
        #         "FCCAnalyses::ReconstructedParticle::get_theta(electrons_sel_iso)",
        #     )
        #     df = df.Define(
        #         "electrons_phi",
        #         "FCCAnalyses::ReconstructedParticle::get_phi(electrons_sel_iso)",
        #         )
        #     df = df.Define(
        #         "electrons_q",
        #         "FCCAnalyses::ReconstructedParticle::get_charge(electrons_sel_iso)",
        #         )
        #     df = df.Define(
        #         "electrons_n", "FCCAnalyses::ReconstructedParticle::get_n(electrons_sel_iso)",
        #     )
        ## create a new collection of reconstructed particles removing muons with p>12
        df = df.Define(
            "ReconstructedParticlesNoMuons",
            "FCCAnalyses::ReconstructedParticle::remove(ReconstructedParticles,muons_sel_iso)",
        )
        df = df.Define(
            "ReconstructedParticlesNoMuNoEl",
            "FCCAnalyses::ReconstructedParticle::remove(ReconstructedParticlesNoMuons,electrons_sel_iso)",
        )
        
        #Add in overlap removal so that I only consider jets that dont have a lepton overlapping the radius of it


        ## perform exclusive jet clustering
        global jetClusteringHelper
        global jetFlavourHelper
        global jetFlavourHelper_R5
        global jetClusteringHelper_R5
        
        ## define jet and run clustering parameters
        ## name of collections in EDM root files
        collections = {
            "GenParticles": "Particle",
            "PFParticles": "ReconstructedParticles",
            "PFTracks": "EFlowTrack",
            "PFPhotons": "EFlowPhoton",
            "PFNeutralHadrons": "EFlowNeutralHadron",
            "TrackState": "EFlowTrack_1",
            "TrackerHits": "TrackerHits",
            "CalorimeterHits": "CalorimeterHits",
            "dNdx": "EFlowTrack_2",
            "PathLength": "EFlowTrack_L",
            "Bz": "magFieldBz",
        }

        nJets = 4 if  channel == "semihad" else 6
        #Add in overlap removal so that I only consider jets that dont have a lepton overlapping the radius of it
        # This is where the overlap removal will need to be so that ReconstructedParticlesNoMuNoEl also has no overlapping leptons

        collections_noleps = copy.deepcopy(collections)
        collections_noleps["PFParticles"] = "ReconstructedParticlesNoMuNoEl"
        if saveExclJets:
            jetClusteringHelper = ExclusiveJetClusteringHelper(
                collections_noleps["PFParticles"], nJets
            )
        ## Jet cone size to change, currernlty is .5
        deltaR_threshold=0.5
        jetClusteringHelper_R5  = InclusiveJetClusteringHelper(
            collections_noleps["PFParticles"], deltaR_threshold, 5, "R5"
        )
        if  saveExclJets:
            df = jetClusteringHelper.define(df)
        df = jetClusteringHelper_R5.define(df)
        ## define jet flavour tagging parameters
        #Add in overlap removal so that I only consider jets that dont have a lepton overlapping the radius of it
        if saveExclJets:
            jetFlavourHelper = JetFlavourHelper(
                collections_noleps,
                jetClusteringHelper.jets,
                jetClusteringHelper.constituents,
            )
            ## figure out wher ethe reco jet colelction comes from
        jetFlavourHelper_R5 = JetFlavourHelper(
            collections_noleps,
            jetClusteringHelper_R5.jets,
            jetClusteringHelper_R5.constituents,
            "R5",
        )
        # Can make efficiency plots for jet flavor taggings for the Bs can also start trying new clustering algorithms and 
        # plot jet distributions for the different clustering algorithms and see if there is a difference in the jet distributions
        



        if saveExclJets:    df = jetFlavourHelper.define(df)
        
        df = jetFlavourHelper_R5.define(df)
        ## tagger inference
        if  saveExclJets: df = jetFlavourHelper.inference(weaver_preproc, weaver_model, df)
        df = jetFlavourHelper_R5.inference(weaver_preproc, weaver_model,df)

        # df = df.Define(
        #     f"lep_p", "muons_sel_iso.size() >0 ? FCCAnalyses::ReconstructedParticle::get_p(muons_sel_iso)[0] : (electrons_sel_iso.size() > 0 ? FCCAnalyses::ReconstructedParticle::get_p(electrons_sel_iso)[0] : -999) "
        # )
        # df = df.Define(
        #     f'lep_theta', 'muons_sel_iso.size() >0 ? FCCAnalyses::ReconstructedParticle::get_theta(muons_sel_iso)[0] : (electrons_sel_iso.size() > 0 ? FCCAnalyses::ReconstructedParticle::get_theta(electrons_sel_iso)[0] : -999) '
        # )
        # df = df.Define(
        #     f'lep_phi', 'muons_sel_iso.size() >0 ? FCCAnalyses::ReconstructedParticle::get_phi(muons_sel_iso)[0] : (electrons_sel_iso.size() > 0 ? FCCAnalyses::ReconstructedParticle::get_phi(electrons_sel_iso)[0] : -999) '
        # )
        # df = df.Define(
        #     f"nlep",
        #     "electrons_sel_iso.size()+muons_sel_iso.size()")
        


        # df = df.Define(
        #     f"missing_p",
        #     "FCCAnalyses::ReconstructedParticle::get_p(MissingET)[0]",
        # )

        
        # df = df.Define(
        #     f'missing_p_theta', 'ReconstructedParticle::get_theta(MissingET)[0]',
        # )

        # df = df.Define(
        #     f'missing_p_phi', 'ReconstructedParticle::get_phi(MissingET)[0]',
        # )

        if saveExclJets:
            df = df.Define(
                f"jets_p4",
                "JetConstituentsUtils::compute_tlv_jets({})".format(
                    jetClusteringHelper.jets
                ),
            )
        
        df = df.Define(
            f"jets_R5_p4",
            "JetConstituentsUtils::compute_tlv_jets({})".format(
                jetClusteringHelper_R5.jets
            ),
        )

        df = df.Define(f"jets_R5_pflavor_unfiltered", "JetTaggingUtils::get_flavour({}, Particle)".format(jetClusteringHelper_R5.jets) )
        
        
        df = df.Define(f"jets_R5_p_unfiltered",           "JetClusteringUtils::get_p({})".format(jetClusteringHelper_R5.jets))
        df=df.Define(f"jets_R5_p_unfiltered_size", "jets_R5_p_unfiltered.size()")
        df = df.Define(f"jets_R5_theta_unfiltered",       "JetClusteringUtils::get_theta({})".format(jetClusteringHelper_R5.jets))
        df=df.Define(f"jets_R5_tlv_unfiltered",           "JetConstituentsUtils::compute_tlv_jets({})".format(jetClusteringHelper_R5.jets))
        


    


        ## Want to get tlv for all remaining leptons and then delta R calc between jets_R5_tlv and leptons_tlv
        # df=df.Define("remaining_muons", "FCCAnalyses::ReconstructedParticle::get(Muon0, muons_sel_iso)")
        # df=df.Define("remaining_electrons", "FCCAnalyses::ReconstructedParticle::get(Electron0, electrons_sel_iso)")
        # df=df.Define("remaining_leptons", "FCCAnalyses::ReconstructedParticle::merge(remaining_muons, remaining_electrons)")
        # df=df.Define("remaining_leptons_p", "FCCAnalyses::ReconstructedParticle::get_p(remaining_leptons)")
        # df=df.Define("remaining_muons_p", "FCCAnalyses::ReconstructedParticle::get_p(remaining_muons)")
        # df=df.Define("remaining_electrons_p", "FCCAnalyses::ReconstructedParticle::get_p(remaining_electrons)")

        df = df.Define("remaining_muons_tlv", "FCCAnalyses::ReconstructedParticle::get_tlv(muons_sel_iso)")
        df = df.Define("remaining_electrons_tlv", "FCCAnalyses::ReconstructedParticle::get_tlv(electrons_sel_iso)")

        df=df.Define("remaining_muons_deltaR", "FCCAnalyses::TruthMatching::Delta_R_calc(jets_R5_tlv_unfiltered, remaining_muons_tlv)")
        df=df.Define("remaining_electrons_deltaR", "FCCAnalyses::TruthMatching::Delta_R_calc(jets_R5_tlv_unfiltered, remaining_electrons_tlv)")
        
        df=df.Define("jet_removal_mask", 
                    f"""
                    ROOT::VecOps::RVec<bool> mask(jets_R5_theta_unfiltered.size(), true);
                    // Check Delta R for muons
                    for(size_t i = 0; i < remaining_muons_tlv.size(); i++) {{
                        for(size_t j = 0; j < jets_R5_theta_unfiltered.size(); j++) {{
                            size_t deltaR_index = i * jets_R5_theta_unfiltered.size() + j;
                            if(deltaR_index < remaining_muons_deltaR.size() && remaining_muons_deltaR[deltaR_index] < {deltaR_threshold}) {{
                                mask[j] = false;
                            }}
                        }}
                    }}
                    // Check Delta R for electrons
                    for(size_t i = 0; i < remaining_electrons_tlv.size(); i++) {{
                        for(size_t j = 0; j < jets_R5_theta_unfiltered.size(); j++) {{
                            size_t deltaR_index = i * jets_R5_theta_unfiltered.size() + j;
                            if(deltaR_index < remaining_electrons_deltaR.size() && remaining_electrons_deltaR[deltaR_index] < {deltaR_threshold}) {{
                                mask[j] = false;
                            }}
                        }}
                    }}
                    return mask;
                    """)
    
    
        ''' 
        Implemented logic to calculate Delta R between jets and remaining leptons (muons and electrons).
        Instead of using the minimum Delta R, all Delta R values between each lepton and each jet are checked.
        If any Delta R value for a jet to a lepton (muon or electron) is below the threshold (set to jet radius),
        that jet is marked for removal using a mask. The jet collection is then filtered to exclude these jets.
        This makes sure that jets overlapping with any lepton (based on Delta R) are removed from the analysis,
        avoiding index mismatch issues and accounting for cases where a lepton might be close to multiple jets.
        '''
        
        df=df.Define("jets_R5_pflavor", "jets_R5_pflavor_unfiltered[jet_removal_mask]")
        df=df.Define(f"PseudoJetCollection_masked", f"{jetClusteringHelper_R5.jets}[jet_removal_mask]")
        df=df.Define("masked_jet_constitutents", f"{jetClusteringHelper_R5.constituents}[jet_removal_mask]")

        df=df.Define("jets_R5_eta", "JetClusteringUtils::get_eta(PseudoJetCollection_masked)")
        df=df.Define("jets_R5_phi", "JetClusteringUtils::get_phi(PseudoJetCollection_masked)")
        df=df.Define("jets_R5_pt", "JetClusteringUtils::get_pt(PseudoJetCollection_masked)")
        df=df.Define("jets_R5_m", "JetClusteringUtils::get_m(PseudoJetCollection_masked)")
        df=df.Define("jets_R5_e", "JetClusteringUtils::get_e(PseudoJetCollection_masked)")
        df=df.Define(f"jets_R5_tlv", "jets_R5_tlv_unfiltered[jet_removal_mask]")
        df=df.Define(f"jets_R5_p", "jets_R5_p_unfiltered[jet_removal_mask]")
        df=df.Define(f"jets_R5_theta", "jets_R5_theta_unfiltered[jet_removal_mask]")
        
        
        # df=df.Define("masked_jet_constituents", "FCCAnalyses::JetClusteringUtils::get_constituents(PseudoJetCollection_masked)")
        df= df.Define("jet_mother_stuff", "FCCAnalyses::TruthMatching::getJetMotherPdgId(PseudoJetCollection_masked, MCParticles, MCRecoAssociations1, MCRecoAssociations1, ReconstructedParticlesNoMuNoEl,Particle0,Particle1)")
        df=df.Define("jet_daughter_stuff", "jet_mother_stuff.first")
        df=df.Define("jet_mother_pdg_id", "jet_mother_stuff.second")
        # This collection is masked so that I can use the masked.jets in the other functions that require it like the sel_tag where u need the jet collection 
        # without the masked jet collection the pflavor indicies are different then when u call the jetClusteringHelper_R5.jets so it doesnt work but this works perfectly
    
        # df=df.Define("jets_R5_pflavor_truth_matched", "FCCAnalyses::TruthMatching::jetTruthFinder(masked_jet_constitutents, ReconstructedParticlesNoMuNoEl, Particle, MCRecoAssociations1)")






        # df=df.Define("jets_R5_masked_pseudojets", "JetClusteringUtils::get_pseudoJets(jets_R5_pflavor_new)")
        
        # Note: The original jets_R5_pflavor is renamed to jets_R5_pflavor_unfiltered to preserve the unfiltered collection.
        # A new filtered collection named jets_R5_pflavor is created by applying the jet_removal_mask. This approach aims to avoid 
        # renaming all downstream references to jets_R5_pflavor, ensuring consistency in size with other filtered collections like 
        # jets_R5_p and jets_R5_theta. However, this method may not work as intended due to potential issues in downstream processes 
        # or functions (e.g., JetTaggingUtils::get_btag) that might still reference the original unfiltered collection structure or size, 
        # leading to index mismatches or out-of-bounds errors. It is critical to verify and update all downstream dependencies to use 
        # the filtered jets_R5_pflavor consistently to prevent such issues.

        # Apply the mask to filter out jets that are too close to leptons
        
        df=df.Define(f"jets_R5_p_size", "jets_R5_p.size()")
        
       
        ## Using filtered collections for momentum and theta, but keeping pflavor unfiltered for now due to indexing issues

        # df = df.Define(f"jet1_R5_p","jets_R5_p[0]")
        # df = df.Define(f"jet2_R5_p","jets_R5_p[1]")
        # df = df.Define(f"jet3_R5_p","jets_R5_p.size()>2 ? jets_R5_p[2] : -999")
        # df = df.Define(f"jet4_R5_p","jets_R5_p.size()>3 ? jets_R5_p[3] : -999")
        # df = df.Define(f"jet5_R5_p","jets_R5_p.size()>4 ? jets_R5_p[4] : -999")
        # df = df.Define(f"jet6_R5_p","jets_R5_p.size()>5 ? jets_R5_p[5] : -999")

        # df = df.Define(f"jet1_R5_theta","jets_R5_theta[0]")
        # df = df.Define(f"jet2_R5_theta","jets_R5_theta[1]")
        # df = df.Define(f"jet3_R5_theta","jets_R5_theta.size()>2 ? jets_R5_theta[2] : -999")
        # df = df.Define(f"jet4_R5_theta","jets_R5_theta.size()>3 ? jets_R5_theta[3] : -999")
        # df = df.Define(f"jet5_R5_theta","jets_R5_theta.size()>4 ? jets_R5_theta[4] : -999")
        # df = df.Define(f"jet6_R5_theta","jets_R5_theta.size()>5 ? jets_R5_theta[5] : -999")
        
    
        # df = df.Define(f"jet1_R5_pflavor","jets_R5_pflavor[0]")
        # df = df.Define(f"jet2_R5_pflavor","jets_R5_pflavor[1]")
        # df = df.Define(f"jet3_R5_pflavor","jets_R5_p.size()>2 ? jets_R5_pflavor[2] : -999")
        # df = df.Define(f"jet4_R5_pflavor","jets_R5_p.size()>3 ? jets_R5_pflavor[3] : -999")
        # df = df.Define(f"jet5_R5_pflavor","jets_R5_p.size()>4 ? jets_R5_pflavor[4] : -999")
        # df = df.Define(f"jet6_R5_pflavor","jets_R5_p.size()>5 ? jets_R5_pflavor[5] : -999")
        df = df.Define(f"njets_R5",       "return int(jets_R5_pflavor.size())")
        df = df.Define(f"jets_R5_btag_true", "JetTaggingUtils::get_btag({}, 1.0)".format('jets_R5_pflavor'))
        df = df.Define(f"jets_R5_ctag_true", "JetTaggingUtils::get_ctag({}, 1.0)".format('jets_R5_pflavor'))
        df = df.Define(f"jets_R5_ltag_true", "JetTaggingUtils::get_ltag({}, 1.0)".format('jets_R5_pflavor'))
        df = df.Define(f"jets_R5_gtag_true", "JetTaggingUtils::get_gtag({}, 1.0)".format('jets_R5_pflavor'))
        ## This function the get_quarktag puts a 1 or 0 if the jet is whatever jet flavor it is selecting for 
        ## The seltag function then allows you to select the jets that are 1 for the flavor you are selecting for 

        b_eff = .95
        c_eff = 10**-1.5
        l_eff = 10**-3
        g_eff = 10**-1.7
        uncert_b_eff = 0.25
        
        # df = df.Define("jets_R5_btag_eff_p9",  "JetTaggingUtils::get_btag({},{},{},{},{})".format('jets_R5_pflavor', b_eff, c_eff, l_eff, g_eff))
        # df = df.Define("jets_R5_btag_eff_p89", "JetTaggingUtils::get_btag({},{},{},{},{})".format('jets_R5_pflavor', b_eff-uncert_b_eff, c_eff, l_eff, g_eff))
        # df = df.Define("jets_R5_btag_eff_p91", "JetTaggingUtils::get_btag({},{},{},{},{})".format('jets_R5_pflavor', b_eff+uncert_b_eff, c_eff, l_eff, g_eff))


    
        
        # This is where error comes from when i used the filreted jets_R5_pflavor_new
        df = df.Define("jets_R5_btagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_btag_true,PseudoJetCollection_masked)")
        df = df.Define("jets_R5_ctagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_ctag_true,PseudoJetCollection_masked)")
        df = df.Define("jets_R5_ltagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_ltag_true,PseudoJetCollection_masked)")
        df = df.Define("jets_R5_gtagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_gtag_true,PseudoJetCollection_masked)")

        # df = df.Define("jets_R5_btagged_eff_p9", "JetTaggingUtils::sel_tag(true)(jets_R5_btag_eff_p9,PseudoJetCollection_masked)")
        # df = df.Define("jets_R5_btagged_eff_p89", "JetTaggingUtils::sel_tag(true)(jets_R5_btag_eff_p89,PseudoJetCollection_masked)")
        # df = df.Define("jets_R5_btagged_eff_p91", "JetTaggingUtils::sel_tag(true)(jets_R5_btag_eff_p91,PseudoJetCollection_masked)")

        df = df.Define(f"nbjets_R5_true", "return int(jets_R5_btagged_true.size())")
        df = df.Define(f"ncjets_R5_true", "return int(jets_R5_ctagged_true.size())")
        df = df.Define(f"nljets_R5_true", "return int(jets_R5_ltagged_true.size())")
        df = df.Define(f"ngjets_R5_true", "return int(jets_R5_gtagged_true.size())")


        df = df.Define(f"bjets_R5_true",  "JetConstituentsUtils::compute_tlv_jets({})". format('jets_R5_btagged_true'))
        df=df.Define(f"bjets_R5_true_pt", "JetClusteringUtils::get_pt({})".format('bjets_R5_true'))
        df=df.Define(f"bjets_R5_true_m", "JetClusteringUtils::get_m({})".format('bjets_R5_true'))
        df=df.Define(f"bjets_R5_true_theta","JetClusteringUtils::get_theta({})".format('bjets_R5_true'))

        df=df.Define(f"cjets_R5_true",  "JetConstituentsUtils::compute_tlv_jets({})". format('jets_R5_ctagged_true'))
        df=df.Define(f"cjets_R5_true_theta","JetClusteringUtils::get_theta({})".format('cjets_R5_true'))
        df=df.Define(f"ljets_R5_true",  "JetConstituentsUtils::compute_tlv_jets({})". format('jets_R5_ltagged_true'))
        df=df.Define(f"ljets_R5_true_theta","JetClusteringUtils::get_theta({})".format('ljets_R5_true'))
        df=df.Define(f"gjets_R5_true",  "JetConstituentsUtils::compute_tlv_jets({})". format('jets_R5_gtagged_true'))
        df=df.Define(f"gjets_R5_true_theta","JetClusteringUtils::get_theta({})".format('gjets_R5_true'))


        
        
        # df = df.Define("bjet1_R5_true_p","nbjets_R5_true > 1 ? bjets_R5_true[0].P() : -999")
        # df = df.Define("ljet1_R5_true_p","nljets_R5_true > 1 ? ljets_R5_true[0].P() : -999")
        # df = df.Define("nbjets_R5_eff_p9", "return int(jets_R5_btagged_eff_p9.size())")
        # df = df.Define("nbjets_R5_eff_p89", "return int(jets_R5_btagged_eff_p89.size())")
        # df = df.Define("nbjets_R5_eff_p91", "return int(jets_R5_btagged_eff_p91.size())")

        # df = df.Define("bjet_R5_eff_p9_p4",  "JetConstituentsUtils::compute_tlv_jets({})". format('jets_R5_btagged_eff_p9'))
        # df = df.Define("bjet_R5_eff_p91_p4", "JetConstituentsUtils::compute_tlv_jets({})".format('jets_R5_btagged_eff_p91'))
        # df = df.Define("bjet_R5_eff_p89_p4", "JetConstituentsUtils::compute_tlv_jets({})".format('jets_R5_btagged_eff_p89'))
        # df = df.Define("mbbar_p9",  "nbjets_R5_eff_p9 >   1 ? JetConstituentsUtils::InvariantMass(bjet_R5_eff_p9_p4[0],  bjet_R5_eff_p9_p4[1])  : -999")
        # df = df.Define("mbbar_p91", "nbjets_R5_eff_p91 >  1 ? JetConstituentsUtils::InvariantMass(bjet_R5_eff_p91_p4[0], bjet_R5_eff_p91_p4[1]) : -999")
        # df = df.Define("mbbar_p89", "nbjets_R5_eff_p89 >  1 ? JetConstituentsUtils::InvariantMass(bjet_R5_eff_p89_p4[0], bjet_R5_eff_p89_p4[1]) : -999")

        df = df.Define("jets_R5_isB","recojet_isB_R5[jet_removal_mask]")
        df = df.Define("jets_R5_isC","recojet_isC_R5[jet_removal_mask]")
        df = df.Define("jets_R5_isU","recojet_isU_R5[jet_removal_mask]")
        df = df.Define("jets_R5_isD","recojet_isD_R5[jet_removal_mask]")
        df = df.Define("jets_R5_isG","recojet_isG_R5[jet_removal_mask]")
        df = df.Define("jets_R5_isS","recojet_isS_R5[jet_removal_mask]")
        df = df.Define("jets_R5_isTAU","recojet_isTAU_R5[jet_removal_mask]")

        df = df.Define(f"jets_R5_isB_true_b", "jets_R5_isB[jets_R5_btag_true]")
        df = df.Define(f"jets_R5_isC_true_b", "jets_R5_isC[jets_R5_btag_true]")
        df = df.Define(f"jets_R5_isU_true_b", "jets_R5_isU[jets_R5_btag_true]")
        df = df.Define(f"jets_R5_isD_true_b", "jets_R5_isD[jets_R5_btag_true]")
        df = df.Define(f"jets_R5_isG_true_b", "jets_R5_isG[jets_R5_btag_true]")
        df = df.Define(f"jets_R5_isS_true_b", "jets_R5_isB[jets_R5_btag_true]")
        df = df.Define(f"jets_R5_isTau_true_b", "jets_R5_isTAU[jets_R5_btag_true]")

        df=df.Define(f"jets_R5_isC_true_c", "jets_R5_isC[jets_R5_ctag_true]")
        df=df.Define(f"jets_R5_isB_true_c", "jets_R5_isB[jets_R5_ctag_true]")
        df=df.Define(f"jets_R5_isU_true_c", "jets_R5_isU[jets_R5_ctag_true]")
        df=df.Define(f"jets_R5_isD_true_c", "jets_R5_isD[jets_R5_ctag_true]")
        df=df.Define(f"jets_R5_isG_true_c", "jets_R5_isG[jets_R5_ctag_true]")
        df=df.Define(f"jets_R5_isS_true_c", "jets_R5_isS[jets_R5_ctag_true]")
        df=df.Define(f"jets_R5_isTau_true_c", "jets_R5_isTAU[jets_R5_ctag_true]")
        
        

        # df = df.Define("jet1_R5_isG", "jets_R5_isG[0]")
        # df = df.Define("jet2_R5_isG", "jets_R5_isG[1]")
        # df = df.Define("jet3_R5_isG", "jets_R5_p.size()>2 ? jets_R5_isG[2] : -999")
        # df = df.Define("jet4_R5_isG", "jets_R5_p.size()>3 ? jets_R5_isG[3] : -999")
        # df = df.Define("jet5_R5_isG", "jets_R5_p.size()>4 ? jets_R5_isG[4] : -999")
        # df = df.Define("jet6_R5_isG", "jets_R5_p.size()>5 ? jets_R5_isG[5] : -999")

        # df = df.Define("jet1_R5_isU", "jets_R5_isU[0]")
        # df = df.Define("jet2_R5_isU", "jets_R5_isU[1]")
        # df = df.Define("jet3_R5_isU", "jets_R5_p.size()>2 ? jets_R5_isU[2] : -999")
        # df = df.Define("jet4_R5_isU", "jets_R5_p.size()>3 ? jets_R5_isU[3] : -999")
        # df = df.Define("jet5_R5_isU", "jets_R5_p.size()>4 ? jets_R5_isU[4] : -999")
        # df = df.Define("jet6_R5_isU", "jets_R5_p.size()>5 ? jets_R5_isU[5] : -999")

        # df = df.Define("jet1_R5_isB", "jets_R5_isB[0]")
        # df = df.Define("jet2_R5_isB", "jets_R5_isB[1]")
        # df = df.Define("jet3_R5_isB", "jets_R5_p.size()>2 ? jets_R5_isB[2] : -999")
        # df = df.Define("jet4_R5_isB", "jets_R5_p.size()>3 ? jets_R5_isB[3] : -999")
        # df = df.Define("jet5_R5_isB", "jets_R5_p.size()>4 ? jets_R5_isB[4] : -999")
        # df = df.Define("jet6_R5_isB", "jets_R5_p.size()>5 ? jets_R5_isB[5] : -999")
        
        # df = df.Define("jet1_R5_isS", "jets_R5_isS[0]")
        # df = df.Define("jet2_R5_isS", "jets_R5_isS[1]")
        # df = df.Define("jet3_R5_isS", "jets_R5_p.size()>2 ? jets_R5_isS[2] : -999")
        # df = df.Define("jet4_R5_isS", "jets_R5_p.size()>3 ? jets_R5_isS[3] : -999")
        # df = df.Define("jet5_R5_isS", "jets_R5_p.size()>4 ? jets_R5_isS[4] : -999")
        # df = df.Define("jet6_R5_isS", "jets_R5_p.size()>5 ? jets_R5_isS[5] : -999")

        # df = df.Define("jet1_R5_isC", "jets_R5_isC[0]")
        # df = df.Define("jet2_R5_isC", "jets_R5_isC[1]")
        # df = df.Define("jet3_R5_isC", "jets_R5_p.size()>2 ? jets_R5_isC[2] : -999")
        # df = df.Define("jet4_R5_isC", "jets_R5_p.size()>3 ? jets_R5_isC[3] : -999")
        # df = df.Define("jet5_R5_isC", "jets_R5_p.size()>4 ? jets_R5_isC[4] : -999")
        # df = df.Define("jet6_R5_isC", "jets_R5_p.size()>5 ? jets_R5_isC[5] : -999")

        # df = df.Define("jet1_R5_isD", "jets_R5_isD[0]")
        # df = df.Define("jet2_R5_isD", "jets_R5_isD[1]")
        # df = df.Define("jet3_R5_isD", "jets_R5_p.size()>2 ? jets_R5_isD[2] : -999")
        # df = df.Define("jet4_R5_isD", "jets_R5_p.size()>3 ? jets_R5_isD[3] : -999")
        # df = df.Define("jet5_R5_isD", "jets_R5_p.size()>4 ? jets_R5_isD[4] : -999")
        # df = df.Define("jet6_R5_isD", "jets_R5_p.size()>5 ? jets_R5_isD[5] : -999")

        # df = df.Define("jet1_R5_isTAU", "jets_R5_isTAU[0]")
        # df = df.Define("jet2_R5_isTAU", "jets_R5_isTAU[1]")
        # df = df.Define("jet3_R5_isTAU", "jets_R5_p.size()>2 ? jets_R5_isTAU[2] : -999")
        # df = df.Define("jet4_R5_isTAU", "jets_R5_p.size()>3 ? jets_R5_isTAU[3] : -999")
        # df = df.Define("jet5_R5_isTAU", "jets_R5_p.size()>4 ? jets_R5_isTAU[4] : -999")
        # df = df.Define("jet6_R5_isTAU", "jets_R5_p.size()>5 ? jets_R5_isTAU[5] : -999")

        
        
        # df = df.Define("bjets_R5_WPp5","ZHfunctions::sel_btag(0.5)(jets_R5_isB)")
        # df = df.Define("bjets_R5_WPp8","ZHfunctions::sel_btag(0.8)(jets_R5_isB)")
        # df = df.Define("bjets_R5_WPp85","ZHfunctions::sel_btag(0.85)(jets_R5_isB)")
        # df = df.Define("bjets_R5_WPp9","ZHfunctions::sel_btag(0.9)(jets_R5_isB)")

        # df = df.Define("nbjets_R5_WPp5","bjets_R5_WPp5.size()")
        # df = df.Define("nbjets_R5_WPp8","bjets_R5_WPp8.size()")
        # df = df.Define("nbjets_R5_WPp85","bjets_R5_WPp85.size()")
        # df = df.Define("nbjets_R5_WPp9","bjets_R5_WPp9.size()")

    
        #['recojet_isG_R5', 'recojet_isU_R5', 'recojet_isS_R5', 'recojet_isC_R5', 'recojet_isB_R5', 'recojet_isTAU_R5', 'recojet_isD_R5', 'jet_nmu_R5', 'jet_nel_R5', 'jet_nchad_R5', 'jet_ngamma_R5', 'jet_nnhad_R5']
        # if  saveExclJets:
        #     df = df.Define("jets_isB",   "JetFlavourUtils::get_weight(MVAVec_, 4)")
        #     df = df.Define("bjets_WPp5", "ZHfunctions::sel_btag(0.5)(jets_isB)")
        #     df = df.Define("bjets_WPp8", "ZHfunctions::sel_btag(0.8)(jets_isB)")
        #     df = df.Define("bjets_WPp85", "ZHfunctions::sel_btag(0.85)(jets_isB)")
        #     df = df.Define("bjets_WPp9", "ZHfunctions::sel_btag(0.9)(jets_isB)")
        #     df = df.Define("nbjets_WPp5", "bjets_WPp5.size()")
        #     df = df.Define("nbjets_WPp8", "bjets_WPp8.size()")
        #     df = df.Define("nbjets_WPp85", "bjets_WPp85.size()")
        #     df = df.Define("nbjets_WPp9", "bjets_WPp9.size()")
    
        #     df = df.Define("jet1", "jets_p4[0]")
        #     df = df.Define("jet2", "jets_p4[1]")
        #     df = df.Define("jet3", "jets_p4[2]")
        #     df = df.Define("jet4", "jets_p4[3]")
        #     df = df.Define("jet1_p","jet1.P()")
        #     df = df.Define("jet2_p","jet2.P()")
        #     df = df.Define("jet3_p","jet3.P()")
        #     df = df.Define("jet4_p","jet4.P()")
        #     df = df.Define("jet5_p","jets_p4.size()>4 ? jets_p4[4].P() : -999")
        #     df = df.Define("jet6_p","jets_p4.size()>5 ? jets_p4[5].P() : -999")
        #     df = df.Define("recojet_theta", "JetClusteringUtils::get_theta(jet)")
        #     df = df.Define("jet1_theta","recojet_theta[0]")
        #     df = df.Define("jet2_theta","recojet_theta[1]")
        #     df = df.Define("jet3_theta","recojet_theta[2]")
        #     df = df.Define("jet4_theta","recojet_theta[3]")
        #     df = df.Define("jet5_theta","jets_p4.size()>4 ? recojet_theta[4] : -999")
        #     df = df.Define("jet6_theta","jets_p4.size()>5 ? recojet_theta[5] : -999")
            
        #     df = df.Define("jet1_isTau","recojet_isTAU[0]")
        #     df = df.Define("jet2_isTau","recojet_isTAU[1]")
        #     df = df.Define("jet3_isTau","recojet_isTAU[2]")
        #     df = df.Define("jet4_isTau","recojet_isTAU[3]")
        #     df = df.Define("jet5_isTau","jets_p4.size()>4 ? recojet_isTAU[4] : -999")
        #     df = df.Define("jet6_isTau","jets_p4.size()>5 ? recojet_isTAU[5] : -999")
        
        #     df = df.Define("recojet_phi", "JetClusteringUtils::get_phi_std(jet)")
        #     df = df.Define("jet1_phi","recojet_phi[0]")
        #     df = df.Define("jet2_phi","recojet_phi[1]")
        #     df = df.Define("jet3_phi","recojet_phi[2]")
        #     df = df.Define("jet4_phi","recojet_phi[3]")
        #     df = df.Define("jet5_phi","jets_p4.size()>4 ? recojet_phi[4] : -999")
        #     df = df.Define("jet6_phi","jets_p4.size()>5 ? recojet_phi[5] : -999")
        #     df = df.Define("njets", "jets_p4.size()")
        
        #     df = df.Define("d_12", "JetClusteringUtils::get_exclusive_dmerge(_jet, 1)")
        #     df = df.Define("d_23", "JetClusteringUtils::get_exclusive_dmerge(_jet, 2)")
        #     df = df.Define("d_34", "JetClusteringUtils::get_exclusive_dmerge(_jet, 3)")
        #     df = df.Define("d_45", "jets_p4.size()>4 ? JetClusteringUtils::get_exclusive_dmerge(_jet, 4) : -999")
        #     df = df.Define("d_56", "jets_p4.size()>5 ? JetClusteringUtils::get_exclusive_dmerge(_jet, 5) : -999")


        #     df = df.Define("jet1_isG", "JetFlavourUtils::get_weight(MVAVec_, 0)[0]")
        #     df = df.Define("jet2_isG", "JetFlavourUtils::get_weight(MVAVec_, 0)[1]")
        #     df = df.Define("jet3_isG", "JetFlavourUtils::get_weight(MVAVec_, 0)[2]")
        #     df = df.Define("jet4_isG", "JetFlavourUtils::get_weight(MVAVec_, 0)[3]")
        #     df = df.Define("jet5_isG", "jets_p4.size()>4 ? JetFlavourUtils::get_weight(MVAVec_, 0)[4] : -999")
        #     df = df.Define("jet6_isG", "jets_p4.size()>5 ? JetFlavourUtils::get_weight(MVAVec_, 0)[5] : -999")
            
        #     df = df.Define("jet1_isQ", "JetFlavourUtils::get_weight(MVAVec_, 1)[0]")
        #     df = df.Define("jet2_isQ", "JetFlavourUtils::get_weight(MVAVec_, 1)[1]")
        #     df = df.Define("jet3_isQ", "JetFlavourUtils::get_weight(MVAVec_, 1)[2]")
        #     df = df.Define("jet4_isQ", "JetFlavourUtils::get_weight(MVAVec_, 1)[3]")
        #     df = df.Define("jet5_isQ", "jets_p4.size()>4 ? JetFlavourUtils::get_weight(MVAVec_, 1)[4] : -999")
        #     df = df.Define("jet6_isQ", "jets_p4.size()>5 ? JetFlavourUtils::get_weight(MVAVec_, 1)[5] : -999")
            
        #     df = df.Define("jet1_isS", "JetFlavourUtils::get_weight(MVAVec_, 2)[0]")
        #     df = df.Define("jet2_isS", "JetFlavourUtils::get_weight(MVAVec_, 2)[1]")
        #     df = df.Define("jet3_isS", "JetFlavourUtils::get_weight(MVAVec_, 2)[2]")
        #     df = df.Define("jet4_isS", "JetFlavourUtils::get_weight(MVAVec_, 2)[3]")
        #     df = df.Define("jet5_isS", "jets_p4.size()>4 ? JetFlavourUtils::get_weight(MVAVec_, 2)[4] : -999")
        #     df = df.Define("jet6_isS", "jets_p4.size()>5 ? JetFlavourUtils::get_weight(MVAVec_, 2)[5] : -999")
            
        #     df = df.Define("jet1_isC", "JetFlavourUtils::get_weight(MVAVec_, 3)[0]")
        #     df = df.Define("jet2_isC", "JetFlavourUtils::get_weight(MVAVec_, 3)[1]")
        #     df = df.Define("jet3_isC", "JetFlavourUtils::get_weight(MVAVec_, 3)[2]")
        #     df = df.Define("jet4_isC", "JetFlavourUtils::get_weight(MVAVec_, 3)[3]")
        #     df = df.Define("jet5_isC", "jets_p4.size()>4 ? JetFlavourUtils::get_weight(MVAVec_, 3)[4] : -999")
        #     df = df.Define("jet6_isC", "jets_p4.size()>5 ? JetFlavourUtils::get_weight(MVAVec_, 3)[5] : -999")
    
        #     df = df.Define("jet1_isB", "JetFlavourUtils::get_weight(MVAVec_, 4)[0]")
        #     df = df.Define("jet2_isB", "JetFlavourUtils::get_weight(MVAVec_, 4)[1]")
        #     df = df.Define("jet3_isB", "JetFlavourUtils::get_weight(MVAVec_, 4)[2]")
        #     df = df.Define("jet4_isB", "JetFlavourUtils::get_weight(MVAVec_, 4)[3]")
        #     df = df.Define("jet5_isB", "jets_p4.size()>4 ? JetFlavourUtils::get_weight(MVAVec_, 4)[4] : -999")
        #     df = df.Define("jet6_isB", "jets_p4.size()>5 ? JetFlavourUtils::get_weight(MVAVec_, 4)[5] : -999")
        
        
        



        
            
        
        # df1=nleps(df,1)
        # df2=nleps(df,2)
        return df

    # __________________________________________________________
    # Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        print('incl jets',jetFlavourHelper_R5.outputBranches())
        #print('excl jets',jetFlavourHelper.outputBranches())
        #all_branches += jetFlavourHelper_R5.outputBranches()
        return all_branches

        
        #all_branches+= jetClusteringHelper.outputBranches()

        ## outputs jet scores and constituent breakdown
        #branchList += jetFlavourHelper.outputBranches()
    
        #return all_branches #branchList




        ##test command fccanalysis run --nevents=10 treemaker_WbWb_reco.py