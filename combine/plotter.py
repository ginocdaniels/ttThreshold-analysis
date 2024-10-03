import ROOT,sys

config="noflavWPpt5"
cuts=sys.argv[1] #sig or cr or incl
channel=sys.argv[2] #had or semihad
ecm=sys.argv[3] 

lumi=36000 #pb
br_semihad=0.438
br_had=0.457
xsec_tt=0.1 if ecm =="340" else 0.5
xsec_sig=xsec_tt*(br_semihad if "semihad" in channel else br_had)
lumi_txt=f'{lumi/1000:.1f}'

print('sig xsec value is ',xsec_sig)

useLog=False

ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptStat(0)


def if3(cond, iftrue, iffalse):
    return iftrue if cond else iffalse

def drawSLatex(xpos,ypos,text,size):
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAlign(12)
    latex.SetTextSize(size)
    latex.SetTextFont(42)
    latex.DrawLatex(xpos,ypos,text)

#vname= if3(cuts == 'cr', "BDT_cut_zerobtag_nbjets_cr", if3(cuts == 'sig',"BDT_cut_onebtag_nbjets_sig","BDT_cut_nbjets"))
vname = 'no_cut_njets' #BDT_cut_nbjets' #no_cut_BDT_score' #no_cut_nbjets'
xtitle= "N_{jets}" # with BDT score > 0.5" #"BDT score" #
print('used variable is \t', vname)
def stackPlot(fname):

    Canv = ROOT.TCanvas(f'Canv_{channel}_{config}_{ecm}',"",600,600)
    Canv.Range(0,0,1,1);   Canv.SetFillColor(0);   Canv.SetBorderMode(0);   Canv.SetBorderSize(2);
    Canv.SetTickx(1);   Canv.SetTicky(1);   Canv.SetLeftMargin(0.16);   Canv.SetRightMargin(0.08);
    Canv.SetBottomMargin(0.13);   Canv.SetFrameFillStyle(0);   Canv.SetFrameBorderMode(0);
    
    legend = ROOT.TLegend(0.5,0.6,0.85,0.8);
    legend.SetNColumns(1);legend.SetFillColor(0);legend.SetFillStyle(0); legend.SetShadowColor(0);   legend.SetLineColor(0);
    legend.SetTextFont(42);        legend.SetBorderSize(0);   legend.SetTextSize(0.04);
    hs=ROOT.THStack(f'hs_{channel}_{config}_{ecm}',""); 
    f_in=ROOT.TFile.Open(fname)
    h_sig=f_in.Get('x_sig');
    h_bkg=f_in.Get('x_bkg_%s'%channel);
