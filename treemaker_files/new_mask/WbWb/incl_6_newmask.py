import os, copy
import urllib
# list of processes
all_processes = {
    #  "p8_ee_ZZ_ecm365":{ "fraction": 1,},
    "wzp6_ee_WbWb_PY6mod_ecm365":{ "fraction": 1,},
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
jetClusteringHelper_R5 = None


all_branches = [
    "njets_R5","jets_R5_pflavor", "jets_R5_p_unfiltered_size","jets_R5_p_size", "jets_R5_theta_unfiltered",
      "bjets_R5_true","ljets_R5_true","jets_R5_tlv","jets_R5_p","jets_R5_theta", "electrons_iso", "muons_iso", "electrons_sel","muons_all_p", "electrons_all_p","bjets_R5_true_theta",
      "jets_R5_isC","jets_R5_isU","jets_R5_isD","jets_R5_isB","jets_R5_isG","jets_R5_isS","jets_R5_isTAU","cjets_R5_true_theta","ljets_R5_true_theta","gjets_R5_true_theta",
      "all_thetas_merged", 
      "nbjets_R5_true", "ncjets_R5_true","nljets_R5_true","ngjets_R5_true","jets_R5_eta","jets_R5_phi",
      "bjets_R5_true_pt", "bjets_R5_true_m", "jets_R5_pt", "jets_R5_m", "jets_R5_e", "jets_R5_tlv_unfiltered", "jet_lep_deltaR",
     
]



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
        # df = df.Alias("Muon0", "Muon_objIdx.index")
        df = df.Alias("Electron0","Electron#0.index")
        # df = df.Alias("Electron0","Electron_objIdx.index")
        
        
        ## Find fraction of ones taht are cut make the d value optimized and find the ineefciecy add the prompt nonprompt together and find the fraction of erach that u ose with that cut and try to optimize this
        # normalized them as well as well so u can add them together because otherwize we dont have same number of events and it doesnt work for the bins 
        #Then we can send in condor jobs do cd/condor 
        # all interesting proceses wz bb qq. files will be in eos/user/g/gidaniel
        # to send in jobs do python3 send_all.py condor_q to check whats going on condor rm gidaniel to remove everythign
        # ls std/condor.1231753 does something 
        # df = df.Alias("Particle0",           "Particle#0.index"); 
        # df = df.Alias("Particle0",           "_Particle_parents.index");    
        # df = df.Alias("Particle1",           "Particle#1.index");    
        # df = df.Alias("Particle1",           "_Particle_daughters.index");    
        df = df.Alias("MCParticles",         "Particle");     

        df = df.Alias("MCRecoAssociations0", "MCRecoAssociations#0.index"); 
        df = df.Alias("MCRecoAssociations1", "MCRecoAssociations#1.index");
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
        df = df.Define(f"jets_R5_pflavor_unfiltered", "JetTaggingUtils::get_flavour({}, Particle)".format(jetClusteringHelper_R5.jets) )
        
        
        df = df.Define(f"jets_R5_p_unfiltered",           "JetClusteringUtils::get_p({})".format(jetClusteringHelper_R5.jets))
        df=df.Define(f"jets_R5_p_unfiltered_size", "jets_R5_p_unfiltered.size()")
        df = df.Define(f"jets_R5_theta_unfiltered",       "JetClusteringUtils::get_theta({})".format(jetClusteringHelper_R5.jets))
        df=df.Define(f"jets_R5_tlv_unfiltered",           "JetConstituentsUtils::compute_tlv_jets({})".format(jetClusteringHelper_R5.jets))
        df=df.Define(f"PseudoJetCollection_masked", f"{jetClusteringHelper_R5.jets}")
        df = df.Define("remaining_muons_tlv", "FCCAnalyses::ReconstructedParticle::get_tlv(muons_sel_iso)")
        df = df.Define("remaining_electrons_tlv", "FCCAnalyses::ReconstructedParticle::get_tlv(electrons_sel_iso)")
        df=df.Define("merged_iso_muons_electrons", "FCCAnalyses::ReconstructedParticle::merge(muons_sel_iso, electrons_sel_iso)")
        df=df.Define("merged_iso_muons_electrons_tlv", "FCCAnalyses::ReconstructedParticle::get_tlv(merged_iso_muons_electrons)")
        df=df.Define("jet_lep_deltaR", "FCCAnalyses::TruthMatching::Delta_R_calc(jets_R5_tlv_unfiltered, merged_iso_muons_electrons_tlv)")

        df = df.Define("Jets_R5_filtered", """
            ROOT::VecOps::RVec<fastjet::PseudoJet> result;
            for (size_t i = 0; i < jets_R5_tlv_unfiltered.size(); ++i) {
                bool overlaps = false;
                for (size_t j = 0; j < merged_iso_muons_electrons_tlv.size(); ++j) {
                    float dR = jets_R5_tlv_unfiltered[i].DeltaR(merged_iso_muons_electrons_tlv[j]);
                    if (dR < 0.5) {
                        overlaps = true;
                        break;
                    }
                }
                if (!overlaps) {
                    result.push_back(PseudoJetCollection_masked[i]);
                }
            }
            return result;
        """)



        




        # df = df.Define("jets_R5_tlv", "jets_R5_tlv_filtered")
       


        if saveExclJets:    df = jetFlavourHelper.define(df)
        
        df = jetFlavourHelper_R5.define(df)
        ## tagger inference
        if  saveExclJets: df = jetFlavourHelper.inference(weaver_preproc, weaver_model, df)
        df = jetFlavourHelper_R5.inference(weaver_preproc, weaver_model,df)

        df = df.Define("jets_R5_isB","recojet_isB_R5")
        df = df.Define("jets_R5_isC","recojet_isC_R5")
        df = df.Define("jets_R5_isU","recojet_isU_R5")
        df = df.Define("jets_R5_isD","recojet_isD_R5")
        df = df.Define("jets_R5_isG","recojet_isG_R5")
        df = df.Define("jets_R5_isS","recojet_isS_R5")
        df = df.Define("jets_R5_isTAU","recojet_isTAU_R5")



       
        # df=df.Filter("jets_R5_tlv_filtered")

    
        # df= df.Filter("isOverlapping_muons || isOverlapping_electrons")
        
       
        
        df=df.Define("jets_R5_pflavor", "JetTaggingUtils::get_flavour(Jets_R5_filtered, Particle)")
        
        # df=df.Define("masked_jet_constitutents", f"{jetClusteringHelper_R5.constituents}")

        df=df.Define("jets_R5_eta", "JetClusteringUtils::get_eta(Jets_R5_filtered)")
        df=df.Define("jets_R5_phi", "JetClusteringUtils::get_phi(Jets_R5_filtered)")
        df=df.Define("jets_R5_pt", "JetClusteringUtils::get_pt(Jets_R5_filtered)")
        df=df.Define("jets_R5_m", "JetClusteringUtils::get_m(Jets_R5_filtered)")
        df=df.Define("jets_R5_e", "JetClusteringUtils::get_e(Jets_R5_filtered)")
        df=df.Define(f"jets_R5_tlv", "JetConstituentsUtils::compute_tlv_jets(Jets_R5_filtered)")
        df=df.Define(f"jets_R5_p", "JetClusteringUtils::get_p(Jets_R5_filtered)")
        df=df.Define(f"jets_R5_theta", "JetClusteringUtils::get_theta(Jets_R5_filtered)")
        
        
        # df=df.Define("masked_jet_constituents", "FCCAnalyses::JetClusteringUtils::get_constituents(PseudoJetCollection_masked)")
        # df= df.Define("jet_mother_stuff", "FCCAnalyses::TruthMatching::getJetMotherPdgId(PseudoJetCollection_masked, MCParticles, MCRecoAssociations1, MCRecoAssociations1, ReconstructedParticlesNoMuNoEl,Particle0,Particle1)")
        # df=df.Define("jet_daughter_stuff", "jet_mother_stuff.first")
        # df=df.Define("jet_mother_pdg_id", "jet_mother_stuff.second")
        # This collection is masked so that I can use the masked.jets in the other functions that require it like the sel_tag where u need the jet collection 
        # without the masked jet collection the pflavor indicies are different then when u call the jetClusteringHelper_R5.jets so it doesnt work but this works perfectly
    
        # df=df.Define("jets_R5_pflavor_truth_matched", "FCCAnalyses::TruthMatching::jetTruthFinder(masked_jet_constitutents, ReconstructedParticlesNoMuNoEl, Particle, MCRecoAssociations1)")






    
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
        df = df.Define("jets_R5_btagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_btag_true,Jets_R5_filtered)")
        df = df.Define("jets_R5_ctagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_ctag_true,Jets_R5_filtered)")
        df = df.Define("jets_R5_ltagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_ltag_true,Jets_R5_filtered)")
        df = df.Define("jets_R5_gtagged_true", "JetTaggingUtils::sel_tag(true)(jets_R5_gtag_true,Jets_R5_filtered)")

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


        

        # df = df.Define(f"jets_R5_isB_true_b", "jets_R5_isB[jets_R5_btag_true]")
        # df = df.Define(f"jets_R5_isC_true_b", "jets_R5_isC[jets_R5_btag_true]")
        # df = df.Define(f"jets_R5_isU_true_b", "jets_R5_isU[jets_R5_btag_true]")
        # df = df.Define(f"jets_R5_isD_true_b", "jets_R5_isD[jets_R5_btag_true]")
        # df = df.Define(f"jets_R5_isG_true_b", "jets_R5_isG[jets_R5_btag_true]")
        # df = df.Define(f"jets_R5_isS_true_b", "jets_R5_isB[jets_R5_btag_true]")
        # df = df.Define(f"jets_R5_isTau_true_b", "jets_R5_isTAU[jets_R5_btag_true]")

        # df=df.Define(f"jets_R5_isC_true_c", "jets_R5_isC[jets_R5_ctag_true]")
        # df=df.Define(f"jets_R5_isB_true_c", "jets_R5_isB[jets_R5_ctag_true]")
        # df=df.Define(f"jets_R5_isU_true_c", "jets_R5_isU[jets_R5_ctag_true]")
        # df=df.Define(f"jets_R5_isD_true_c", "jets_R5_isD[jets_R5_ctag_true]")
        # df=df.Define(f"jets_R5_isG_true_c", "jets_R5_isG[jets_R5_ctag_true]")
        # df=df.Define(f"jets_R5_isS_true_c", "jets_R5_isS[jets_R5_ctag_true]")
        # df=df.Define(f"jets_R5_isTau_true_c", "jets_R5_isTAU[jets_R5_ctag_true]")
        
    
        return df

    # __________________________________________________________
    # Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        print('incl jets',jetFlavourHelper_R5.outputBranches())
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