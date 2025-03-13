import ROOT, os, subprocess, sys, optparse
from array import array
import math

fitvars={
    'zerob_had':['njets_R5',"N_{jets}"],
    'oneb_had':['njets_R5',"N_{jets}"],
    'twob_had':['njets_R5',"N_{jets}"], #mbbar
    'zerob_semihad':['singlebin',"N_{events}"],
    'oneb_semihad':['njets_R5',"N_{jets}"],
    'twob_semihad':['njets_R5',"N_{jets}"],
}

fancyname={'singlebin': "N_{events}",
           'BDT_score': "BDT",
           "zerob":"N_{bjets}=0",
           "oneb":"N_{bjets}=1",
           "twob":"N_{bjets}=2",
           'njgt0':"N_{jets}#geq1",
           'njgt1':"N_{jets}#geq2",
           "njets_R5":"N_{jets}"}

import datetime
date = datetime.date.today().isoformat()
def drawSLatex(xpos,ypos,text,size):
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAlign(12)
    latex.SetTextSize(size)
    latex.SetTextFont(42)
    latex.DrawLatex(xpos,ypos,text)

def histStyle(hist,xtitle,color,lstyle):
    hist.Sumw2()
    hist.SetLineColor  (color)
    hist.SetLineWidth  (2)
    hist.SetLineStyle  (lstyle)
    hist.GetXaxis().SetTitle(xtitle)
    hist.GetYaxis().SetTitle('Events')
    hist.GetYaxis().SetTitleSize(0.05)
    hist.GetXaxis().SetLabelSize(0.35);
    hist.GetYaxis().SetTitleOffset(0.85);
    #hist.Scale(1.0/hist.Integral())
    return hist

def drawhists(ecm,channel,hname_nom,hname,syst,sel,vname,xtitle):
    if ecm == "365":
        lumi=2650*1000
        lumi_txt=f'{lumi/1e6:.1f}'
    else:
        lumi=41.0*1000
        lumi_txt=f'{lumi/1e3:.1f}'
    #semihad_njgt0_effp9_zerob_singlebin_345.root
    esel="njgt0" if channel == "semihad" else "njgt1"
    filetoread = ROOT.TFile(f'rootfiles/{channel}_{esel}_effp9_{sel}_{vname}_{ecm}.root','READ')
    print(filetoread.GetName())
    h_nom = filetoread.Get(f'x_{hname_nom}')
    h_up  = filetoread.Get(f'x_{hname}_{syst}Up')
    h_dn  = filetoread.Get(f'x_{hname}_{syst}Down')
    
    print(type(h_nom),type(h_up),type(h_dn))
    h_nom.SetDirectory(0);    h_up.SetDirectory(0);    h_dn.SetDirectory(0)
    h_n=histStyle(h_nom,vname,ROOT.kRed,1)
    h_u=histStyle(h_up,vname,ROOT.kBlue,2)
    h_d=histStyle(h_dn,vname,ROOT.kGreen+2,5)
    print(h_n.GetName(),h_u.GetName(),h_d.GetName())
    h_n.SetDirectory(0);    h_u.SetDirectory(0);    h_d.SetDirectory(0)
    Canv = ROOT.TCanvas(f'Canv_{channel}_{ecm}_{hname}_{sel}_{syst}_{vname}',"",800,800)
    Canv.Range(0,0,1,1);   Canv.SetFillColor(0);   Canv.SetBorderMode(0);   Canv.SetBorderSize(2);
    Canv.SetTickx(1);   Canv.SetTicky(1);   Canv.SetLeftMargin(0.16);   Canv.SetRightMargin(0.08);        #_Canv.SetLogy();
    Canv.SetBottomMargin(0.13);   Canv.SetFrameFillStyle(0);   Canv.SetFrameBorderMode(0); Canv.cd();
    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0.02)
    #pad1.SetGridy();pad1.SetGridx()
    pad1.Draw()
    Canv.cd()
    pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0.0)
    pad2.SetBottomMargin(0.3)
    pad2.SetGridy()
    pad2.Draw()
    pad1.cd()
    t2a = drawSLatex(0.2,0.65,"#bf{FCC-ee} #it{Simulation (Delphes)}",0.04);
    if ecm == "365":
        t3a = drawSLatex(0.66,0.8,"%s ab^{#minus1} (%s GeV)"%(lumi_txt,ecm),0.035);
    else:    
        t3a = drawSLatex(0.66,0.8,"%s fb^{#minus1} (%s GeV)"%(lumi_txt,ecm),0.035);


    legend = ROOT.TLegend(0.2,0.75,0.85,0.85);
    legend.SetNColumns(3);legend.SetFillColor(0);legend.SetFillStyle(0); legend.SetShadowColor(0);   legend.SetLineColor(0);
    legend.SetTextFont(42);        legend.SetBorderSize(0);   legend.SetTextSize(0.04);
    legend.AddEntry('NULL',f'{channel}; '+fancyname[sel]+fancyname[esel],'')
    #legend.AddEntry('NULL',f'ecm: {ecm} GeV','')
    legend.AddEntry('NULL',f'proc: {hname_nom}','')
    legend.AddEntry('NULL',f'uncert: {syst}','')
    legend.AddEntry(h_n,'nom','l')
    legend.AddEntry(h_u,'up','l')
    legend.AddEntry(h_d,'dn','l')
    h_n.GetYaxis().SetRangeUser(0,1.25*max(h_n.GetMaximum(),h_u.GetMaximum(),h_d.GetMaximum()))
    #h_n.GetYaxis().SetRangeUser(0,5*max(h_n.Integral(),h_u.Integral(),h_d.Integral()))
    h_n.Draw('hist');h_u.Draw('histsame');h_d.Draw('histsame');
    legend.Draw("same")
    plotsdir=f"/eos/user/a/anmehta/www/FCC_top/{date}_syst_variations"
    if not os.path.isdir(plotsdir):        os.system("mkdir %s"%plotsdir);  os.system('cp ~/public/index.php %s/'%plotsdir)
    pad2.cd()
    hUp=h_u.Clone();
    hDn=h_d.Clone();
    hnom=h_n.Clone();
    hUp.Divide(hnom); hUp.SetMarkerColor(ROOT.kBlue);hUp.SetLineColor(ROOT.kBlue); hUp.SetMarkerStyle(26)
    hDn.Divide(hnom); hDn.SetMarkerColor(ROOT.kGreen+2);hDn.SetLineColor(ROOT.kGreen+2); hDn.SetMarkerStyle(32)
    hUp.Draw(); hDn.Draw("psame");
    hUp.GetYaxis().SetTitle("var/nom");  hUp.GetXaxis().SetTitle(xtitle) #"n_{jets}");
    hUp.GetXaxis().SetTitleFont(42);     
    hUp.GetYaxis().SetLabelOffset(0.015)     
    hUp.GetYaxis().SetLabelSize(0.1);    hUp.GetYaxis().SetTitleSize(0.135);    hUp.GetYaxis().SetTitleOffset(0.38);
    hUp.GetXaxis().SetLabelSize(0.1);    hUp.GetXaxis().SetTitleSize(0.12);    hUp.GetXaxis().SetTitleOffset(0.9);
    hUp.GetYaxis().SetRangeUser(0.8,1.52);     hUp.GetYaxis().SetNdivisions(607);    ROOT.gStyle.SetErrorX(0.5);

    Canv.Print(f"{plotsdir}/{sel}_{hname_nom}_{syst}_{channel}_{ecm}_{vname}.pdf")
    Canv.Print(f"{plotsdir}/{sel}_{hname_nom}_{syst}_{channel}_{ecm}_{vname}.png")

    return True

