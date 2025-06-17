import uproot 
import pandas as pd
import awkward as ak
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import boost_histogram as bh
import os
def create_rocs(channel, ecm, deltaR_label, clustering_label,n_lep_0,n_lep_1,n_lep_2):
    if n_lep_0:
        channel_ecm_zero_leptons_brocs= pd.read_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}zero{clustering_label}/b_roc_{deltaR_label}zero{clustering_label}.csv")
        plt.plot(channel_ecm_zero_leptons_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_zero_leptons_brocs["inefficiencies_c_jets_passing_cut"],color="blue",label="b vs c")
        plt.plot(channel_ecm_zero_leptons_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_zero_leptons_brocs["inefficiencies_ud_jets_passing_cut"],color="black",label="b vs ud")
        plt.plot(channel_ecm_zero_leptons_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_zero_leptons_brocs["inefficiencies_s_jets_passing_cut"],color="purple",label="b vs s")
        plt.plot(channel_ecm_zero_leptons_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_zero_leptons_brocs["inefficiencies_g_jets_passing_cut"],color="red",label="b vs g")

    if n_lep_1 :
        channel_ecm_one_lepton_brocs= pd.read_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}one{clustering_label}/b_roc_{deltaR_label}one{clustering_label}.csv")
        plt.plot(channel_ecm_one_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_one_lepton_brocs["inefficiencies_c_jets_passing_cut"],color="blue",label="b vs c", linestyle="--")
        plt.plot(channel_ecm_one_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_one_lepton_brocs["inefficiencies_ud_jets_passing_cut"],color="black",label="b vs ud", linestyle="--")
        plt.plot(channel_ecm_one_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_one_lepton_brocs["inefficiencies_s_jets_passing_cut"],color="purple",label="b vs s", linestyle="--")
        plt.plot(channel_ecm_one_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_one_lepton_brocs["inefficiencies_g_jets_passing_cut"],color="red",label="b vs g", linestyle="--")

    if n_lep_2:
        channel_ecm_two_lepton_brocs= pd.read_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}two{clustering_label}/b_roc_{deltaR_label}two{clustering_label}.csv")
        plt.plot(channel_ecm_two_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_two_lepton_brocs["inefficiencies_c_jets_passing_cut"],color="blue",label="b vs c", linestyle="-.")
        plt.plot(channel_ecm_two_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_two_lepton_brocs["inefficiencies_ud_jets_passing_cut"],color="black",label="b vs ud", linestyle="-.")
        plt.plot(channel_ecm_two_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_two_lepton_brocs["inefficiencies_s_jets_passing_cut"],color="purple",label="b vs s", linestyle="-.")
        plt.plot(channel_ecm_two_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_two_lepton_brocs["inefficiencies_g_jets_passing_cut"],color="red",label="b vs g", linestyle="-.")

    if n_lep_0 or n_lep_1 or n_lep_2:   
        plt.xlabel("jet tagging efficiency")
        plt.ylabel("jet misd. probability")
        plt.yscale("log")
        plt.legend(frameon=False)
        plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/b_roc_{deltaR_label}{clustering_label}_combined.pdf")
        plt.close()




    if n_lep_0:
        channel_ecm_zero_leptons_crocs= pd.read_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}zero{clustering_label}/c_roc_{deltaR_label}zero{clustering_label}.csv")
        plt.plot(channel_ecm_zero_leptons_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_zero_leptons_crocs["inefficiencies_b_jets_passing_cut_C"],color="blue",label="c vs b")
        plt.plot(channel_ecm_zero_leptons_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_zero_leptons_crocs["inefficiencies_ud_jets_passing_cut_C"],color="black",label="c vs ud")
        plt.plot(channel_ecm_zero_leptons_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_zero_leptons_crocs["inefficiencies_s_jets_passing_cut_C"],color="purple",label="c vs s")
        plt.plot(channel_ecm_zero_leptons_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_zero_leptons_crocs["inefficiencies_g_jets_passing_cut_C"],color="red",label="c vs g")

    if n_lep_1:

   
        channel_ecm_one_lepton_crocs= pd.read_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}one{clustering_label}/c_roc_{deltaR_label}one{clustering_label}.csv")
        plt.plot(channel_ecm_one_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_one_lepton_crocs["inefficiencies_b_jets_passing_cut_C"],color="blue",label="c vs b", linestyle="--")
        plt.plot(channel_ecm_one_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_one_lepton_crocs["inefficiencies_ud_jets_passing_cut_C"],color="black",label="c vs ud", linestyle="--")
        plt.plot(channel_ecm_one_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_one_lepton_crocs["inefficiencies_s_jets_passing_cut_C"],color="purple",label="c vs s", linestyle="--")
        plt.plot(channel_ecm_one_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_one_lepton_crocs["inefficiencies_g_jets_passing_cut_C"],color="red",label="c vs g", linestyle="--")
        
    if n_lep_2:
        channel_ecm_two_lepton_crocs= pd.read_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}two{clustering_label}/c_roc_{deltaR_label}two{clustering_label}.csv")
        plt.plot(channel_ecm_two_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_two_lepton_crocs["inefficiencies_b_jets_passing_cut_C"],color="blue",label="c vs b", linestyle="-.")
        plt.plot(channel_ecm_two_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_two_lepton_crocs["inefficiencies_ud_jets_passing_cut_C"],color="black",label="c vs ud", linestyle="-.")
        plt.plot(channel_ecm_two_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_two_lepton_crocs["inefficiencies_s_jets_passing_cut_C"],color="purple",label="c vs s", linestyle="-.")
        plt.plot(channel_ecm_two_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_two_lepton_crocs["inefficiencies_g_jets_passing_cut_C"],color="red",label="c vs g", linestyle="-.")

    if n_lep_0 or n_lep_1 or n_lep_2:   
        plt.xlabel("jet tagging efficiency")
        plt.ylabel("jet misd. probability")
        plt.yscale("log")
        plt.legend(frameon=False)
        plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/c_roc_{deltaR_label}{clustering_label}_combined.pdf")
        plt.close()




    if n_lep_0 and n_lep_1 and n_lep_2:   
        fig, ax = plt.subplots(2, 3, figsize=(14, 12))
        ax[0,0].plot(channel_ecm_zero_leptons_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_zero_leptons_brocs["inefficiencies_c_jets_passing_cut"],color="blue",label="b vs c")
        ax[0,0].plot(channel_ecm_zero_leptons_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_zero_leptons_brocs["inefficiencies_ud_jets_passing_cut"],color="black",label="b vs ud")
        ax[0,0].plot(channel_ecm_zero_leptons_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_zero_leptons_brocs["inefficiencies_s_jets_passing_cut"],color="purple",label="b vs s")
        ax[0,0].plot(channel_ecm_zero_leptons_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_zero_leptons_brocs["inefficiencies_g_jets_passing_cut"],color="red",label="b vs g")
        ax[0,0].set_title("0 leptons")
        ax[0,0].set_xlabel("jet tagging efficiency")
        ax[0,0].set_ylabel("jet misd. probability")
        ax[0, 0].set_yscale("log")
        ax[0,0].legend(frameon=False)
        ax[0,0].set_xlim(0,1)
        ax[0,0].set_ylim(0,1.05)



        ax[0,1].plot(channel_ecm_one_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_one_lepton_brocs["inefficiencies_c_jets_passing_cut"],color="blue",label="b vs c", linestyle="--")
        ax[0,1].plot(channel_ecm_one_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_one_lepton_brocs["inefficiencies_ud_jets_passing_cut"],color="black",label="b vs ud", linestyle="--")
        ax[0,1].plot(channel_ecm_one_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_one_lepton_brocs["inefficiencies_s_jets_passing_cut"],color="purple",label="b vs s", linestyle="--")
        ax[0,1].plot(channel_ecm_one_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_one_lepton_brocs["inefficiencies_g_jets_passing_cut"],color="red",label="b vs g", linestyle="--")
        ax[0,1].set_title("1 lepton")
        ax[0,1].set_xlabel("jet tagging efficiency")
        ax[0,1].set_ylabel("jet misd. probability")
        ax[0,1].set_yscale("log")
        ax[0,1].legend(frameon=False)
        ax[0,1].set_xlim(0,1)
        ax[0,1].set_ylim(0,1.05)


        ax[0,2].plot(channel_ecm_two_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_two_lepton_brocs["inefficiencies_c_jets_passing_cut"],color="blue",label="b vs c", linestyle="-.")
        ax[0,2].plot(channel_ecm_two_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_two_lepton_brocs["inefficiencies_ud_jets_passing_cut"],color="black",label="b vs ud", linestyle="-.")
        ax[0,2].plot(channel_ecm_two_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_two_lepton_brocs["inefficiencies_s_jets_passing_cut"],color="purple",label="b vs s", linestyle="-.")
        ax[0,2].plot(channel_ecm_two_lepton_brocs["efficiencies_b_jets_passing_cut"],channel_ecm_two_lepton_brocs["inefficiencies_g_jets_passing_cut"],color="red",label="b vs g", linestyle="-.")
        ax[0,2].set_title("2 leptons")
        ax[0,2].set_xlabel("jet tagging efficiency")
        ax[0,2].set_ylabel("jet misd. probability")
        ax[0,2].set_yscale("log")
        ax[0,2].legend(frameon=False)
        ax[0,2].set_xlim(0,1)
        ax[0,2].set_ylim(0,1.05)


        ax[1,0].plot(channel_ecm_zero_leptons_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_zero_leptons_crocs["inefficiencies_b_jets_passing_cut_C"],color="blue",label="c vs b")
        ax[1,0].plot(channel_ecm_zero_leptons_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_zero_leptons_crocs["inefficiencies_ud_jets_passing_cut_C"],color="black",label="c vs ud")
        ax[1,0].plot(channel_ecm_zero_leptons_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_zero_leptons_crocs["inefficiencies_s_jets_passing_cut_C"],color="purple",label="c vs s")
        ax[1,0].plot(channel_ecm_zero_leptons_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_zero_leptons_crocs["inefficiencies_g_jets_passing_cut_C"],color="red",label="c vs g")

        ax[1,0].set_title("0 leptons")
        ax[1,0].set_xlabel("jet tagging efficiency")
        ax[1,0].set_ylabel("jet misd. probability")
        ax[1,0].set_yscale("log")
        ax[1,0].legend(frameon=False)
        ax[1,0].set_xlim(0,1)
        ax[1,0].set_ylim(0,1.05)


        ax[1,1].plot(channel_ecm_one_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_one_lepton_crocs["inefficiencies_b_jets_passing_cut_C"],color="blue",label="c vs b", linestyle="--")
        ax[1,1].plot(channel_ecm_one_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_one_lepton_crocs["inefficiencies_ud_jets_passing_cut_C"],color="black",label="c vs ud", linestyle="--")
        ax[1,1].plot(channel_ecm_one_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_one_lepton_crocs["inefficiencies_s_jets_passing_cut_C"],color="purple",label="c vs s", linestyle="--")
        ax[1,1].plot(channel_ecm_one_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_one_lepton_crocs["inefficiencies_g_jets_passing_cut_C"],color="red",label="c vs g", linestyle="--")
        ax[1,1].set_title("1 lepton")
        ax[1,1].set_xlabel("jet tagging efficiency")
        ax[1,1].set_ylabel("jet misd. probability")
        ax[1,1].set_yscale("log")
        ax[1,1].legend(frameon=False)
        ax[1,1].set_xlim(0,1)
        ax[1,1].set_ylim(0,1.05)


        ax[1,2].plot(channel_ecm_two_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_two_lepton_crocs["inefficiencies_b_jets_passing_cut_C"],color="blue",label="c vs b", linestyle="-.")
        ax[1,2].plot(channel_ecm_two_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_two_lepton_crocs["inefficiencies_ud_jets_passing_cut_C"],color="black",label="c vs ud", linestyle="-.")
        ax[1,2].plot(channel_ecm_two_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_two_lepton_crocs["inefficiencies_s_jets_passing_cut_C"],color="purple",label="c vs s", linestyle="-.")
        ax[1,2].plot(channel_ecm_two_lepton_crocs["efficiencies_c_jets_passing_cut_C"],channel_ecm_two_lepton_crocs["inefficiencies_g_jets_passing_cut_C"],color="red",label="c vs g", linestyle="-.")
        ax[1,2].set_title("2 leptons")
        ax[1,2].set_xlabel("jet tagging efficiency")
        ax[1,2].set_ylabel("jet misd. probability")
        ax[1,2].set_yscale("log")
        ax[1,2].legend(frameon=False)
        ax[1,2].set_xlim(0,1)
        ax[1,2].set_ylim(0,1.05)


        fig.savefig(f"all_jets_{channel}/{ecm}/jet_plots/b_roc_c_roc_{deltaR_label}{clustering_label}_combined.pdf")

# create_rocs("WbWb", 365, "0.5", "R5",True,True,True)
# create_rocs("ZZ", 365, "0.5", "R5",False,False,True)
# create_rocs("nunuH", 365, "0.5", "R5",True,False,False)
# create_rocs("Zbb", 91, "0.5", "R5",True,False,False)

create_rocs("WbWb", 345, "0.5", "R5",True,True,True)