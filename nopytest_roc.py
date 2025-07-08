import uproot 
import pandas as pd
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt
import boost_histogram as bh
import os
import glob
from multiprocessing import Pool, Manager
import logging
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_file(file_path, shared_data):
    """
    Process a single ROOT file and update shared data structures.
    """
    logging.info(f"Processing file: {file_path}")
    try:
        with uproot.open(file_path) as file:
            if "events;1" in file:
                events = file["events;1"]
            elif "events;2" in file:
                events = file["events;2"]
            elif "events;3" in file:
                events = file["events;3"]
            elif "events;4" in file:
                events = file["events;4"]
            elif "events;5" in file:
                events = file["events;5"]
            elif "events;6" in file:
                events = file["events;6"]
            elif "events;7" in file:
                events = file["events;7"]
            elif "events;8" in file:
                events = file["events;8"]
            elif "events;9" in file:
                events = file["events;9"]
            elif "events;30" in file:
                events = file["events;30"]
            elif "events;11" in file:
                events = file["events;11"]
            elif "events;12" in file:
                events = file["events;12"]
            else:
                logging.warning(f"Could not find 'events' or 'events;1' in file: {file_path}")
                return
            arrays = events.arrays(["nbjets_R5_true", "ncjets_R5_true", "nljets_R5_true", "ngjets_R5_true",
                                    "bjets_R5_true", "ljets_R5_true", "jets_R5_theta", "bjets_R5_true_theta",
                                    "jets_R5_isC", "jets_R5_isU", "jets_R5_isD", "jets_R5_isB", "jets_R5_isG", "jets_R5_isS",
                                    "cjets_R5_true_theta", "ljets_R5_true_theta", "gjets_R5_true_theta","njets_R5",], how=dict)
            
            jets_R5_isB = arrays["jets_R5_isB"]
            jets_R5_isC = arrays["jets_R5_isC"]
            jets_R5_isU = arrays["jets_R5_isU"]
            jets_R5_isD = arrays["jets_R5_isD"]
            jets_R5_isS = arrays["jets_R5_isS"]
            jets_R5_isG = arrays["jets_R5_isG"]
            njets_R5 = arrays["njets_R5"]
            # print(max(njets_R5))
            jets_R5_theta = arrays["jets_R5_theta"]
            nbjets_R5_true = arrays["nbjets_R5_true"]
            nbjets_R5_true_total = np.sum(nbjets_R5_true)
            bjets_R5_true_theta = arrays["bjets_R5_true_theta"]
            ncjets_R5_true = arrays["ncjets_R5_true"]
            ncjets_R5_true_total = np.sum(ncjets_R5_true)
            cjets_R5_true_theta = arrays["cjets_R5_true_theta"]

            # Vectorized matching for b-jets and c-jets
            bjet_match_mask = ak.Array([
                [theta in bjets_R5_true_theta[i] for theta in jets_R5_theta[i]]
                for i in range(len(jets_R5_theta))
            ])
            cjet_match_mask = ak.Array([
                [theta in cjets_R5_true_theta[i] for theta in jets_R5_theta[i]]
                for i in range(len(jets_R5_theta))
            ])

            flattened_bjet_match_mask = ak.flatten(bjet_match_mask)
            combined_nested_isB_masked = ak.flatten(jets_R5_isB)[flattened_bjet_match_mask]
            combined_nested_isC_masked = ak.flatten(jets_R5_isC)[flattened_bjet_match_mask]
            combined_nested_isU_masked = ak.flatten(jets_R5_isU)[flattened_bjet_match_mask]
            combined_nested_isD_masked = ak.flatten(jets_R5_isD)[flattened_bjet_match_mask]
            combined_nested_isS_masked = ak.flatten(jets_R5_isS)[flattened_bjet_match_mask]
            combined_nested_isG_masked = ak.flatten(jets_R5_isG)[flattened_bjet_match_mask]
            
            flattened_cjet_match_mask = ak.flatten(cjet_match_mask)
            combined_nested_isB_masked_for_C = ak.flatten(jets_R5_isB)[flattened_cjet_match_mask]
            combined_nested_isC_masked_for_C = ak.flatten(jets_R5_isC)[flattened_cjet_match_mask]
            combined_nested_isU_masked_for_C = ak.flatten(jets_R5_isU)[flattened_cjet_match_mask]
            combined_nested_isD_masked_for_C = ak.flatten(jets_R5_isD)[flattened_cjet_match_mask]
            combined_nested_isS_masked_for_C = ak.flatten(jets_R5_isS)[flattened_cjet_match_mask]
            combined_nested_isG_masked_for_C = ak.flatten(jets_R5_isG)[flattened_cjet_match_mask]
            
            # Append results to shared lists
            with shared_data['lock']:
                shared_data['total_b_jets_per_event'] += nbjets_R5_true_total
                shared_data['total_c_jets_per_event'] += ncjets_R5_true_total
                shared_data['combined_nested_isB_for_b_jets'].append(combined_nested_isB_masked)
                shared_data['combined_nested_isC_for_b_jets'].append(combined_nested_isC_masked)
                shared_data['combined_nested_isU_for_b_jets'].append(combined_nested_isU_masked)
                shared_data['combined_nested_isD_for_b_jets'].append(combined_nested_isD_masked)
                shared_data['combined_nested_isS_for_b_jets'].append(combined_nested_isS_masked)
                shared_data['combined_nested_isG_for_b_jets'].append(combined_nested_isG_masked)
                shared_data['combined_nested_isB_for_c_jets'].append(combined_nested_isB_masked_for_C)
                shared_data['combined_nested_isC_for_c_jets'].append(combined_nested_isC_masked_for_C)
                shared_data['combined_nested_isU_for_c_jets'].append(combined_nested_isU_masked_for_C)
                shared_data['combined_nested_isD_for_c_jets'].append(combined_nested_isD_masked_for_C)
                shared_data['combined_nested_isS_for_c_jets'].append(combined_nested_isS_masked_for_C)
                shared_data['combined_nested_isG_for_c_jets'].append(combined_nested_isG_masked_for_C)
                shared_data["njets_R5"].append(njets_R5)
                
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {str(e)}")
        raise

