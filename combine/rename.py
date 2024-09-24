import ROOT,sys
channel="semihad"
ecm="340"
config="noflav"
doWhat=sys.argv[1] #sig or cr
tmp=[]

vname="BDT_cut_zerobtag_nbjets" if "cr" in doWhat else "BDT_cut_onebtag_nbjets"

f_sig=ROOT.TFile.Open("/eos/cms/store/cmst3/group/top/anmehta/FCC//output_condor_06092024/WbWb/outputs/histmaker/{chan}/{config}/wzp6_ee_WbWb_semihad_ecm{ecm}.root".format(ecm=ecm,chan=channel,config=config));
h_sig=f_sig.Get(vname).Clone("x_sig")
h_obs=f_sig.Get(vname).Clone("x_data_obs")
h_sig.SetDirectory(0)
h_obs.SetDirectory(0)
#tmp.append(h_sig)
f_sig.Close();

f_bkg=ROOT.TFile.Open("/eos/cms/store/cmst3/group/top/anmehta/FCC//output_condor_06092024/WbWb/outputs/histmaker/{chan}/{config}/p8_ee_WW_ecm{ecm}.root".format(ecm=ecm,chan=channel,config=config));
h_bkg=f_bkg.Get(vname).Clone("x_bkg")
#tmp.append(h_bkg);
h_bkg.SetDirectory(0)
f_bkg.Close();

print(type(h_bkg))
print(type(h_sig))

f_out=ROOT.TFile("/afs/cern.ch/work/a/anmehta/public/latest_combine/CMSSW_14_1_0_pre4/src/fcc/datacard_%s_%s_%s.root"%(doWhat,config,ecm),"RECREATE");
f_out.cd();
h_sig.Write();
h_bkg.Write();
h_obs.Write();
f_out.Close();
