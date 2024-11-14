import ROOT, os, subprocess, sys, optparse
from array import array
import math

import datetime
date = datetime.date.today().isoformat()

def histStyle(hist,xtitle,color,lstyle):
    hist.SetLineColor  (color)
    hist.SetLineWidth  (2)
    hist.SetLineStyle  (lstyle)
    hist.GetXaxis().SetTitle(xtitle)
    hist.GetYaxis().SetTitle('Events')
    hist.GetXaxis().SetLabelSize(0.35);
    hist.GetXaxis().SetLabelOffset(0.85);
    #hist.Scale(1.0/hist.Integral())
    return hist

def drawhists(ecm,channel,hname,syst,sel):

    filetoread = ROOT.TFile(f'rootfiles/{channel}_{sel}_noBDT_bWP9_{ecm}.root','READ')
    print(filetoread.GetName())
    h_nom = filetoread.Get(f'x_{hname}')
    h_up  = filetoread.Get(f'x_{hname}_{syst}Up')
    h_dn  = filetoread.Get(f'x_{hname}_{syst}Down')
    
    print(type(h_nom),type(h_up),type(h_dn))
    h_nom.SetDirectory(0);    h_up.SetDirectory(0);    h_dn.SetDirectory(0)
    h_n=histStyle(h_nom,'n_{jets}',ROOT.kRed,1)
    h_u=histStyle(h_up,'n_{jets}',ROOT.kBlue,2)
    h_d=histStyle(h_dn,'n_{jets}',ROOT.kGreen+4,5)
    print(h_n.GetName(),h_u.GetName(),h_d.GetName())
    h_n.SetDirectory(0);    h_u.SetDirectory(0);    h_d.SetDirectory(0)
    Canv = ROOT.TCanvas(f'Canv_{channel}_{ecm}_{hname}',"",800,800)
    Canv.Range(0,0,1,1);   Canv.SetFillColor(0);   Canv.SetBorderMode(0);   Canv.SetBorderSize(2);
    Canv.SetTickx(1);   Canv.SetTicky(1);   Canv.SetLeftMargin(0.16);   Canv.SetRightMargin(0.08);        #_Canv.SetLogy();
    Canv.SetBottomMargin(0.13);   Canv.SetFrameFillStyle(0);   Canv.SetFrameBorderMode(0); Canv.cd();
    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0)
    pad1.SetGridy();pad1.SetGridx()
    pad1.Draw()
    Canv.cd()
    pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0.0)
    pad2.SetBottomMargin(0.3)
    pad2.SetGridy()
    pad2.Draw()
    pad1.cd()
    legend = ROOT.TLegend(0.5,0.6,0.8,0.85);
    legend.SetNColumns(1);legend.SetFillColor(0);legend.SetFillStyle(0); legend.SetShadowColor(0);   legend.SetLineColor(0);
    legend.SetTextFont(42);        legend.SetBorderSize(0);   legend.SetTextSize(0.04);
    legend.AddEntry('NULL',f'channel: {channel}; ecm: {ecm} GeV','')
    legend.AddEntry('NULL',f'proc:{hname}; uncert: {syst}','')
    legend.AddEntry(h_n,'nom','l')
    legend.AddEntry(h_u,'up','l')
    legend.AddEntry(h_d,'dn','l')
    h_n.GetYaxis().SetRangeUser(0,1.005*max(h_n.Integral(),h_u.Integral(),h_d.Integral()))
    #h_n.GetYaxis().SetRangeUser(0,5*max(h_n.Integral(),h_u.Integral(),h_d.Integral()))
    h_n.Draw('hist');h_u.Draw('histsame');h_d.Draw('histsame');
    legend.Draw("same")
    plotsdir=f"/eos/user/a/anmehta/www/FCC_top/{date}variations"
    if not os.path.isdir(plotsdir):        os.system("mkdir %s"%plotsdir);  os.system('cp ~/public/index.php %s/'%plotsdir)
    pad2.cd()
    hUp=h_u.Clone();
    hDn=h_d.Clone();
    hnom=h_n.Clone();
    hUp.Divide(hnom); hUp.SetMarkerColor(ROOT.kBlue);hUp.SetLineColor(ROOT.kBlue); hUp.SetMarkerStyle(26)
    hDn.Divide(hnom); hDn.SetMarkerColor(ROOT.kGreen+4);hDn.SetLineColor(ROOT.kGreen+4); hDn.SetMarkerStyle(32)
    hUp.Draw(); hDn.Draw("psame");
    hUp.GetYaxis().SetTitle("var/nom");  hUp.GetXaxis().SetTitle("n_{jets}");
    hUp.GetXaxis().SetTitleFont(42);    hUp.GetXaxis().SetLabelSize(0.11);    hUp.GetXaxis().SetTitleSize(0.12);
    hUp.GetXaxis().SetTitleOffset(0.95);      
    hUp.GetYaxis().SetLabelSize(0.11);    hUp.GetYaxis().SetTitleSize(0.12);    hUp.GetYaxis().SetTitleOffset(0.44);
    hUp.GetYaxis().SetRangeUser(0.8,1.22);     hUp.GetYaxis().SetNdivisions(607);    ROOT.gStyle.SetErrorX(0.5);

    Canv.Print(f"{plotsdir}_zoomed/{sel}_{hname}_{syst}_{channel}_{ecm}.pdf")
    Canv.Print(f"{plotsdir}_zoomed/{sel}_{hname}_{syst}_{channel}_{ecm}.png")

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
        for sel in ['zerob','oneb','twob']:
            for ch in ['semihad','had']:
                drawhists(ecm,ch,'sig','ps',sel)
                drawhists(ecm,ch,'sig','btag',sel)
                drawhists(ecm,ch,'sig','topmass',sel)
                drawhists(ecm,ch,f'bkg_{ch}','btag',sel)
