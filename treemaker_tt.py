import os, copy

# list of processes
processList = {
    "wzp6_ee_WbWb_semihad_ecm345": {
        "fraction": 1,
        "crossSection": 1,
    },
    
    "wzp6_ee_WbWb_semihad_ecm350": {
        "fraction": 1,
        "crossSection": 1,
    },

    "wzp6_ee_WbWb_semihad_ecm355": {
        "fraction": 1,
        "crossSection": 1,
    },
    
}

# Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics (mandatory)
#prodTag     = "FCCee/winter2023/IDEA/"

#Optional: output directory, default is local running directory
outputDir   = "./outputs/treemaker/tt/acceptance_atleast1_genlep_status1_ptgt5"


# additional/costom C++ functions, defined in header files (optional)
includePaths = ["examples/functions.h"]

## latest particle transformer model, trained on 9M jets in winter2023 samples
model_name = "fccee_flavtagging_edm4hep_wc_v1"

## model files needed for unit testing in CI

## model files locally stored on /eos
eos_dir ="/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/IDEA/"
samples=["wzp6_ee_WbWb_semihad_ecm350"]#wzp6_ee_WbWb_lep_ecm350","wzp6_ee_WbWb_lep_ecm355","wzp6_ee_WbWb_had_ecm355","wzp6_ee_WbWb_lep_ecm345","wzp6_ee_WbWb_had_ecm350","wzp6_ee_WbWb_had_ecm345","wzp6_ee_WbWb_semihad_ecm350","wzp6_ee_WbWb_ecm350","wzp6_ee_WbWb_semihad_ecm355","wzp6_ee_WbWb_ecm355","wzp6_ee_WbWb_semihad_ecm345","wzp6_ee_WbWb_ecm345","wzp6_ee_SM_tt_tWsTWb_tlepTall_ecm365","wzp6_ee_SM_tt_tWsTWb_tlightTall_ecm365","wzp6_ee_SM_tt_tWsTWb_theavyTall_ecm365","wzp6_ee_SM_tt_tWbTWs_tallTlep_ecm365","wzp6_ee_SM_tt_tWbTWs_tallTlight_ecm365","wzp6_ee_SM_tt_tWbTWs_tallTheavy_ecm365"]


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

#files_In=get_files(eos_dir,samples[0])
inputDir    = eos_dir#get_files(eos_dir,samples[0])
#from addons.ONNXRuntime.jetFlavourHelper import JetFlavourHelper
from addons.FastJet.jetClusteringHelper import (
    ExclusiveJetClusteringHelper,
)

#jetFlavourHelper = None
jetClusteringHelper = None


# Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis:

    # __________________________________________________________
    # Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):

        # __________________________________________________________
        # Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2

        # define some aliases to be used later on
        df = df.Alias("Particle0", "Particle#0.index")
        df = df.Alias("Particle1", "Particle#1.index")
        df = df.Alias("MCRecoAssociations0", "MCRecoAssociations#0.index")
        df = df.Alias("MCRecoAssociations1", "MCRecoAssociations#1.index")
        df = df.Alias("Muon0", "Muon#0.index")
        df = df.Alias("Jet0", "Jet#0.index")
        df = df.Alias("Electron0","Electron#0.index")

        # get all the leptons from the collection
        df = df.Define(
            "muons_all",
            "FCCAnalyses::ReconstructedParticle::get(Muon0, ReconstructedParticles)",
        )
        df = df.Define(
            "electrons_all",
            "FCCAnalyses::ReconstructedParticle::get(Electron0, ReconstructedParticles)",
        )
        df = df.Define(
            "jets_all",
            "FCCAnalyses::ReconstructedParticle::get(Jet0, ReconstructedParticles)",
        )
        

        # select leptons with momentum > 20 GeV
        df = df.Define(
            "muons",
            "FCCAnalyses::ReconstructedParticle::sel_p(20)(muons_all)",
        )
        df = df.Define(
            "muons_p", "FCCAnalyses::ReconstructedParticle::get_p(muons)"
        )

        df = df.Define(
            "electrons",
            "FCCAnalyses::ReconstructedParticle::sel_p(20)(electrons_all)",
        )
        df = df.Define(
            "electrons_p", "FCCAnalyses::ReconstructedParticle::get_p(electrons)"
        )

        df = df.Define(
            "jets",
            "FCCAnalyses::ReconstructedParticle::sel_p(10)(jets_all)",
        )
