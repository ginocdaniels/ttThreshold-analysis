import os, copy
import urllib
# list of processes
all_processes = {
    "wzp6_ee_WbWb_PY6mod_ecm365": {
        "fraction": 1,
    },
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
    # "wzp6_ee_nunuH_Hcc_ecm365":{ "fraction": 1,},
    # "wzp6_ee_nunuH_Hss_ecm365":{ "fraction": 1,},
    # "wzp6_ee_nunuH_Huu_ecm365":{ "fraction": 1,},
    # "wzp6_ee_nunuH_Hdd_ecm365":{ "fraction": 1,},

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
#    "wzp6_ee_WbWb_ecm365": {
#        "fraction": 1,
#    },
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
    # "wzp6_ee_WbWb_had_ecm365": {
    #      "fraction": 1,
    # },

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

saveExclJets = True

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
outputDir   = "/eos/user/g/gidaniel/outputs/treemaker/WbWb/{}".format(channel)


# additional/costom C++ functions, defined in header files (optional)
# includePaths = ["examples/functions.h", "examples/truth_matching.h", "examples/MCParticleUtils.h","examples/test_funcs.h"]
includePaths = ["functions.h", "truth_matching.h"]
## latest particle transformer model, trained on 9M jets in winter2023 samples
model_name = "fccee_flavtagging_edm4hep_wc" #"fccee_flavtagging_edm4hep_wc_v1"

## model files locally stored on /eos
eos_dir ="/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/IDEA/"
# eos_dir = "/eos/user/g/gidaniel/ttThreshold-analysis/"
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

# inputDir = "/eos/user/g/gidaniel/ttThreshold-analysis/"

from addons.ONNXRuntime.jetFlavourHelper import JetFlavourHelper
from addons.FastJet.jetClusteringHelper import (
    ExclusiveJetClusteringHelper,
    InclusiveJetClusteringHelper,
)

jetFlavourHelper = None
jetFlavourHelper_R5 = None
jetClusteringHelper = None
jetClusteringHelper = None


all_branches = [
    "njets_R5","jets_R5_pflavor", "jets_R5_p_unfiltered_size","jets_R5_p_size", "jets_R5_theta_unfiltered",
      "bjets_R5_true","ljets_R5_true","remaining_muons_deltaR","remaining_electrons_deltaR","jets_R5_tlv","jets_R5_p","jets_R5_theta", "electrons_iso", "muons_iso", "electrons_sel","muons_all_p", "electrons_all_p","bjets_R5_true_theta",
      "jets_R5_isC","jets_R5_isU","jets_R5_isD","jets_R5_isB","jets_R5_isG","jets_R5_isS","jets_R5_isTAU","cjets_R5_true_theta","ljets_R5_true_theta","gjets_R5_true_theta",
      "all_thetas_merged", 
      "jets_R5_isB_true_b", "jets_R5_isC_true_b", "jets_R5_isU_true_b", "jets_R5_isD_true_b", "jets_R5_isG_true_b", "jets_R5_isS_true_b", "jets_R5_isTau_true_b",
      "jets_R5_isC_true_c", "jets_R5_isB_true_c", "jets_R5_isU_true_c", "jets_R5_isD_true_c", "jets_R5_isG_true_c", "jets_R5_isS_true_c", "jets_R5_isTau_true_c",
      "nbjets_R5_true", "ncjets_R5_true","nljets_R5_true","ngjets_R5_true","jets_R5_eta","jets_R5_phi",
      "bjets_R5_true_pt", "bjets_R5_true_m", "jets_R5_pt", "jets_R5_m", "jets_R5_e","W_collection_1","pt_Wcollection_1","W_collection_1_sim_status","W_collection_1_gen_status","W1_22_daughter1","W1_22_daughter_test","all_pdgs",
      "W_daughter_1_pdg","W_daughter_2_pdg"
     
]




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
        # df = df.Alias("Muon0", "Muon_objIdx.index")
        df = df.Alias("Electron0","Electron#0.index")
        # df = df.Alias("Electron0","Electron_objIdx.index")
        
        
        ## Find fraction of ones taht are cut make the d value optimized and find the ineefciecy add the prompt nonprompt together and find the fraction of erach that u ose with that cut and try to optimize this
        # normalized them as well as well so u can add them together because otherwize we dont have same number of events and it doesnt work for the bins 
        #Then we can send in condor jobs do cd/condor 
        # all interesting proceses wz bb qq. files will be in eos/user/g/gidaniel
        # to send in jobs do python3 send_all.py condor_q to check whats going on condor rm gidaniel to remove everythign
        # ls std/condor.1231753 does something 
        df = df.Alias("Particle0",           "Particle#0.index"); 
        # df = df.Alias("Particle0",           "_Particle_parents.index");    
        df = df.Alias("Particle1",           "Particle#1.index");    
        # df = df.Alias("Particle1",           "_Particle_daughters.index");    
        df = df.Alias("MCParticles",         "Particle");     

        df = df.Alias("MCRecoAssociations0", "MCRecoAssociations#0.index"); 
        df = df.Alias("MCRecoAssociations1", "MCRecoAssociations#1.index");
        # select Z bosons from events


        df=df.Define("all_pdgs", "FCCAnalyses::MCParticle::get_pdg(MCParticles)")
        df=df.Define("W_collection_1", "FCCAnalyses::MCParticle::sel_pdgID(24,true)(MCParticles)")
        df=df.Define("W_collection_1_sim_status", "FCCAnalyses::MCParticle::get_simStatus(W_collection_1)")
        df=df.Define("W_collection_1_gen_status", "FCCAnalyses::MCParticle::get_genStatus(W_collection_1)")
        # df=df.Define("W_collection_1_status22", "FCCAnalyses::MCParticle::sel_genStatus(22)(W_collection_1)")
        df=df.Define("pt_Wcollection_1", "FCCAnalyses::MCParticle::get_pt(W_collection_1)")
        df=df.Define("W1_22_daughter_test", "FCCAnalyses::myUtils::get_MCDaughter1(W_collection_1,Particle0)")
        df=df.Define("W1_22_daughter1", "FCCAnalyses::TruthMatching::get_MCDaughter1_W(W_collection_1,Particle0,MCParticles)")
        df=df.Define("W_daughter_1_pdg", "W1_22_daughter1[0]")
        df=df.Define("W_daughter_1_pdg_abs", "abs(W_daughter_1_pdg)")
        df=df.Define("W_daughter_2_pdg", "W1_22_daughter1[1]")
        df=df.Define("W_daughter_2_pdg_abs", "abs(W_daughter_2_pdg)")

        df=df.Define("W_daughter_1_pdg_abs_is_quark", "W_daughter_1_pdg_abs <= 6 && W_daughter_1_pdg_abs >= 1")
        df=df.Define("W_daughter_2_pdg_abs_is_quark", "W_daughter_2_pdg_abs <= 6 && W_daughter_2_pdg_abs >= 1")
        
        df=df.Filter("W_daughter_1_pdg_abs_is_quark && W_daughter_2_pdg_abs_is_quark")


        # Make sure one Z decays to nunu and Make sure one decays to 2 quarks 





        # df=df.Define("neutrino_collection_1", "FCCAnalyses::MCParticle::sel_pdgID(12,true)(MCParticles)")
        # df=df.Define("neutrino_collection_2", "FCCAnalyses::MCParticle::sel_pdgID(14,true)(MCParticles)")
        # df=df.Define("neutrino_collection_3", "FCCAnalyses::MCParticle::sel_pdgID(16,true)(MCParticles)")
        # df=df.Define("merged_neutrinos_1", "FCCAnalyses::MCParticle::mergeParticles(neutrino_collection_1, neutrino_collection_2)")

        # df=df.Define("merged_neutrinos_2", "FCCAnalyses::MCParticle::mergeParticles(merged_neutrinos_1, neutrino_collection_3)")
        # df=df.Filter("merged_neutrinos_2.size() == 0")
       

       
        
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
       
        
        # df = df.Filter("muons_sel_iso.size() + electrons_sel_iso.size() == 0")
        # df = df.Filter("muons_sel_iso.size() + electrons_sel_iso.size() == 1")
        # df = df.Filter("muons_sel_iso.size() + electrons_sel_iso.size() == 2")
       
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
        global jetClusteringHelper
        
        ## define jet and run clustering parameters
        ## name of collections in EDM root files
        # collections = {
        #     "GenParticles": "Particle",
        #     "PFParticles": "ReconstructedParticles",
        #     "PFTracks": "EFlowTrack",
        #     "PFPhotons": "EFlowPhoton",
        #     "PFNeutralHadrons": "EFlowNeutralHadron",
        #     "TrackState": "EFlowTrack_1",
        #     "TrackerHits": "TrackerHits",
        #     "CalorimeterHits": "CalorimeterHits",
        #     "dNdx": "EFlowTrack.dEdx",
        #     "PathLength": "EFlowTrack_L",
        #     "Bz": "magFieldBz",
        # }
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

        nJets = 6
        #Add in overlap removal so that I only consider jets that dont have a lepton overlapping the radius of it
        # This is where the overlap removal will need to be so that ReconstructedParticlesNoMuNoEl also has no overlapping leptons

        collections_noleps = copy.deepcopy(collections)
        collections_noleps["PFParticles"] = "ReconstructedParticlesNoMuNoEl"
        if saveExclJets:
            jetClusteringHelper = ExclusiveJetClusteringHelper(
                collections_noleps["PFParticles"], nJets
            )
        ## Jet cone size to change, currernlty is .5
       
        if  saveExclJets:
            df = jetClusteringHelper.define(df)
      
        ## define jet flavour tagging parameters
        #Add in overlap removal so that I only consider jets that dont have a lepton overlapping the radius of it
        if saveExclJets:
            jetFlavourHelper = JetFlavourHelper(
                collections_noleps,
                jetClusteringHelper.jets,
                jetClusteringHelper.constituents,
                "R5",
            )
       
        



        if saveExclJets:    df = jetFlavourHelper.define(df)
      
        if  saveExclJets: df = jetFlavourHelper.inference(weaver_preproc, weaver_model, df)
   

    
        if saveExclJets:
            df = df.Define(
                f"jets_p4",
                "JetConstituentsUtils::compute_tlv_jets({})".format(
                    jetClusteringHelper.jets
                ),
            )
        
    
        df = df.Define(f"jets_R5_pflavor_unfiltered", "JetTaggingUtils::get_flavour({}, Particle)".format(jetClusteringHelper.jets) )
        
        
        df = df.Define(f"jets_R5_p_unfiltered",           "JetClusteringUtils::get_p({})".format(jetClusteringHelper.jets))
        df=df.Define(f"jets_R5_p_unfiltered_size", "jets_R5_p_unfiltered.size()")
        df = df.Define(f"jets_R5_theta_unfiltered",       "JetClusteringUtils::get_theta({})".format(jetClusteringHelper.jets))
        df=df.Define(f"jets_R5_tlv_unfiltered",           "JetConstituentsUtils::compute_tlv_jets({})".format(jetClusteringHelper.jets))
        
        df = df.Define("remaining_muons_tlv", "FCCAnalyses::ReconstructedParticle::get_tlv(muons_sel_iso)")
        df = df.Define("remaining_electrons_tlv", "FCCAnalyses::ReconstructedParticle::get_tlv(electrons_sel_iso)")

        df=df.Define("remaining_muons_deltaR", "FCCAnalyses::TruthMatching::Delta_R_calc(jets_R5_tlv_unfiltered, remaining_muons_tlv)")
        df=df.Define("remaining_electrons_deltaR", "FCCAnalyses::TruthMatching::Delta_R_calc(jets_R5_tlv_unfiltered, remaining_electrons_tlv)")
       
    
      
        df=df.Define("jets_R5_pflavor", "jets_R5_pflavor_unfiltered")
        df=df.Define(f"PseudoJetCollection_masked", f"{jetClusteringHelper.jets}")
        df=df.Define("masked_jet_constitutents", f"{jetClusteringHelper.constituents}")

        df=df.Define("jets_R5_eta", "JetClusteringUtils::get_eta(PseudoJetCollection_masked)")
        df=df.Define("jets_R5_phi", "JetClusteringUtils::get_phi(PseudoJetCollection_masked)")
        df=df.Define("jets_R5_pt", "JetClusteringUtils::get_pt(PseudoJetCollection_masked)")
        df=df.Define("jets_R5_m", "JetClusteringUtils::get_m(PseudoJetCollection_masked)")
        df=df.Define("jets_R5_e", "JetClusteringUtils::get_e(PseudoJetCollection_masked)")
        df=df.Define(f"jets_R5_tlv", "jets_R5_tlv_unfiltered")
        df=df.Define(f"jets_R5_p", "jets_R5_p_unfiltered")
        df=df.Define(f"jets_R5_theta", "jets_R5_theta_unfiltered")
        
      
    
        df=df.Define(f"jets_R5_p_size", "jets_R5_p.size()")
        
       
        ## Using filtered collections for momentum and theta, but keeping pflavor unfiltered for now due to indexing issues

    
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
      
    
        
        # This is where error comes from when i used the filreted jets_R5_pflavor_new
        df = df.Define("jets_R5_btagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_btag_true,PseudoJetCollection_masked)")
        df = df.Define("jets_R5_ctagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_ctag_true,PseudoJetCollection_masked)")
        df = df.Define("jets_R5_ltagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_ltag_true,PseudoJetCollection_masked)")
        df = df.Define("jets_R5_gtagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_gtag_true,PseudoJetCollection_masked)")

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


        df = df.Define("jets_R5_isB","recojet_isB_R5")
        df = df.Define("jets_R5_isC","recojet_isC_R5")
        df = df.Define("jets_R5_isU","recojet_isU_R5")
        df = df.Define("jets_R5_isD","recojet_isD_R5")
        df = df.Define("jets_R5_isG","recojet_isG_R5")
        df = df.Define("jets_R5_isS","recojet_isS_R5")
        df = df.Define("jets_R5_isTAU","recojet_isTAU_R5")

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
        
    
        return df

    # __________________________________________________________
    # Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        print('incl jets',jetFlavourHelper.outputBranches())
        # print('incl jets class:', jetFlavourHelper_R5.__class__.__name__)
        # print('incl jets attributes:', dir(jetFlavourHelper_R5)["defintion"])
        # print('incl jets attributes:', jetFlavourHelper_R5.__class__.__name__)
        #print('excl jets',jetFlavourHelper.outputBranches())
        #all_branches += jetFlavourHelper_R5.outputBranches()
        return all_branches

        
        #all_branches+= jetClusteringHelper.outputBranches()

        ## outputs jet scores and constituent breakdown
        #branchList += jetFlavourHelper.outputBranches()
    
        #return all_branches #branchList




        ##test command fccanalysis run --nevents=10 treemaker_WbWb_reco.py