##am    num_sig=[];num_bkg=[];
##am    err_sig=[];err_bkg=[];
##am    num_data=[];
##am    for i in range(h_sig.GetNbinsX()):
##am        num_sig.append(h_sig.GetBinContent(i+1));err_sig.append(h_sig.GetBinError(i+1));
##am        num_bkg.append(h_bkg.GetBinContent(i+1));err_bkg.append(h_bkg.GetBinError(i+1));
##am        num_data.append(h_sig.GetBinContent(i+1)+h_bkg.GetBinContent(i+1));
##am    print('sig',num_sig,err_sig)
##am    print('bkg',num_bkg,err_bkg)
##am    print('data',num_data)
        
    h_bkg.SetDirectory(0);    h_sig.SetDirectory(0);
    h_sig.SetFillColor(ROOT.kAzure+1); h_sig.SetLineColor(ROOT.kBlack)
    h_bkg.SetFillColor(ROOT.kOrange+1); h_bkg.SetLineColor(ROOT.kBlack)
    
    f_in.Close();


    hs.Add(h_bkg);
    hs.Add(h_sig);
    
    legend.AddEntry('NULL',f'{channel}','')#e^{#plus}e^{#minus} #rightarrow WbWb/WW  #rightarrow %s'%channel,'')
    legend.AddEntry(h_sig,f"WbWb ({h_sig.Integral():.2e})","F");
    legend.AddEntry(h_bkg,f"WW  ({h_bkg.Integral():.2e})","F");
    hs.Draw("HIST");
    hs.GetXaxis().SetTitle(xtitle)
    hs.GetYaxis().SetTitle("Events");
    hs.GetYaxis().SetLabelSize(0.04);    hs.GetYaxis().SetTitleSize(0.045);    hs.GetYaxis().SetTitleOffset(1.12);
    hs.GetXaxis().SetTitleSize(0.045);    hs.GetXaxis().SetTitleOffset(1.0); hs.GetXaxis().SetLabelSize(0.04);
    
    hs.GetXaxis().SetTitleFont(42);        hs.GetYaxis().SetTitleFont(42);    
    t2a = drawSLatex(0.2,0.85,"#bf{FCC-ee} #it{Simulation (Delphes)}",0.04);
    t3a = drawSLatex(0.66,0.915,"%s fb^{#minus1} (%s GeV)"%(lumi_txt,ecm),0.035);

    pf=""
    morey=1.0
    if useLog:
        Canv.SetLogy();
        pf='_log'
        #    t2a = drawSLatex(0.16,0.935,"#bf{FCC-ee} #it{Simulation (Delphes)}",0.04);
        #   t3a = drawSLatex(0.7,0.935,"36 fb^{#minus1} (345 GeV)",0.035);
        morey=20
    else:
        hs.GetYaxis().SetTitleOffset(1.25);
        morey=1.55 #if 'cr' not in channel else 2e12
        
    hs.SetMaximum(morey*(h_sig.Integral()+h_bkg.Integral()));    legend.Draw("same");
    Canv.Update();
    Canv.Print(f"/eos/user/a/anmehta/www/FCC_top/{vname}_{channel}_{ecm}{pf}.pdf")
    Canv.Print(f"/eos/user/a/anmehta/www/FCC_top/{vname}_{channel}_{ecm}{pf}.png")
    return True

def getHist(isSig,h_name):
    sf=1.0;sumW=1.0;xsec_M=1.0;
    if isSig:
        proc=f'wzp6_ee_WbWb_{channel}_ecm{ecm}'
        xsec_M=xsec_sig#[ecm]
    else:
        proc=f'p8_ee_WW_ecm{ecm}'
    f_in=ROOT.TFile.Open(f'/eos/cms/store/cmst3/group/top/anmehta/FCC//output_condor_06092024/WbWb/outputs/histmaker/{channel}/{config}/{proc}.root')
    h_in=f_in.Get(vname).Clone(h_name)
    xsec=f_in.Get('crossSection').GetVal()
    sumW=f_in.Get('sumOfWeights').GetVal()
    N_tot=f_in.Get('eventsProcessed').GetVal()
    print('input integral ',h_in.Integral())
    #h_in.Scale(1.0/h_in.Integral())
    #print('normalized integral ',h_in.Integral())
    #sf=xsec*xsec_M*lumi*sumW/N_tot
    sf=xsec*xsec_M*lumi/sumW
    print('isSig\t',isSig,"\t sumW \t",sumW,N_tot)
    h_in.Scale(sf)
    print('final yield',h_in.Integral(),sf)
    h_in.SetDirectory(0)
    f_in.Close();
    return h_in

h_sig=getHist(True,"x_sig")
print('sig',h_sig.Integral())
h_obs=h_sig.Clone("x_data_obs")
#h_obs=getHist(True,"x_data_obs")
h_bkg=getHist(False,"x_bkg_%s"%channel)
h_obs.Add(h_bkg)
print('bkg',h_bkg.Integral())
print(type(h_bkg))
print(type(h_sig))

#f_out=ROOT.TFile("/afs/cern.ch/work/a/anmehta/public/latest_combine/CMSSW_14_1_0_pre4/src/fcc/datacard_%s_%s_%s.root"%(cuts,config,ecm),"RECREATE");
fout_name=f"{channel}_{cuts}_{config}_{ecm}.root"
f_out=ROOT.TFile(fout_name,"RECREATE");
f_out.cd();
h_sig.Write();
h_bkg.Write();
h_obs.Write();
#f_out.Write();
f_out.Close();

stackPlot(fout_name)