#        df = df.Define(
 #           "jets_p", "FCCAnalyses::ReconstructedParticle::get_p(jets)"
  #      )

        
        df = df.Define(
            "muons_theta",
            "FCCAnalyses::ReconstructedParticle::get_theta(muons)",
        )
        df = df.Define(
            "muons_phi",
            "FCCAnalyses::ReconstructedParticle::get_phi(muons)",
        )
        df = df.Define(
            "muons_q",
            "FCCAnalyses::ReconstructedParticle::get_charge(muons)",
        )
        df = df.Define(
            "muons_no", "FCCAnalyses::ReconstructedParticle::get_n(muons)",
        )
        # compute the muon isolation and store muons with an isolation cut of 0df = df.25 in a separate column muons_sel_iso
        df = df.Define(
            "muons_iso",
            "FCCAnalyses::ZHfunctions::coneIsolation(0.01, 0.5)(muons, ReconstructedParticles)",
        )
        df = df.Define(
            "muons_sel_iso",
            "FCCAnalyses::ZHfunctions::sel_iso(0.25)(muons, muons_iso)",
        )

        df = df.Define(
            "electrons_theta",
            "FCCAnalyses::ReconstructedParticle::get_theta(electrons)",
        )
        df = df.Define(
            "electrons_phi",
            "FCCAnalyses::ReconstructedParticle::get_phi(electrons)")
        df = df.Define(
            "electrons_q",
            "FCCAnalyses::ReconstructedParticle::get_charge(electrons)")
        df = df.Define(
            "electrons_no", "FCCAnalyses::ReconstructedParticle::get_n(electrons)"
        )
        # compute the muon isolation and store electrons with an isolation cut of 0df = df.25 in a separate column electrons_sel_iso
        df = df.Define(
            "electrons_iso",
            "FCCAnalyses::ZHfunctions::coneIsolation(0.01, 0.5)(electrons, ReconstructedParticles)",
        )
        df = df.Define(
            "electrons_sel_iso",
            "FCCAnalyses::ZHfunctions::sel_iso(0.25)(electrons, electrons_iso)",
        )
        #df = df.Define("status2", "FCCAnalyses::MCParticle::sel_genStatus(2)(Particle)")

        df = df.Define("gen_muons",                       "FCCAnalyses::MCParticle::sel_pdgID(13, true)(Particle)")
        df = df.Define("gen_electrons",                   "FCCAnalyses::MCParticle::sel_pdgID(11, true)(Particle)")
        df = df.Define("gen_electrons_status1",           "FCCAnalyses::MCParticle::sel_genStatus(1)(gen_electrons)") 
        df = df.Define("ngen_electrons_status1",          "FCCAnalyses::MCParticle::get_n(gen_electrons_status1)")
        df = df.Define("gen_muons_status1",               "FCCAnalyses::MCParticle::sel_genStatus(1)(gen_muons)") 
        df = df.Define("ngen_muons_status1",              "FCCAnalyses::MCParticle::get_n(gen_muons_status1)")        
        df = df.Define("ngen_leps_status1",               "ngen_muons_status1+ngen_electrons_status1")


        df = df.Define("gen_electrons_status1_ptgt20",           "FCCAnalyses::MCParticle::sel_pt(5)(gen_electrons_status1)") 
        df = df.Define("ngen_electrons_status1_ptgt20",          "FCCAnalyses::MCParticle::get_n(gen_electrons_status1_ptgt20)")


        df = df.Define("gen_muons_status1_ptgt20",           "FCCAnalyses::MCParticle::sel_pt(5)(gen_muons_status1)",) 
        df = df.Define("ngen_muons_status1_ptgt20",          "FCCAnalyses::MCParticle::get_n(gen_muons_status1_ptgt20)",)
        df = df.Define("ngen_leps_status1_ptgt20",           "ngen_muons_status1_ptgt20+ngen_electrons_status1_ptgt20")

        
        df = df.Define("gen_el_status1_e",  "FCCAnalyses::MCParticle::get_e(gen_electrons_status1)")
        df = df.Define("gen_el_status1_p",  "FCCAnalyses::MCParticle::get_p(gen_electrons_status1)")
        df = df.Define("gen_el_status1_pt", "FCCAnalyses::MCParticle::get_pt(gen_electrons_status1)")
        df = df.Define("gen_el_status1_px", "FCCAnalyses::MCParticle::get_px(gen_electrons_status1)")
        df = df.Define("gen_el_status1_py", "FCCAnalyses::MCParticle::get_py(gen_electrons_status1)")
        df = df.Define("gen_el_status1_pz", "FCCAnalyses::MCParticle::get_pz(gen_electrons_status1)")

        df = df.Define("gen_mu_status1_e",  "FCCAnalyses::MCParticle::get_e(gen_muons_status1)")
        df = df.Define("gen_mu_status1_p",  "FCCAnalyses::MCParticle::get_p(gen_muons_status1)")
        df = df.Define("gen_mu_status1_pt", "FCCAnalyses::MCParticle::get_pt(gen_muons_status1)")
        df = df.Define("gen_mu_status1_px", "FCCAnalyses::MCParticle::get_px(gen_muons_status1)")
        df = df.Define("gen_mu_status1_py", "FCCAnalyses::MCParticle::get_py(gen_muons_status1)")
        df = df.Define("gen_mu_status1_pz", "FCCAnalyses::MCParticle::get_pz(gen_muons_status1)")

        
        df  = df.Define('genUquarks',    'FCCAnalyses::MCParticle::sel_pdgID(1, true)(Particle)')
        df  = df.Define('genDquarks',    'FCCAnalyses::MCParticle::sel_pdgID(2, true)(Particle)')
        df  = df.Define('genSquarks',    'FCCAnalyses::MCParticle::sel_pdgID(3, true)(Particle)')
        df  = df.Define('genCquarks',    'FCCAnalyses::MCParticle::sel_pdgID(4, true)(Particle)')
        df  = df.Define('genBquarks',    'FCCAnalyses::MCParticle::sel_pdgID(5, true)(Particle)')        


        df = df.Define("ngen_uQs","FCCAnalyses::MCParticle::get_n(genUquarks)")
        df = df.Define("ngen_dQs","FCCAnalyses::MCParticle::get_n(genDquarks)")
        df = df.Define("ngen_sQs","FCCAnalyses::MCParticle::get_n(genSquarks)")
        df = df.Define("ngen_cQs","FCCAnalyses::MCParticle::get_n(genCquarks)")
        df = df.Define("ngen_bQs","FCCAnalyses::MCParticle::get_n(genBquarks)")


        

        df = df.Define("ngen_partons","ngen_uQs+ngen_dQs+ngen_sQs+ngen_cQs+ngen_bQs");
        df = df.Define("gen_uQs_ptgt10","FCCAnalyses::MCParticle::sel_pt(10)(genUquarks)")
        df = df.Define("gen_dQs_ptgt10","FCCAnalyses::MCParticle::sel_pt(10)(genDquarks)")
        df = df.Define("gen_sQs_ptgt10","FCCAnalyses::MCParticle::sel_pt(10)(genSquarks)")
        df = df.Define("gen_cQs_ptgt10","FCCAnalyses::MCParticle::sel_pt(10)(genCquarks)")
        df = df.Define("gen_bQs_ptgt10","FCCAnalyses::MCParticle::sel_pt(10)(genBquarks)")
        df = df.Define("ngen_uQs_ptgt10","FCCAnalyses::MCParticle::get_n(gen_uQs_ptgt10)")
        df = df.Define("ngen_dQs_ptgt10","FCCAnalyses::MCParticle::get_n(gen_dQs_ptgt10)")
        df = df.Define("ngen_sQs_ptgt10","FCCAnalyses::MCParticle::get_n(gen_sQs_ptgt10)")
        df = df.Define("ngen_cQs_ptgt10","FCCAnalyses::MCParticle::get_n(gen_cQs_ptgt10)")
        df = df.Define("ngen_bQs_ptgt10","FCCAnalyses::MCParticle::get_n(gen_bQs_ptgt10)")
        df = df.Define("ngen_partons_ptgt10","ngen_uQs_ptgt10+ngen_dQs_ptgt10+ngen_sQs_ptgt10+ngen_cQs_ptgt10+ngen_bQs_ptgt10");
        
        
        df_fullyLep = df.Filter("(muons_no + electrons_no) == 2 && (muons_sel_iso.size() + electrons_sel_iso.size()) == 2")
        #df_semiLep  = df.Filter("(muons_no + electrons_no) == 1 && (muons_sel_iso.size() + electrons_sel_iso.size()) == 1")
        #df           = df.Filter("(muons_no + electrons_no) == 1 && (muons_sel_iso.size() + electrons_sel_iso.size()) == 1") # && gen_leps_no > 0")
        #df_had       = df.Filter("(muons_no + electrons_no) == 0 && (muons_sel_iso.size() + electrons_sel_iso.size()) == 0")
        df           = df.Filter("(ngen_muons_status1_ptgt20 + ngen_electrons_status1_ptgt20 >0)") # && ngen_partons > 3") #_ptgt10 > 3")
        #df           = df.Filter("ngen_electrons_status1_ptgt20 ==1 ")#+ ngen_electrons_status1 ==1)")# && ngen_partons > 3") #_ptgt10 > 3")
        df           = df.Define("genleps_status1","ngen_muons_status1_ptgt20 > ngen_electrons_status1_ptgt20  ? gen_muons_status1_ptgt20 : gen_electrons_status1_ptgt20");



        
        ## here cluster jets in the events but first remove muons from the list of
        ## reconstructed particles
        
        ## create a new collection of reconstructed particles removing muons with p>20
        df = df.Define(
            "ReconstructedParticlesNoMuons",
            "FCCAnalyses::ReconstructedParticle::remove(ReconstructedParticles,muons)",
        )
        df = df.Define(
            "ReconstructedParticlesNoMuNoEl",
            "FCCAnalyses::ReconstructedParticle::remove(ReconstructedParticlesNoMuons,electrons)",
        )

        #        df = df.Define("n_gen_lep","gen_muons.size()+gen_electrons.size()");

        ## perform N=2 jet clustering
        global jetClusteringHelper
        #        global jetFlavourHelper

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

        collections_noleps = copy.deepcopy(collections)
        collections_noleps["PFParticles"] = "ReconstructedParticlesNoMuNoEl"
        
        jetClusteringHelper = ExclusiveJetClusteringHelper(
            collections_noleps["PFParticles"], 5
        )
        df = jetClusteringHelper.define(df)

        ## define jet flavour tagging parameters

        #jetFlavourHelper = JetFlavourHelper(
        #    collections_noleps,
        #    jetClusteringHelper.jets,
        #    jetClusteringHelper.constituents,
        #)


        #df  = df.Filter("event_njet > 4")
        df = df.Define(
            "lep_p", "muons_sel_iso.size() >0 ? FCCAnalyses::ReconstructedParticle::get_p(muons)[0] : (electrons_sel_iso.size() > 0 ? FCCAnalyses::ReconstructedParticle::get_p(electrons)[0] : -9999) "
        )  # momentum of the mu
        df = df.Define(
            "nlep",
            "electrons_sel_iso.size()+muons_sel_iso.size()")
        
        df = df.Define(
            "missingEnergy",
            "FCCAnalyses::ZHfunctions::missingEnergy(350., ReconstructedParticles)",
        )
        # .Define("cosTheta_miss", "FCCAnalyses::get_cosTheta_miss(missingEnergy)")
        df = df.Define(
            "cosTheta_miss",
            "FCCAnalyses::ZHfunctions::get_cosTheta_miss(MissingET)",
        )

        df = df.Define(
            "missing_p",
            "FCCAnalyses::ReconstructedParticle::get_p(MissingET)",
        )
        

        #########
        ### CUT 3: Njets > 1
        #########
        #df = df.Filter("event_njet > 1")
        
        df = df.Define(
            "jets_p4",
            "JetConstituentsUtils::compute_tlv_jets({})".format(
                jetClusteringHelper.jets
            ),
        )
        df = df.Define("jet1", "jets_p4[0]")
        df = df.Define("jet2", "jets_p4[1]")
        df = df.Define("jet3", "jets_p4[2]")
        df = df.Define("jet4", "jets_p4[3]")
        df = df.Define("jet1_p","jet1.P()")
        df = df.Define("jet2_p","jet2.P()")
        df = df.Define("jet3_p","jet3.P()")
        df = df.Define("jet4_p","jet4.P()")
        df = df.Define("jet5_p","jets_p4.size()>4 ? jets_p4[4].P() : -999")
        df = df.Define("recojet_theta", "JetClusteringUtils::get_theta(jet)")
        df = df.Define("jet1_theta","recojet_theta[0]")
        df = df.Define("jet2_theta","recojet_theta[1]")
        df = df.Define("jet3_theta","recojet_theta[2]")
        df = df.Define("jet4_theta","recojet_theta[3]")
        df = df.Define("jet5_theta","jets_p4.size()>4 ? recojet_theta[4] : -999")
        df = df.Define("njets", "jets_p4.size()")
        df = df.Define("d_12", "JetClusteringUtils::get_exclusive_dmerge(_jet, 1)")
        df = df.Define("d_23", "JetClusteringUtils::get_exclusive_dmerge(_jet, 2)")
        df = df.Define("d_34", "JetClusteringUtils::get_exclusive_dmerge(_jet, 3)")
        df = df.Define("d_45", "jets_p4.size()>4 ? JetClusteringUtils::get_exclusive_dmerge(_jet, 4) : -999")
        #        df = df .Define("d_45{}".format(anatag), "JetClusteringUtils::get_exclusive_dmerge(_jet{}, 4)".format(anatag))
 
        df = df.Define("gen_lep_status1_p",      "FCCAnalyses::MCParticle::get_p(genleps_status1)")
        df = df.Define("gen_lep_status1_theta",  "FCCAnalyses::MCParticle::get_theta(genleps_status1)")
        df = df.Define("gen_lep_status1_phi",    "FCCAnalyses::MCParticle::get_phi(genleps_status1)")
        df = df.Define("gen_lep_status1_charge", "FCCAnalyses::MCParticle::get_charge(genleps_status1)")
        df = df.Define("gen_lep_status1_pdgId",  "FCCAnalyses::MCParticle::get_pdg(genleps_status1)")


