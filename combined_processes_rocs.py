import uproot 
import pandas as pd
import awkward as ak
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import boost_histogram as bh
import os


def load_file_b_jets(channel, ecm, deltaR_label, lepton_amount, clustering_label):
    channel_ecm_leptons_brocs= pd.read_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_amount}{clustering_label}/b_roc_{deltaR_label}{lepton_amount}{clustering_label}.csv")
    return channel_ecm_leptons_brocs





WbWb_345_rocs_zero= load_file_b_jets("WbWb", 345, "0.5", "zero", "R5")
WbWb_345_rocs_one= load_file_b_jets("WbWb", 345, "0.5", "one", "R5")
WbWb_345_rocs_two= load_file_b_jets("WbWb", 345, "0.5", "two", "R5")

WbWb_365_rocs_zero= load_file_b_jets("WbWb", 365, "0.5", "zero", "R5")
WbWb_365_rocs_one= load_file_b_jets("WbWb", 365, "0.5", "one", "R5")
WbWb_365_rocs_two= load_file_b_jets("WbWb", 365, "0.5", "two", "R5")
ZZ_365_rocs= load_file_b_jets("ZZ", 365, "0.5", "two", "R5")
nunuH_365_rocs= load_file_b_jets("nunuH", 365, "0.5", "zero", "R5")
Zbb_91_rocs= load_file_b_jets("Zbb", 91, "0.5", "zero", "R5")




