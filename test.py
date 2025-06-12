import uproot 
import pandas as pd
import awkward as ak
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import boost_histogram as bh
import os

file = uproot.open("/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/wzp6_ee_WbWb_ecm345.root")
events= file["events;1"]
# print(events.keys())
arrays=events.arrays(["D_Iso_Values_Prompt","D_Iso_Values_nonPrompt","n_leps_d_iso_prompt_precut","n_leps_d_iso_non_prompt_precut","n_leps_d_iso_all_precut_status1",
                    "D_Iso_Values_all_status1","gen_leps_status1_mother_pdgId_prompt","gen_leps_status1_mother_pdgId_non_prompt",  "gen_leps_status1_from_b_pdgId","ngen_leps_status1_from_b","ngen_leps_status1_fromW","gen_leps_status1_pdgId",
                    "nbjets_R5_true", "ncjets_R5_true","nljets_R5_true","ngjets_R5_true","njets_R5", "size_gen_leps_status1_fromW",
                    "jet1_R5_isB","jet2_R5_isB","jet3_R5_isB","jet4_R5_isB","jet5_R5_isB","jet6_R5_isB",  
                    "jet1_R5_isC","jet2_R5_isC","jet3_R5_isC","jet4_R5_isC","jet5_R5_isC","jet6_R5_isC",
                    "jet1_R5_pflavor", "jet2_R5_pflavor", "jet3_R5_pflavor", "jet4_R5_pflavor", "jet5_R5_pflavor","jet6_R5_pflavor",
                    "bjets_R5_true","ljets_R5_true",
                     "jet1_R5_isG","jet2_R5_isG","jet3_R5_isG","jet4_R5_isG","jet5_R5_isG","jet6_R5_isG",                
                    "jet1_R5_isU","jet2_R5_isU","jet3_R5_isU","jet4_R5_isU","jet5_R5_isU","jet6_R5_isU", 
                    "jet1_R5_isS","jet2_R5_isS","jet3_R5_isS","jet4_R5_isS","jet5_R5_isS","jet6_R5_isS",

                    "jet1_R5_isD","jet2_R5_isD","jet3_R5_isD","jet4_R5_isD","jet5_R5_isD","jet6_R5_isD",                                
                    "jet1_R5_isTAU","jet2_R5_isTAU","jet3_R5_isTAU","jet4_R5_isTAU","jet5_R5_isTAU","jet6_R5_isTAU","remaining_leptons_p",
                    "remaining_muons_p","remaining_electrons_p","remaining_leptons_merged_size", "jets_R5_p_unfiltered_size","jets_R5_p_size",
                    "remaining_leptons_merged", "jets_R5_theta_unfiltered","jets_R5_pflavor","jets_R5_pflavor_unfiltered",  "jet_mother_pdg_id", "jet_daughter_stuff","muons_all_p", "electrons_all_p",
                 





                    "size_gen_leps_status1_from_b","combined_leptons_per_event","nlep","nlep_total","gen_leps_status1_p_W","gen_leps_status1_from_b_p",
                    "gen_leps_status1_from_b_muons_p","gen_leps_status1_fromW_muons_p", "gen_leps_status1_from_b_electrons_p","gen_leps_status1_fromW_electrons_p",
                "matched_leps_status1_from_b_muons_p_cut_coneIso_2", "matched_leps_status1_from_b_muons_p_cut_coneIso_3", "matched_leps_status1_from_b_muons_p_cut_coneIso_4", "matched_leps_status1_from_b_muons_p_cut_coneIso_5", "matched_leps_status1_from_b_electrons_p_cut_coneIso_2", "matched_leps_status1_from_b_electrons_p_cut_coneIso_3", "matched_leps_status1_from_b_electrons_p_cut_coneIso_4",
     "matched_leps_status1_from_b_electrons_p_cut_coneIso_5", "matched_leps_status1_from_W_muons_p_cut_coneIso_2", "matched_leps_status1_from_W_muons_p_cut_coneIso_3",
      "matched_leps_status1_from_W_muons_p_cut_coneIso_4", "matched_leps_status1_from_W_muons_p_cut_coneIso_5",
      "matched_leps_status1_from_W_electrons_p_cut_coneIso_2", "matched_leps_status1_from_W_electrons_p_cut_coneIso_3", "matched_leps_status1_from_W_electrons_p_cut_coneIso_4",
      "matched_leps_status1_from_W_electrons_p_cut_coneIso_5","remaining_muons_deltaR","remaining_electrons_deltaR","jets_R5_tlv","jets_R5_p","jets_R5_theta", "E_RP_TRK_Z0_pcut","electrons_iso","electrons_sel","muons_iso", "Mu_RP_TRK_Z0_pcut",
      "e_rp_trk_p", "W_boson_origin", "E_RP_TRK_Z0_pcut_iso_cut", "Mu_RP_TRK_Z0_pcut_iso_cut", "W_bosons_pdgId", "bjets_R5_WPp9", "bjets_R5_WPp8","bjets_R5_WPp5", "bjets_R5_WPp85", "nbjets_R5_WPp5","nbjets_R5_WPp8","nbjets_R5_WPp85","nbjets_R5_WPp9","bjets_R5_true_theta",
      "jets_R5_isC","jets_R5_isU","jets_R5_isD","jets_R5_isB",
    
      ], how=dict,)

W_bosons_pdgId=arrays["W_bosons_pdgId"]
W_boson_origin=arrays["W_boson_origin"]
# print(ak.flatten(W_boson_origin),"min W_boson_origin")
# for i in range(0,len(ak.flatten(W_boson_origin))):
#     if ak.flatten(W_boson_origin)[i]!=np.abs(11):
#         print(i,"i")

# for i in range(0,len(ak.flatten(W_boson_origin))):
#     if ak.flatten(W_boson_origin)[i]!=np.abs(11):
#         print(i,"i")

bjets_R5_WPp9=arrays["bjets_R5_WPp9"]
bjets_R5_WPp8=arrays["bjets_R5_WPp8"]
bjets_R5_WPp5=arrays["bjets_R5_WPp5"]
bjets_R5_WPp85=arrays["bjets_R5_WPp85"]
# print(bjets_R5_WPp9,"bjets_R5_WPp9")
# print(bjets_R5_WPp8,"bjets_R5_WPp8")
# print(bjets_R5_WPp5,"bjets_R5_WPp5")
# print(bjets_R5_WPp85,"bjets_R5_WPp85")

nbjets_R5_WPp9=arrays["nbjets_R5_WPp9"]
nbjets_R5_WPp8=arrays["nbjets_R5_WPp8"]
nbjets_R5_WPp5=arrays["nbjets_R5_WPp5"]
nbjets_R5_WPp85=arrays["nbjets_R5_WPp85"]
# print(nbjets_R5_WPp9,"nbjets_R5_WPp9")
# print(nbjets_R5_WPp8,"nbjets_R5_WPp8")
# print(nbjets_R5_WPp5,"nbjets_R5_WPp5")
# print(nbjets_R5_WPp85,"nbjets_R5_WPp85")



# total_bjets_R5_WPp9=np.sum(bjets_R5_WPp9)
# total_bjets_R5_WPp85=np.sum(bjets_R5_WPp85)
# total_bjets_R5_WPp8=np.sum(bjets_R5_WPp8)
# total_bjets_R5_WPp5=np.sum(bjets_R5_WPp5)

# print(total_bjets_R5_WPp9,"total_bjets_R5_WPp9")
# print(total_bjets_R5_WPp85,"total_bjets_R5_WPp85")
# print(total_bjets_R5_WPp8,"total_bjets_R5_WPp8")
# print(total_bjets_R5_WPp5,"total_bjets_R5_WPp5")


bjets_R5_true=arrays["bjets_R5_true"]
# print(bjets_R5_true,"bjets_R5_true")




ncjets_R5_true=arrays["ncjets_R5_true"]


nljets_R5_true=arrays["nljets_R5_true"]
ngjets_R5_true=arrays["ngjets_R5_true"]
# print(ncjets_R5_true, "ncjets_R5_true")
# print(nljets_R5_true,"nljets_R5_true")
# print(ngjets_R5_true,"ngjets_R5_true")

# print(njets_R5,"njets_R5")


# total_bjets_R5_true=np.sum(bjets_R5_true)
# print(total_bjets_R5_true,"total_bjets_R5_true")

# efficiency_bjets_R5_WPp9=total_bjets_R5_WPp9/total_bjets_R5_true
# efficiency_bjets_R5_WPp85=total_bjets_R5_WPp85/total_bjets_R5_true
# efficiency_bjets_R5_WPp8=total_bjets_R5_WPp8/total_bjets_R5_true
# efficiency_bjets_R5_WPp5=total_bjets_R5_WPp5/total_bjets_R5_true

# print(efficiency_bjets_R5_WPp9,"efficiency_bjets_R5_WPp9")
# print(efficiency_bjets_R5_WPp85,"efficiency_bjets_R5_WPp85")
# print(efficiency_bjets_R5_WPp8,"efficiency_bjets_R5_WPp8")
# print(efficiency_bjets_R5_WPp5,"efficiency_bjets_R5_WPp5")

## inefficiencies are b jets that are tagged as c jets but are really b jets

# jets_R5_ctagged_true=arrays["jets_R5_ctagged_true"]
# print(jets_R5_ctagged_true,"jets_R5_ctagged_true")

# print(ak.flatten(W_bosons_pdgId),"max W_bosons_pdgId")

# jets_R5_pflavor_unfiltered=arrays["jets_R5_pflavor_unfiltered"]

# print(jets_R5_pflavor,"jets_R5_pflavor_from_getflavorfunc")
# jet_mother_pdg_id=arrays["jet_mother_pdg_id"]
# jet_daughter_stuff=arrays["jet_daughter_stuff"]
# print(jet_daughter_stuff,"jet_daughter_stuff")
# jets_R5_p=arrays["jets_R5_p"]





# print(jet_daughter_stuff, "jet_flavor")
# print(jet_mother_pdg_id,"jet_mother_pdg_id")

# for i in range(0,len(ak.flatten(jet_mother_pdg_id))):
#     if ak.flatten(jet_mother_pdg_id)[i]==np.abs(6):
#         print(i,"i")





# D_Iso_Values_all_status1=arrays["D_Iso_Values_all_status1"]
# E_RP_TRK_Z0_pcut=arrays["E_RP_TRK_Z0_pcut"]
# Mu_RP_TRK_Z0_pcut=arrays["Mu_RP_TRK_Z0_pcut"]
# E_RP_TRK_Z0_pcut_iso_cut=arrays["E_RP_TRK_Z0_pcut_iso_cut"]
# Mu_RP_TRK_Z0_pcut_iso_cut=arrays["Mu_RP_TRK_Z0_pcut_iso_cut"]





# electrons_iso=arrays["electrons_iso"]
# electrons_sel=arrays["electrons_sel"]
# muons_iso=arrays["muons_iso"]
# muons_all_p=arrays["muons_all_p"]
# electrons_all_p=arrays["electrons_all_p"]
# e_rp_trk_p=arrays["e_rp_trk_p"]




## maybe do the filling stuff before the p cut idk and do the  d isos before the p cut to see if there is any relation between the d isos and the z0



# gen_leps_status1_mother_pdgId_prompt=arrays["gen_leps_status1_mother_pdgId_prompt"]
# gen_leps_status1_mother_pdgId_non_prompt=arrays["gen_leps_status1_mother_pdgId_non_prompt"]

# print(len(ak.flatten(E_RP_TRK_Z0_pcut)),"E_RP_TRK_Z0_pcut")
# print(len(ak.flatten(Mu_RP_TRK_Z0_pcut)),"Mu_RP_TRK_Z0_pcut")
# print((E_RP_TRK_Z0_pcut_iso_cut), "E_RP_TRK_Z0_pcut_iso_cut")
# print((Mu_RP_TRK_Z0_pcut_iso_cut), "Mu_RP_TRK_Z0_pcut_iso_cut")

# print(ak.flatten(muons_iso), "muons_iso")
# print(ak.flatten(electrons_iso), "electrons_iso")

# Create masks to filter nested lists where the length of Z0_pcut matches the corresponding iso collection
# e_mask = [len(z0_list) == len(iso_list) for z0_list, iso_list in zip(E_RP_TRK_Z0_pcut_iso_cut, electrons_iso)]
# mu_mask = [len(z0_list) == len(iso_list) for z0_list, iso_list in zip(Mu_RP_TRK_Z0_pcut_iso_cut, muons_iso)]

# Apply masks to filter the nested lists
# filtered_E_RP_TRK_Z0_pcut_iso_cut = [lst for lst, keep in zip(E_RP_TRK_Z0_pcut_iso_cut, e_mask) if keep]
# filtered_Mu_RP_TRK_Z0_pcut_iso_cut = [lst for lst, keep in zip(Mu_RP_TRK_Z0_pcut_iso_cut, mu_mask) if keep]
# filtered_electrons_iso = [lst for lst, keep in zip(electrons_iso, e_mask) if keep]
# filtered_muons_iso = [lst for lst, keep in zip(muons_iso, mu_mask) if keep]

# Print the lengths of the filtered collections
# print(len(filtered_E_RP_TRK_Z0_pcut_iso_cut), "filtered_E_RP_TRK_Z0_pcut_iso_cut")
# print(len(filtered_Mu_RP_TRK_Z0_pcut_iso_cut), "filtered_Mu_RP_TRK_Z0_pcut_iso_cut")
# print(len(filtered_electrons_iso), "filtered_electrons_iso")
# print(len(filtered_muons_iso), "filtered_muons_iso")
# print(filtered_E_RP_TRK_Z0_pcut_iso_cut[0],"filtered_E_RP_TRK_Z0_pcut_iso_cut")
# print(filtered_Mu_RP_TRK_Z0_pcut_iso_cut[0],"filtered_Mu_RP_TRK_Z0_pcut_iso_cut")
# print(filtered_electrons_iso[0],"filtered_electrons_iso")
# print(filtered_muons_iso[0],"filtered_muons_iso")


# Create a boost histogram for filtered_E_RP_TRK_Z0_pcut_iso_cut values
# Flatten the nested list to get all Z0 values
# e_z0_values = ak.flatten(E_RP_TRK_Z0_pcut)
# print(max(e_z0_values), "max e_z0_values")
# print(min(e_z0_values), "min e_z0_values")


# # Define histogram with appropriate range and bins
# e_z0_hist = bh.Histogram(bh.axis.Regular(100, -.1, .1), storage=bh.storage.Double())

# # Fill the histogram with the Z0 values
# e_z0_hist.fill(e_z0_values)

# plt.stairs(e_z0_hist.view(), e_z0_hist.axes[0].edges)
# plt.title("Electron Z0 Histogram")
# plt.xlabel("Z0")
# plt.ylabel("Number of Entries")
# plt.savefig("e_z0_hist.pdf")
# plt.close()

# mu_z0_values = ak.flatten(Mu_RP_TRK_Z0_pcut)
# print(max(mu_z0_values), "max mu_z0_values")
# print(min(mu_z0_values), "min mu_z0_values")
# mu_z0_hist = bh.Histogram(bh.axis.Regular(100, -1, 1), storage=bh.storage.Double())
# mu_z0_hist.fill(mu_z0_values)
# plt.stairs(mu_z0_hist.view(), mu_z0_hist.axes[0].edges)
# plt.title("Muon Z0 Histogram")
# plt.xlabel("Z0")
# plt.ylabel("Number of Entries")
# plt.savefig("mu_z0_hist.pdf")
# plt.close()

# # Create 2D histogram for Electron Isolation vs Z0 with color plot
# e_iso_values = ak.flatten(electrons_iso)
# e_z0_iso_hist = bh.Histogram(
#     bh.axis.Regular(50, 0, 5),  # x-axis: electron isolation
#     bh.axis.Regular(50, -0.1, 0.1),  # y-axis: Z0
#     storage=bh.storage.Double()
# )
# e_z0_iso_hist.fill(e_iso_values, e_z0_values)