def plots_csvs_for_roc(channel, ecm, deltaR_label, lepton_label, clustering_label, file_list_path, ncpus):
    efficiencies_b_jets_passing_cut = []
    inefficiencies_c_jets_passing_cut = []
    inefficiencies_u_jets_passing_cut = []
    inefficiencies_d_jets_passing_cut = []
    inefficiencies_ud_jets_passing_cut = []
    inefficiencies_s_jets_passing_cut = []
    inefficiencies_g_jets_passing_cut = []
    cutoff_values = [i/10000 for i in range(0, 10000)]
    efficiencies_c_jets_passing_cut_C = []
    inefficiencies_b_jets_passing_cut_C = []
    inefficiencies_u_jets_passing_cut_C = []
    inefficiencies_d_jets_passing_cut_C = []
    inefficiencies_ud_jets_passing_cut_C = []
    inefficiencies_s_jets_passing_cut_C = []
    inefficiencies_g_jets_passing_cut_C = []

    file_list = file_list_path
    logging.info(f"Starting processing of {len(file_list)} files for channel {channel} at ecm {ecm}")

    # Use Manager to share data between processes
    manager = Manager()
    shared_data = manager.dict()
    shared_data['lock'] = manager.Lock()
    shared_data['total_b_jets_per_event'] = 0
    shared_data['total_c_jets_per_event'] = 0
    shared_data['combined_nested_isB_for_b_jets'] = manager.list()
    shared_data['combined_nested_isC_for_b_jets'] = manager.list()
    shared_data['combined_nested_isU_for_b_jets'] = manager.list()
    shared_data['combined_nested_isD_for_b_jets'] = manager.list()
    shared_data['combined_nested_isS_for_b_jets'] = manager.list()
    shared_data['combined_nested_isG_for_b_jets'] = manager.list()
    shared_data['combined_nested_isB_for_c_jets'] = manager.list()
    shared_data['combined_nested_isC_for_c_jets'] = manager.list()
    shared_data['combined_nested_isU_for_c_jets'] = manager.list()
    shared_data['combined_nested_isD_for_c_jets'] = manager.list()
    shared_data['combined_nested_isS_for_c_jets'] = manager.list()
    shared_data['combined_nested_isG_for_c_jets'] = manager.list()
    shared_data['njets_R5'] = manager.list()
    # Create a pool of workers to process files in parallel
    logging.info(f"Using {ncpus} CPU cores for parallel processing")
    with Pool(processes=ncpus) as pool:
        pool.starmap(process_file, [(file_path, shared_data) for file_path in file_list])

    logging.info("Finished processing all files. Concatenating results...")

    # Concatenate all arrays at once after the loop
    combined_nested_isB_for_b_jets = ak.concatenate(list(shared_data['combined_nested_isB_for_b_jets']))
    combined_nested_isC_for_b_jets = ak.concatenate(list(shared_data['combined_nested_isC_for_b_jets']))
    combined_nested_isU_for_b_jets = ak.concatenate(list(shared_data['combined_nested_isU_for_b_jets']))
    combined_nested_isD_for_b_jets = ak.concatenate(list(shared_data['combined_nested_isD_for_b_jets']))
    combined_nested_isS_for_b_jets = ak.concatenate(list(shared_data['combined_nested_isS_for_b_jets']))
    combined_nested_isG_for_b_jets = ak.concatenate(list(shared_data['combined_nested_isG_for_b_jets']))

    combined_nested_isB_for_c_jets = ak.concatenate(list(shared_data['combined_nested_isB_for_c_jets']))
    combined_nested_isC_for_c_jets = ak.concatenate(list(shared_data['combined_nested_isC_for_c_jets']))
    combined_nested_isU_for_c_jets = ak.concatenate(list(shared_data['combined_nested_isU_for_c_jets']))
    combined_nested_isD_for_c_jets = ak.concatenate(list(shared_data['combined_nested_isD_for_c_jets']))
    combined_nested_isS_for_c_jets = ak.concatenate(list(shared_data['combined_nested_isS_for_c_jets']))
    combined_nested_isG_for_c_jets = ak.concatenate(list(shared_data['combined_nested_isG_for_c_jets']))
    njets_R5_dist = ak.concatenate(list(shared_data['njets_R5']))
    total_b_jets_all_events = shared_data['total_b_jets_per_event']
    total_c_jets_all_events = shared_data['total_c_jets_per_event']
    print(total_b_jets_all_events, total_c_jets_all_events)

    # Vectorize the cutoff loop using numpy operations for b-jets
    cutoff_values_array = np.array(cutoff_values)
    b_scores = np.array(combined_nested_isB_for_b_jets)
    c_scores = np.array(combined_nested_isC_for_b_jets)
    u_scores = np.array(combined_nested_isU_for_b_jets)
    d_scores = np.array(combined_nested_isD_for_b_jets)
    s_scores = np.array(combined_nested_isS_for_b_jets)
    g_scores = np.array(combined_nested_isG_for_b_jets)

    efficiencies_b_jets_passing_cut = np.sum(b_scores > cutoff_values_array[:, None], axis=1) / total_b_jets_all_events
    inefficiencies_c_jets_passing_cut = np.sum(c_scores > cutoff_values_array[:, None], axis=1) / total_b_jets_all_events
    inefficiencies_u_jets_passing_cut = np.sum(u_scores > cutoff_values_array[:, None], axis=1) / total_b_jets_all_events
    inefficiencies_d_jets_passing_cut = np.sum(d_scores > cutoff_values_array[:, None], axis=1) / total_b_jets_all_events
    inefficiencies_s_jets_passing_cut = np.sum(s_scores > cutoff_values_array[:, None], axis=1) / total_b_jets_all_events
    inefficiencies_g_jets_passing_cut = np.sum(g_scores > cutoff_values_array[:, None], axis=1) / total_b_jets_all_events
    inefficiencies_ud_jets_passing_cut = ((np.sum(u_scores > cutoff_values_array[:, None], axis=1) + np.sum(d_scores > cutoff_values_array[:, None], axis=1)) * 0.5) / total_b_jets_all_events

    # Vectorize the cutoff loop using numpy operations for c-jets
    c_scores_C = np.array(combined_nested_isC_for_c_jets)
    b_scores_C = np.array(combined_nested_isB_for_c_jets)
    u_scores_C = np.array(combined_nested_isU_for_c_jets)
    d_scores_C = np.array(combined_nested_isD_for_c_jets)
    s_scores_C = np.array(combined_nested_isS_for_c_jets)
    g_scores_C = np.array(combined_nested_isG_for_c_jets)

    efficiencies_c_jets_passing_cut_C = np.sum(c_scores_C > cutoff_values_array[:, None], axis=1) / total_c_jets_all_events
    inefficiencies_b_jets_passing_cut_C = np.sum(b_scores_C > cutoff_values_array[:, None], axis=1) / total_c_jets_all_events
    inefficiencies_u_jets_passing_cut_C = np.sum(u_scores_C > cutoff_values_array[:, None], axis=1) / total_c_jets_all_events
    inefficiencies_d_jets_passing_cut_C = np.sum(d_scores_C > cutoff_values_array[:, None], axis=1) / total_c_jets_all_events
    inefficiencies_s_jets_passing_cut_C = np.sum(s_scores_C > cutoff_values_array[:, None], axis=1) / total_c_jets_all_events
    inefficiencies_g_jets_passing_cut_C = np.sum(g_scores_C > cutoff_values_array[:, None], axis=1) / total_c_jets_all_events
    inefficiencies_ud_jets_passing_cut_C = ((np.sum(u_scores_C > cutoff_values_array[:, None], axis=1) + np.sum(d_scores_C > cutoff_values_array[:, None], axis=1)) * 0.5) / total_c_jets_all_events
    
    # Ensure output directories exist for plots
    b_jets_plot_dir = f"/eos/user/g/gidaniel/ttThreshold-analysis/all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}"
    c_jets_plot_dir = f"/eos/user/g/gidaniel/ttThreshold-analysis/all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}"
    b_jets_csv_dir = f"/eos/user/g/gidaniel/ttThreshold-analysis/all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}"
    c_jets_csv_dir = f"/eos/user/g/gidaniel/ttThreshold-analysis/all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}"
    local_plot_dir = f"all_jets_{channel}/{ecm}/jet_plots/B_jets/B_scores"
    
    os.makedirs(b_jets_plot_dir, exist_ok=True)
    os.makedirs(c_jets_plot_dir, exist_ok=True)
    os.makedirs(b_jets_csv_dir, exist_ok=True)
    os.makedirs(c_jets_csv_dir, exist_ok=True)
    os.makedirs(local_plot_dir, exist_ok=True)

    # B-jet plots
    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_c_jets_passing_cut, color="blue", label="b vs c")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(c-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{b_jets_plot_dir}/btag_efficiency_vs_c_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_u_jets_passing_cut, color="green", label="b vs u")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(u-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{b_jets_plot_dir}/btag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_d_jets_passing_cut, color="red", label="b vs d")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(d-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{b_jets_plot_dir}/btag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_ud_jets_passing_cut, color="purple", label="b vs ud")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(ud-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{b_jets_plot_dir}/btag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_s_jets_passing_cut, color="orange", label="b vs s")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(s-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{b_jets_plot_dir}/btag_efficiency_vs_s_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_g_jets_passing_cut, color="brown", label="b vs g")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(g-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{b_jets_plot_dir}/btag_efficiency_vs_g_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_ud_jets_passing_cut, color="green", label="b vs ud")
    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_c_jets_passing_cut, color="blue", label="b vs c")
    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_s_jets_passing_cut, color="orange", label="b vs s")
    plt.plot(efficiencies_b_jets_passing_cut, inefficiencies_g_jets_passing_cut, color="brown", label="b vs g")
    plt.yscale("log")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("jet misid. probability")
    plt.legend(frameon=False)
    plt.savefig(f"{b_jets_plot_dir}/b_roc_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    # C-jet plots
    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_b_jets_passing_cut_C, color="blue", label="c vs b")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(b-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{c_jets_plot_dir}/ctag_efficiency_vs_b_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_u_jets_passing_cut_C, color="green", label="c vs u")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(u-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{c_jets_plot_dir}/ctag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_d_jets_passing_cut_C, color="red", label="c vs d")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(d-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{c_jets_plot_dir}/ctag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_ud_jets_passing_cut_C, color="purple", label="c vs ud")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(ud-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{c_jets_plot_dir}/ctag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_s_jets_passing_cut_C, color="orange", label="c vs s")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(s-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{c_jets_plot_dir}/ctag_efficiency_vs_s_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_g_jets_passing_cut_C, color="brown", label="c vs g")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(g-jet misid. probability)")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"{c_jets_plot_dir}/ctag_efficiency_vs_g_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_s_jets_passing_cut_C, color="orange", label="c vs s")
    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_g_jets_passing_cut_C, color="brown", label="c vs g")
    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_ud_jets_passing_cut_C, color="green", label="c vs ud")
    plt.plot(efficiencies_c_jets_passing_cut_C, inefficiencies_b_jets_passing_cut_C, color="blue", label="c vs b")
    plt.yscale("log")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("jet misid. probability")
    plt.legend(frameon=False)
    plt.savefig(f"{c_jets_plot_dir}/c_roc_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    # Save B-jet CSV files
    df = pd.DataFrame({"efficiencies_b_jets_passing_cut": efficiencies_b_jets_passing_cut, "inefficiencies_c_jets_passing_cut": inefficiencies_c_jets_passing_cut, "cutoff_values": cutoff_values, "nbjets_true": total_b_jets_all_events})
    df.to_csv(f"{b_jets_csv_dir}/btag_efficiency_vs_c_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df1 = pd.DataFrame({"efficiencies_b_jets_passing_cut": efficiencies_b_jets_passing_cut, "inefficiencies_u_jets_passing_cut": inefficiencies_u_jets_passing_cut, "cutoff_values": cutoff_values, "nbjets_true": total_b_jets_all_events})
    df1.to_csv(f"{b_jets_csv_dir}/btag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df2 = pd.DataFrame({"efficiencies_b_jets_passing_cut": efficiencies_b_jets_passing_cut, "inefficiencies_d_jets_passing_cut": inefficiencies_d_jets_passing_cut, "cutoff_values": cutoff_values, "nbjets_true": total_b_jets_all_events})
    df2.to_csv(f"{b_jets_csv_dir}/btag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df3 = pd.DataFrame({"efficiencies_b_jets_passing_cut": efficiencies_b_jets_passing_cut, "inefficiencies_ud_jets_passing_cut": inefficiencies_ud_jets_passing_cut, "cutoff_values": cutoff_values, "nbjets_true": total_b_jets_all_events})
    df3.to_csv(f"{b_jets_csv_dir}/btag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df5 = pd.DataFrame({"efficiencies_b_jets_passing_cut": efficiencies_b_jets_passing_cut, "inefficiencies_s_jets_passing_cut": inefficiencies_s_jets_passing_cut, "cutoff_values": cutoff_values, "nbjets_true": total_b_jets_all_events})
    df5.to_csv(f"{b_jets_csv_dir}/btag_efficiency_vs_s_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df6 = pd.DataFrame({"efficiencies_b_jets_passing_cut": efficiencies_b_jets_passing_cut, "inefficiencies_g_jets_passing_cut": inefficiencies_g_jets_passing_cut, "cutoff_values": cutoff_values, "nbjets_true": total_b_jets_all_events})
    df6.to_csv(f"{b_jets_csv_dir}/btag_efficiency_vs_g_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df4 = pd.DataFrame({"efficiencies_b_jets_passing_cut": efficiencies_b_jets_passing_cut, "inefficiencies_ud_jets_passing_cut": inefficiencies_ud_jets_passing_cut, "inefficiencies_c_jets_passing_cut": inefficiencies_c_jets_passing_cut, "inefficiencies_s_jets_passing_cut": inefficiencies_s_jets_passing_cut, "inefficiencies_g_jets_passing_cut": inefficiencies_g_jets_passing_cut, "cutoff_values": cutoff_values, "nbjets_true": total_b_jets_all_events})
    df4.to_csv(f"{b_jets_csv_dir}/b_roc_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    # Save C-jet CSV files
    df_C = pd.DataFrame({"efficiencies_c_jets_passing_cut_C": efficiencies_c_jets_passing_cut_C, "inefficiencies_b_jets_passing_cut_C": inefficiencies_b_jets_passing_cut_C, "cutoff_values": cutoff_values, "ncjets_true": total_c_jets_all_events})
    df_C.to_csv(f"{c_jets_csv_dir}/ctag_efficiency_vs_b_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df1_C = pd.DataFrame({"efficiencies_c_jets_passing_cut_C": efficiencies_c_jets_passing_cut_C, "inefficiencies_u_jets_passing_cut_C": inefficiencies_u_jets_passing_cut_C, "cutoff_values": cutoff_values, "ncjets_true": total_c_jets_all_events})
    df1_C.to_csv(f"{c_jets_csv_dir}/ctag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df2_C = pd.DataFrame({"efficiencies_c_jets_passing_cut_C": efficiencies_c_jets_passing_cut_C, "inefficiencies_d_jets_passing_cut_C": inefficiencies_d_jets_passing_cut_C, "cutoff_values": cutoff_values, "ncjets_true": total_c_jets_all_events})
    df2_C.to_csv(f"{c_jets_csv_dir}/ctag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df3_C = pd.DataFrame({"efficiencies_c_jets_passing_cut_C": efficiencies_c_jets_passing_cut_C, "inefficiencies_ud_jets_passing_cut_C": inefficiencies_ud_jets_passing_cut_C, "cutoff_values": cutoff_values, "ncjets_true": total_c_jets_all_events})
    df3_C.to_csv(f"{c_jets_csv_dir}/ctag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df5_C = pd.DataFrame({"efficiencies_c_jets_passing_cut_C": efficiencies_c_jets_passing_cut_C, "inefficiencies_s_jets_passing_cut_C": inefficiencies_s_jets_passing_cut_C, "cutoff_values": cutoff_values, "ncjets_true": total_c_jets_all_events})
    df5_C.to_csv(f"{c_jets_csv_dir}/ctag_efficiency_vs_s_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df6_C = pd.DataFrame({"efficiencies_c_jets_passing_cut_C": efficiencies_c_jets_passing_cut_C, "inefficiencies_g_jets_passing_cut_C": inefficiencies_g_jets_passing_cut_C, "cutoff_values": cutoff_values, "ncjets_true": total_c_jets_all_events})
    df6_C.to_csv(f"{c_jets_csv_dir}/ctag_efficiency_vs_g_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    df4_C = pd.DataFrame({"efficiencies_c_jets_passing_cut_C": efficiencies_c_jets_passing_cut_C, "inefficiencies_ud_jets_passing_cut_C": inefficiencies_ud_jets_passing_cut_C, "inefficiencies_b_jets_passing_cut_C": inefficiencies_b_jets_passing_cut_C, "inefficiencies_s_jets_passing_cut_C": inefficiencies_s_jets_passing_cut_C, "inefficiencies_g_jets_passing_cut_C": inefficiencies_g_jets_passing_cut_C, "cutoff_values": cutoff_values, "ncjets_true": total_c_jets_all_events})
    df4_C.to_csv(f"{c_jets_csv_dir}/c_roc_{deltaR_label}{lepton_label}{clustering_label}.csv", index=False)

    ### Jet Distribution as a function of n leps
    histb = bh.Histogram(bh.axis.Regular(110, 0, 1))
    hist_c = bh.Histogram(bh.axis.Regular(110, 0, 1))
    hist_u = bh.Histogram(bh.axis.Regular(110, 0, 1))
    hist_d = bh.Histogram(bh.axis.Regular(110, 0, 1))

    histb.fill(combined_nested_isB_for_b_jets)
    hist_c.fill(combined_nested_isC_for_b_jets)
    hist_u.fill(combined_nested_isU_for_b_jets)
    hist_d.fill(combined_nested_isD_for_b_jets)

    hist_valueb = histb.view()
    hist_valuec = hist_c.view()
    hist_valueu = hist_u.view()
    hist_valued = hist_d.view()

    hist_valueb_norm = hist_valueb / hist_valueb.sum() if hist_valueb.sum() > 0 else hist_valueb
    hist_valuec_norm = hist_valuec / hist_valuec.sum() if hist_valuec.sum() > 0 else hist_valuec
    hist_valueu_norm = hist_valueu / hist_valueu.sum() if hist_valueu.sum() > 0 else hist_valueu
    hist_valued_norm = hist_valued / hist_valued.sum() if hist_valued.sum() > 0 else hist_valued

    plt.stairs(hist_valueb_norm, histb.axes[0].edges, color="blue", label="Normalized B Tag Score for true b jets")
    plt.stairs(hist_valuec_norm, hist_c.axes[0].edges, color="red", label="Normalized C Tag Score for true b jets")
    plt.xlabel("B Tag Score")
    plt.ylabel("Normalized Number of Jets")
    plt.title(f"Normalized B and C Tag Score for true b jets R={deltaR_label}")
    plt.yscale("log")
    plt.legend()
    plt.savefig(f"{local_plot_dir}/btag_score_b_c_jet_combined_deltaR_{deltaR_label}{lepton_label}{clustering_label}_normalized_withfiltered.pdf")
    plt.close()

    plt.stairs(hist_valueb_norm, histb.axes[0].edges, color="blue", label="Normalized B Tag Score for true b jets")
    plt.stairs(hist_valueu_norm, hist_u.axes[0].edges, color="green", label="Normalized U Tag Score for true b jets")
    plt.stairs(hist_valued_norm, hist_d.axes[0].edges, color="black", label="Normalized D Tag Score for true b jets")
    plt.xlabel("B Tag Score")
    plt.ylabel("Normalized Number of Jets")
    plt.yscale("log")
    plt.legend()
    plt.title(f"Normalized B, U, and D Tag Score for true b jets R={deltaR_label}")
    plt.savefig(f"{local_plot_dir}/btag_score_b_u_d_jet_combined_deltaR_{deltaR_label}{lepton_label}{clustering_label}_normalized_withfiltered.pdf")
    plt.close()


    n_jet_dist_hist = bh.Histogram(bh.axis.Regular(12, 0, 12))
    n_jet_dist_hist.fill(njets_R5_dist)
    n_jet_dist_hist_value = n_jet_dist_hist.view()
    n_jet_dist_hist_value_norm = n_jet_dist_hist_value / n_jet_dist_hist_value.sum() if n_jet_dist_hist_value.sum() > 0 else n_jet_dist_hist_value
    plt.stairs(n_jet_dist_hist_value_norm, n_jet_dist_hist.axes[0].edges, color="blue", label="Jet Distribution")
    plt.xlabel("Number of Jets")
    plt.ylabel("Normalized Number of Events")
    plt.title(f"Number of Jets for jets {channel} {ecm}")
    plt.savefig(f"{local_plot_dir}/n_jet_dist_deltaR_{deltaR_label}{lepton_label}{clustering_label}_normalized_withfiltered.pdf")
    plt.close()

ecm_345 = 345
ecm_365 = 365
ecm_91 = 91
ecm_355 = 355
ecm_240 = 240
# if __name__ == "__main__":
parser = argparse.ArgumentParser(description="Run ROC analysis with specified number of CPUs.")
parser.add_argument("--ncpus", type=int, default=os.cpu_count(), help="Number of CPUs to use for parallel processing")
args = parser.parse_args()

# file_nunuH_Hqq_240_inclusive=[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1041/WbWb_inclusive_240/semihad/wzp6_ee_nunuH_Hbb_ecm240/events_{i}.root" for i in range(12)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1041/WbWb_inclusive_240/semihad/wzp6_ee_nunuH_Hcc_ecm240/events_{i}.root" for i in range(11)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1041/WbWb_inclusive_240/semihad/wzp6_ee_nunuH_Hss_ecm240/events_{i}.root" for i in range(11)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1041/WbWb_inclusive_240/semihad/wzp6_ee_nunuH_Huu_ecm240/events_{i}.root" for i in range(49)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1041/WbWb_inclusive_240/semihad/wzp6_ee_nunuH_Hdd_ecm240/events_{i}.root" for i in range(50)]

# plots_csvs_for_roc("nunuH_Hqq_240_inclusive", ecm_240, "0.5", "zero", "R5", file_nunuH_Hqq_240_inclusive, args.ncpus)


# file_nunuH_Hqq_240_exclusive=[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1047/WbWb_exclusive_240/semihad/wzp6_ee_nunuH_Hbb_ecm240/events_{i}.root" for i in range(12)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1047/WbWb_exclusive_240/semihad/wzp6_ee_nunuH_Hcc_ecm240/events_{i}.root" for i in range(11)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1047/WbWb_exclusive_240/semihad/wzp6_ee_nunuH_Hss_ecm240/events_{i}.root" for i in range(11)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1047/WbWb_exclusive_240/semihad/wzp6_ee_nunuH_Huu_ecm240/events_{i}.root" for i in range(49)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250707_1047/WbWb_exclusive_240/semihad/wzp6_ee_nunuH_Hdd_ecm240/events_{i}.root" for i in range(50)]

# plots_csvs_for_roc("nunuH_Hqq_240_exclusive", ecm_240, "0.5", "zero", "R5", file_nunuH_Hqq_240_exclusive, args.ncpus)

file_ZZ_365_incl_2jets=glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250708_1425/WbWb_inclusive_2jets/semihad/p8_ee_ZZ_ecm365/events_*.root")
file_ZZ_365_incl_4jets=glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250708_1426/WbWb_inclusive_4jets/semihad/p8_ee_ZZ_ecm365/events_*.root")
file_ZZ_365_excl_2jets=glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250708_1426/WbWb_exclusive_2jets/semihad/p8_ee_ZZ_ecm365/events_*.root")
file_ZZ_365_excl_4jets=glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250708_1427/WbWb_exclusive_4jets/semihad/p8_ee_ZZ_ecm365/events_*.root")
plots_csvs_for_roc("ZZ_365_incl_2jets", ecm_365, "0.5", "zero", "R5", file_ZZ_365_incl_2jets, args.ncpus)
plots_csvs_for_roc("ZZ_365_incl_4jets", ecm_365, "0.5", "zero", "R5", file_ZZ_365_incl_4jets, args.ncpus)
plots_csvs_for_roc("ZZ_365_excl_2jets", ecm_365, "0.5", "zero", "R5", file_ZZ_365_excl_2jets, args.ncpus)
plots_csvs_for_roc("ZZ_365_excl_4jets", ecm_365, "0.5", "zero", "R5", file_ZZ_365_excl_4jets, args.ncpus)







# nunuH_Hqq_365_zero_list=["wzp6_ee_nunuH_Hbb_ecm365","wzp6_ee_nunuH_Hss_ecm365", "wzp6_ee_nunuH_Hcc_ecm365", "wzp6_ee_nunuH_Huu_ecm365", "wzp6_ee_nunuH_Hdd_ecm365"]

# file_nunuH_Hqq_365= [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_0947/WbWb_zero/semihad/wzp6_ee_nunuH_Hbb_ecm365/events_{i}.root" for i in range(12)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_0947/WbWb_zero/semihad/wzp6_ee_nunuH_Hss_ecm365/events_{i}.root" for i in range(12)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_0947/WbWb_zero/semihad/wzp6_ee_nunuH_Hcc_ecm365/events_{i}.root" for i in range(12)] +[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_0947/WbWb_zero/semihad/wzp6_ee_nunuH_Huu_ecm365/events_{i}.root" for i in range(12)] +[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_0947/WbWb_zero/semihad/wzp6_ee_nunuH_Hdd_ecm365/events_{i}.root" for i in range(12)]

# plots_csvs_for_roc("nunuH_Hqq_365_zero", ecm_365, "0.5", "zero", "R5", file_nunuH_Hqq_365, args.ncpus)

# nunuH_Hqq_365_zero_list=["wzp6_ee_nunuH_Hbb_ecm365","wzp6_ee_nunuH_Hss_ecm365", "wzp6_ee_nunuH_Hcc_ecm365", "wzp6_ee_nunuH_Huu_ecm365", "wzp6_ee_nunuH_Hdd_ecm365"]

# file_nunuH_Hqq_365= [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_1121/WbWb_zero_check/semihad/wzp6_ee_nunuH_Hbb_ecm365/events_{i}.root" for i in range(12)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_1121/WbWb_zero_check/semihad/wzp6_ee_nunuH_Hss_ecm365/events_{i}.root" for i in range(12)] + [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_1121/WbWb_zero_check/semihad/wzp6_ee_nunuH_Hcc_ecm365/events_{i}.root" for i in range(12)] +[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_1121/WbWb_zero_check/semihad/wzp6_ee_nunuH_Huu_ecm365/events_{i}.root" for i in range(12)] +[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250706_1121/WbWb_zero_check/semihad/wzp6_ee_nunuH_Hdd_ecm365/events_{i}.root" for i in range(12)]

# plots_csvs_for_roc("nunuH_Hqq_365_zero_check", ecm_365, "0.5", "zero", "R5", file_nunuH_Hqq_365, args.ncpus)




# nunuH_Hqq_365_zero_list=["wzp6_ee_nunuH_Hbb_ecm365","wzp6_ee_nunuH_Hss_ecm365", "wzp6_ee_nunuH_Hcc_ecm365", "wzp6_ee_nunuH_Huu_ecm365", "wzp6_ee_nunuH_Hdd_ecm365"]



## Current plots/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1845/WbWb_zero_exclusive_2/semihad/wzp6_ee_nunuH_Hcc_ecm365/events_0.root
#next
# file_nunuH_Hqq_365 = [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1845/WbWb_zero_exclusive_2/semihad/wzp6_ee_nunuH_Hbb_ecm365/events_{i}.root" for i in range(12)] +[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1845/WbWb_zero_exclusive_2/semihad/wzp6_ee_nunuH_Hss_ecm365/events_{i}.root" for i in range(12)] +[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1845/WbWb_zero_exclusive_2/semihad/wzp6_ee_nunuH_Hcc_ecm365/events_{i}.root" for i in range(12)] +[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1845/WbWb_zero_exclusive_2/semihad/wzp6_ee_nunuH_Huu_ecm365/events_{i}.root" for i in range(12)] +[f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1845/WbWb_zero_exclusive_2/semihad/wzp6_ee_nunuH_Hdd_ecm365/events_{i}.root" for i in range(12)]

# plots_csvs_for_roc("nunuH_Hqq_365_zero_exclusive_2", ecm_365, "0.5", "zero", "R5", file_nunuH_Hqq_365, args.ncpus)

# file_ZZ_365_two_inclusive_nunu= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1855/WbWb_two_inclusive/semihad/p8_ee_ZZ_ecm365/events_*.root")
# plots_csvs_for_roc("ZZ_two_inclusive_nunu", ecm_365, "0.5", "two", "R5", file_ZZ_365_two_inclusive_nunu, args.ncpus)
#last two are uncommented then plot all of them together


## exclusive rocs processing
#next  after ZZ_zero_inclusive_nunu
# file_ZZ_365_two_exclusive_2_nunu= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1014/WbWb_two_exclusive_2_nunu/semihad/p8_ee_ZZ_ecm365/events_*.root")
# plots_csvs_for_roc("ZZ_two_exclusive_2_nunu", ecm_365, "0.5", "two", "R5", file_ZZ_365_two_exclusive_2_nunu, args.ncpus)


# file_ZZ_365_zero_exclusive_4_nunu= [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1026/WbWb_zero_exclusive_4_nunu/semihad/p8_ee_ZZ_ecm365/events_{i}.root" for i in range(60)]
# file_ZZ_365_zero_exclusive_4_nunu= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1026/WbWb_zero_exclusive_4_nunu/semihad/p8_ee_ZZ_ecm365/events_*.root")
# plots_csvs_for_roc("ZZ_zero_exclusive_4_nunu", ecm_365, "0.5", "zero", "R5", file_ZZ_365_zero_exclusive_4_nunu, args.ncpus)

# file_ZZ_365_zero_inclusive_nunu= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250705_1015/WbWb_zero_inclusive_nunu/semihad/p8_ee_ZZ_ecm365/events_*.root")
# plots_csvs_for_roc("ZZ_zero_inclusive_nunu", ecm_365, "0.5", "zero", "R5", file_ZZ_365_zero_inclusive_nunu, args.ncpus)
## Current plots





##tests for 365 GeV
# file_WbWb_365_zero= ("/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/wzp6_ee_WbWb_ecm365.root")
# plots_csvs_for_roc("WbWb",ecm_365,"0.5","zero","R5",file_WbWb_365_zero, args.ncpus)





# file_WbWb_355_zero= ["/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/wzp6_ee_WbWb_ecm355.root"]
# plots_csvs_for_roc("WbWb",ecm_355,"0.5","zero","R5",file_WbWb_355_zero, args.ncpus)









## 365 GeV
# file_WW_365 = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1630/WbWb_zero/semihad/p8_ee_WW_ecm365/events_*")
# plots_csvs_for_roc("WW", ecm_365, "0.5", "zero", "R5", file_WW_365, args.ncpus)
# file_WbWb_365 = glob.glob(f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1630/WbWb_zero/semihad/wzp6_ee_WbWb_ecm365/events_*")
# plots_csvs_for_roc("WbWb",ecm_365,"0.5","zero","R5",file_WbWb_365, args.ncpus)
# file_ZZ_365 = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1630/WbWb_zero/semihad/p8_ee_ZZ_ecm365/events_*")
# plots_csvs_for_roc("ZZ", ecm_365, "0.5", "zero", "R5", file_ZZ_365, args.ncpus)
# file_WWZ_Zbb_365= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1630/WbWb_zero/semihad/wzp6_ee_WWZ_Zbb_ecm365/events_*")
# plots_csvs_for_roc("WWZ_Zbb", ecm_365, "0.5", "zero", "R5", file_WWZ_Zbb_365, args.ncpus)
# file_nunuH_bb_365 = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1630/WbWb_zero/semihad/wzp6_ee_nunuH_Hbb_ecm365/events_*")
# plots_csvs_for_roc("nunuH", ecm_365, "0.5", "zero", "R5", file_nunuH_bb_365, args.ncpus)
# file_nunuH_cc_365= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1630/WbWb_zero/semihad/wzp6_ee_nunuH_Hcc_ecm365/events_*")
# plots_csvs_for_roc("nunuH_cc", ecm_365, "0.5", "zero", "R5", file_nunuH_cc_365, args.ncpus)


#next run for 365 GeV
# file_WbWb_365_one = glob.glob(f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/wzp6_ee_WbWb_ecm365/events_*")
# plots_csvs_for_roc("WbWb",ecm_365,"0.5","one","R5",file_WbWb_365_one, args.ncpus)

# file_ZZ_365_one = ["/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_0.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_1.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_2.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_3.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_4.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_5.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_6.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_7.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_8.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_9.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/p8_ee_ZZ_ecm365/events_10.root"]
# plots_csvs_for_roc("ZZ", ecm_365, "0.5", "one", "R5", file_ZZ_365_one, args.ncpus)

# file_WWZ_Zbb_365_one= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/wzp6_ee_WWZ_Zbb_ecm365/events_*")
# plots_csvs_for_roc("WWZ_Zbb", ecm_365, "0.5", "one", "R5", file_WWZ_Zbb_365_one, args.ncpus)
# file_nunuH_bb_365_one = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/wzp6_ee_nunuH_Hbb_ecm365/events_*")
# plots_csvs_for_roc("nunuH", ecm_365, "0.5", "one", "R5", file_nunuH_bb_365_one, args.ncpus)
# file_nunuH_cc_365_one= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1631/WbWb_one/semihad/wzp6_ee_nunuH_Hcc_ecm365/events_*")
# plots_csvs_for_roc("nunuH_cc", ecm_365, "0.5", "one", "R5", file_nunuH_cc_365_one, args.ncpus)

# file_WW_365_two = ["/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_0.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_1.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_2.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_3.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_4.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_5.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_6.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_7.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_8.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_9.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_10.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_11.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_12.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_13.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_14.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_15.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_16.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_17.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_18.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_19.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_20.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_21.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_22.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_23.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_24.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_25.root"
# ,"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_26.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_27.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_WW_ecm365/events_28.root"]
# plots_csvs_for_roc("WW",ecm_365,"0.5","two","R5",file_WW_365_two, args.ncpus)
# file_WbWb_365_two = glob.glob(f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/wzp6_ee_WbWb_ecm365/events_*")
# plots_csvs_for_roc("WbWb",ecm_365,"0.5","two","R5",file_WbWb_365_two, args.ncpus)

# file_ZZ_365_two = ["/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_0.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_1.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_2.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_3.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_4.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_5.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_6.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_7.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_8.root",
# "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_9.root", "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/p8_ee_ZZ_ecm365/events_10.root"]
# plots_csvs_for_roc("ZZ", ecm_365, "0.5", "two", "R5", file_ZZ_365_two, args.ncpus)

# file_WWZ_Zbb_365_two= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/wzp6_ee_WWZ_Zbb_ecm365/events_*")
# plots_csvs_for_roc("WWZ_Zbb", ecm_365, "0.5", "two", "R5", file_WWZ_Zbb_365_two, args.ncpus)
# file_nunuH_bb_365_two = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/wzp6_ee_nunuH_Hbb_ecm365/events_*")
# plots_csvs_for_roc("nunuH", ecm_365, "0.5", "two", "R5", file_nunuH_bb_365_two, args.ncpus)
# file_nunuH_cc_365_two= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1632/WbWb_two/semihad/wzp6_ee_nunuH_Hcc_ecm365/events_*")
# plots_csvs_for_roc("nunuH_cc", ecm_365, "0.5", "two", "R5", file_nunuH_cc_365_two, args.ncpus)
## 365 GeV

## 345 GeV
## think i ran all this too whoops
# file_WW_345_zero = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1702/WbWb_zero/semihad/p8_ee_WW_ecm345/events_*")
# plots_csvs_for_roc("WW",ecm_345,"0.5","zero","R5",file_WW_345_zero, args.ncpus)
# file_WbWb_345_zero = glob.glob(f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1702/WbWb_zero/semihad/wzp6_ee_WbWb_ecm345/events_*")
# plots_csvs_for_roc("WbWb",ecm_345,"0.5","zero","R5",file_WbWb_345_zero, args.ncpus)
# file_ZZ_345_zero = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1702/WbWb_zero/semihad/p8_ee_ZZ_ecm345/events_*")
# plots_csvs_for_roc("ZZ",ecm_345,"0.5","zero","R5",file_ZZ_345_zero, args.ncpus)
# file_WWZ_Zbb_345_zero= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1702/WbWb_zero/semihad/wzp6_ee_WWZ_Zbb_ecm345/events_*")
# plots_csvs_for_roc("WWZ_Zbb",ecm_345,"0.5","zero","R5",file_WWZ_Zbb_345_zero, args.ncpus)

# file_WW_345_one = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1703/WbWb_one/semihad/p8_ee_WW_ecm345/events_*")
# plots_csvs_for_roc("WW",ecm_345,"0.5","one","R5",file_WW_345_one, args.ncpus)
# file_WbWb_345_one = glob.glob(f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1703/WbWb_one/semihad/wzp6_ee_WbWb_ecm345/events_*")
# plots_csvs_for_roc("WbWb",ecm_345,"0.5","one","R5",file_WbWb_345_one, args.ncpus)
# file_ZZ_345_one = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1703/WbWb_one/semihad/p8_ee_ZZ_ecm345/events_*")
# plots_csvs_for_roc("ZZ",ecm_345,"0.5","one","R5",file_ZZ_345_one, args.ncpus)
#WWz zbb is next to run as long ass zz is finished
# file_WWZ_Zbb_345_one= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1703/WbWb_one/semihad/wzp6_ee_WWZ_Zbb_ecm345/events_*")
# plots_csvs_for_roc("WWZ_Zbb",ecm_345,"0.5","one","R5",file_WWZ_Zbb_345_one, args.ncpus)

# file_WW_345_two = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1704/WbWb_two/semihad/p8_ee_WW_ecm345/events_*")
# plots_csvs_for_roc("WW",ecm_345,"0.5","two","R5",file_WW_345_two, args.ncpus)
# file_WbWb_345_two = glob.glob(f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1704/WbWb_two/semihad/wzp6_ee_WbWb_ecm345/events_*")
# plots_csvs_for_roc("WbWb",ecm_345,"0.5","two","R5",file_WbWb_345_two, args.ncpus)
# file_ZZ_345_two = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1704/WbWb_two/semihad/p8_ee_ZZ_ecm345/events_*")
# plots_csvs_for_roc("ZZ",ecm_345,"0.5","two","R5",file_ZZ_345_two, args.ncpus)
# file_WWZ_Zbb_345_two= glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1704/WbWb_two/semihad/wzp6_ee_WWZ_Zbb_ecm345/events_*")
# plots_csvs_for_roc("WWZ_Zbb",ecm_345,"0.5","two","R5",file_WWZ_Zbb_345_two, args.ncpus)
## 345 GeV

##91 GeV Zbb Zcc Zss Zud


# file_Zss_91_zero = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250624_1248/WbWb_zero/semihad/p8_ee_Zss_ecm91/events_*")
# plots_csvs_for_roc("Zss",ecm_91,"0.5","zero","R5",file_Zss_91_zero, args.ncpus)
# file_Zss_91_one = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250624_1321/WbWb_one/semihad/p8_ee_Zss_ecm91/events_*")
# plots_csvs_for_roc("Zss",ecm_91,"0.5","one","R5",file_Zss_91_one, args.ncpus)

# file_Zss_91_two = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250624_1357/WbWb_two/semihad/p8_ee_Zss_ecm91/events_*")
# plots_csvs_for_roc("Zss",ecm_91,"0.5","two","R5",file_Zss_91_two, args.ncpus)





# file_Zud_91_zero = [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250624_1412/WbWb_zero/semihad/p8_ee_Zud_ecm91/events_{i}.root" for i in range(100)]
# plots_csvs_for_roc("Zud",ecm_91,"0.5","zero","R5",file_Zud_91_zero, args.ncpus)

# file_Zud_91_one=glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250625_0806/WbWb_one/semihad/p8_ee_Zud_ecm91/events_*")
# plots_csvs_for_roc("Zud",ecm_91,"0.5","one","R5",file_Zud_91_one, args.ncpus)

# file_Zud_91_two=glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250625_0837/WbWb_two/semihad/p8_ee_Zud_ecm91/events_*")
# plots_csvs_for_roc("Zud",ecm_91,"0.5","two","R5",file_Zud_91_two, args.ncpus)




# file_Zbb_91_zero = [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250625_0847/WbWb_zero/semihad/p8_ee_Zbb_ecm91/events_{i}.root" for i in range(100)]
# plots_csvs_for_roc("Zbb",ecm_91,"0.5","zero","R5",file_Zbb_91_zero, args.ncpus)


# file_Zbb_91_one = [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250625_1139/WbWb_one/semihad/p8_ee_Zbb_ecm91/events_{i}.root" for i in range(100)]
# plots_csvs_for_roc("Zbb",ecm_91,"0.5","one","R5",file_Zbb_91_one, args.ncpus)






# file_Zbb_91_two = [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250625_1354/WbWb_two/semihad/p8_ee_Zbb_ecm91/events_{i}.root" for i in range(100)]
# plots_csvs_for_roc("Zbb",ecm_91,"0.5","two","R5",file_Zbb_91_two, args.ncpus)




# file_Zcc_91_zero = [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250624_0806/WbWb_zero/semihad/p8_ee_Zcc_ecm91/events_{i}.root" for i in range(40)]
# plots_csvs_for_roc("Zcc",ecm_91,"0.5","zero","R5",file_Zcc_91_zero, args.ncpus)
# file_Zcc_91_one = [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250624_1047/WbWb_one/semihad/p8_ee_Zcc_ecm91/events_{i}.root" for i in range(109)]
# plots_csvs_for_roc("Zcc",ecm_91,"0.5","one","R5",file_Zcc_91_one, args.ncpus)






# ## REDO FILE GENERATION
# file_Zcc_91_two = [f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250624_1202/WbWb_two/semihad/p8_ee_Zcc_ecm91/events_{i}.root" for i in range(3500)]
# plots_csvs_for_roc("Zcc",ecm_91,"0.5","two","R5",file_Zcc_91_two, args.ncpus)

## REDO FILE GENERATION



















# Commented out sections remain unchanged
# file_WbWb_365 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/wzp6_ee_WbWb_ecm{ecm_365}.root")
# plots_csvs_for_roc("WbWb",ecm_365,"0.5","zero","R5",file_WbWb_365, args.ncpus)

# file_WbWb_345 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/wzp6_ee_WbWb_ecm{ecm_345}.root")
# plots_csvs_for_roc("WbWb",ecm_345,"0.5","two","R5",file_WbWb_345, args.ncpus)

# file_ZZ_365 = uproot.open(f"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250617_2001/WbWb/semihad/p8_ee_ZZ_ecm365/p8_ee_ZZ_ecm365.root")
# plots_csvs_for_roc("ZZ",ecm_365,"0.5","zero","R5",glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250618_0709/WbWb/semihad/p8_ee_ZZ_ecm365/events_*"), args.ncpus)
# plots_csvs_for_roc("ZZ",ecm_365,"0.5","zero","R5",["/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250618_0709/WbWb/semihad/p8_ee_ZZ_ecm365/events_99.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250618_0709/WbWb/semihad/p8_ee_ZZ_ecm365/events_100.root"], args.ncpus)
# file_nunuH_365 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/wzp6_ee_nunuH_Hbb_ecm{ecm_365}.root")
# plots_csvs_for_roc("nunuH",ecm_365,"0.5","zero","R5",file_nunuH_365, args.ncpus)

# file_Zbb_91 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/p8_ee_Zbb_ecm{ecm_91}.root")

# short_file_list_Zbb=["/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1426/WbWb/semihad/p8_ee_Zbb_ecm91/events_1.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1426/WbWb/semihad/p8_ee_Zbb_ecm91/events_2.root",
#                      "/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1426/WbWb/semihad/p8_ee_Zbb_ecm91/events_3.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1426/WbWb/semihad/p8_ee_Zbb_ecm91/events_4.root"
#                      ,"/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1426/WbWb/semihad/p8_ee_Zbb_ecm91/events_5.root","/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1426/WbWb/semihad/p8_ee_Zbb_ecm91/events_6.root"]

# plots_csvs_for_roc("Zbb",ecm_91,"0.5","zero","R5",glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1426/WbWb/semihad/p8_ee_Zbb_ecm91/events_*"), args.ncpus)
# plots_csvs_for_roc("Zbb",ecm_91,"0.5","zero","R5",short_file_list_Zbb, args.ncpus)

# file_ZZ_365 = glob.glob("/eos/user/g/gidaniel/FCC_tt_threshold/output_condor_20250619_1156/WbWb/semihad/p8_ee_ZZ_ecm365/events_*")
# plots_csvs_for_roc("ZZ",ecm_365,"0.5","two","R5",file_ZZ_365, args.ncpus)