##am        df = df.Define("jet_v1_p", "jet1.p()")
##am        df = df.Define("jet_v1_m", "jet1.M()")
        
        return df

    # __________________________________________________________
    # Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            "nlep",
            "lep_p",
            "njets",
            "jet1_p",
            "jet2_p", "jet3_p","jet4_p","jet5_p",
            "jet1_theta",
            "jet2_theta", "jet3_theta","jet4_theta","jet5_theta",
            "cosTheta_miss",
            "missing_p",
            "d_12","d_23","d_34","d_45","ngen_leps_status1_ptgt20",
            "ngen_partons","ngen_partons_ptgt10",
            "ngen_cQs","ngen_sQs","ngen_bQs","ngen_dQs","ngen_uQs",
            "ngen_muons_status1",
            "ngen_electrons_status1",
            "ngen_leps_status1", 
            "gen_el_status1_e", 
            "gen_el_status1_p", 
            "gen_el_status1_pt",
            "gen_el_status1_px",
            "gen_el_status1_py",
            "gen_el_status1_pz",
            "gen_mu_status1_e", 
            "gen_mu_status1_p", 
            "gen_mu_status1_pt",
            "gen_mu_status1_px",
            "gen_mu_status1_py",
            "gen_mu_status1_pz",
            "gen_lep_status1_p",      
            "gen_lep_status1_theta",  
            "gen_lep_status1_phi",    
            "gen_lep_status1_charge", 
            "gen_lep_status1_pdgId",  
        ]
        branchList += jetClusteringHelper.outputBranches()

        ## outputs jet scores and constituent breakdown
        #branchList += jetFlavourHelper.outputBranches()

        return branchList