if __name__ == '__main__':
    ROOT.gROOT.SetBatch()
    ROOT.gStyle.SetOptStat(0)

#    parser = optparse.OptionParser(usage='usage: %prog [opts] ', version='%prog 1.0')
#    parser.add_option('-c',  '--ch',       dest='channel', type='string',         default='semihad',    help='had/semihad')
#    parser.add_option('-s',  '--sel',      dest='sel' ,    type='string',         default='incl',       help='sig/cr')
#    parser.add_option('-e',  '--ecm',      dest='ecm' ,    type='string',         default='345',        help='ecm')
#    (opts, args) = parser.parse_args()

    for ecm in ['340','345','365']:
        #for sel in ['zerob','oneb','twob']:
        #for ch in ['semihad','had']:                
        for iW in fitvars.keys(): #['singlebin','njets_R5','BDT_score']: #,'mbbar','nbjets_R5_eff_p9',
            ch=iW.split('_')[-1]
            sel=iW.split('_')[0]
            #isel=sel+'_'+ch
            #if not isel in fitvars.keys(): continue
            drawhists(ecm,ch,'sig','sig_sig','ps',sel,fitvars[iW][0],fitvars[iW][1])
            drawhists(ecm,ch,'sig','sig_sig','ps',sel,fitvars[iW][0],fitvars[iW][1])
            drawhists(ecm,ch,f'qq_{ch}',f'qq_{ch}_qq_{ch}','ps',sel,fitvars[iW][0],fitvars[iW][1])
            drawhists(ecm,ch,f'ww_{ch}',f'ww_{ch}_ww_{ch}','ps',sel,fitvars[iW][0],fitvars[iW][1])
            drawhists(ecm,ch,f'wwz_{ch}',f'wwz_{ch}','btag',sel,fitvars[iW][0],fitvars[iW][1])
            drawhists(ecm,ch,'sig','sig','btag',sel,fitvars[iW][0],fitvars[iW][1])
            drawhists(ecm,ch,f'qq_{ch}',f'qq_{ch}','btag',sel,fitvars[iW][0],fitvars[iW][1])
            drawhists(ecm,ch,f'ww_{ch}',f'ww_{ch}','btag',sel,fitvars[iW][0],fitvars[iW][1])
            drawhists(ecm,ch,f'wwz_{ch}',f'wwz_{ch}','btag',sel,fitvars[iW][0],fitvars[iW][1])
            drawhists(ecm,ch,'sig','sig_sig','topmass',sel,fitvars[iW][0],fitvars[iW][1])