# plt.figure()
# plt.imshow(
#     e_z0_iso_hist.view().T,  # Transpose to match axis orientation
#     origin='lower',
#     extent=[0, 5, -0.1, 0.1],  # Define the extent of the axes
#     aspect='auto',
#     cmap='viridis'  # Color map for the histogram
# )
# plt.colorbar(label='Number of Entries')
# plt.title("Electron Isolation vs Z0")
# plt.xlabel("Electron Isolation")
# plt.ylabel("Z0")
# plt.savefig("e_iso_vs_z0_hist.pdf")
# plt.close()

# # Create 2D histogram for Muon Isolation vs Z0 with color plot
# mu_iso_values = ak.flatten(muons_iso)
# mu_z0_iso_hist = bh.Histogram(
#     bh.axis.Regular(50, 0, 5),  # x-axis: muon isolation
#     bh.axis.Regular(50, -0.1, 0.1),  # y-axis: Z0
#     storage=bh.storage.Double()
# )
# mu_z0_iso_hist.fill(mu_iso_values, mu_z0_values)

# plt.figure()
# plt.imshow(
#     mu_z0_iso_hist.view().T,  # Transpose to match axis orientation
#     origin='lower',
#     extent=[0, 5, -0.1, 0.1],  # Define the extent of the axes
#     aspect='auto',
#     cmap='viridis'  # Color map for the histogram
# )
# plt.colorbar(label='Number of Entries')
# plt.title("Muon Isolation vs Z0")
# plt.xlabel("Muon Isolation")
# plt.ylabel("Z0")
# plt.savefig("mu_iso_vs_z0_hist.pdf")
# plt.close()




# print(gen_leps_status1_mother_pdgId_prompt,"gen_leps_status1_mother_pdgId_prompt")
# print(gen_leps_status1_mother_pdgId_non_prompt,"gen_leps_status1_mother_pdgId_non_prompt")
# print(muons_all_p,"muons_all_p")
# print(electrons_all_p,"electrons_all_p")
# print(e_rp_trk_p,"e_rp_trk_p")




# print(electrons_sel,"electrons_sel")
# print(D_Iso_Values_all_status1,"D_Iso_Values_all_status1")

# print(svtracks_e_position,"svtracks_e_position")
# print(check_EVertex,"check_EVertex")
# print(check_MVertex,"check_MVertex")

# print(jets_R5_pflavor,"jets_R5_pflavor")
# print(jet_mother_pdg_id,"jet_mother_pdg_id")

# for i in range(0,len(jet_daughter_stuff)):
#     for j in range(0,len(jet_daughter_stuff[i])):
#         if jet_mother_pdg_id[i][j]==5 and jet_daughter_stuff[i][j]==5:
#             print(i,"i")
# print(jet_daughter_stuff,"jet_daughter_stuff")
# print(jets_R5_p[160],"jets_R5_p")
# print(jets_R5_theta[160],"jets_R5_theta")
# for i in range(0,len(jet_mother_pdg_id)):
#     for j in range(0,len(jet_mother_pdg_id[i])):
#         if jet_mother_pdg_id[i][j]==5:
#             print(i,"i")
# print(jets_R5_pflavor_unfiltered,"jets_R5_pflavor_unfiltered")
# print(jets_R5_pflavor[15069],"jets_R5_pflavor")


# test=arrays["test"]
# print(test,"test")


# jets_R5_tlv=arrays["jets_R5_tlv"]

# print(jets_R5_p,"jets_R5_p_filtered")





# jets_R5_pflavor_filtered=arrays["jets_R5_pflavor_filtered"]
# print(jets_R5_pflavor_filtered[1],"jets_R5_pflavor_filtered")
# # print(jets_R5_tlv,"jets_R5_tlv_filtered")

# print(jets_R5_theta,"jets_R5_theta_filtered")




# jets_R5_pflavor_truth_matched= arrays["jets_R5_pflavor_truth_matched"]
# print(jets_R5_pflavor_truth_matched[15069],"jets_R5_pflavor_truth_matched")
# jets_R5_pflavor_truth_matched_flattened=ak.flatten(jets_R5_pflavor_truth_matched)
# for i in jets_R5_pflavor_truth_matched_flattened:
#     if i==6:
#         print(i,"i")

# print(jets_R5_pflavor_truth_matched,"jets_R5_pflavor_truth_matched")

# print(max(remaining_muons_deltaR),"max remaining_muons_deltaR")
# print(max(remaining_electrons_deltaR),"max remaining_electrons_deltaR")
# print(min(remaining_muons_deltaR),"min remaining_muons_deltaR")
# print(min(remaining_electrons_deltaR),"min remaining_electrons_deltaR")
# print(arrays["remaining_muons_deltaR"],"remaining_muons_deltaR_looking at size")
# print(arrays["remaining_electrons_deltaR"],"remaining_electrons_deltaR_looking at size")
# remaining_leptons_merged_deltaR=ak.flatten(arrays["remaining_leptons_merged_deltaR"])


# remaining_leptons_merged_deltaR_min=(arrays["remaining_leptons_merged_deltaR_min"])
# print(remaining_leptons_merged_deltaR_min,"remaining_leptons_merged_deltaR_min")
# print(len(remaining_leptons_merged_deltaR_min),"len remaining_leptons_merged_deltaR_min")

# remaining_leptons_p=(arrays["remaining_leptons_p"])
# # print(remaining_leptons_p,"remaining_leptons_p")
# remaining_muons_p=(arrays["remaining_muons_p"])
# # print(remaining_muons_p[-2],"remaining_muons_p")
# remaining_electrons_p=(arrays["remaining_electrons_p"])
# # print(remaining_electrons_p[-2],"remaining_electrons_p")

# remaining_muons_deltaR = arrays["remaining_muons_deltaR"]
# remaining_electrons_deltaR = arrays["remaining_electrons_deltaR"]
# # print(remaining_muons_deltaR,"remaining_muons_deltaR")
# # print(remaining_electrons_deltaR,"remaining_electrons_deltaR")

# remaining_leptons_merged = arrays["remaining_leptons_merged"]



# Create masks for muons based on deltaR < 0.4
# muons_mask = []
# for i in range(len(remaining_muons_deltaR)):
#     event_muons_mask = []
#     num_jets = len(jets_R5_theta_unfiltered[i]) if len(jets_R5_theta_unfiltered[i]) > 0 else 1  # Avoid zero step size
#     total_muon_entries = len(remaining_muons_deltaR[i])
#     num_muons = total_muon_entries // num_jets if total_muon_entries > 0 else 0
    
#     for muon_idx in range(num_muons):
#         any_deltaR_below_threshold = False
#         start_idx = muon_idx * num_jets
#         end_idx = min(start_idx + num_jets, total_muon_entries)  # Ensure we don't go out of bounds
#         for k in range(start_idx, end_idx):
#             if remaining_muons_deltaR[i][k] < deltaR_label:
#                 any_deltaR_below_threshold = True
#                 break
#         if any_deltaR_below_threshold:
#             event_muons_mask.append(False)  # Mark muon for removal
#         else:
#             event_muons_mask.append(True)   # Keep muon
#     muons_mask.append(event_muons_mask)

# # Create masks for electrons based on deltaR < 0.4
# electrons_mask = []
# for i in range(len(remaining_electrons_deltaR)):
#     event_electrons_mask = []
#     num_jets = len(jets_R5_theta_unfiltered[i]) if len(jets_R5_theta_unfiltered[i]) > 0 else 1  # Avoid zero step size
#     total_electron_entries = len(remaining_electrons_deltaR[i])
#     num_electrons = total_electron_entries // num_jets if total_electron_entries > 0 else 0
http://cern.ch/account    
#     for electron_idx in range(num_electrons):
#         any_deltaR_below_threshold = False
#         start_idx = electron_idx * num_jets
#         end_idx = min(start_idx + num_jets, total_electron_entries)  # Ensure we don't go out of bounds
#         for k in range(start_idx, end_idx):
#             if remaining_electrons_deltaR[i][k] < deltaR_label:
#                 any_deltaR_below_threshold = True
#                 break
#         if any_deltaR_below_threshold:
#             event_electrons_mask.append(False)  # Mark electron for removal
#         else:
#             event_electrons_mask.append(True)   # Keep electron
#     electrons_mask.append(event_electrons_mask)

# # Calculate the number of non-overlapping leptons per event (deltaR >= 0.4)
# non_overlapping_leptons_per_event = []
# for i in range(len(muons_mask)):
#     non_overlapping_muons = sum(1 for mask in muons_mask[i] if mask)
#     non_overlapping_electrons = sum(1 for mask in electrons_mask[i] if mask) if i < len(electrons_mask) else 0
#     non_overlapping_leptons_per_event.append(non_overlapping_muons + non_overlapping_electrons)


# print(non_overlapping_leptons_per_event)
# print(remaining_leptons_merged)

# print(jets_R5_tlv,"jets_R5_tlv")
# print(jets_R5_p[256676],"jets_R5_p 256676")

# print(bjets_R5_true[256676],"bjets_R5_true 256676")
# print(len(ak.flatten(jets_R5_p)),"len jets_R5_p")
# print(jets_R5_theta[-2],"jets_R5_theta")
# print(len(jets_R5_p[-2]),"len jets_R5_p,-2")
# print(len(ak.flatten(jets_R5_theta)),"len jets_R5_theta")






### deltaR between jets and remaining leptons 

# hist_deltaR_muons=bh.Histogram(bh.axis.Regular(200, 0, 5))
# hist_deltaR_electrons=bh.Histogram(bh.axis.Regular(200, 0, 5))
# for i in range(0,len(remaining_muons_deltaR)):
#     hist_deltaR_muons.fill(remaining_muons_deltaR[i])
# for i in range(0,len(remaining_electrons_deltaR)):
#     hist_deltaR_electrons.fill(remaining_electrons_deltaR[i])
# hist_value_muons_deltaR=hist_deltaR_muons.view()
# hist_value_electrons_deltaR= hist_deltaR_electrons.view()

# plt.stairs(hist_value_muons_deltaR, hist_deltaR_muons.axes[0].edges, color="blue", label="Muons")
# plt.stairs(hist_value_electrons_deltaR, hist_deltaR_electrons.axes[0].edges, color="red", label="Electrons")
# plt.title("Delta R between jets and remaining leptons")
# plt.xlabel("Delta R")
# plt.ylabel("Number of DeltaR values")
# plt.legend()
# plt.savefig("deltaR_jets_leptons.pdf")
# plt.close()

### deltaR between jets and remaining leptons 


# print(max(nbjets_R5_true),"max nbjets_R5_true")
# for i in range(0,len(nbjets_R5_true)):
#     if nbjets_R5_true[i]==5 or nbjets_R5_true[i]==6 or nbjets_R5_true[i]==4:
#         print(i,"index_5_jets")
# print(nbjets_R5_true[256676],"nbjets_R5_true[256676]")
# for i in range(0,len(nbjets_R5_true)):
#     if nbjets_R5_true[i]==6:
#         print(i,"index_6_jets")


        #256676 index_6_jets only event with 6 jets
# print(nbjets_R5_true,"nbjets_R5_true")
# print(ncjets_R5_true,"ncjets_R5_true")
# print(nljets_R5_true,"nljets_R5_true")
# print(ngjets_R5_true,"ngjets_R5_true")
# print(njets_R5,"njets_R5")
# print(min(nbjets_R5_true),"min nbjets_R5_true")







# bjets_R5_true=arrays["bjets_R5_true"]
# # jets_R5_ctagged_true=arrays["jets_R5_ctagged_true"]
# ljets_R5_true=arrays["ljets_R5_true"]
# # jets_R5_gtagged_true=arrays["jets_R5_gtagged_true"]

# print(bjets_R5_true,"bjets_R5_true")
# # print(jets_R5_ctagged_true,"jets_R5_ctagged_true")
# print(ljets_R5_true,"ljets_R5_true")
# print(jets_R5_gtagged_true,"jets_R5_gtagged_true")



### is B jet score
jet1_R5_isB=arrays["jet1_R5_isB"]
jet2_R5_isB=arrays["jet2_R5_isB"]
jet3_R5_isB=arrays["jet3_R5_isB"]
jet4_R5_isB=arrays["jet4_R5_isB"]
jet5_R5_isB=arrays["jet5_R5_isB"]
jet6_R5_isB=arrays["jet6_R5_isB"]

# print(jet1_R5_isB[256676],"jet1_R5_isB")
# print(jet2_R5_isB[256676],"jet2_R5_isB")
# print(jet3_R5_isB[256676],"jet3_R5_isB")
# print(jet4_R5_isB[256676],"jet4_R5_isB")
# print(jet5_R5_isB[256676],"jet5_R5_isB")
# print(jet6_R5_isB[256676],"jet6_R5_isB")



### is C jet score 
jet1_R5_isC=arrays["jet1_R5_isC"]
jet2_R5_isC=arrays["jet2_R5_isC"]
jet3_R5_isC=arrays["jet3_R5_isC"]
jet4_R5_isC=arrays["jet4_R5_isC"]
jet5_R5_isC=arrays["jet5_R5_isC"]
jet6_R5_isC=arrays["jet6_R5_isC"]

# print(jet1_R5_isC,"jet1_R5_isC")
# print(jet2_R5_isC,"jet2_R5_isC")
# print(jet3_R5_isC,"jet3_R5_isC")
# print(jet4_R5_isC,"jet4_R5_isC")
# print(jet5_R5_isC,"jet5_R5_isC")
# print(jet6_R5_isC,"jet6_R5_isC")
### pflavor of jets 
jet1_R5_pflavor=arrays["jet1_R5_pflavor"]
jet2_R5_pflavor=arrays["jet2_R5_pflavor"]
jet3_R5_pflavor=arrays["jet3_R5_pflavor"]
jet4_R5_pflavor=arrays["jet4_R5_pflavor"]
jet5_R5_pflavor=arrays["jet5_R5_pflavor"]
jet6_R5_pflavor=arrays["jet6_R5_pflavor"]

# print(jet1_R5_pflavor[256676],"jet1_R5_pflavor")
# print(jet2_R5_pflavor[256676],"jet2_R5_pflavor")
# print(jet3_R5_pflavor[256676],"jet3_R5_pflavor")
# print(jet4_R5_pflavor[256676],"jet4_R5_pflavor")
# print(jet5_R5_pflavor[256676],"jet5_R5_pflavor")
# print(jet6_R5_pflavor[256676],"jet6_R5_pflavor")

# ### is G jet score 
# jet1_R5_isG=arrays["jet1_R5_isG"]
# jet2_R5_isG=arrays["jet2_R5_isG"]
# jet3_R5_isG=arrays["jet3_R5_isG"]
# jet4_R5_isG=arrays["jet4_R5_isG"]
# jet5_R5_isG=arrays["jet5_R5_isG"]
# jet6_R5_isG=arrays["jet6_R5_isG"]

# print(jet1_R5_isG,"jet1_R5_isG")
# print(jet2_R5_isG,"jet2_R5_isG")
# print(jet3_R5_isG,"jet3_R5_isG")
# print(jet4_R5_isG,"jet4_R5_isG")
# print(jet5_R5_isG,"jet5_R5_isG")
# print(jet6_R5_isG,"jet6_R5_isG")



### is U jet score 
jet1_R5_isU=arrays["jet1_R5_isU"]
jet2_R5_isU=arrays["jet2_R5_isU"]
jet3_R5_isU=arrays["jet3_R5_isU"]
jet4_R5_isU=arrays["jet4_R5_isU"]
jet5_R5_isU=arrays["jet5_R5_isU"]
jet6_R5_isU=arrays["jet6_R5_isU"]

# print(jet1_R5_isU,"jet1_R5_isU")
# print(jet2_R5_isU,"jet2_R5_isU")
# print(jet3_R5_isU,"jet3_R5_isU")
# print(jet4_R5_isU,"jet4_R5_isU")
# print(jet5_R5_isU,"jet5_R5_isU")
# print(jet6_R5_isU,"jet6_R5_isU")