# Overlap b vs jets plots for Processes
plt.plot(WbWb_365_rocs_zero["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_zero["inefficiencies_c_jets_passing_cut"],color="blue",label="WbWb 365 zero", linestyle="--")
plt.plot(WbWb_365_rocs_one["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_one["inefficiencies_c_jets_passing_cut"],color="red",label="WbWb 365 one", linestyle="--")
plt.plot(WbWb_365_rocs_two["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_two["inefficiencies_c_jets_passing_cut"],color="green",label="WbWb 365 two", linestyle="--")

plt.plot(WbWb_345_rocs_zero["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_zero["inefficiencies_c_jets_passing_cut"],color="blue",label="WbWb 345 zero")
plt.plot(WbWb_345_rocs_one["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_one["inefficiencies_c_jets_passing_cut"],color="red",label="WbWb 345 one")
plt.plot(WbWb_345_rocs_two["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_two["inefficiencies_c_jets_passing_cut"],color="green",label="WbWb 345 two")
plt.plot(ZZ_365_rocs["efficiencies_b_jets_passing_cut"],ZZ_365_rocs["inefficiencies_c_jets_passing_cut"],color="purple",label="ZZ 365 two")
plt.plot(nunuH_365_rocs["efficiencies_b_jets_passing_cut"],nunuH_365_rocs["inefficiencies_c_jets_passing_cut"],color="orange",label="nunuH 365 zero")
plt.plot(Zbb_91_rocs["efficiencies_b_jets_passing_cut"],Zbb_91_rocs["inefficiencies_c_jets_passing_cut"],color="black",label="Zbb 91 zero")
plt.title("b vs c jets")
plt.xlabel("jet tagging efficiency")
plt.ylabel("jet misd. probability")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig("all_jets_combined_brocs/all_jets_combined_rocs_b_vs_c.pdf")
plt.close()

# Overlap b vs s jets plots for Processes
plt.plot(WbWb_365_rocs_zero["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_zero["inefficiencies_s_jets_passing_cut"],color="blue",label="WbWb 365 zero", linestyle="--")
plt.plot(WbWb_365_rocs_one["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_one["inefficiencies_s_jets_passing_cut"],color="red",label="WbWb 365 one", linestyle="--")
plt.plot(WbWb_365_rocs_two["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_two["inefficiencies_s_jets_passing_cut"],color="green",label="WbWb 365 two", linestyle="--")
plt.plot(WbWb_345_rocs_zero["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_zero["inefficiencies_s_jets_passing_cut"],color="blue",label="WbWb 345 zero")
plt.plot(WbWb_345_rocs_one["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_one["inefficiencies_s_jets_passing_cut"],color="red",label="WbWb 345 one")
plt.plot(WbWb_345_rocs_two["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_two["inefficiencies_s_jets_passing_cut"],color="green",label="WbWb 345 two")
plt.plot(ZZ_365_rocs["efficiencies_b_jets_passing_cut"],ZZ_365_rocs["inefficiencies_s_jets_passing_cut"],color="purple",label="ZZ 365 two")
plt.plot(nunuH_365_rocs["efficiencies_b_jets_passing_cut"],nunuH_365_rocs["inefficiencies_s_jets_passing_cut"],color="orange",label="nunuH 365 zero")
plt.plot(Zbb_91_rocs["efficiencies_b_jets_passing_cut"],Zbb_91_rocs["inefficiencies_s_jets_passing_cut"],color="black",label="Zbb 91 zero")
plt.title("b vs s jets")
plt.xlabel("jet tagging efficiency")
plt.ylabel("jet misd. probability")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig("all_jets_combined_brocs/all_jets_combined_rocs_b_vs_s.pdf")
plt.close()


# Overlap b vs g jets plots for Processes
plt.plot(WbWb_365_rocs_zero["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_zero["inefficiencies_g_jets_passing_cut"],color="blue",label="WbWb 365 zero", linestyle="--")
plt.plot(WbWb_365_rocs_one["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_one["inefficiencies_g_jets_passing_cut"],color="red",label="WbWb 365 one", linestyle="--")
plt.plot(WbWb_365_rocs_two["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_two["inefficiencies_g_jets_passing_cut"],color="green",label="WbWb 365 two", linestyle="--")
plt.plot(WbWb_345_rocs_zero["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_zero["inefficiencies_g_jets_passing_cut"],color="blue",label="WbWb 345 zero")
plt.plot(WbWb_345_rocs_one["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_one["inefficiencies_g_jets_passing_cut"],color="red",label="WbWb 345 one")
plt.plot(WbWb_345_rocs_two["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_two["inefficiencies_g_jets_passing_cut"],color="green",label="WbWb 345 two")
plt.plot(ZZ_365_rocs["efficiencies_b_jets_passing_cut"],ZZ_365_rocs["inefficiencies_g_jets_passing_cut"],color="purple",label="ZZ 365 two")
plt.plot(nunuH_365_rocs["efficiencies_b_jets_passing_cut"],nunuH_365_rocs["inefficiencies_g_jets_passing_cut"],color="orange",label="nunuH 365 zero")
plt.plot(Zbb_91_rocs["efficiencies_b_jets_passing_cut"],Zbb_91_rocs["inefficiencies_g_jets_passing_cut"],color="black",label="Zbb 91 zero")
plt.title("b vs g jets")
plt.xlabel("jet tagging efficiency")
plt.ylabel("jet misd. probability")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig("all_jets_combined_brocs/all_jets_combined_rocs_b_vs_g.pdf")
plt.close()


# Overlap b vs ud jets plots for Processes
plt.plot(WbWb_365_rocs_zero["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_zero["inefficiencies_ud_jets_passing_cut"],color="blue",label="WbWb 365 zero", linestyle="--")
plt.plot(WbWb_365_rocs_one["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_one["inefficiencies_ud_jets_passing_cut"],color="red",label="WbWb 365 one", linestyle="--")
plt.plot(WbWb_365_rocs_two["efficiencies_b_jets_passing_cut"],WbWb_365_rocs_two["inefficiencies_ud_jets_passing_cut"],color="green",label="WbWb 365 two", linestyle="--")
plt.plot(WbWb_345_rocs_zero["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_zero["inefficiencies_ud_jets_passing_cut"],color="blue",label="WbWb 345 zero")
plt.plot(WbWb_345_rocs_one["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_one["inefficiencies_ud_jets_passing_cut"],color="red",label="WbWb 345 one")
plt.plot(WbWb_345_rocs_two["efficiencies_b_jets_passing_cut"],WbWb_345_rocs_two["inefficiencies_ud_jets_passing_cut"],color="green",label="WbWb 345 two")
plt.plot(ZZ_365_rocs["efficiencies_b_jets_passing_cut"],ZZ_365_rocs["inefficiencies_ud_jets_passing_cut"],color="purple",label="ZZ 365 two")
plt.plot(nunuH_365_rocs["efficiencies_b_jets_passing_cut"],nunuH_365_rocs["inefficiencies_ud_jets_passing_cut"],color="orange",label="nunuH 365 zero")
plt.plot(Zbb_91_rocs["efficiencies_b_jets_passing_cut"],Zbb_91_rocs["inefficiencies_ud_jets_passing_cut"],color="black",label="Zbb 91 zero")
plt.title("b vs ud jets")
plt.xlabel("jet tagging efficiency")
plt.ylabel("jet misd. probability")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig("all_jets_combined_brocs/all_jets_combined_rocs_b_vs_ud.pdf")
plt.close()



# Overlap c vs jets plots for Processes
def load_file_c_jets(channel, ecm, deltaR_label, lepton_amount, clustering_label):
    channel_ecm_leptons_crocs= pd.read_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_amount}{clustering_label}/c_roc_{deltaR_label}{lepton_amount}{clustering_label}.csv")
    return channel_ecm_leptons_crocs

WbWb_365_rocs_zero_c= load_file_c_jets("WbWb", 365, "0.5", "zero", "R5")
WbWb_365_rocs_one_c= load_file_c_jets("WbWb", 365, "0.5", "one", "R5")
WbWb_365_rocs_two_c= load_file_c_jets("WbWb", 365, "0.5", "two", "R5")

WbWb_345_rocs_zero_c= load_file_c_jets("WbWb", 345, "0.5", "zero", "R5")
WbWb_345_rocs_one_c= load_file_c_jets("WbWb", 345, "0.5", "one", "R5")
WbWb_345_rocs_two_c= load_file_c_jets("WbWb", 345, "0.5", "two", "R5")

ZZ_365_rocs_c= load_file_c_jets("ZZ", 365, "0.5", "two", "R5")
nunuH_365_rocs_c= load_file_c_jets("nunuH", 365, "0.5", "zero", "R5")
Zbb_91_rocs_c= load_file_c_jets("Zbb", 91, "0.5", "zero", "R5")







# Overlap c vs b jets plots for Processes   
plt.plot(WbWb_365_rocs_zero_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_zero_c["inefficiencies_b_jets_passing_cut_C"],color="blue",label="WbWb 365 zero", linestyle="--")
plt.plot(WbWb_365_rocs_one_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_one_c["inefficiencies_b_jets_passing_cut_C"],color="red",label="WbWb 365 one", linestyle="--")
plt.plot(WbWb_365_rocs_two_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_two_c["inefficiencies_b_jets_passing_cut_C"],color="green",label="WbWb 365 two", linestyle="--")
plt.plot(WbWb_345_rocs_zero_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_zero_c["inefficiencies_b_jets_passing_cut_C"],color="blue",label="WbWb 345 zero")
plt.plot(WbWb_345_rocs_one_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_one_c["inefficiencies_b_jets_passing_cut_C"],color="red",label="WbWb 345 one")
plt.plot(WbWb_345_rocs_two_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_two_c["inefficiencies_b_jets_passing_cut_C"],color="green",label="WbWb 345 two")
plt.plot(ZZ_365_rocs_c["efficiencies_c_jets_passing_cut_C"],ZZ_365_rocs_c["inefficiencies_b_jets_passing_cut_C"],color="purple",label="ZZ 365 two")
plt.plot(nunuH_365_rocs_c["efficiencies_c_jets_passing_cut_C"],nunuH_365_rocs_c["inefficiencies_b_jets_passing_cut_C"],color="orange",label="nunuH 365 zero")
plt.plot(Zbb_91_rocs_c["efficiencies_c_jets_passing_cut_C"],Zbb_91_rocs_c["inefficiencies_b_jets_passing_cut_C"],color="black",label="Zbb 91 zero")
plt.title("c vs b jets")
plt.xlabel("jet tagging efficiency")
plt.ylabel("jet misd. probability")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig("all_jets_combined_crocs/all_jets_combined_rocs_c_vs_b.pdf")
plt.close()


# Overlap c vs s jets plots for Processes
plt.plot(WbWb_365_rocs_zero_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_zero_c["inefficiencies_s_jets_passing_cut_C"],color="blue",label="WbWb 365 zero", linestyle="--")
plt.plot(WbWb_365_rocs_one_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_one_c["inefficiencies_s_jets_passing_cut_C"],color="red",label="WbWb 365 one", linestyle="--")
plt.plot(WbWb_365_rocs_two_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_two_c["inefficiencies_s_jets_passing_cut_C"],color="green",label="WbWb 365 two", linestyle="--")
plt.plot(WbWb_345_rocs_zero_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_zero_c["inefficiencies_s_jets_passing_cut_C"],color="blue",label="WbWb 345 zero")
plt.plot(WbWb_345_rocs_one_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_one_c["inefficiencies_s_jets_passing_cut_C"],color="red",label="WbWb 345 one")
plt.plot(WbWb_345_rocs_two_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_two_c["inefficiencies_s_jets_passing_cut_C"],color="green",label="WbWb 345 two")
plt.plot(ZZ_365_rocs_c["efficiencies_c_jets_passing_cut_C"],ZZ_365_rocs_c["inefficiencies_s_jets_passing_cut_C"],color="purple",label="ZZ 365 two")
plt.plot(nunuH_365_rocs_c["efficiencies_c_jets_passing_cut_C"],nunuH_365_rocs_c["inefficiencies_s_jets_passing_cut_C"],color="orange",label="nunuH 365 zero")
plt.plot(Zbb_91_rocs_c["efficiencies_c_jets_passing_cut_C"],Zbb_91_rocs_c["inefficiencies_s_jets_passing_cut_C"],color="black",label="Zbb 91 zero")
plt.title("c vs s jets")
plt.xlabel("jet tagging efficiency")
plt.ylabel("jet misd. probability")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig("all_jets_combined_crocs/all_jets_combined_rocs_c_vs_s.pdf")
plt.close()


# Overlap c vs g jets plots for Processes
plt.plot(WbWb_365_rocs_zero_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_zero_c["inefficiencies_g_jets_passing_cut_C"],color="blue",label="WbWb 365 zero", linestyle="--")
plt.plot(WbWb_365_rocs_one_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_one_c["inefficiencies_g_jets_passing_cut_C"],color="red",label="WbWb 365 one", linestyle="--")
plt.plot(WbWb_365_rocs_two_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_two_c["inefficiencies_g_jets_passing_cut_C"],color="green",label="WbWb 365 two", linestyle="--")
plt.plot(WbWb_345_rocs_zero_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_zero_c["inefficiencies_g_jets_passing_cut_C"],color="blue",label="WbWb 345 zero")
plt.plot(WbWb_345_rocs_one_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_one_c["inefficiencies_g_jets_passing_cut_C"],color="red",label="WbWb 345 one")
plt.plot(WbWb_345_rocs_two_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_two_c["inefficiencies_g_jets_passing_cut_C"],color="green",label="WbWb 345 two")
plt.plot(ZZ_365_rocs_c["efficiencies_c_jets_passing_cut_C"],ZZ_365_rocs_c["inefficiencies_g_jets_passing_cut_C"],color="purple",label="ZZ 365 two")
plt.plot(nunuH_365_rocs_c["efficiencies_c_jets_passing_cut_C"],nunuH_365_rocs_c["inefficiencies_g_jets_passing_cut_C"],color="orange",label="nunuH 365 zero")
plt.plot(Zbb_91_rocs_c["efficiencies_c_jets_passing_cut_C"],Zbb_91_rocs_c["inefficiencies_g_jets_passing_cut_C"],color="black",label="Zbb 91 zero")
plt.title("c vs g jets")
plt.xlabel("jet tagging efficiency")
plt.ylabel("jet misd. probability")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig("all_jets_combined_crocs/all_jets_combined_rocs_c_vs_g.pdf")
plt.close()


# Overlap c vs ud jets plots for Processes
plt.plot(WbWb_365_rocs_zero_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_zero_c["inefficiencies_ud_jets_passing_cut_C"],color="blue",label="WbWb 365 zero", linestyle="--")
plt.plot(WbWb_365_rocs_one_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_one_c["inefficiencies_ud_jets_passing_cut_C"],color="red",label="WbWb 365 one", linestyle="--")
plt.plot(WbWb_365_rocs_two_c["efficiencies_c_jets_passing_cut_C"],WbWb_365_rocs_two_c["inefficiencies_ud_jets_passing_cut_C"],color="green",label="WbWb 365 two", linestyle="--")
plt.plot(WbWb_345_rocs_zero_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_zero_c["inefficiencies_ud_jets_passing_cut_C"],color="blue",label="WbWb 345 zero")
plt.plot(WbWb_345_rocs_one_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_one_c["inefficiencies_ud_jets_passing_cut_C"],color="red",label="WbWb 345 one")
plt.plot(WbWb_345_rocs_two_c["efficiencies_c_jets_passing_cut_C"],WbWb_345_rocs_two_c["inefficiencies_ud_jets_passing_cut_C"],color="green",label="WbWb 345 two")
plt.plot(ZZ_365_rocs_c["efficiencies_c_jets_passing_cut_C"],ZZ_365_rocs_c["inefficiencies_ud_jets_passing_cut_C"],color="purple",label="ZZ 365 two")
plt.plot(nunuH_365_rocs_c["efficiencies_c_jets_passing_cut_C"],nunuH_365_rocs_c["inefficiencies_ud_jets_passing_cut_C"],color="orange",label="nunuH 365 zero")
plt.plot(Zbb_91_rocs_c["efficiencies_c_jets_passing_cut_C"],Zbb_91_rocs_c["inefficiencies_ud_jets_passing_cut_C"],color="black",label="Zbb 91 zero")
plt.title("c vs ud jets")
plt.xlabel("jet tagging efficiency")
plt.ylabel("jet misd. probability")
plt.yscale("log")
plt.legend(frameon=False)
plt.savefig("all_jets_combined_crocs/all_jets_combined_rocs_c_vs_ud.pdf")
plt.close()

