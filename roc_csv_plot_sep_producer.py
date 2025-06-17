import uproot 
import pandas as pd
import awkward as ak
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import boost_histogram as bh
import os





def plots_csvs_for_roc(channel,ecm,deltaR_label,lepton_label,clustering_label,file_name_path):
    file = file_name_path



    events= file["events;1"]
    arrays=events.arrays(["nlep", "lep_p", 'lep_theta', 'lep_phi',
        "missing_p", "missing_p_theta", "missing_p_phi",
        "njets_R5",  "jet1_R5_p", "jet2_R5_p", "jet3_R5_p", "jet4_R5_p", "jet5_R5_p", "jet6_R5_p",
        "jet1_R5_theta",  "jet2_R5_theta",  "jet3_R5_theta",  "jet4_R5_theta", "jet5_R5_theta", "jet6_R5_theta",
        "jet1_R5_pflavor", "jet2_R5_pflavor", "jet3_R5_pflavor", "jet4_R5_pflavor", "jet5_R5_pflavor","jet6_R5_pflavor",
        "nbjets_R5_true", "ncjets_R5_true","nljets_R5_true","ngjets_R5_true",
        "nbjets_R5_eff_p9", "nbjets_R5_eff_p89","nbjets_R5_eff_p91",
        "jet1_R5_isG","jet2_R5_isG","jet3_R5_isG","jet4_R5_isG","jet5_R5_isG","jet6_R5_isG",                
        "jet1_R5_isU","jet2_R5_isU","jet3_R5_isU","jet4_R5_isU","jet5_R5_isU","jet6_R5_isU",                
        "jet1_R5_isB","jet2_R5_isB","jet3_R5_isB","jet4_R5_isB","jet5_R5_isB","jet6_R5_isB",                
        "jet1_R5_isS","jet2_R5_isS","jet3_R5_isS","jet4_R5_isS","jet5_R5_isS","jet6_R5_isS",                
        "jet1_R5_isC","jet2_R5_isC","jet3_R5_isC","jet4_R5_isC","jet5_R5_isC","jet6_R5_isC",                
        "jet1_R5_isD","jet2_R5_isD","jet3_R5_isD","jet4_R5_isD","jet5_R5_isD","jet6_R5_isD", "jets_R5_pflavor", "jets_R5_p_unfiltered_size","jets_R5_p_size", "jets_R5_theta_unfiltered",
        "jet1_R5_isTAU","jet2_R5_isTAU","jet3_R5_isTAU","jet4_R5_isTAU","jet5_R5_isTAU","jet6_R5_isTAU","mbbar_p9","mbbar_p89","mbbar_p91", "bjet1_R5_true_p","ljet1_R5_true_p",
        "bjets_R5_true","ljets_R5_true","remaining_muons_deltaR","remaining_electrons_deltaR","jets_R5_tlv","jets_R5_p","jets_R5_theta",
        "jet_mother_pdg_id", "jet_daughter_stuff","E_RP_TRK_Z0_pcut", "electrons_iso", "muons_iso", "electrons_sel", "Mu_RP_TRK_Z0_pcut","muons_all_p", "electrons_all_p","bjets_R5_WPp9", "bjets_R5_WPp8","bjets_R5_WPp5", "bjets_R5_WPp85","nbjets_R5_WPp5","nbjets_R5_WPp8","nbjets_R5_WPp85","nbjets_R5_WPp9", "bjets_R5_true_theta",
        "jets_R5_isC","jets_R5_isU","jets_R5_isD","jets_R5_isB","jets_R5_isG","jets_R5_isS","jets_R5_isTAU","cjets_R5_true_theta","ljets_R5_true_theta","gjets_R5_true_theta"
        ], how=dict,)







    jets_R5_isB=arrays["jets_R5_isB"]
    jets_R5_isC=arrays["jets_R5_isC"]
    jets_R5_isU=arrays["jets_R5_isU"]
    jets_R5_isD=arrays["jets_R5_isD"]
    jets_R5_pflavor=arrays["jets_R5_pflavor"]
    jets_R5_isS=arrays["jets_R5_isS"]
    jets_R5_isG=arrays["jets_R5_isG"]


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
    combined_nested_isS_masked=ak.flatten(jets_R5_isS)[flattened_bjet_match_mask]
    combined_nested_isG_masked=ak.flatten(jets_R5_isG)[flattened_bjet_match_mask]

    df_bjet_match_mask=pd.DataFrame({f"bjet_match_mask{deltaR_label}{lepton_label}":flattened_bjet_match_mask})
    df_combined_nested_isB_masked=pd.DataFrame({f"combined_nested_isB_masked_R{deltaR_label}{lepton_label}":combined_nested_isB_masked})
    df_combined_nested_isC_masked=pd.DataFrame({f"combined_nested_isC_masked_R{deltaR_label}{lepton_label}":combined_nested_isC_masked})
    df_combined_nested_isU_masked=pd.DataFrame({f"combined_nested_isU_masked_R{deltaR_label}{lepton_label}":combined_nested_isU_masked})
    df_combined_nested_isD_masked=pd.DataFrame({f"combined_nested_isD_masked_R{deltaR_label}{lepton_label}":combined_nested_isD_masked})
    df_combined_nested_isS_masked=pd.DataFrame({f"combined_nested_isS_masked_R{deltaR_label}{lepton_label}":combined_nested_isS_masked})
    df_combined_nested_isG_masked=pd.DataFrame({f"combined_nested_isG_masked_R{deltaR_label}{lepton_label}":combined_nested_isG_masked})

    ## how cna i amek it so that if the jet_plots3_csvs{deltaR_label}{lepton_label} folder does not exist, it creates it
    if not os.path.exists(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}"):
        os.makedirs(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}")
    if not os.path.exists(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}"):
        os.makedirs(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}")



    df_bjet_match_mask.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/bjet_match_mask_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isB_masked.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isB_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isC_masked.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isC_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isU_masked.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isU_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isD_masked.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isD_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isS_masked.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isS_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isG_masked.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isG_masked_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)

    ### Number Jets before and after overlap removal
    efficiencies_b_jets_passing_cut=[]
    inefficiencies_c_jets_passing_cut=[]
    inefficiencies_u_jets_passing_cut=[]
    inefficiencies_d_jets_passing_cut=[]
    inefficiencies_ud_jets_passing_cut=[]
    inefficiencies_s_jets_passing_cut=[]
    inefficiencies_g_jets_passing_cut=[]
    cutoff_values=[]

    for i in range(0,10000): 
        cuttoff_mask_val=i/10000
        b_score_cutoff_1_mask = combined_nested_isB_masked > cuttoff_mask_val
        c_score_cutoff_1_mask=combined_nested_isC_masked > cuttoff_mask_val
        u_score_cutoff_1_mask=combined_nested_isU_masked > cuttoff_mask_val
        d_score_cutoff_1_mask=combined_nested_isD_masked > cuttoff_mask_val
        s_score_cutoff_1_mask=combined_nested_isS_masked > cuttoff_mask_val
        g_score_cutoff_1_mask=combined_nested_isG_masked > cuttoff_mask_val

        b_score_cutoff_1= combined_nested_isB_masked[b_score_cutoff_1_mask]
        c_score_cutoff_1= combined_nested_isC_masked[c_score_cutoff_1_mask]
        u_score_cutoff_1= combined_nested_isU_masked[u_score_cutoff_1_mask]
        d_score_cutoff_1= combined_nested_isD_masked[d_score_cutoff_1_mask]
        s_score_cutoff_1= combined_nested_isS_masked[s_score_cutoff_1_mask]
        g_score_cutoff_1= combined_nested_isG_masked[g_score_cutoff_1_mask]
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

        inefficiency_s_jets_passing_cut_total=len(s_score_cutoff_1)
        # print(inefficiency_s_jets_passing_cut_total,"s jets passing cut")
        inefficiency_s_jets_passing_cut=inefficiency_s_jets_passing_cut_total/nbjets_R5_true_total

        inefficiency_g_jets_passing_cut_total=len(g_score_cutoff_1)
        inefficiency_g_jets_passing_cut=inefficiency_g_jets_passing_cut_total/nbjets_R5_true_total
    
        inefficiency_ud_jets_passing_cut=((inefficiency_d_jets_passing_cut_total+inefficiency_u_jets_passing_cut_total)*0.5)/nbjets_R5_true_total
        cutoff_values.append(cuttoff_mask_val)
        efficiencies_b_jets_passing_cut.append(efficiency_b_jets_passing_cut)
        inefficiencies_c_jets_passing_cut.append(inefficiency_c_jets_passing_cut)
        inefficiencies_u_jets_passing_cut.append(inefficiency_u_jets_passing_cut)
        inefficiencies_d_jets_passing_cut.append(inefficiency_d_jets_passing_cut)
        inefficiencies_ud_jets_passing_cut.append(inefficiency_ud_jets_passing_cut)
        inefficiencies_s_jets_passing_cut.append(inefficiency_s_jets_passing_cut)
        inefficiencies_g_jets_passing_cut.append(inefficiency_g_jets_passing_cut)



    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_c_jets_passing_cut,color="blue",label="b vs c")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(c-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs C Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_c_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_u_jets_passing_cut,color="green",label="b vs u")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(u-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs U Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_d_jets_passing_cut,color="red",label="b vs d")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(d-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs D Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()
    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_ud_jets_passing_cut,color="purple",label="b vs ud")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(ud-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs UD Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    # plt.xscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_s_jets_passing_cut,color="orange",label="b vs s")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(s-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs S Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_s_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_g_jets_passing_cut,color="brown",label="b vs g")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(g-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs G Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_g_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_ud_jets_passing_cut,color="green",label="b vs ud")
    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_c_jets_passing_cut,color="blue",label="b vs c")
    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_s_jets_passing_cut,color="orange",label="b vs s")
    plt.plot(efficiencies_b_jets_passing_cut,inefficiencies_g_jets_passing_cut,color="brown",label="b vs g")
    # plt.title(f"b ROC {deltaR_label}")
    plt.yscale("log")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("jet misd. probability")
    # plt.xscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/b_roc_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()


    df=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_c_jets_passing_cut":inefficiencies_c_jets_passing_cut,"cutoff_values":cutoff_values, "nbjets_true": nbjets_R5_true_total})
    df.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_c_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)

    df1=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_u_jets_passing_cut":inefficiencies_u_jets_passing_cut,"cutoff_values":cutoff_values, "nbjets_true": nbjets_R5_true_total})
    df1.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df2=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_d_jets_passing_cut":inefficiencies_d_jets_passing_cut,"cutoff_values":cutoff_values, "nbjets_true": nbjets_R5_true_total})
    df2.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df3=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_ud_jets_passing_cut":inefficiencies_ud_jets_passing_cut,"cutoff_values":cutoff_values, "nbjets_true": nbjets_R5_true_total})
    df3.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df5=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_s_jets_passing_cut":inefficiencies_s_jets_passing_cut,"cutoff_values":cutoff_values, "nbjets_true": nbjets_R5_true_total})
    df5.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_s_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df6=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_g_jets_passing_cut":inefficiencies_g_jets_passing_cut,"cutoff_values":cutoff_values, "nbjets_true": nbjets_R5_true_total})
    df6.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/btag_efficiency_vs_g_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)




    df4=pd.DataFrame({"efficiencies_b_jets_passing_cut":efficiencies_b_jets_passing_cut,"inefficiencies_ud_jets_passing_cut":inefficiencies_ud_jets_passing_cut,"inefficiencies_c_jets_passing_cut":inefficiencies_c_jets_passing_cut,"inefficiencies_s_jets_passing_cut":inefficiencies_s_jets_passing_cut,"inefficiencies_g_jets_passing_cut":inefficiencies_g_jets_passing_cut,"cutoff_values":cutoff_values, "nbjets_true": nbjets_R5_true_total})
    df4.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/B_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/b_roc_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)



    ### B TAGGING ROCS

    ### C Tagging ROCS
    jets_R5_theta = arrays["jets_R5_theta"]

    ncjets_R5_true=(arrays["ncjets_R5_true"])
    ncjets_R5_true_total=np.sum(ncjets_R5_true)
    print(ncjets_R5_true_total,"ncjets_R5_true_total")
    cjets_R5_true_theta = arrays["cjets_R5_true_theta"]
    print(len(ak.flatten(cjets_R5_true_theta)), "should be same as number of true cjets total")

    cjet_match_mask = []
    for i in range(len(jets_R5_theta)):
        event_match_mask_C = []
        for j in range(len(jets_R5_theta[i])):
            if any(jets_R5_theta[i][j] == theta for theta in cjets_R5_true_theta[i]):
                event_match_mask_C.append(True)
            
        cjet_match_mask.append(event_match_mask_C)

    flattened_cjet_match_mask=ak.flatten(cjet_match_mask)
    combined_nested_isB_masked_for_C=ak.flatten(jets_R5_isB)[flattened_cjet_match_mask]
    combined_nested_isC_masked_for_C=ak.flatten(jets_R5_isC)[flattened_cjet_match_mask]
    combined_nested_isU_masked_for_C=ak.flatten(jets_R5_isU)[flattened_cjet_match_mask]
    combined_nested_isD_masked_for_C=ak.flatten(jets_R5_isD)[flattened_cjet_match_mask]
    combined_nested_isS_masked_for_C=ak.flatten(jets_R5_isS)[flattened_cjet_match_mask]
    combined_nested_isG_masked_for_C=ak.flatten(jets_R5_isG)[flattened_cjet_match_mask]

    df_cjet_match_mask=pd.DataFrame({f"cjet_match_mask{deltaR_label}{lepton_label}":flattened_cjet_match_mask})
    df_combined_nested_isB_masked_for_C=pd.DataFrame({f"combined_nested_isB_masked_R{deltaR_label}{lepton_label}":combined_nested_isB_masked_for_C})
    df_combined_nested_isC_masked_for_C=pd.DataFrame({f"combined_nested_isC_masked_R{deltaR_label}{lepton_label}":combined_nested_isC_masked_for_C})
    df_combined_nested_isU_masked_for_C=pd.DataFrame({f"combined_nested_isU_masked_R{deltaR_label}{lepton_label}":combined_nested_isU_masked_for_C})
    df_combined_nested_isD_masked_for_C=pd.DataFrame({f"combined_nested_isD_masked_R{deltaR_label}{lepton_label}":combined_nested_isD_masked_for_C})
    df_combined_nested_isS_masked_for_C=pd.DataFrame({f"combined_nested_isS_masked_R{deltaR_label}{lepton_label}":combined_nested_isS_masked_for_C})
    df_combined_nested_isG_masked_for_C=pd.DataFrame({f"combined_nested_isG_masked_R{deltaR_label}{lepton_label}":combined_nested_isG_masked_for_C})


    ## how cna i amek it so that if the jet_plots3_csvs{deltaR_label}{lepton_label} folder does not exist, it creates it
    if not os.path.exists(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}"):
        os.makedirs(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}")
    if not os.path.exists(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}"):
        os.makedirs(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}")



    df_cjet_match_mask.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/cjet_match_mask_R{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isB_masked_for_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isB_masked_R_for_C{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isC_masked_for_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isC_masked_R_for_C{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isU_masked_for_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isU_masked_R_for_C{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isD_masked_for_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isD_masked_R_for_C{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)

    df_combined_nested_isS_masked_for_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isS_masked_R_for_C{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df_combined_nested_isG_masked_for_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/combined_nested_isG_masked_R_for_C{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)


    ### Number Jets before and after overlap removal
    efficiencies_c_jets_passing_cut_C=[]
    inefficiencies_b_jets_passing_cut_C=[]
    inefficiencies_u_jets_passing_cut_C=[]
    inefficiencies_d_jets_passing_cut_C=[]
    inefficiencies_ud_jets_passing_cut_C=[]
    inefficiencies_s_jets_passing_cut_C=[]
    inefficiencies_g_jets_passing_cut_C=[]
    cutoff_values=[]

    for i in range(0,10000): 
        cuttoff_mask_val=i/10000
        c_score_cutoff_1_mask_for_C = combined_nested_isC_masked_for_C > cuttoff_mask_val
        b_score_cutoff_1_mask_for_C=combined_nested_isB_masked_for_C > cuttoff_mask_val
        u_score_cutoff_1_mask_for_C=combined_nested_isU_masked_for_C > cuttoff_mask_val
        d_score_cutoff_1_mask_for_C=combined_nested_isD_masked_for_C > cuttoff_mask_val
        s_score_cutoff_1_mask_for_C=combined_nested_isS_masked_for_C > cuttoff_mask_val
        g_score_cutoff_1_mask_for_C=combined_nested_isG_masked_for_C > cuttoff_mask_val

        c_score_cutoff_1_for_C= combined_nested_isC_masked_for_C[c_score_cutoff_1_mask_for_C]
        b_score_cutoff_1_for_C= combined_nested_isB_masked_for_C[b_score_cutoff_1_mask_for_C]
        u_score_cutoff_1_for_C= combined_nested_isU_masked_for_C[u_score_cutoff_1_mask_for_C]
        d_score_cutoff_1_for_C= combined_nested_isD_masked_for_C[d_score_cutoff_1_mask_for_C]
        s_score_cutoff_1_for_C= combined_nested_isS_masked_for_C[s_score_cutoff_1_mask_for_C]
        g_score_cutoff_1_for_C= combined_nested_isG_masked_for_C[g_score_cutoff_1_mask_for_C]
        total_c_jets_passing_cut_for_C=len(c_score_cutoff_1_for_C)
        efficiency_c_jets_passing_cut_for_C=total_c_jets_passing_cut_for_C/ncjets_R5_true_total
        # print(total_b_jets_passing_cut,"b jets passing cut")
        # print(total_b_jets_passing_cut,nbjets_R5_true_total)

        inefficiency_b_jets_passing_cut_total_for_C=len(b_score_cutoff_1_for_C)
        # print(inefficiency_c_jets_passing_cut_total,"c jets passing cut")
        inefficiency_b_jets_passing_cut_for_C=inefficiency_b_jets_passing_cut_total_for_C/ncjets_R5_true_total

        inefficiency_u_jets_passing_cut_total_for_C=len(u_score_cutoff_1_for_C)
        # print(inefficiency_u_jets_passing_cut_total,"u jets passing cut")
        inefficiency_u_jets_passing_cut_for_C=inefficiency_u_jets_passing_cut_total_for_C/ncjets_R5_true_total

        inefficiency_d_jets_passing_cut_total_for_C=len(d_score_cutoff_1_for_C)
        # print(inefficiency_d_jets_passing_cut_total,"d jets passing cut")
        inefficiency_d_jets_passing_cut_for_C=inefficiency_d_jets_passing_cut_total_for_C/ncjets_R5_true_total

        inefficiency_s_jets_passing_cut_total_for_C=len(s_score_cutoff_1_for_C)
        inefficiency_s_jets_passing_cut_for_C=inefficiency_s_jets_passing_cut_total_for_C/ncjets_R5_true_total

        inefficiency_g_jets_passing_cut_total_for_C=len(g_score_cutoff_1_for_C)
        inefficiency_g_jets_passing_cut_for_C=inefficiency_g_jets_passing_cut_total_for_C/ncjets_R5_true_total

        inefficiency_ud_jets_passing_cut_for_C=((inefficiency_d_jets_passing_cut_total_for_C+inefficiency_u_jets_passing_cut_total_for_C)*0.5)/ncjets_R5_true_total
        cutoff_values.append(cuttoff_mask_val)
        efficiencies_c_jets_passing_cut_C.append(efficiency_c_jets_passing_cut_for_C)
        inefficiencies_b_jets_passing_cut_C.append(inefficiency_b_jets_passing_cut_for_C)
        inefficiencies_u_jets_passing_cut_C.append(inefficiency_u_jets_passing_cut_for_C)
        inefficiencies_d_jets_passing_cut_C.append(inefficiency_d_jets_passing_cut_for_C)
        inefficiencies_ud_jets_passing_cut_C.append(inefficiency_ud_jets_passing_cut_for_C)
        inefficiencies_s_jets_passing_cut_C.append(inefficiency_s_jets_passing_cut_for_C)
        inefficiencies_g_jets_passing_cut_C.append(inefficiency_g_jets_passing_cut_for_C)



    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_b_jets_passing_cut_C,color="blue",label="c vs b")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(c-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs C Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_b_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_u_jets_passing_cut_C,color="green",label="c vs u")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(u-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs U Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_d_jets_passing_cut_C,color="red",label="c vs d")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(d-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs D Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()
    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_ud_jets_passing_cut_C,color="purple",label="c vs ud")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(ud-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs UD Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_s_jets_passing_cut_C,color="orange",label="c vs s")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(s-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs S Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_s_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()

    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_g_jets_passing_cut_C,color="brown",label="c vs g")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("log10(g-jet misd. probability)")
    # plt.title(f"B Tagging Efficiency vs G Tagging Inefficiency, R={deltaR_label}")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_g_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()


    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_s_jets_passing_cut_C,color="orange",label="c vs s")
    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_g_jets_passing_cut_C,color="brown",label="c vs g")
    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_ud_jets_passing_cut_C,color="green",label="c vs ud")
    plt.plot(efficiencies_c_jets_passing_cut_C,inefficiencies_b_jets_passing_cut_C,color="blue",label="c vs b")

    # plt.title(f"b ROC {deltaR_label}")
    plt.yscale("log")
    plt.xlabel("jet tagging efficiency")
    plt.ylabel("jet misd. probability")
    plt.legend(frameon=False)
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/C_jets/jet_plots3{deltaR_label}{lepton_label}{clustering_label}/c_roc_{deltaR_label}{lepton_label}{clustering_label}.pdf")
    plt.close()


    df_C=pd.DataFrame({"efficiencies_c_jets_passing_cut_C":efficiencies_c_jets_passing_cut_C,"inefficiencies_b_jets_passing_cut_C":inefficiencies_b_jets_passing_cut_C,"cutoff_values":cutoff_values, "ncjets_true": ncjets_R5_true_total})
    df_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_b_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)

    df1_C=pd.DataFrame({"efficiencies_c_jets_passing_cut_C":efficiencies_c_jets_passing_cut_C,"inefficiencies_u_jets_passing_cut_C":inefficiencies_u_jets_passing_cut_C,"cutoff_values":cutoff_values, "ncjets_true": ncjets_R5_true_total})
    df1_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_u_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df2_C=pd.DataFrame({"efficiencies_c_jets_passing_cut_C":efficiencies_c_jets_passing_cut_C,"inefficiencies_d_jets_passing_cut_C":inefficiencies_d_jets_passing_cut_C,"cutoff_values":cutoff_values, "ncjets_true": ncjets_R5_true_total})
    df2_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_d_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df3_C=pd.DataFrame({"efficiencies_c_jets_passing_cut_C":efficiencies_c_jets_passing_cut_C,"inefficiencies_ud_jets_passing_cut_C":inefficiencies_ud_jets_passing_cut_C,"cutoff_values":cutoff_values, "ncjets_true": ncjets_R5_true_total})
    df3_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_ud_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df5_C=pd.DataFrame({"efficiencies_c_jets_passing_cut_C":efficiencies_c_jets_passing_cut_C,"inefficiencies_s_jets_passing_cut_C":inefficiencies_s_jets_passing_cut_C,"cutoff_values":cutoff_values, "ncjets_true": ncjets_R5_true_total})
    df5_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_s_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)
    df6_C=pd.DataFrame({"efficiencies_c_jets_passing_cut_C":efficiencies_c_jets_passing_cut_C,"inefficiencies_g_jets_passing_cut_C":inefficiencies_g_jets_passing_cut_C,"cutoff_values":cutoff_values, "ncjets_true": ncjets_R5_true_total})
    df6_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/ctag_efficiency_vs_g_inefficiency_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)

    df4_C=pd.DataFrame({"efficiencies_c_jets_passing_cut_C":efficiencies_c_jets_passing_cut_C,"inefficiencies_ud_jets_passing_cut_C":inefficiencies_ud_jets_passing_cut_C,"inefficiencies_b_jets_passing_cut_C":inefficiencies_b_jets_passing_cut_C,"inefficiencies_s_jets_passing_cut_C":inefficiencies_s_jets_passing_cut_C,"inefficiencies_g_jets_passing_cut_C":inefficiencies_g_jets_passing_cut_C,"cutoff_values":cutoff_values, "ncjets_true": ncjets_R5_true_total})
    df4_C.to_csv(f"all_jets_{channel}/{ecm}/jet_csvs/C_jets/jet_plots3_csvs{deltaR_label}{lepton_label}{clustering_label}/c_roc_{deltaR_label}{lepton_label}{clustering_label}.csv",index=False)


    ### Jet Dist as func of n leps
    if not os.path.exists(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/B_scores"):
        os.makedirs(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/B_scores")


    histb = bh.Histogram(bh.axis.Regular(110, 0, 1))
    hist_c=bh.Histogram(bh.axis.Regular(110, 0, 1))
    hist_u=bh.Histogram(bh.axis.Regular(110, 0, 1))
    hist_d=bh.Histogram(bh.axis.Regular(110, 0, 1))

    for i in range(0,len(combined_nested_isB_masked)):
        histb.fill(combined_nested_isB_masked[i])
        hist_c.fill(combined_nested_isC_masked[i])
        hist_u.fill(combined_nested_isU_masked[i])
        hist_d.fill(combined_nested_isD_masked[i])


    hist_valueb=histb.view()
    hist_valuec=hist_c.view()
    hist_valueu=hist_u.view()
    hist_valued=hist_d.view()



    hist_valueb_norm=hist_valueb/hist_valueb.sum()


    hist_valuec_norm=hist_valuec/hist_valuec.sum()
    hist_valueu_norm=hist_valueu/hist_valueu.sum()
    hist_valued_norm=hist_valued/hist_valued.sum()
    plt.stairs(hist_valueb_norm,histb.axes[0].edges, color="blue", label="Normalized B Tag Score for true b jets")
    plt.stairs(hist_valuec_norm,hist_c.axes[0].edges, color="red", label="Normalized C Tag Score for true b jets")

    plt.xlabel("B Tag Score")
    plt.ylabel("Normalized Number of Jets")
    plt.title(f"Normalized B and C Tag Score for true b jets R={deltaR_label}")
    plt.yscale("log")
    plt.legend()
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/B_scores/btag_score_b_c_jet_combined_deltaR_{deltaR_label}_normalized_withfiltered.pdf")
    plt.close()

    plt.stairs(hist_valueb_norm,histb.axes[0].edges, color="blue", label="Normalized B Tag Score for true b jets")
    plt.stairs(hist_valueu_norm,hist_u.axes[0].edges, color="green", label="Normalized U Tag Score for true b jets")
    plt.stairs(hist_valued_norm,hist_d.axes[0].edges, color="black", label="Normalized D Tag Score for true b jets")
    plt.xlabel("B Tag Score")
    plt.ylabel("Normalized Number of Jets")
    plt.yscale("log")
    plt.legend()
    plt.title(f"Normalized B, U, and D Tag Score for true b jets R={deltaR_label}")
    plt.savefig(f"all_jets_{channel}/{ecm}/jet_plots/B_jets/B_scores/btag_score_b_u_d_jet_combined_deltaR_{deltaR_label}_normalized_withfiltered.pdf")
    plt.close()

ecm_345 = 345
ecm_365 = 365
ecm_91 = 91

# file_WW_365 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/p8_ee_WW_ecm{ecm_365}.root")
# plots_csvs_for_roc("WW",ecm_365,"0.5","zero","R5",file_WW_365)


# file_WbWb_365 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/wzp6_ee_WbWb_ecm{ecm_365}.root")
# plots_csvs_for_roc("WbWb",ecm_365,"0.5","zero","R5",file_WbWb_365)


file_WbWb_345 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/wzp6_ee_WbWb_ecm{ecm_345}.root")
plots_csvs_for_roc("WbWb",ecm_345,"0.5","two","R5",file_WbWb_345)

# file_ZZ_365 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/p8_ee_ZZ_ecm{ecm_365}.root")
# plots_csvs_for_roc("ZZ",ecm_365,"0.5","two","R5",file_ZZ_365)


# file_nunuH_365 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/wzp6_ee_nunuH_Hbb_ecm{ecm_365}.root")
# plots_csvs_for_roc("nunuH",ecm_365,"0.5","zero","R5",file_nunuH_365)

# file_Zbb_91 = uproot.open(f"/eos/user/g/gidaniel/outputs/treemaker/WbWb/semihad/p8_ee_Zbb_ecm{ecm_91}.root")
# plots_csvs_for_roc("Zbb",ecm_91,"0.5","zero","R5",file_Zbb_91)