### is S jet score 
# jet1_R5_isS=arrays["jet1_R5_isS"]
# jet2_R5_isS=arrays["jet2_R5_isS"]
# jet3_R5_isS=arrays["jet3_R5_isS"]
# jet4_R5_isS=arrays["jet4_R5_isS"]
# jet5_R5_isS=arrays["jet5_R5_isS"]
# jet6_R5_isS=arrays["jet6_R5_isS"]

# print(jet1_R5_isS,"jet1_R5_isS")
# print(jet2_R5_isS,"jet2_R5_isS")
# print(jet3_R5_isS,"jet3_R5_isS")
# print(jet4_R5_isS,"jet4_R5_isS")
# print(jet5_R5_isS,"jet5_R5_isS")
# print(jet6_R5_isS,"jet6_R5_isS")


### is D jet score 
jet1_R5_isD=arrays["jet1_R5_isD"]
jet2_R5_isD=arrays["jet2_R5_isD"]
jet3_R5_isD=arrays["jet3_R5_isD"]
jet4_R5_isD=arrays["jet4_R5_isD"]
jet5_R5_isD=arrays["jet5_R5_isD"]
jet6_R5_isD=arrays["jet6_R5_isD"]

# print(jet1_R5_isD,"jet1_R5_isD")
# print(jet2_R5_isD,"jet2_R5_isD")
# print(jet3_R5_isD,"jet3_R5_isD")
# print(jet4_R5_isD,"jet4_R5_isD")
# print(jet5_R5_isD,"jet5_R5_isD")
# print(jet6_R5_isD,"jet6_R5_isD")


### is TAU jet score 
# jet1_R5_isTAU=arrays["jet1_R5_isTAU"]
# jet2_R5_isTAU=arrays["jet2_R5_isTAU"]
# jet3_R5_isTAU=arrays["jet3_R5_isTAU"]
# jet4_R5_isTAU=arrays["jet4_R5_isTAU"]
# jet5_R5_isTAU=arrays["jet5_R5_isTAU"]
# jet6_R5_isTAU=arrays["jet6_R5_isTAU"]

# print(jet1_R5_isTAU,"jet1_R5_isTAU")
# print(jet2_R5_isTAU,"jet2_R5_isTAU")
# print(jet3_R5_isTAU,"jet3_R5_isTAU")
# print(jet4_R5_isTAU,"jet4_R5_isTAU")
# print(jet5_R5_isTAU,"jet5_R5_isTAU")
# print(jet6_R5_isTAU,"jet6_R5_isTAU")






# lepton_list_no_overlap_size=arrays["lepton_list_no_overlap_size"]
jets_R5_p_unfiltered_size=arrays["jets_R5_p_unfiltered_size"]
jets_R5_p_size=arrays["jets_R5_p_size"]

# print(remaining_leptons_merged_size,"remaining_leptons_merged_size")
# print(lepton_list_no_overlap_size,"lepton_list_no_overlap_size")
# print(jets_R5_p_unfiltered_size,"jets_R5_p_unfiltered_size")
# print(jets_R5_p_size,"jets_R5_p_size")


### Lepton Dist before and after overlap removal 

# hist_lepton_dist_before_overlap_removal=bh.Histogram(bh.axis.Regular(7, 0, 7)) 
# hist_lepton_dist_after_overlap_removal=bh.Histogram(bh.axis.Regular(7, 0, 7)) 
# for i in range(len(remaining_leptons_merged_size)):
#     hist_lepton_dist_before_overlap_removal.fill(remaining_leptons_merged_size[i])
#     hist_lepton_dist_after_overlap_removal.fill(non_overlapping_leptons_per_event[i])
# plt.stairs(hist_lepton_dist_before_overlap_removal.view(),hist_lepton_dist_before_overlap_removal.axes[0].edges, color="blue", label="Lepton Dist before overlap removal")
# plt.xlabel("Number of Leptons per event")
# plt.ylabel("Number of Events")
# plt.title(f"Lepton Dist before overlap removal R={deltaR_label}")
# plt.legend()
# plt.savefig(f"jet_plots/lepton_dist_before_overlap_removal_{deltaR_label}.pdf")
# plt.close()
# ### nomrmalized lepton dist before
# hist_lepton_dist_before_overlap_removal_norm=hist_lepton_dist_before_overlap_removal.view()/hist_lepton_dist_before_overlap_removal.view().sum()

# plt.stairs(hist_lepton_dist_before_overlap_removal_norm.view(),hist_lepton_dist_before_overlap_removal.axes[0].edges, color="blue", label="Normalized Lepton Dist before overlap removal")
# plt.xlabel("Number of Leptons per event")
# plt.ylabel("Normalized Number of Events")
# plt.title("Normalized Lepton Dist before overlap removal")
# plt.legend()
# plt.savefig(f"jet_plots/lepton_dist_before_overlap_removal_{deltaR_label}_normalized.pdf")
# plt.close()

# hist_lepton_dist_after_overlap_removal_norm=hist_lepton_dist_after_overlap_removal.view()/hist_lepton_dist_after_overlap_removal.view().sum()
# plt.stairs(hist_lepton_dist_after_overlap_removal_norm.view(),hist_lepton_dist_after_overlap_removal.axes[0].edges, color="red", label="Normalized Lepton Dist after overlap removal")
# plt.xlabel("Number of Leptons per event")
# plt.ylabel("Normalized Number of Events")
# plt.title(f"Normalized Lepton Dist after overlap removal R={deltaR_label}")
# plt.legend()
# plt.savefig(f"jet_plots/lepton_dist_after_overlap_removal_{deltaR_label}_normalized.pdf")
# plt.close()

# plt.stairs(hist_lepton_dist_after_overlap_removal.view(),hist_lepton_dist_after_overlap_removal.axes[0].edges, color="red", label="Lepton Dist after overlap removal")
# plt.xlabel("Number of Leptons per event")
# plt.ylabel("Number of Events")
# plt.title(f"Lepton Dist after overlap removal R={deltaR_label}")
# plt.legend()
# plt.savefig(f"jet_plots/lepton_dist_after_overlap_removal_{deltaR_label}.pdf")
# plt.close()

### Lepton Dist before and after overlap removal 

### Number Jets before and after overlap removal

# hist_jets_dist_before_overlap_removal=bh.Histogram(bh.axis.Regular(7, 0, 7)) 
# hist_jets_dist_after_overlap_removal=bh.Histogram(bh.axis.Regular(7, 0, 7)) 
# for i in range(len(jets_R5_p_unfiltered_size)):
#     hist_jets_dist_before_overlap_removal.fill(jets_R5_p_unfiltered_size[i])
#     hist_jets_dist_after_overlap_removal.fill(jets_R5_p_size[i])
# plt.stairs(hist_jets_dist_before_overlap_removal.view(),hist_jets_dist_before_overlap_removal.axes[0].edges, color="blue", label="Jets Dist before overlap removal")
# plt.xlabel("Number of Jets per event")
# plt.ylabel("Number of Events")
# plt.title(f"Jets Dist before overlap removal R={deltaR_label}")
# plt.legend()
# plt.savefig(f"jet_plots/jets_dist_before_overlap_removal_{deltaR_label}.pdf")
# plt.close()
# #normalized
# hist_jets_dist_before_overlap_removal_norm=hist_jets_dist_before_overlap_removal.view()/hist_jets_dist_before_overlap_removal.view().sum()

# plt.stairs(hist_jets_dist_before_overlap_removal_norm.view(),hist_jets_dist_before_overlap_removal.axes[0].edges, color="blue", label="Normalized Jets Dist before overlap removal")
# plt.xlabel("Number of Jets per event")
# plt.ylabel("Normalized Number of Events")
# plt.title(f"Normalized Jets Dist before overlap removal R={deltaR_label}")
# plt.legend()
# plt.savefig(f"jet_plots/jets_dist_before_overlap_removal_{deltaR_label}_normalized.pdf")
# plt.close()




# hist_jets_dist_after_overlap_removal_norm=hist_jets_dist_after_overlap_removal.view()/hist_jets_dist_after_overlap_removal.view().sum()
# plt.stairs(hist_jets_dist_after_overlap_removal_norm.view(),hist_jets_dist_after_overlap_removal.axes[0].edges, color="red", label="Normalized Jets Dist after overlap removal")
# plt.xlabel("Number of Jets per event")
# plt.ylabel("Normalized Number of Events")
# plt.title(f"Normalized Jets Dist after overlap removal R={deltaR_label}")
# plt.legend()
# plt.savefig(f"jet_plots/jets_dist_after_overlap_removal_{deltaR_label}_normalized.pdf")
# plt.close()


# plt.stairs(hist_jets_dist_after_overlap_removal.view(),hist_jets_dist_after_overlap_removal.axes[0].edges, color="red", label="Jets Dist after overlap removal")
# plt.xlabel("Number of Jets per event")
# plt.ylabel("Number of Events")
# plt.title(f"Jets Dist after overlap removal R={deltaR_label}")
# plt.legend()
# plt.savefig(f"jet_plots/jets_dist_after_overlap_removal_{deltaR_label}.pdf")
# plt.close()



jets_R5_isB=arrays["jets_R5_isB"]
jets_R5_isC=arrays["jets_R5_isC"]
jets_R5_isU=arrays["jets_R5_isU"]
jets_R5_isD=arrays["jets_R5_isD"]
jets_R5_pflavor=arrays["jets_R5_pflavor"]
lepton_label="zero"
deltaR_label = 0.4
clustering_label="R5"


jets_R5_theta = arrays["jets_R5_theta"]

nbjets_R5_true=(arrays["nbjets_R5_true"])
nbjets_R5_true_total=np.sum(nbjets_R5_true)
print(nbjets_R5_true_total,"nbjets_R5_true_total")
bjets_R5_true_theta = arrays["bjets_R5_true_theta"]

bjet_match_mask = []
for i in range(len(jets_R5_theta)):
    event_match_mask = []
    for j in range(len(jets_R5_theta[i])):
        if any(jets_R5_theta[i][j] == theta for theta in bjets_R5_true_theta[i]):
            event_match_mask.append(True)
        
    bjet_match_mask.append(event_match_mask)

flattened_bjet_match_mask=ak.flatten(bjet_match_mask)
combined_nested_isB_masked=ak.flatten(jets_R5_isB)[flattened_bjet_match_mask]
combined_nested_isC_masked=ak.flatten(jets_R5_isC)[flattened_bjet_match_mask]
combined_nested_isU_masked=ak.flatten(jets_R5_isU)[flattened_bjet_match_mask]
combined_nested_isD_masked=ak.flatten(jets_R5_isD)[flattened_bjet_match_mask]

df_bjet_match_mask=pd.DataFrame({f"bjet_match_mask{deltaR_label}{lepton_label}":flattened_bjet_match_mask})
df_combined_nested_isB_masked=pd.DataFrame({f"combined_nested_isB_masked_R{deltaR_label}{lepton_label}":combined_nested_isB_masked})
df_combined_nested_isC_masked=pd.DataFrame({f"combined_nested_isC_masked_R{deltaR_label}{lepton_label}":combined_nested_isC_masked})
df_combined_nested_isU_masked=pd.DataFrame({f"combined_nested_isU_masked_R{deltaR_label}{lepton_label}":combined_nested_isU_masked})
df_combined_nested_isD_masked=pd.DataFrame({f"combined_nested_isD_masked_R{deltaR_label}{lepton_label}":combined_nested_isD_masked})

## how cna i amek it so that if the jet_plots3_csvs{deltaR_label}{lepton_label} folder does not exist, it creates it
if not os.path.exists(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}"):
    os.makedirs(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}")
if not os.path.exists(f"all_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}"):
    os.makedirs(f"all_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}")



df_bjet_match_mask.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/bjet_match_mask_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
df_combined_nested_isB_masked.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isB_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
df_combined_nested_isC_masked.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isC_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
df_combined_nested_isU_masked.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isU_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
df_combined_nested_isD_masked.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isD_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)

### Number Jets before and after overlap removal




### B TAGGING ROCS

#5 is b 
#4 is c 
#21 is g 
# <4 is light jet so just the mask for the collection
# #normalized



efficiencies_b_jets_passing_cut=[]
inefficiencies_c_jets_passing_cut=[]
inefficiencies_u_jets_passing_cut=[]
inefficiencies_d_jets_passing_cut=[]
inefficiencies_ud_jets_passing_cut=[]
cutoff_values=[]

for i in range(0,10000): 
    cuttoff_mask_val=i/10000
    b_score_cutoff_1_mask = combined_nested_isB_masked > cuttoff_mask_val
    c_score_cutoff_1_mask=combined_nested_isC_masked > cuttoff_mask_val
    u_score_cutoff_1_mask=combined_nested_isU_masked > cuttoff_mask_val
    d_score_cutoff_1_mask=combined_nested_isD_masked > cuttoff_mask_val
    b_score_cutoff_1= combined_nested_isB_masked[b_score_cutoff_1_mask]
    c_score_cutoff_1= combined_nested_isC_masked[c_score_cutoff_1_mask]
    u_score_cutoff_1= combined_nested_isU_masked[u_score_cutoff_1_mask]
    d_score_cutoff_1= combined_nested_isD_masked[d_score_cutoff_1_mask]
    
    total_b_jets_passing_cut=len(b_score_cutoff_1)
    efficiency_b_jets_passing_cut=total_b_jets_passing_cut/nbjets_R5_true_total
    # print(total_b_jets_passing_cut,"b jets passing cut")
    # print(total_b_jets_passing_cut,nbjets_R5_true_total)

    inefficiency_c_jets_passing_cut_total=len(c_score_cutoff_1)
    # print(inefficiency_c_jets_passing_cut_total,"c jets passing cut")
    inefficiency_c_jets_passing_cut=inefficiency_c_jets_passing_cut_total/nbjets_R5_true_total

    inefficiency_u_jets_passing_cut_total=len(u_score_cutoff_1)
    # print(inefficiency_u_jets_passing_cut_total,"u jets passing cut")
    inefficiency_u_jets_passing_cut=inefficiency_u_jets_passing_cut_total/nbjets_R5_true_total

    inefficiency_d_jets_passing_cut_total=len(d_score_cutoff_1)
    # print(inefficiency_d_jets_passing_cut_total,"d jets passing cut")
    inefficiency_d_jets_passing_cut=inefficiency_d_jets_passing_cut_total/nbjets_R5_true_total

    inefficiency_ud_jets_passing_cut=((inefficiency_d_jets_passing_cut_total+inefficiency_u_jets_passing_cut_total)*0.5)/nbjets_R5_true_total
    cutoff_values.append(cuttoff_mask_val)
    efficiencies_b_jets_passing_cut.append(efficiency_b_jets_passing_cut)
    inefficiencies_c_jets_passing_cut.append(inefficiency_c_jets_passing_cut)
    inefficiencies_u_jets_passing_cut.append(inefficiency_u_jets_passing_cut)
    inefficiencies_d_jets_passing_cut.append(inefficiency_d_jets_passing_cut)
    inefficiencies_ud_jets_passing_cut.append(inefficiency_ud_jets_passing_cut)




plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_c_jets_passing_cut,color="blue",label="b vs c")
plt.xlabel("jet tagging efficiency")
plt.ylabel("log10(c-jet misd. probability)")
# plt.title(f"B Tagging Efficiency vs C Tagging Inefficiency, R={deltaR_label}")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig(f"all_jets/jet_plots/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_c_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
plt.close()

plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_u_jets_passing_cut,color="green",label="b vs u")
plt.xlabel("jet tagging efficiency")
plt.ylabel("log10(u-jet misd. probability)")
# plt.title(f"B Tagging Efficiency vs U Tagging Inefficiency, R={deltaR_label}")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig(f"all_jets/jet_plots/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
plt.close()

plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_d_jets_passing_cut,color="red",label="b vs d")
plt.xlabel("jet tagging efficiency")
plt.ylabel("log10(d-jet misd. probability)")
# plt.title(f"B Tagging Efficiency vs D Tagging Inefficiency, R={deltaR_label}")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig(f"all_jets/jet_plots/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
plt.close()
plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_ud_jets_passing_cut,color="purple",label="b vs ud")
plt.xlabel("jet tagging efficiency")
plt.ylabel("log10(ud-jet misd. probability)")
# plt.title(f"B Tagging Efficiency vs UD Tagging Inefficiency, R={deltaR_label}")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig(f"all_jets/jet_plots/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
plt.close()

plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_ud_jets_passing_cut,color="green",label="b vs ud")
plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_c_jets_passing_cut,color="blue",label="b vs c")
# plt.title(f"b ROC {deltaR_label}")
plt.yscale("log")
plt.xlabel("jet tagging efficiency")
plt.ylabel("jet misd. probability")
plt.legend(frameon=False)
plt.savefig(f"all_jets/jet_plots/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/b_roc_{deltaR_label}{lepton_label}{clustering_label}.pdf")
plt.close()


df=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_c_jets_passing_cut":inefficiencies_c_jets_passing_cut,"cutoff_values":cutoff_values})
df.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_c_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)

df1=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_u_jets_passing_cut":inefficiencies_u_jets_passing_cut,"cutoff_values":cutoff_values})
df1.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
df2=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_d_jets_passing_cut":inefficiencies_d_jets_passing_cut,"cutoff_values":cutoff_values})
df2.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
df3=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_ud_jets_passing_cut":inefficiencies_ud_jets_passing_cut,"cutoff_values":cutoff_values})
df3.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
df4=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_ud_jets_passing_cut":inefficiencies_ud_jets_passing_cut,"inefficiencies_c_jets_passing_cut":inefficiencies_c_jets_passing_cut,"cutoff_values":cutoff_values})
df4.to_csv(f"all_jets/jet_csvs/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/b_roc_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
### B TAGGING ROCS

### Jet Dist as func of n leps
# njets_R5=arrays["njets_R5"]
# n_jets_R5_true=arrays["njets_R5"]
# print(max(n_jets_R5_true))
# remaining_leptons_merged_size=arrays["remaining_leptons_merged_size"]

# mask_0_leps=remaining_leptons_merged_size==0
# mask_1_lep=remaining_leptons_merged_size==1
# mask_2_leps=remaining_leptons_merged_size==2
# mask_3_leps=remaining_leptons_merged_size==3
# mask_4_leps=remaining_leptons_merged_size==4
# mask_5_leps=remaining_leptons_merged_size==5
# mask_6_leps=remaining_leptons_merged_size==6


# n_jets_0_leps=n_jets_R5_true[mask_0_leps]
# n_jets_1_lep=n_jets_R5_true[mask_1_lep]
# n_jets_2_leps=n_jets_R5_true[mask_2_leps]
# n_jets_3_leps=n_jets_R5_true[mask_3_leps]
# n_jets_4_leps=n_jets_R5_true[mask_4_leps]
# n_jets_5_leps=n_jets_R5_true[mask_5_leps]
# n_jets_6_leps=n_jets_R5_true[mask_6_leps]


# # Create histograms for number of jets for each lepton count using boost_histogram
# # Define bins for the histograms
# bins = bh.axis.Regular(13, 0, 13)  # 9 bins from 0 to 9

# # Create histograms for each lepton category
# hist_0_leps = bh.Histogram(bins)
# hist_0_leps.fill(n_jets_0_leps)

# hist_1_lep = bh.Histogram(bins)
# hist_1_lep.fill(n_jets_1_lep)

# hist_2_leps = bh.Histogram(bins)
# hist_2_leps.fill(n_jets_2_leps)

# hist_3_leps = bh.Histogram(bins)
# hist_3_leps.fill(n_jets_3_leps)

# hist_4_leps = bh.Histogram(bins)
# hist_4_leps.fill(n_jets_4_leps)

# hist_5_leps = bh.Histogram(bins)
# hist_5_leps.fill(n_jets_5_leps)

# hist_6_leps = bh.Histogram(bins)
# hist_6_leps.fill(n_jets_6_leps)

# # Normalize the histograms for density
# total_0 = np.sum(hist_0_leps.values()) 
# total_1 = np.sum(hist_1_lep.values()) 
# total_2 = np.sum(hist_2_leps.values()) 
# total_3 = np.sum(hist_3_leps.values()) 
# total_4 = np.sum(hist_4_leps.values()) 
# total_5 = np.sum(hist_5_leps.values()) 
# total_6 = np.sum(hist_6_leps.values()) 

# # Create a figure with a grid of subplots (2 rows, 3 columns for 6 plots, plus 1 extra slot)
# fig, axs = plt.subplots(3, 3, figsize=(12, 10))

# # Plot for 0 Leptons
# axs[0,0].stairs(hist_0_leps.values() / total_0, hist_0_leps.axes[0].edges, label='0 Leptons', color='blue', alpha=0.5)
# axs[0,0].set_xlabel("Number of Jets (R5)")
# axs[0,0].set_ylabel("Normalized Frequency")
# axs[0,0].set_title("0 Leptons")
# axs[0,0].legend()

# # Plot for 1 Lepton
# axs[0,1].stairs(hist_1_lep.values() / total_1, hist_1_lep.axes[0].edges, label='1 Lepton', color='blue', alpha=0.5)
# axs[0,1].set_xlabel("Number of Jets (R5)")
# axs[0,1].set_ylabel("Normalized Frequency")
# axs[0,1].set_title("1 Lepton")
# axs[0,1].legend()

# # Plot for 2 Leptons
# axs[0,2].stairs(hist_2_leps.values() / total_2, hist_2_leps.axes[0].edges, label='2 Leptons', color='blue', alpha=0.5)
# axs[0,2].set_xlabel("Number of Jets (R5)")
# axs[0,2].set_ylabel("Normalized Frequency")
# axs[0,2].set_title("2 Leptons")
# axs[0,2].legend()

# # Plot for 3 Leptons
# axs[1,0].stairs(hist_3_leps.values() / total_3, hist_3_leps.axes[0].edges, label='3 Leptons', color='blue', alpha=0.5)
# axs[1,0].set_xlabel("Number of Jets (R5)")
# axs[1,0].set_ylabel("Normalized Frequency")
# axs[1,0].set_title("3 Leptons")
# axs[1,0].legend()

# # Plot for 4 Leptons
# axs[1,1].stairs(hist_4_leps.values() / total_4, hist_4_leps.axes[0].edges, label='4 Leptons', color='blue', alpha=0.5)
# axs[1,1].set_xlabel("Number of Jets (R5)")
# axs[1,1].set_ylabel("Normalized Frequency")
# axs[1,1].set_title("4 Leptons")
# axs[1,1].legend()

# # Plot for 5 Leptons
# axs[1,2].stairs(hist_5_leps.values() / total_5, hist_5_leps.axes[0].edges, label='5 Leptons', color='blue', alpha=0.5)
# axs[1,2].set_xlabel("Number of Jets (R5)")
# axs[1,2].set_ylabel("Normalized Frequency")
# axs[1,2].set_title("5 Leptons")
# axs[1,2].legend()

# axs[2,0].stairs(hist_6_leps.values() / total_6, hist_6_leps.axes[0].edges, label='6 Leptons', color='blue', alpha=0.5)
# axs[2,0].set_xlabel("Number of Jets (R5)")
# axs[2,0].set_ylabel("Normalized Frequency")
# axs[2,0].set_title("6 Leptons")
# axs[2,0].legend()

# axs[2,1].axis('off')  
# axs[2,2].axis('off')

# plt.tight_layout()
# plt.savefig(f"jet_plots3/n_jets_distribution_by_lepton_count_combined_deltaR_{deltaR_label}.pdf")
# plt.close()



### Jet Dist as func of n leps

# histb = bh.Histogram(bh.axis.Regular(110, 0, 1))
# hist_c=bh.Histogram(bh.axis.Regular(110, 0, 1))
# hist_u=bh.Histogram(bh.axis.Regular(110, 0, 1))
# hist_d=bh.Histogram(bh.axis.Regular(110, 0, 1))

# for i in range(0,len(b_score_masked_1)):
#     histb.fill(b_score_masked_1[i])
#     hist_c.fill(b_score_c_masked_1[i])
#     hist_u.fill(b_score_masked_u_1[i])
#     hist_d.fill(b_score_masked_d_1[i])
# for i in range(0,len(b_score_masked_2)):
#     histb.fill(b_score_masked_2[i])
#     hist_c.fill(b_score_c_masked_2[i])
#     hist_u.fill(b_score_masked_u_2[i])
#     hist_d.fill(b_score_masked_d_2[i])
# for i in range(0,len(b_score_masked_3)):
#     histb.fill(b_score_masked_3[i])
#     hist_c.fill(b_score_c_masked_3[i])
#     hist_u.fill(b_score_masked_u_3[i])
#     hist_d.fill(b_score_masked_d_3[i])
# for i in range(0,len(b_score_masked_4)):
#     histb.fill(b_score_masked_4[i])
#     hist_c.fill(b_score_c_masked_4[i])
#     hist_u.fill(b_score_masked_u_4[i])
#     hist_d.fill(b_score_masked_d_4[i])
# for i in range(0,len(b_score_masked_5)):
#     histb.fill(b_score_masked_5[i])
#     hist_c.fill(b_score_c_masked_5[i])
#     hist_u.fill(b_score_masked_u_5[i])
#     hist_d.fill(b_score_masked_d_5[i])
# for i in range(0,len(b_score_masked_6)):
#     histb.fill(b_score_masked_6[i])
#     hist_c.fill(b_score_c_masked_6[i])
#     hist_u.fill(b_score_masked_u_6[i])
#     hist_d.fill(b_score_masked_d_6[i])

# hist_valueb=histb.view()
# hist_valuec=hist_c.view()
# hist_valueu=hist_u.view()
# hist_valued=hist_d.view()



# hist_valueb_norm=hist_valueb/hist_valueb.sum()


# hist_valuec_norm=hist_valuec/hist_valuec.sum()
# hist_valueu_norm=hist_valueu/hist_valueu.sum()
# hist_valued_norm=hist_valued/hist_valued.sum()
# plt.stairs(hist_valueb_norm,histb.axes[0].edges, color="blue", label="Normalized B Tag Score for true b jets")
# plt.stairs(hist_valuec_norm,hist_c.axes[0].edges, color="red", label="Normalized C Tag Score for true b jets")

# plt.xlabel("B Tag Score")
# plt.ylabel("Normalized Number of Jets")
# plt.title(f"Normalized B and C Tag Score for true b jets R={deltaR_label}")
# plt.legend()
# plt.savefig(f"jet_plots/btag_score_b_c_jet_combined_deltaR_{deltaR_label}_normalized_withfiltered.pdf")
# plt.close()

# plt.stairs(hist_valueb_norm,histb.axes[0].edges, color="blue", label="Normalized B Tag Score for true b jets")
# plt.stairs(hist_valueu_norm,hist_u.axes[0].edges, color="green", label="Normalized U Tag Score for true b jets")
# plt.stairs(hist_valued_norm,hist_d.axes[0].edges, color="black", label="Normalized D Tag Score for true b jets")
# plt.xlabel("B Tag Score")
# plt.ylabel("Normalized Number of Jets")
# plt.legend()
# plt.title(f"Normalized B, U, and D Tag Score for true b jets R={deltaR_label}")
# plt.savefig(f"jet_plots/btag_score_b_u_d_jet_combined_deltaR_{deltaR_label}_normalized_withfiltered.pdf")
# plt.close()

# # ### normalized












# plt.stairs(hist_valueb,histb_c.axes[0].edges, color="blue", label="B vs C Tag Score for true b jets")
# plt.xlabel("B Tag Score")
# plt.ylabel("Number of Jets")
# plt.title("B and C Tag Score for true b jets R=0.5 ")
# plt.legend()
# plt.savefig("btag_score_b_c_jet_combined_deltaR_05.pdf")
# plt.close()

# plt.stairs(hist_b_d_u.view(),hist_b_d_u.axes[0].edges, color="red", label="B vs D vs U Tag Score for true b jets")
# plt.xlabel("B Tag Score")
# plt.ylabel("Number of Jets")
# plt.title("B vs D vs U Tag Score for true b jets R=0.5 ")
# plt.legend()
# plt.savefig("btag_score_b_d_u_jet_combined_deltaR_05.pdf")
# plt.close()



# ## Normalized B vs C tag score and Normalized B vs D vs U tag score 
# hist_b_c_norm=histb_c.view()/histb_c.view().sum()
# hist_b_d_u_norm=hist_b_d_u.view()/hist_b_d_u.view().sum()
# plt.stairs(hist_b_c_norm,histb_c.axes[0].edges, color="blue", label="Normalized B vs C Tag Score for true b jets")
# plt.stairs(hist_b_d_u_norm,hist_b_d_u.axes[0].edges, color="red", label="Normalized B vs D vs U Tag Score for true b jets")
# plt.xlabel("B Tag Score")
# plt.ylabel("Normalized Number of Jets")
# plt.title("Normalized B vs C and B vs D vs U Tag Score for true b jets R=0.5 ")
# plt.legend()
# plt.savefig("btag_score_b_c_b_d_u_jet_combined_deltaR_05_normalized.pdf")
# plt.close()



### B TAGGING ROCS









### B vs C tag score separate hists
# masked_true_btagged_R5_1= jet1_R5_pflavor==5
# masked_true_btagged_R5_2= jet2_R5_pflavor==5
# masked_true_btagged_R5_3= jet3_R5_pflavor==5
# masked_true_btagged_R5_4= jet4_R5_pflavor==5
# masked_true_btagged_R5_5= jet5_R5_pflavor==5
# masked_true_btagged_R5_6= jet6_R5_pflavor==5

# b_score_masked_1=jet1_R5_isB[masked_true_btagged_R5_1]
# b_score_masked_2=jet2_R5_isB[masked_true_btagged_R5_2]
# b_score_masked_3=jet3_R5_isB[masked_true_btagged_R5_3]
# b_score_masked_4=jet4_R5_isB[masked_true_btagged_R5_4]
# b_score_masked_5=jet5_R5_isB[masked_true_btagged_R5_5]
# b_score_masked_6=jet6_R5_isB[masked_true_btagged_R5_6]

# b_score_c_masked_1=jet1_R5_isC[masked_true_btagged_R5_1]
# b_score_c_masked_2=jet2_R5_isC[masked_true_btagged_R5_2]
# b_score_c_masked_3=jet3_R5_isC[masked_true_btagged_R5_3]
# b_score_c_masked_4=jet4_R5_isC[masked_true_btagged_R5_4]
# b_score_c_masked_5=jet5_R5_isC[masked_true_btagged_R5_5]
# b_score_c_masked_6=jet6_R5_isC[masked_true_btagged_R5_6]



# histb = bh.Histogram(bh.axis.Regular(110, 0, 1))
# for i in range(0,len(b_score_masked_1)):
#     histb.fill(b_score_masked_1[i])
# for i in range(0,len(b_score_masked_2)):
#     histb.fill(b_score_masked_2[i])
# for i in range(0,len(b_score_masked_3)):
#     histb.fill(b_score_masked_3[i])
# for i in range(0,len(b_score_masked_4)):
#     histb.fill(b_score_masked_4[i])
# for i in range(0,len(b_score_masked_5)):
#     histb.fill(b_score_masked_5[i])
# for i in range(0,len(b_score_masked_6)):
#     histb.fill(b_score_masked_6[i])






# histc = bh.Histogram(bh.axis.Regular(110, 0, 1))
# for i in range(0,len(b_score_c_masked_1)):
#     histc.fill(b_score_c_masked_1[i])
# for i in range(0,len(b_score_c_masked_2)):
#     histc.fill(b_score_c_masked_2[i])
# for i in range(0,len(b_score_c_masked_3)):
#     histc.fill(b_score_c_masked_3[i])
# for i in range(0,len(b_score_c_masked_4)):
#     histc.fill(b_score_c_masked_4[i])
# for i in range(0,len(b_score_c_masked_5)):
#     histc.fill(b_score_c_masked_5[i])
# for i in range(0,len(b_score_c_masked_6)):
#     histc.fill(b_score_c_masked_6[i])


# # Add in overlap removal so that I only consider jets that dont have a lepton overlapping the radius of it

# hist_valueb=histb.view()
# hist_valuec=histc.view()

# plt.stairs(hist_valueb,histb.axes[0].edges, color="blue", label="B Tag Score from true b jets")
# # plt.title("Jets B Tag Score")
# plt.xlabel("B Tag Score")
# plt.ylabel("Number of Jets")
# # plt.savefig("btag_score_b.png")
# # plt.close()

# plt.stairs(hist_valuec,histc.axes[0].edges, color="red", label="C Tag Score from true b jets")
# plt.title("B and C Tag Score from true b jets R=0.5 ")
# # plt.xlabel("B Tag Score")
# # plt.ylabel("Number of Jets")
# plt.legend()
# plt.savefig("btag_score_b_c_jet_deltaR_05.png")
# plt.close()

# plt.title("Jets C Tag Score")
# plt.xlabel("C Tag Score")
# plt.ylabel("Number of Jets")
# plt.savefig("btag_score_c.png")
# plt.close()

### B vs C tag score 







# ### ROC Curve plot for all CONE ISOS e,mu

# Initalized all arrays for D Iso vals 
# matched_leps_status1_from_b_muons_p_cut_coneIso_2= ak.flatten(arrays["matched_leps_status1_from_b_muons_p_cut_coneIso_2"])
# matched_leps_status1_from_b_muons_p_cut_coneIso_3= ak.flatten(arrays["matched_leps_status1_from_b_muons_p_cut_coneIso_3"])
# matched_leps_status1_from_b_muons_p_cut_coneIso_4= ak.flatten(arrays["matched_leps_status1_from_b_muons_p_cut_coneIso_4"])
# matched_leps_status1_from_b_muons_p_cut_coneIso_5= ak.flatten(arrays["matched_leps_status1_from_b_muons_p_cut_coneIso_5"])
# matched_leps_status1_from_b_muons_p_cut_coneIso_6= ak.flatten(arrays["matched_leps_status1_from_b_muons_p_cut_coneIso_6"])

# matched_leps_status1_from_b_electrons_p_cut_coneIso_2= ak.flatten(arrays["matched_leps_status1_from_b_electrons_p_cut_coneIso_2"])
# matched_leps_status1_from_b_electrons_p_cut_coneIso_3= ak.flatten(arrays["matched_leps_status1_from_b_electrons_p_cut_coneIso_3"])
# matched_leps_status1_from_b_electrons_p_cut_coneIso_4= ak.flatten(arrays["matched_leps_status1_from_b_electrons_p_cut_coneIso_4"])
# matched_leps_status1_from_b_electrons_p_cut_coneIso_5= ak.flatten(arrays["matched_leps_status1_from_b_electrons_p_cut_coneIso_5"])
# matched_leps_status1_from_b_electrons_p_cut_coneIso_6= ak.flatten(arrays["matched_leps_status1_from_b_electrons_p_cut_coneIso_6"])

# matched_leps_status1_from_W_muons_p_cut_coneIso_2= ak.flatten(arrays["matched_leps_status1_from_W_muons_p_cut_coneIso_2"])
# matched_leps_status1_from_W_muons_p_cut_coneIso_3= ak.flatten(arrays["matched_leps_status1_from_W_muons_p_cut_coneIso_3"])
# matched_leps_status1_from_W_muons_p_cut_coneIso_4= ak.flatten(arrays["matched_leps_status1_from_W_muons_p_cut_coneIso_4"])
# matched_leps_status1_from_W_muons_p_cut_coneIso_5= ak.flatten(arrays["matched_leps_status1_from_W_muons_p_cut_coneIso_5"])
# matched_leps_status1_from_W_muons_p_cut_coneIso_6= ak.flatten(arrays["matched_leps_status1_from_W_muons_p_cut_coneIso_6"])

# matched_leps_status1_from_W_electrons_p_cut_coneIso_2= ak.flatten(arrays["matched_leps_status1_from_W_electrons_p_cut_coneIso_2"])
# matched_leps_status1_from_W_electrons_p_cut_coneIso_3= ak.flatten(arrays["matched_leps_status1_from_W_electrons_p_cut_coneIso_3"])
# matched_leps_status1_from_W_electrons_p_cut_coneIso_4= ak.flatten(arrays["matched_leps_status1_from_W_electrons_p_cut_coneIso_4"])
# matched_leps_status1_from_W_electrons_p_cut_coneIso_5= ak.flatten(arrays["matched_leps_status1_from_W_electrons_p_cut_coneIso_5"])
# matched_leps_status1_from_W_electrons_p_cut_coneIso_6= ak.flatten(arrays["matched_leps_status1_from_W_electrons_p_cut_coneIso_6"])

# # # Inititalize efficiencies and inefficiencies for muons and electrons

# efficiencies_muons_W_2 = []
# efficiencies_muons_W_3 = []
# efficiencies_muons_W_4 = []
# efficiencies_muons_W_5 = []
# efficiencies_muons_W_6 = []



# inefficiencies_muons_b_2 = []
# inefficiencies_muons_b_3 = []
# inefficiencies_muons_b_4 = []
# inefficiencies_muons_b_5 = []
# inefficiencies_muons_b_6 = []


# efficiencies_electrons_W_2 = []
# efficiencies_electrons_W_3 = []
# efficiencies_electrons_W_4 = []
# efficiencies_electrons_W_5 = []
# efficiencies_electrons_W_6 = []

# inefficiencies_electrons_b_2 = []
# inefficiencies_electrons_b_3 = []
# inefficiencies_electrons_b_4 = []
# inefficiencies_electrons_b_5 = []
# inefficiencies_electrons_b_6 = []

# # Loop through D_Iso values and calculate efficiencies and inefficiencies
# d_values_check= 100
# d_iso_with=[]
# for i in range(0,d_values_check):
#     d_val = i / d_values_check  # D_Iso value from 0 to 1
#     # Create masks for muons and electrons based on D_Iso values
#     mask_muons_b_2 = matched_leps_status1_from_b_muons_p_cut_coneIso_2 < d_val
#     mask_muons_b_3 = matched_leps_status1_from_b_muons_p_cut_coneIso_3 < d_val
#     mask_muons_b_4 = matched_leps_status1_from_b_muons_p_cut_coneIso_4 < d_val
#     mask_muons_b_5 = matched_leps_status1_from_b_muons_p_cut_coneIso_5 < d_val
#     mask_muons_b_6 = matched_leps_status1_from_b_muons_p_cut_coneIso_6 < d_val
#     mask_muons_W_2 = matched_leps_status1_from_W_muons_p_cut_coneIso_2 < d_val
#     mask_muons_W_3 = matched_leps_status1_from_W_muons_p_cut_coneIso_3 < d_val
#     mask_muons_W_4 = matched_leps_status1_from_W_muons_p_cut_coneIso_4 < d_val
#     mask_muons_W_5 = matched_leps_status1_from_W_muons_p_cut_coneIso_5 < d_val
#     mask_muons_W_6 = matched_leps_status1_from_W_muons_p_cut_coneIso_6 < d_val
#     mask_electrons_b_2 = matched_leps_status1_from_b_electrons_p_cut_coneIso_2 < d_val
#     mask_electrons_b_3 = matched_leps_status1_from_b_electrons_p_cut_coneIso_3 < d_val
#     mask_electrons_b_4 = matched_leps_status1_from_b_electrons_p_cut_coneIso_4 < d_val
#     mask_electrons_b_5 = matched_leps_status1_from_b_electrons_p_cut_coneIso_5 < d_val
#     mask_electrons_b_6 = matched_leps_status1_from_b_electrons_p_cut_coneIso_6 < d_val
#     mask_electrons_W_2 = matched_leps_status1_from_W_electrons_p_cut_coneIso_2 < d_val
#     mask_electrons_W_3 = matched_leps_status1_from_W_electrons_p_cut_coneIso_3 < d_val
#     mask_electrons_W_4 = matched_leps_status1_from_W_electrons_p_cut_coneIso_4 < d_val
#     mask_electrons_W_5 = matched_leps_status1_from_W_electrons_p_cut_coneIso_5 < d_val
#     mask_electrons_W_6 = matched_leps_status1_from_W_electrons_p_cut_coneIso_6 < d_val
#     # Apply masks to collections 
#     muons_b_2 = matched_leps_status1_from_b_muons_p_cut_coneIso_2[mask_muons_b_2]
#     muons_b_3 = matched_leps_status1_from_b_muons_p_cut_coneIso_3[mask_muons_b_3]
#     muons_b_4 = matched_leps_status1_from_b_muons_p_cut_coneIso_4[mask_muons_b_4]
#     muons_b_5 = matched_leps_status1_from_b_muons_p_cut_coneIso_5[mask_muons_b_5]
#     muons_b_6 = matched_leps_status1_from_b_muons_p_cut_coneIso_6[mask_muons_b_6]
#     muons_W_2 = matched_leps_status1_from_W_muons_p_cut_coneIso_2[mask_muons_W_2]
#     muons_W_3 = matched_leps_status1_from_W_muons_p_cut_coneIso_3[mask_muons_W_3]
#     muons_W_4 = matched_leps_status1_from_W_muons_p_cut_coneIso_4[mask_muons_W_4]
#     muons_W_5 = matched_leps_status1_from_W_muons_p_cut_coneIso_5[mask_muons_W_5]
#     muons_W_6 = matched_leps_status1_from_W_muons_p_cut_coneIso_6[mask_muons_W_6]

#     electrons_b_2 = matched_leps_status1_from_b_electrons_p_cut_coneIso_2[mask_electrons_b_2]
#     electrons_b_3 = matched_leps_status1_from_b_electrons_p_cut_coneIso_3[mask_electrons_b_3]
#     electrons_b_4 = matched_leps_status1_from_b_electrons_p_cut_coneIso_4[mask_electrons_b_4]
#     electrons_b_5 = matched_leps_status1_from_b_electrons_p_cut_coneIso_5[mask_electrons_b_5]
#     electrons_b_6 = matched_leps_status1_from_b_electrons_p_cut_coneIso_6[mask_electrons_b_6]
#     electrons_W_2 = matched_leps_status1_from_W_electrons_p_cut_coneIso_2[mask_electrons_W_2]
#     electrons_W_3 = matched_leps_status1_from_W_electrons_p_cut_coneIso_3[mask_electrons_W_3]
#     electrons_W_4 = matched_leps_status1_from_W_electrons_p_cut_coneIso_4[mask_electrons_W_4]
#     electrons_W_5 = matched_leps_status1_from_W_electrons_p_cut_coneIso_5[mask_electrons_W_5]
#     electrons_W_6 = matched_leps_status1_from_W_electrons_p_cut_coneIso_6[mask_electrons_W_6]
#     # Calculated inefficienes are the from b and efficiencies are from W 
#     efficiency_muons_W_2 = len(muons_W_2) / len(matched_leps_status1_from_W_muons_p_cut_coneIso_2)
#     inefficiency_muons_b_2 = len(muons_b_2) / len(matched_leps_status1_from_b_muons_p_cut_coneIso_2)
#     efficiency_muons_W_3 = len(muons_W_3) / len(matched_leps_status1_from_W_muons_p_cut_coneIso_3)
#     inefficiency_muons_b_3 = len(muons_b_3) / len(matched_leps_status1_from_b_muons_p_cut_coneIso_3)
#     efficiency_muons_W_4 = len(muons_W_4) / len(matched_leps_status1_from_W_muons_p_cut_coneIso_4)
#     inefficiency_muons_b_4 = len(muons_b_4) / len(matched_leps_status1_from_b_muons_p_cut_coneIso_4)
#     efficiency_muons_W_5 = len(muons_W_5) / len(matched_leps_status1_from_W_muons_p_cut_coneIso_5)
#     inefficiency_muons_b_5 = len(muons_b_5) / len(matched_leps_status1_from_b_muons_p_cut_coneIso_5)
#     efficiency_muons_W_6 = len(muons_W_6) / len(matched_leps_status1_from_W_muons_p_cut_coneIso_6)
#     inefficiency_muons_b_6 = len(muons_b_6) / len(matched_leps_status1_from_b_muons_p_cut_coneIso_6)

#     efficiencies_muons_W_2.append(efficiency_muons_W_2)
#     inefficiencies_muons_b_2.append(inefficiency_muons_b_2)
#     efficiencies_muons_W_3.append(efficiency_muons_W_3)
#     inefficiencies_muons_b_3.append(inefficiency_muons_b_3)
#     efficiencies_muons_W_4.append(efficiency_muons_W_4)
#     inefficiencies_muons_b_4.append(inefficiency_muons_b_4)
#     efficiencies_muons_W_5.append(efficiency_muons_W_5)
#     inefficiencies_muons_b_5.append(inefficiency_muons_b_5)
#     efficiencies_muons_W_6.append(efficiency_muons_W_6)
#     inefficiencies_muons_b_6.append(inefficiency_muons_b_6)
#     # Calculate efficiencies and inefficiencies for electrons
#     efficiency_electrons_W_2 = len(electrons_W_2) / len(matched_leps_status1_from_W_electrons_p_cut_coneIso_2)
#     inefficiency_electrons_b_2 = len(electrons_b_2) / len(matched_leps_status1_from_b_electrons_p_cut_coneIso_2)
#     efficiency_electrons_W_3 = len(electrons_W_3) / len(matched_leps_status1_from_W_electrons_p_cut_coneIso_3)
#     inefficiency_electrons_b_3 = len(electrons_b_3) / len(matched_leps_status1_from_b_electrons_p_cut_coneIso_3)
#     efficiency_electrons_W_4 = len(electrons_W_4) / len(matched_leps_status1_from_W_electrons_p_cut_coneIso_4)
#     inefficiency_electrons_b_4 = len(electrons_b_4) / len(matched_leps_status1_from_b_electrons_p_cut_coneIso_4)
#     efficiency_electrons_W_5 = len(electrons_W_5) / len(matched_leps_status1_from_W_electrons_p_cut_coneIso_5)
#     inefficiency_electrons_b_5 = len(electrons_b_5) / len(matched_leps_status1_from_b_electrons_p_cut_coneIso_5)
#     efficiency_electrons_W_6 = len(electrons_W_6) / len(matched_leps_status1_from_W_electrons_p_cut_coneIso_6)
#     inefficiency_electrons_b_6 = len(electrons_b_6) / len(matched_leps_status1_from_b_electrons_p_cut_coneIso_6)
#     efficiencies_electrons_W_2.append(efficiency_electrons_W_2)
#     inefficiencies_electrons_b_2.append(inefficiency_electrons_b_2)
#     efficiencies_electrons_W_3.append(efficiency_electrons_W_3)
#     inefficiencies_electrons_b_3.append(inefficiency_electrons_b_3)
#     efficiencies_electrons_W_4.append(efficiency_electrons_W_4)
#     inefficiencies_electrons_b_4.append(inefficiency_electrons_b_4)
#     efficiencies_electrons_W_5.append(efficiency_electrons_W_5)
#     inefficiencies_electrons_b_5.append(inefficiency_electrons_b_5)
#     efficiencies_electrons_W_6.append(efficiency_electrons_W_6)
#     inefficiencies_electrons_b_6.append(inefficiency_electrons_b_6)
#     d_iso_with.append(d_val)
  


# ### ROC Curve plot for all CONE ISOS
# plt.figure(figsize=(10, 6))
# plt.plot(inefficiencies_muons_b_2, efficiencies_muons_W_2, label='Muons ROC ConeIso 0.2', color='blue')
# plt.plot(inefficiencies_muons_b_3, efficiencies_muons_W_3, label='Muons ROC ConeIso 0.3', color='green')
# plt.plot(inefficiencies_muons_b_4, efficiencies_muons_W_4, label='Muons ROC ConeIso 0.4', color='orange')
# plt.plot(inefficiencies_muons_b_5, efficiencies_muons_W_5, label='Muons ROC ConeIso 0.5', color='red')
# plt.plot(inefficiencies_muons_b_6, efficiencies_muons_W_6, label='Muons ROC ConeIso 0.6', color='purple')
# # plt.xscale("log")
# # # plt.yscale("log")
# # plt.title('ROC Curve for Muons D_Iso [0.2, 0.6]')
# # plt.ylabel('Efficiency (Prompt muons)')
# # plt.xlabel('Inefficiency (Non-Prompt muons)')
# # plt.legend()
# # plt.savefig("ROC_Curve_Muons_D_Iso.pdf")
# # plt.close()

# plt.plot(inefficiencies_electrons_b_2, efficiencies_electrons_W_2, label='Electrons ROC ConeIso 0.2', color='blue', linestyle="dashed")
# plt.plot(inefficiencies_electrons_b_3, efficiencies_electrons_W_3, label='Electrons ROC ConeIso 0.3', color='green', linestyle="dashed")
# plt.plot(inefficiencies_electrons_b_4, efficiencies_electrons_W_4, label='Electrons ROC ConeIso 0.4', color='orange', linestyle="dashed")
# plt.plot(inefficiencies_electrons_b_5, efficiencies_electrons_W_5, label='Electrons ROC ConeIso 0.5', color='red', linestyle="dashed")
# plt.plot(inefficiencies_electrons_b_6, efficiencies_electrons_W_6, label='Electrons ROC ConeIso 0.6', color='purple', linestyle="dashed")
# plt.plot(inefficiencies_electrons_b_3[30], efficiencies_electrons_W_3[30], marker='*', markersize=12, color="Green", label="D_Iso 0.3 Point")
# # plt.axvline(d_iso_with[7], color='black', linestyle='dashed', linewidth=1, label='D_Iso Cut 0.07')
# # plt.axvline(inefficiencies_electrons_b_3[30], color='Green', linestyle='dotted', linewidth=1, label='D Iso Cut 0.3')
# # plt.axvline(inefficiencies_electrons_b_3[20], color='Blue', linestyle='dotted', linewidth=1, label='D Iso Cut 0.2')
# # plt.axvline(inefficiencies_electrons_b_3[25], color='Brown', linestyle='dotted', linewidth=1, label='D Iso Cut 0.25')
# print(d_iso_with[30])
# print(d_iso_with[20])

# plt.ylabel('Efficiency (Prompt)')
# plt.xlabel('Inefficiency (Non-Prompt)')
# plt.xscale("log")
# plt.yscale("log")
# # plt.title('ROC Curve for Electrons D_Iso [0.2, 0.6]')
# plt.title('ROC Curve Combined D_Iso [0.2, 0.6]')
# # plt.ylabel('Efficiency (Prompt electrons)')
# # plt.xlabel('Inefficiency (Non-Prompt electrons)')
# plt.legend()
# plt.savefig("ROC_Curve_combined_p12_cut_verticals.pdf")
# # plt.savefig("ROC_Curve_Electrons_D_Iso.pdf")
# plt.close()
# # Create Dataframe to CSV to store results
# df_D_Iso_eff_ineff_muons= pd.DataFrame({"efficiencies_muons_W_2":efficiencies_muons_W_2, "inefficiencies_muons_b_2": inefficiencies_muons_b_2,
#                                         "efficiencies_muons_W_3":efficiencies_muons_W_3, "inefficiencies_muons_b_3": inefficiencies_muons_b_3,
#                                         "efficiencies_muons_W_4":efficiencies_muons_W_4, "inefficiencies_muons_b_4": inefficiencies_muons_b_4,
#                                         "efficiencies_muons_W_5":efficiencies_muons_W_5, "inefficiencies_muons_b_5": inefficiencies_muons_b_5,
#                                         "efficiencies_muons_W_6":efficiencies_muons_W_6, "inefficiencies_muons_b_6": inefficiencies_muons_b_6,
#                                         "D_Iso_Values": d_iso_with})
# df_D_Iso_eff_ineff_muons.to_csv("csvs2/D_Iso_efficiency_inefficiency_muons.csv", index=False)

# df_D_Iso_eff_ineff_electrons= pd.DataFrame({"efficiencies_electrons_W_2":efficiencies_electrons_W_2, "inefficiencies_electrons_b_2": inefficiencies_electrons_b_2,
#                                         "efficiencies_electrons_W_3":efficiencies_electrons_W_3, "inefficiencies_electrons_b_3": inefficiencies_electrons_b_3,
#                                         "efficiencies_electrons_W_4":efficiencies_electrons_W_4, "inefficiencies_electrons_b_4": inefficiencies_electrons_b_4,
#                                         "efficiencies_electrons_W_5":efficiencies_electrons_W_5, "inefficiencies_electrons_b_5": inefficiencies_electrons_b_5,
#                                         "efficiencies_electrons_W_6":efficiencies_electrons_W_6, "inefficiencies_electrons_b_6": inefficiencies_electrons_b_6,
#                                         "D_Iso_Values": d_iso_with})
# df_D_Iso_eff_ineff_electrons.to_csv("csvs2/D_Iso_efficiency_inefficiency_electrons.csv", index=False)

# ### ROC Curve plot for all CONE ISOS after momentum cut 











### Delta R Hists 0.01 truth match DR max is good 

# All_Delta_R_B= arrays["All_Delta_R_B"]
# All_Delta_R_W= arrays["All_Delta_R_W"]

# # Create histograms for Delta R values
# hist_delta_R_W = bh.Histogram(bh.axis.Regular(1000, 0, 10), storage=bh.storage.Weight())
# hist_delta_R_B = bh.Histogram(bh.axis.Regular(1000, 0, 10), storage=bh.storage.Weight())
# # Fill the histograms with the Delta R values
# hist_delta_R_W.fill(ak.flatten(All_Delta_R_W), weight=1.0)
# hist_delta_R_B.fill(ak.flatten(All_Delta_R_B), weight=1.0)
# # Create views of the histograms
# hist_delta_R_W_view = hist_delta_R_W.view()
# hist_delta_R_B_view = hist_delta_R_B.view()
# # Plot the histograms
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.stairs(hist_delta_R_W_view.value, hist_delta_R_W.axes[0].edges, fill=True, label="Delta R W")
# plt.axvline(0.01, color='red', linestyle='dashed', linewidth=1, label='D_R Cutoff 0.01')
# plt.title("Delta R W")
# plt.xlabel("Delta R W")
# plt.ylabel("Events")
# plt.legend()
# plt.subplot(1, 2, 2)
# plt.stairs(hist_delta_R_B_view.value, hist_delta_R_B.axes[0].edges, fill=True, label="Delta R B")
# plt.axvline(0.01, color='red', linestyle='dashed', linewidth=1, label='D_R Cutoff 0.01')
# plt.title("Delta R B")
# plt.xlabel("Delta R B")
# plt.ylabel("Events")
# plt.legend()
# plt.tight_layout()
# plt.savefig("Delta_R_W_B.pdf")

# ### Delta R Hists

# ### P Dists for Wb muons and Wb electrons

# gen_leps_status1_from_b_muons_p= arrays["gen_leps_status1_from_b_muons_p"]
# gen_leps_status1_from_b_electrons_p= arrays["gen_leps_status1_from_b_electrons_p"]
# gen_leps_status1_fromW_muons_p= arrays["gen_leps_status1_fromW_muons_p"]
# gen_leps_status1_fromW_electrons_p= arrays["gen_leps_status1_fromW_electrons_p"]
# # # Create histograms for muons and electrons
# hist_b_muons_p = bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hist_b_electrons_p = bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hist_W_muons_p = bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hist_W_electrons_p = bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# # Fill the histograms with the p values
# hist_b_muons_p.fill(ak.flatten(gen_leps_status1_from_b_muons_p), weight=1.0)
# hist_b_electrons_p.fill(ak.flatten(gen_leps_status1_from_b_electrons_p), weight=1.0)
# hist_W_muons_p.fill(ak.flatten(gen_leps_status1_fromW_muons_p), weight=1.0)
# hist_W_electrons_p.fill(ak.flatten(gen_leps_status1_fromW_electrons_p), weight=1.0)
# # Create views of the histograms
# hist_b_muons_p_view = hist_b_muons_p.view()
# hist_b_electrons_p_view = hist_b_electrons_p.view()
# hist_W_muons_p_view = hist_W_muons_p.view()
# hist_W_electrons_p_view = hist_W_electrons_p.view()
# # Plot the histograms
# # THink pcut of 15 is the best for both of them
# plt.figure(figsize=(12, 6))
# plt.subplot(2, 2, 1)
# plt.stairs(hist_b_muons_p_view.value, hist_b_muons_p.axes[0].edges, fill=True, label="p B Muons")
# plt.axvline(15, color='red', linestyle='dashed', linewidth=1, label='p Cutoff 15')
# plt.title("p B Muons")
# plt.xlabel("p B Muons")
# plt.ylabel("Events")
# plt.legend()
# plt.subplot(2, 2, 2)
# plt.stairs(hist_b_electrons_p_view.value, hist_b_electrons_p.axes[0].edges, fill=True, label="p B Electrons")
# plt.axvline(15, color='red', linestyle='dashed', linewidth=1, label='p Cutoff 15')
# plt.title("p B Electrons")
# plt.xlabel("p B Electrons")
# plt.ylabel("Events")
# plt.legend()
# plt.subplot(2, 2, 3)
# plt.stairs(hist_W_muons_p_view.value, hist_W_muons_p.axes[0].edges, fill=True, label="p W Muons")
# plt.axvline(15, color='red', linestyle='dashed', linewidth=1, label='p Cutoff 15')
# plt.title("p W Muons")
# plt.xlabel("p W Muons")
# plt.ylabel("Events")
# plt.legend()
# plt.subplot(2, 2, 4)
# plt.stairs(hist_W_electrons_p_view.value, hist_W_electrons_p.axes[0].edges, fill=True, label="p W Electrons")
# plt.axvline(15, color='red', linestyle='dashed', linewidth=1, label='p Cutoff 15')
# plt.title("p W Electrons")
# plt.xlabel("p W Electrons")
# plt.ylabel("Events")
# plt.legend()
# plt.tight_layout()
# plt.savefig("p_Muons_Electrons_from_Wb_and_b.pdf")
# plt.close()

### P Dists for Wb muons and Wb electrons


### P Dists for Wb muons and Wb electrons

# gen_leps_status1_from_bW_muons_p= arrays["gen_leps_status1_from_bW_muons_p"]
# gen_leps_status1_from_bW_electrons_p= arrays["gen_leps_status1_from_bW_electrons_p"]
# # Create histograms for muons and electrons
# hist_muons_p = bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hist_electrons_p = bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# # Fill the histograms with the p values
# hist_muons_p.fill(ak.flatten(gen_leps_status1_from_bW_muons_p), weight=1.0)
# hist_electrons_p.fill(ak.flatten(gen_leps_status1_from_bW_electrons_p), weight=1.0)
# # Create views of the histograms
# hist_muons_p_view = hist_muons_p.view()
# hist_electrons_p_view = hist_electrons_p.view()
# # Plot the histograms
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.stairs(hist_muons_p_view.value, hist_muons_p.axes[0].edges, fill=True, label="p Muons")
# plt.title("p Muons from Wb")
# plt.xlabel("p Muons")
# plt.ylabel("Events")
# plt.axvline(15, color='red', linestyle='dashed', linewidth=1, label='p Cutoff 15')
# plt.legend()
# plt.subplot(1, 2, 2)
# plt.stairs(hist_electrons_p_view.value, hist_electrons_p.axes[0].edges, fill=True, label="p Electrons")
# plt.axvline(15, color='red', linestyle='dashed', linewidth=1, label='p Cutoff 15')
# plt.title("p Electrons from Wb")
# plt.xlabel("p Electrons")
# plt.ylabel("Events")
# plt.legend()
# plt.tight_layout()
# plt.savefig("p_Muons_Electrons_from_Wb.pdf")
# plt.close()

### P Dists for Wb muons and Wb electrons

### Efficiency and Inefficiency Calculations for momentum cuts on electrons and muons from W and b ROC Curves

# Do this for Muon cuts from 12-20 
# efficiencies_muons= []
# efficiencies_electrons= []
# inefficiencies_muons= []
# inefficiencies_electrons= []
# for p in range(12, 21):
#     mask_muons_W= ak.flatten(gen_leps_status1_fromW_muons_p)> p
#     mask_muons_b= ak.flatten(gen_leps_status1_from_b_muons_p) > p
#     mask_electrons_W= ak.flatten(gen_leps_status1_fromW_electrons_p) > p
#     mask_electrons_b= ak.flatten(gen_leps_status1_from_b_electrons_p) > p
#     muons_W_passed= ak.flatten(gen_leps_status1_fromW_muons_p)[mask_muons_W]
#     muons_b_passed= ak.flatten(gen_leps_status1_from_b_muons_p)[mask_muons_b]
#     electrons_W_passed= ak.flatten(gen_leps_status1_fromW_electrons_p)[mask_electrons_W]
#     electrons_b_passed= ak.flatten(gen_leps_status1_from_b_electrons_p)[mask_electrons_b]
#     efficiency_muons_W= len(muons_W_passed)/len(ak.flatten(gen_leps_status1_fromW_muons_p))
#     inefficiency_muons_b= len(muons_b_passed)/len(ak.flatten(gen_leps_status1_from_b_muons_p))
#     efficiency_electrons_W= len(electrons_W_passed)/len(ak.flatten(gen_leps_status1_fromW_electrons_p))
#     inefficiency_electrons_b= len(electrons_b_passed)/len(ak.flatten(gen_leps_status1_from_b_electrons_p))
#     efficiencies_muons.append(efficiency_muons_W)
#     inefficiencies_muons.append(inefficiency_muons_b)
#     efficiencies_electrons.append(efficiency_electrons_W)
#     inefficiencies_electrons.append(inefficiency_electrons_b)



# ### ROC Curves for momentum cuts on electrons and muons from W and b
# plt.figure(figsize=(10, 6))
# plt.scatter(inefficiencies_muons, efficiencies_muons,label='Muons ROC', color='blue')
# plt.title('ROC Curve for Muons from W and b pcut[12,21)')
# plt.ylabel('Efficiency (W muons)')
# plt.xlabel('Inefficiency (b muons)')
# plt.legend()
# plt.savefig("ROC_Curve_Muons_scatter.pdf")
# plt.close()

# plt.scatter(inefficiencies_electrons, efficiencies_electrons, label='Electrons ROC', color='orange')
# plt.title('ROC Curve for Electrons from W and b pcut[12,21)')
# plt.ylabel('Efficiency (W electrons)')
# plt.xlabel('Inefficiency (b electrons)')
# plt.legend()
# plt.savefig("ROC_Curve_Electrons_scatter.pdf")
# plt.close()

# # # Create Dataframe to CSV to store results
# df_momentum_cut_eff_ineff= pd.DataFrame({"p": list(range(12, 21)), "Efficiency Muons from W": efficiencies_muons, "Inefficiency Muons from b": inefficiencies_muons,
#                   "Efficiency Electrons from W": efficiencies_electrons, "Inefficiency Electrons from b": inefficiencies_electrons})
# df_momentum_cut_eff_ineff.to_csv("csvs2/momentum_cut_efficiency_inefficiency.csv", index=False)
























# n_leps_d_iso_prompt_precut= arrays["n_leps_d_iso_prompt_precut"]
# n_leps_d_iso_non_prompt_precut= arrays["n_leps_d_iso_non_prompt_precut"]
# n_leps_d_iso_all_precut_status1= arrays["n_leps_d_iso_all_precut_status1"]
# #on this quick check expect number to be the same 
# D_Iso_Values_Prompt= ak.flatten(arrays["D_Iso_Values_Prompt"])
# D_Iso_Values_nonPrompt= ak.flatten(arrays["D_Iso_Values_nonPrompt"])
# D_Iso_Values_all_status1= ak.flatten(arrays["D_Iso_Values_all_status1"])

# size_gen_leps_status1_fromW= arrays["size_gen_leps_status1_fromW"]
# size_gen_leps_status1_from_b= arrays["size_gen_leps_status1_from_b"]

# combined_leptons_per_event_reco= arrays["combined_leptons_per_event"]
# nlep= arrays["nlep"]
# nlep_total_precut= arrays["nlep_total"]

# print(ak.flatten(All_Delta_R_W),"All_Delta_R_W")
# print(n_leps_d_iso_prompt_precut, "Prompt")
# print(size_gen_leps_status1_fromW, "size_gen_leps_status1_fromW_gen")
# print(arrays["D_Iso_Values_Prompt"], "Prompt")
# print(combined_leptons_per_event_reco,"combined_leptons_per_event_reco")
# print(nlep_total_precut,"nlep_total_precut")



### Momentum Dists 

# fraction_not_passing_cut= arrays["fraction_not_passing_cut"]
# size_passing_cut=arrays["size_passing_cut"]
# print("fraction_not_passing_cut", np.sum(fraction_not_passing_cut))
# print("size_passing_cut", np.sum(size_passing_cut))
# print(np.sum(nlep_total_precut), "nlep_total_precut")
# fraction_not_cutoff_by_sel_iso_and_momentum_cut= np.sum(size_passing_cut)/np.sum(nlep_total_precut)
# print(fraction_not_cutoff_by_sel_iso_and_momentum_cut, "fraction_not_cutoff_by_sel_iso_and_momentum_cut")


# gen_leps_status1_p_W= arrays["gen_leps_status1_p_W"]
# gen_leps_status1_from_b_p= arrays["gen_leps_status1_from_b_p"]
# momentum_post_cut= arrays["momentum_post_iso_cut"]
# leps_that_dont_pass_iso_p= arrays["leps_that_dont_pass_iso_p"]
# momentum_from_94= arrays["momentum_from_94"]
# momentum_merged_leptons_list_past_5_iso_sel= arrays["momentum_merged_leptons_list_past_5_iso_sel"]
# merged_leptons_list_just_past_5= arrays["merged_leptons_list_just_past_5"]

# hist_gen_leps_status1_p= bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hist_gen_leps_from_b_p= bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hist_momentum_post_cut= bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hist_leps_that_dont_pass_iso_p= bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hists_momentum_94= bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hists_momentum_merged_leptons_list_past_5_iso_sel= bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# hists_merged_leptons_list_just_past_5= bh.Histogram(bh.axis.Regular(100, 0, 100), storage=bh.storage.Weight())
# # Fill the histograms with the flattened arrays



# hist_gen_leps_status1_p.fill(ak.flatten(gen_leps_status1_p_W), weight=1.0)
# hist_gen_leps_from_b_p.fill(ak.flatten(gen_leps_status1_from_b_p), weight=1.0)
# hist_momentum_post_cut.fill(ak.flatten(momentum_post_cut), weight=1.0)
# hist_leps_that_dont_pass_iso_p.fill(ak.flatten(leps_that_dont_pass_iso_p), weight=1.0)
# hists_momentum_94.fill(ak.flatten(momentum_from_94), weight=1.0)
# hists_momentum_merged_leptons_list_past_5_iso_sel.fill(ak.flatten(momentum_merged_leptons_list_past_5_iso_sel), weight=1.0)
# hists_merged_leptons_list_just_past_5.fill(ak.flatten(merged_leptons_list_just_past_5), weight=1.0)

# hist_gen_leps_status1_p_view = hist_gen_leps_status1_p.view()
# hist_gen_leps_from_b_p_view = hist_gen_leps_from_b_p.view()
# hist_momentum_post_cut_view = hist_momentum_post_cut.view()
# hist_leps_that_dont_pass_iso_p_view = hist_leps_that_dont_pass_iso_p.view()
# hists_momentum_94_view = hists_momentum_94.view()
# hists_momentum_merged_leptons_list_past_5_iso_sel_view = hists_momentum_merged_leptons_list_past_5_iso_sel.view()
# hists_merged_leptons_list_just_past_5_view = hists_merged_leptons_list_just_past_5.view()

# fig, axs = plt.subplots(3, 3, figsize=(12, 10))
# axs[0, 0].stairs(hist_gen_leps_status1_p_view.value, hist_gen_leps_status1_p.axes[0].edges, fill=True, label="gen_leps_status1_p_W")
# axs[0, 0].set_title("gen_leps_status1_p_W")
# axs[0, 0].set_xlabel("gen_leps_status1_p_W")
# axs[0, 0].set_ylabel("Events")
# axs[0, 1].stairs(hist_gen_leps_from_b_p_view.value, hist_gen_leps_from_b_p.axes[0].edges, fill=True, label="gen_leps_from_b_p")
# axs[0, 1].set_title("gen_leps_from_b_p")
# axs[0, 1].set_xlabel("gen_leps_from_b_p")
# axs[0, 1].set_ylabel("Events")
# axs[1, 0].stairs(hist_momentum_post_cut_view.value, hist_momentum_post_cut.axes[0].edges, fill=True, label="momentum_post_iso_cut")
# axs[1, 0].set_title("momentum_post_iso_cut")
# axs[1, 0].set_xlabel("momentum_post_iso_cut")
# axs[1, 0].set_ylabel("Events")
# axs[1, 1].stairs(hist_leps_that_dont_pass_iso_p_view.value, hist_leps_that_dont_pass_iso_p.axes[0].edges, fill=True, label="leps_that_dont_pass_iso_p")
# axs[1, 1].set_title("leps_that_dont_pass_iso_p")
# axs[1, 1].set_xlabel("leps_that_dont_pass_iso_p")
# axs[1, 1].set_ylabel("Events")
# axs[2, 0].stairs(hists_momentum_94_view.value, hists_momentum_94.axes[0].edges, fill=True, label="momentum_from_94")
# axs[2, 0].set_title("momentum_from_94")
# axs[2, 0].set_xlabel("momentum_from_94")
# axs[2, 0].set_ylabel("Events")
# axs[2, 1].stairs(hists_momentum_merged_leptons_list_past_5_iso_sel_view.value, hists_momentum_merged_leptons_list_past_5_iso_sel.axes[0].edges, fill=True, label="momentum_merged_leptons_list_past_5_iso_sel")
# axs[2, 1].set_title("momentum_merged_leptons_list_past_5_iso_sel")
# axs[2, 1].set_xlabel("momentum_merged_leptons_list_past_5_iso_sel")
# axs[2, 1].set_ylabel("Events")
# axs[2, 2].stairs(hists_merged_leptons_list_just_past_5_view.value, hists_merged_leptons_list_just_past_5.axes[0].edges, fill=True, label="merged_leptons_list_just_past_5")
# axs[2, 2].set_title("merged_leptons_list_just_past_5")
# axs[2, 2].set_xlabel("merged_leptons_list_just_past_5")
# axs[2, 2].set_ylabel("Events")
# axs[0, 2].axis('off')  # Hide the empty subplot
# axs[1,2].axis('off')  # Hide the empty subplot
# axs[0, 0].legend()

# plt.tight_layout()
# plt.savefig("Momentum_Dists_new_remove_fullstats_momentum_reco_cut_5.pdf")

### Momentum Dists 



# B info 

# print(ak.flatten(All_Delta_R_B),"All_Delta_R_B")
# print(arrays["D_Iso_Values_nonPrompt"], "NonPrompt")
# print(n_leps_d_iso_non_prompt_precut, "NonPrompt")
# print(size_gen_leps_status1_from_b, "size_gen_leps_status1_from_b_gen")

# B info 



# print(len(D_Iso_Values_all_status1),"all_status1")
# print(len(D_Iso_Values_Prompt),"prompt_precut")
# print(len(D_Iso_Values_nonPrompt),"nonPrompt_precut")
# print(D_Iso_Values_all_status1)



# mask0= D_Iso_Values_Prompt < 0.20
# mask1= D_Iso_Values_nonPrompt < 0.20
# mask2= D_Iso_Values_all_status1 < 0.20
# n_leps_d_iso_prompt_postcut= n_leps_d_iso_prompt_precut
# n_leps_d_iso_nonPrompt_postcut= n_leps_d_iso_non_prompt_precut
# n_leps_d_iso_postcut_all_status1= n_leps_d_iso_all_precut_status1
#post cut meaning we mask them not cut in treemaker 

 
### Lepton Dist Events (Prompt only) check

 # Your array here
# hist = bh.Histogram(bh.axis.Regular(6, 0, 6), storage=bh.storage.Weight())

# # Fill the histogram with the array values
# hist.fill(combined_leptons_per_event_reco)
# #normalize and plot hits
# hist_view = hist.view()
# hist_sum= hist.sum().value
# normalized_hist_vals = hist_view.value / hist_sum
# print("Normalized Histogram Values:", normalized_hist_vals)
# print(hist)
# print(normalized_hist_vals,"normalized_hist_vals")
# plt.figure(figsize=(8, 6))
# plt.stairs(normalized_hist_vals, hist.axes[0].edges, fill=True, label="Lepton Dist")
# # plt.stairs(hist_view.value, hist.axes[0].edges, fill=True, label="Lepton Dist")
# plt.xlabel("#Leptons per event")
# plt.ylabel("Events")
# plt.title("Lepton Dist coneIso(0.01,0.03) all reco")
# plt.legend()
# plt.savefig("lepton_dist_normalized.pdf")

### Lepton Dist Events (Prompt only) check

# print(np.sum(n_leps_d_iso_postcut_prompt),"postcut_prompt.25diso")
# print(np.sum(n_leps_d_iso_postcut_nonPrompt),"postcut_nonPrompt.25diso")
# print(np.sum(n_leps_d_iso_postcut_all_status1),"postcut_all_status1.25diso")

### Jet Multiplicity for D_iso Stuff

# D_iso_for_jets=0.25
# mask1= D_Iso_Values_Prompt < D_iso_for_jets
# D_Iso_cut= D_Iso_Values_Prompt[mask1]
# mask2= D_Iso_Values_nonPrompt < D_iso_for_jets
# D_Iso_nonPrompt_cut= D_Iso_Values_nonPrompt[mask2]
# efficiency_prompt_cut= len(D_Iso_cut)/(len(D_Iso_Values_Prompt))
# inefficiency=len(D_Iso_nonPrompt_cut)/len(D_Iso_Values_nonPrompt)
# # print(efficiency_prompt_cut,"efficiency_prompt_cut")
# # print(len(D_Iso_cut))
# # print(np.sum(n_leps_d_iso_prompt_precut))

# njets_R5= np.sum(arrays["njets_R5"])
# nb_jets= np.sum(arrays["nbjets_R5_true"])
# nc_jets= np.sum(arrays["ncjets_R5_true"])
# nljets= np.sum(arrays["nljets_R5_true"])
# ngjets= np.sum(arrays["ngjets_R5_true"])

# print(np.sum(nb_jets),"number of b jets")
# print(np.sum(nc_jets),"number of c jets")
# print(np.sum(nljets),"number of leptons jets")
# print(np.sum(ngjets),"number of g jets")
# print(np.sum(njets_R5),"number of jets")

# import os
# # Create the DataFrame
# f = pd.DataFrame({
#     "njets_R5": [njets_R5],
#     "nb_jets": [nb_jets],
#     "nc_jets": [nc_jets],
#     "nljets": [nljets],
#     "ngjets": [ngjets],
#     "D_iso_for_jets": [D_iso_for_jets],
#     "effciency": [efficiency_prompt_cut],
#     "inefficiency": [inefficiency],
# })

# # Append the DataFrame to the CSV file
# f.to_csv('csvs/Jet_multiplicity_as_function_d_iso.csv', mode='a', index=False, header=not os.path.exists('csvs/Jet_multiplicity_as_function_d_iso.csv'))

### Jet Multiplicity for D_iso Stuff







# D_Iso_Values_Prompt= arrays["D_Iso_Values_Prompt"]
# print(D_Iso_Values_Prompt)
# D_Iso_Values_nonPrompt= arrays["D_Iso_Values_nonPrompt"]
# print(D_Iso_Values_nonPrompt)
# p_values_fromW= arrays["p_values_fromW"]
# gen_leps_status1_p_W= arrays["gen_leps_status1_p_W"]


# all_status2_taus_fromWs= arrays["all_status2_taus_fromWs"]
# print(all_status2_taus_fromWs,"all_status2_taus_fromWs")

# all_status2_taus_fromWs_e_mu_daughters= arrays["all_status2_taus_fromWs_e_mu_daughters"]
# print(ak.flatten(all_status2_taus_fromWs_e_mu_daughters))






# gen_leps_status1_pdgId= arrays["gen_leps_status1_pdgId"]
# print(len(ak.flatten(gen_leps_status1_pdgId)),"pdgId_particles_fromW")

# gen_leps_status1_from_b_pdgId= arrays["gen_leps_status1_from_b_pdgId"]
# print(len(ak.flatten(gen_leps_status1_from_b_pdgId)),"pdgId_from_b")

# gen_leps_status1_mother_pdgId_prompt= arrays["gen_leps_status1_mother_pdgId_prompt"]
# print(ak.flatten(gen_leps_status1_mother_pdgId_prompt),"pdgId_prompt_mother_unfiltered")


# ngen_leps_status1_fromW= arrays["ngen_leps_status1_fromW"]
# print(ngen_leps_status1_fromW,"number leps from W")

# ngen_leps_status1_from_b= arrays["ngen_leps_status1_from_b"]
# print(ngen_leps_status1_from_b,"number leps from b")


# sanity_checks_from_b= arrays["sanity_checks_from_b"]
# print(ak.flatten(sanity_checks_from_b),"sanity_checks_from_b")
# sanity_checks_fromW= arrays["sanity_checks_fromW"]
# print(ak.flatten(sanity_checks_fromW),"sanity_checks_fromW")






###Normalize combined D_Iso_Values Curve

# combined_data = D_Iso_Values_all_status1
# bins = 150
# range = (0, 2)
# # Define histogram with Weight storage and proper axis
# hist = bh.Histogram(bh.axis.Regular(bins, *range), storage=bh.storage.Weight())

# # Fill the histogram
# hist.fill(combined_data, weight=1.0)

# # Get the sum of weights
# sum_weights = hist.sum().value

# # For normalization with Weight storage, we need to access the view's value attribute
# hist_view = hist.view()
# normalized_values = hist_view.value / sum_weights
# normalized_variances = hist_view.variance / (sum_weights * sum_weights)

# # Plot using the normalized values
# plt.figure(figsize=(8, 6))
# plt.stairs(normalized_values, hist.axes[0].edges, fill=True, label="Normalized D_Iso_Values")
# plt.title("Combined Normalized D_Iso_Values Histogram .4 Cone Iso")
# plt.xlabel("D_Iso_Values")
# plt.ylabel("Normalized Events")
# plt.xscale("log")
# plt.yscale("log")
# plt.xlim(0, 2)
# plt.ylim(0, 1)  # or plt.ylim(0, np.max(normalized_values) * 1.2)
# plt.legend()
# plt.savefig("normalized_histogram_.4.pdf")
# plt.savefig("normalized_histogram_.4.png")
# plt.close()

###Normalize combined D_Iso_Values Curve




# print(D_Iso_Values_Prompt,"prompt_precut")
# print(D_Iso_Values_nonPrompt,"nonPrompt_precut")

# print(D_Iso_Values_all_status1, " all_D_Iso_Values_all_status1")







# muons_n= arrays["muons_n"]
# electrons_n= arrays["electrons_n"]
# print(np.sum(muons_n),"number of muons")
# print(np.sum(electrons_n),"number of electrons")

# mask1= D_Iso_Values_Prompt < 0.26
# mask2= D_Iso_Values_nonPrompt < 0.26
# D_iso_prompt_cut= len(D_Iso_Values_Prompt[mask1])
# D_iso_nonPrompt_cut= len(D_Iso_Values_nonPrompt[mask2])
# efficiency_prompt_cut_check= D_iso_prompt_cut/np.sum(n_leps_d_iso_prompt_precut)
# inefficiency_non_prompt_cut_check= D_iso_nonPrompt_cut/np.sum(n_leps_d_iso_non_prompt_precut)



# print(efficiency_prompt_cut_check,"efficiency_prompt_cut_ total prompt after / total prompt before, want increase this")
# print(inefficiency_non_prompt_cut_check,"inefficiency_non_prompt_cut, total nonPrompt after / total nonPrompt before, want to decrease this")
# muon_size= arrays["muon_size"]
# electron_size= arrays["electron_size"]
# nlep_total= arrays["nlep_total"]
# merged_leptons_list= arrays["merged_leptons_list"]
# merged_leptons_list_coneIso= ak.flatten(arrays["merged_leptons_list_coneIso"])




### ROC CURVE CALCS

# efficiencies=[]
# inefficiencies=[]
# d_iso_cuts_with_associated_efficiencies=[]
# total_leps_after_cut=[]
# amount_d_values_check=100
# for i in range(0,amount_d_values_check):
#     mask1= D_Iso_Values_Prompt < i/amount_d_values_check
#     mask2= D_Iso_Values_nonPrompt < i/amount_d_values_check
#     D_iso_prompt_cut= len(D_Iso_Values_Prompt[mask1])
#     D_iso_nonPrompt_cut= len(D_Iso_Values_nonPrompt[mask2])
#     # print(D_iso_nonPrompt_cut)
#     efficiency_prompt_cut= D_iso_prompt_cut/np.sum(n_leps_d_iso_prompt_precut)
#     inefficiency_non_prompt_cut= D_iso_nonPrompt_cut/np.sum(n_leps_d_iso_non_prompt_precut)
#     efficiencies.append(efficiency_prompt_cut)
#     inefficiencies.append(inefficiency_non_prompt_cut)
#     total_leps_after_cut.append(D_iso_prompt_cut+D_iso_nonPrompt_cut)
#     d_iso_cuts_with_associated_efficiencies.append(i/amount_d_values_check)
# print(efficiencies)
# print(inefficiencies)
# print(total_leps_after_cut)

### ROC CURVE CALCS




# hist2=bh.Histogram(bh.axis.Regular(100, 0, 1), storage=bh.storage.Weight())
# hist2.fill(ak.flatten(merged_leptons_list_coneIso), weight=1.0)
# hist2_view = hist2.view()
# plt.figure(figsize=(8, 6))
# plt.stairs(hist2_view.value, hist2.axes[0].edges, fill=True, label="D_Iso_Values_all_status1")
# plt.title("Filled Hist of #leps passing all D_Iso Vals")
# plt.xlabel("D_Iso_Values_all_status1")
# plt.ylabel("Events")
# plt.legend()
# plt.savefig("filled_histogram_all_status1.pdf")

### Lepton Number as function of D_Iso Cutoff

# plt.plot(d_iso_cuts_with_associated_efficiencies, total_leps_after_cut, label="#Prompt+#NonPrompt After Cut")
# plt.ylabel("#Prompt+#NonPrompt After Cut")
# plt.xlabel("D_Iso Cutoff")
# plt.title("Total #Prompt+#NonPrompt After Cut vs D_Iso Cutoff")
# plt.legend()
# plt.savefig("plots_WbWb/Total_Leptons_After_Cut_vs_D_Iso_Cutoff.pdf")

# number_all_reco_leps=[]
# associated_d_vals=[]
# print(merged_leptons_list_coneIso)
# for i in range(0, amount_d_values_check):
#     mask1= merged_leptons_list_coneIso <i/amount_d_values_check
#     D_iso_number_cut= len(merged_leptons_list_coneIso[mask1])
#     number_all_reco_leps.append(D_iso_number_cut)
#     associated_d_vals.append(i/amount_d_values_check)


# plt.plot(associated_d_vals, number_all_reco_leps, label="All Reco Leptons After Cut")
# plt.ylabel("#All Reco Leptons After Cut")
# plt.xlabel("D_Iso Cutoff")
# plt.title("Total #All Reco Leptons After Cut vs D_Iso Cutoff")
# plt.legend()
# plt.savefig("plots_WbWb/All_Reco_Leptons_After_Cut_vs_D_Iso_Cutoff.pdf")

### Lepton Number as function of D_Iso Cutoff


### ROC CURVE

# plt.scatter(inefficiencies, efficiencies, label="ROC Curve", color="blue",s=1)
# plt.ylabel("Efficiency Promp_Postcut/Prompt_Precut")
# plt.xlabel("Inefficiency, NonPrompt_Postcut/NonPrompt_Precut")
# plt.title("no_size_filter_ROC Curve D_Iso Cutoffs_.3 [0,1]")
# #sanity check cause i was using diff muon electron all list and see if still game same thing as before 
# plt.axvline(inefficiencies[20],color='red',linestyle='dashed',linewidth=1)
# plt.xscale("log")
# plt.yscale("linear")
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.tick_params(axis='x', labelsize=10)
# plt.savefig("plots_csvs/no_size_filter_new_ROC_curve_data_0.01->0.3.pdf")
# plt.close()
# import pandas as pd
# # signal_background_precut_ratio=np.sum(n_leps_d_iso_prompt_precut)/np.sum(n_leps_d_iso_non_prompt_precut)
# # signal_backgroun_postcut_dcut= np.sum(n_leps_d_iso_postcut_prompt)/np.sum(n_leps_d_iso_postcut_nonPrompt)
# df= pd.DataFrame({"Inefficiency": inefficiencies, "Efficiency": efficiencies,"D_Iso_Cutoff": d_iso_cuts_with_associated_efficiencies,"All_status_1_number": len(D_Iso_Values_all_status1), "Prompt_number": len(D_Iso_Values_Prompt), "NonPrompt_number": len(D_Iso_Values_nonPrompt), "Total_leps_after_cut": total_leps_after_cut})
# df.to_csv("csvs2/no_size_filter_new_ROC_curve_data_0.01->0.3.csv", index=False)
# print(d_iso_cuts_with_associated_efficiencies[20])
# # Efficiency vs D_Iso Cutoff
# plt.plot(d_iso_cuts_with_associated_efficiencies, efficiencies)
# plt.ylabel("Efficiency Promp_Postcut/Prompt_Precut")
# plt.xlabel("D_Iso Cutoff")
# plt.title("Efficiency vs D_Iso Cutoff")

# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.savefig("Efficiency_vs_D_Iso_Cutoff.pdf")
# plt.close()

### ROC CURVE

### Inefficiency vs D_Iso Cutoff

# plt.plot(d_iso_cuts_with_associated_efficiencies, inefficiencies)
# plt.ylabel("Inefficiency NonPrompt_Postcut/NonPrompt_Precut")
# plt.xlabel("D_Iso Cutoff")
# plt.title("Inefficiency vs D_Iso Cutoff")
# # plt.yscale("log")
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.savefig("Inefficiency_vs_D_Iso_Cutoff.pdf")
# plt.close()


# plt.plot(d_iso_cuts_with_associated_efficiencies, efficiencies, label="Efficiency")
# plt.ylabel("Efficiency Promp_Postcut/Prompt_Precut")
# plt.xlabel("D_Iso Cutoff")
# plt.title("Efficiency vs D_Iso Cutoff")
# plt.plot(d_iso_cuts_with_associated_efficiencies, inefficiencies, label="Inefficiency")
# plt.ylabel("Efficiencies(In)")

# plt.title("Inefficiency vs D_Iso Cutoff")

# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.savefig("Efficiencies_Inefficiences_vs_cutoff.pdf")
# plt.legend()
# plt.close()

### Inefficiency vs D_Iso Cutoff














### 2D histogram with x axis as d iso and y axis as z0 for prompt and nonprompt 

# gen_leps_status1_fromW_z0= arrays["gen_leps_status1_fromW_z0"]
# gen_leps_status1_fromW_z0_matched_indices_z0= arrays["gen_leps_status1_fromW_z0_matched_indices_z0"]
# matched_fromW_leptons_and_z0_p_cut_z0= arrays["matched_fromW_leptons_and_z0_p_cut_z0"]
# fromW_reco_indices= arrays["fromW_reco_indices"]
# gen_leps_status1_fromW_z0_matched_indices_z0_matched_indices= arrays["gen_leps_status1_fromW_z0_matched_indices_z0_matched_indices"]
# print(len(ak.flatten(gen_leps_status1_fromW_z0)),"gen_leps_status1_fromW_z0")
# print(len(ak.flatten(matched_fromW_leptons_and_z0_p_cut_z0)),"matched_fromW_leptons_and_z0_p_cut_z0")
# print(len(ak.flatten(gen_leps_status1_fromW_z0_matched_indices_z0)),"gen_leps_status1_fromW_z0_matched_indices_z0")
# # print(fromW_reco_indices,"fromW_reco_indices")
# # print(gen_leps_status1_fromW_z0_matched_indices_z0_matched_indices,"indices from matched W z0s")



# gen_leps_status1_from_b_z0= arrays["gen_leps_status1_from_b_z0"]
# gen_leps_status1_from_b_z0_matched_indices_z0= arrays["gen_leps_status1_from_b_z0_matched_indices_z0"]
# gen_leps_status1_from_b_z0_matched_indices_z0_matched_indices= arrays["gen_leps_status1_from_b_z0_matched_indices_z0_matched_indices"]
# from_b_reco_indices= arrays["from_b_reco_indices"]



# # print(gen_leps_status1_from_b_z0,"gen_leps_status1_from_b_z0")
# print(len(ak.flatten(gen_leps_status1_from_b_z0_matched_indices_z0)),"gen_leps_status1_from_b_z0_matched_indices_z0")
# # print(from_b_reco_indices,"from_b_reco_indices")
# print(len(ak.flatten(gen_leps_status1_from_b_z0_matched_indices_z0_matched_indices)),"indices from matched b z0s")
# matched_fromb_leptons_and_z0_p_cut_z0= arrays["matched_fromb_leptons_and_z0_p_cut_z0"]
# print(len(ak.flatten(matched_fromb_leptons_and_z0_p_cut_z0)),"matched_fromb_leptons_and_z0_p_cut_z0")
# # matched_fromb_leptons_and_z0_check= arrays["matched_fromb_leptons_and_z0_check"]
# # print(len(ak.flatten(matched_fromb_leptons_and_z0_check)),"matched_fromb_leptons_and_z0_check_see if same length as p cut z0 it shouldnt be ")
# matched_fromb_leptons_and_z0_check_p= arrays["matched_fromb_leptons_and_z0_check_p"]
# print(min(ak.flatten(matched_fromb_leptons_and_z0_check_p)),"matched_fromb_leptons_and_z0_check_p")
# # gen_leps_status1_fromW_vertex_xyz= arrays["gen_leps_status1_fromW_vertex_xyz"]
# # print(gen_leps_status1_fromW_vertex_xyz,"gen_leps_status1_fromW_vertex_xyz")
# # gen_leps_status1_from_b_vertex_xyz= arrays["gen_leps_status1_from_b_vertex_xyz"]
# # print(gen_leps_status1_from_b_vertex_xyz,"gen_leps_status1_from_b_vertex_xyz")


# D_Iso_Values_Prompt_z0= arrays["D_Iso_Values_Prompt_z0"]
# print(len(ak.flatten(D_Iso_Values_Prompt_z0)),"D_Iso_Values_Prompt_z0")

# D_Iso_Values_Prompt = arrays["D_Iso_Values_Prompt"]
# print(len(ak.flatten(D_Iso_Values_Prompt)),"D_Iso_Values_Prompt")

# z0_Values_Prompt= arrays["z0_Values_Prompt"]
# print(len(ak.flatten(z0_Values_Prompt)),"z0_Values_Prompt")

# D_Iso_Values_NonPrompt_z0= arrays["D_Iso_Values_NonPrompt_z0"]
# print(len(ak.flatten(D_Iso_Values_NonPrompt_z0)),"D_Iso_Values_NonPrompt_z0")
# D_Iso_Values_nonPrompt= arrays["D_Iso_Values_nonPrompt"]
# print(len(ak.flatten(D_Iso_Values_nonPrompt)),"D_Iso_Values_nonPrompt")

# z0_Values_NonPrompt= arrays["z0_Values_NonPrompt"]
# print(len(ak.flatten(z0_Values_NonPrompt)),"z0_Values_NonPrompt")
# print(len(ak.flatten(gen_leps_status1_from_b_z0)),"gen_leps_status1_from_b_z0")
# print(max(ak.flatten(z0_Values_NonPrompt)),"max z0_Values_NonPrompt")
# print(min(ak.flatten(z0_Values_NonPrompt)),"min z0_Values_NonPrompt")
# print(max(ak.flatten(z0_Values_Prompt)),"max z0_Values_Prompt")
# print(min(ak.flatten(z0_Values_Prompt)),"min z0_Values_Prompt")

#Hists for filling of d iso and z0 values
# hist_d_iso_prompt= bh.Histogram(bh.axis.Regular(100, 0, 3))
# hist_d_iso_non_prompt= bh.Histogram(bh.axis.Regular(100, 0, 3))
# hist_z0_prompt= bh.Histogram(bh.axis.Regular(100, 0, 10))
# hist_z0_non_prompt= bh.Histogram(bh.axis.Regular(100, 0, 10))
# for i in range(len(ak.flatten(D_Iso_Values_Prompt))):
#     hist_d_iso_prompt.fill(ak.flatten(D_Iso_Values_Prompt)[i])
# for i in range(len(ak.flatten(D_Iso_Values_nonPrompt))):
#     hist_d_iso_non_prompt.fill(ak.flatten(D_Iso_Values_nonPrompt)[i])
# for i in range(len(ak.flatten(z0_Values_Prompt))):
#     hist_z0_prompt.fill(ak.flatten(z0_Values_Prompt)[i])
# for i in range(len(ak.flatten(z0_Values_NonPrompt))):
#     hist_z0_non_prompt.fill(ak.flatten(z0_Values_NonPrompt)[i])

# plt.stairs(hist_d_iso_prompt.view(), hist_d_iso_prompt.axes[0].centers)
# # plt.stairs(hist_d_iso_non_prompt.view(), hist_d_iso_non_prompt.axes[0].centers)
# # plt.stairs(hist_z0_prompt.view(), hist_z0_prompt.axes[0].centers)
# # plt.stairs(hist_z0_non_prompt.view(), hist_z0_non_prompt.axes[0].centers)
# plt.savefig("hist_d_iso_prompt.png")
# plt.savefig("hist_d_iso_non_prompt.png")
# plt.savefig("hist_z0_prompt.png")
# plt.savefig("hist_z0_non_prompt.png")


## 2D histogram with x axis as d iso and y axis as z0 for prompt and nonprompt 
# hist_d_iso_z0 = bh.Histogram(bh.axis.Regular(100, 0, 1), bh.axis.Regular(100, 0, .1))
# for i in range(len(ak.flatten(D_Iso_Values_Prompt))):
#     hist_d_iso_z0.fill(ak.flatten(D_Iso_Values_Prompt)[i], ak.flatten(z0_Values_Prompt)[i])
# plt.figure()
# plt.imshow(hist_d_iso_z0.view().T, origin='lower', extent=[0, 1, 0, .1], aspect='auto')
# plt.colorbar(label='Counts')
# plt.xlabel('D Isolation')
# plt.ylabel('z0')
# plt.title('Prompt Leptons: D Isolation vs z0')
# plt.savefig("hist_d_iso_z0_prompt.pdf")
# plt.close()

# hist_d_iso_z0_non_prompt = bh.Histogram(bh.axis.Regular(100, 0, 4), bh.axis.Regular(100, -.75, .75))
# for i in range(len(ak.flatten(D_Iso_Values_nonPrompt))):
#     hist_d_iso_z0_non_prompt.fill(ak.flatten(D_Iso_Values_nonPrompt)[i], ak.flatten(z0_Values_NonPrompt)[i])
# plt.figure()
# plt.imshow(hist_d_iso_z0_non_prompt.view().T, origin='lower', extent=[0, 4, -.75, .75], aspect='auto')
# plt.colorbar(label='Counts')
# plt.xlabel('D Isolation')
# plt.ylabel('z0')
# plt.title('Non-Prompt Leptons: D Isolation vs z0')
# plt.savefig("hist_d_iso_z0_non_prompt.pdf")
# plt.close()

### 2D histogram with x axis as d iso and y axis as z0 for prompt and nonprompt 




































