import ROOT,sys,optparse



def if3(cond, iftrue, iffalse):
    return iftrue if cond else iffalse

def drawSLatex(xpos,ypos,text,size):
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAlign(12)
    latex.SetTextSize(size)
    latex.SetTextFont(42)
    latex.DrawLatex(xpos,ypos,text)

def stackPlot(fname,vname,lumi,channel,config,ecm,useLog,showInt):
    lumi_txt=f'{lumi/1000:.1f}'
    Canv = ROOT.TCanvas(f'Canv_{channel}_{config}_{ecm}',"",600,600)
    Canv.Range(0,0,1,1);   Canv.SetFillColor(0);   Canv.SetBorderMode(0);   Canv.SetBorderSize(2);
    Canv.SetTickx(1);   Canv.SetTicky(1);   Canv.SetLeftMargin(0.16);   Canv.SetRightMargin(0.08);
    Canv.SetBottomMargin(0.13);   Canv.SetFrameFillStyle(0);   Canv.SetFrameBorderMode(0);
    
    #legend = ROOT.TLegend(0.5 if showInt else 0.635,0.67,0.8 if showInt else  0.875,0.85);
    legend = ROOT.TLegend(0.5,0.635,0.8,0.8);
    legend.SetNColumns(1);legend.SetFillColor(0);legend.SetFillStyle(0); legend.SetShadowColor(0);   legend.SetLineColor(0);
    legend.SetTextFont(42);        legend.SetBorderSize(0);   legend.SetTextSize(0.04);
    hs=ROOT.THStack(f'hs_{channel}_{config}_{ecm}',""); 
    f_in=ROOT.TFile.Open(fname)
    h_sig=f_in.Get('x_sig');
    h_bkg=f_in.Get('x_bkg_%s'%channel);
    h_bkg.SetDirectory(0);    h_sig.SetDirectory(0);
    h_sig.SetFillColor(ROOT.kAzure+1); h_sig.SetLineColor(ROOT.kBlack)
    h_bkg.SetFillColor(ROOT.kOrange+1); h_bkg.SetLineColor(ROOT.kBlack)
    
    f_in.Close();
    hs.Add(h_bkg);
    hs.Add(h_sig);
    legend.AddEntry('NULL',f'{channel}','')#e^{#plus}e^{#minus} #rightarrow WbWb/WW  #rightarrow %s'%channel,'')

    legend.AddEntry(h_sig, 'WbWb'+ (f"({h_sig.Integral():.2e})" if showInt else ''),"F");
    legend.AddEntry(h_bkg,  'WW '+ (f"({h_bkg.Integral():.2e})" if showInt else ''),"F");

    hs.Draw("HIST");
    hs.GetXaxis().SetTitle(xtitle)
    hs.GetYaxis().SetTitle("Events");
    hs.GetYaxis().SetLabelSize(0.04);    hs.GetYaxis().SetTitleSize(0.045);    hs.GetYaxis().SetTitleOffset(1.22);
    hs.GetXaxis().SetTitleSize(0.045);    hs.GetXaxis().SetTitleOffset(1.0); hs.GetXaxis().SetLabelSize(0.04);
    hs.GetYaxis().SetMaxDigits(3);
    hs.GetXaxis().SetTitleFont(42);        hs.GetYaxis().SetTitleFont(42);    
    t2a = drawSLatex(0.2,0.85,"#bf{FCC-ee} #it{Simulation (Delphes)}",0.04);
    t3a = drawSLatex(0.66,0.915,"%s fb^{#minus1} (%s GeV)"%(lumi_txt,ecm),0.035);

    pf=""
    morey=1.0
    if useLog:
        Canv.SetLogy();
        pf='_log'
        morey=20
    else:
        hs.GetYaxis().SetTitleOffset(1.25);
        morey=1.65 if 'incl' not in channel else 0.5
        
    hs.SetMaximum(morey*(h_sig.Integral()+h_bkg.Integral()));   legend.Draw("same");
    Canv.Update();
    Canv.Print(f"/eos/user/a/anmehta/www/FCC_top/{vname}_{channel}_{config}_{ecm}{pf}.pdf")
    Canv.Print(f"/eos/user/a/anmehta/www/FCC_top/{vname}_{channel}_{config}_{ecm}{pf}.png")
    return True

def getHist(isSig,vname,h_name,xsec_sig,channel,config,ecm):
    sf=1.0;sumW=1.0;xsec_M=1.0;
    if isSig:
        proc=f'wzp6_ee_WbWb_{channel}_ecm{ecm}'
        xsec_M=xsec_sig
    else:
        proc=f'p8_ee_WW_ecm{ecm}'
    f_in=ROOT.TFile.Open(f'/eos/cms/store/cmst3/group/top/anmehta/FCC//output_condor_06092024/WbWb/outputs/histmaker/{channel}/{config}/{proc}.root')
    h_in=f_in.Get(vname).Clone(h_name);    xsec=f_in.Get('crossSection').GetVal();    sumW=f_in.Get('sumOfWeights').GetVal()
    #N_tot=f_in.Get('eventsProcessed').GetVal()
    print('sumW',sumW)
    print('input ylds',h_in.Integral())
    sf=xsec*xsec_M*lumi/sumW
    h_in.Scale(sf);    h_in.SetDirectory(0);    f_in.Close();
    print('integral after scaling',h_in.Integral())
    return h_in

def cards(mkplots,lumi,xsec_sig,channel,sel,config,ecm,logy,vname,xtitle,showInt):
    h_sig=getHist(True,vname,"x_sig",xsec_sig,channel,config,ecm)
    print('sig',h_sig.Integral())
    h_obs=h_sig.Clone("x_data_obs")
    h_bkg=getHist(False,vname,"x_bkg_%s"%channel,1.0,channel,config,ecm)
    h_obs.Add(h_bkg)
    print('bkg',h_bkg.Integral())
    fout_name=f"{channel}_{sel}_{config}_{ecm}.root"
    f_out=ROOT.TFile(fout_name,"RECREATE");
    f_out.cd();
    h_sig.Write();    h_bkg.Write();    h_obs.Write();    f_out.Close();
    if mkplots:
        stackPlot(fout_name,vname,lumi,channel,config,ecm,logy,showInt)


if __name__ == '__main__':
    ROOT.gROOT.SetBatch()
    ROOT.gStyle.SetOptStat(0)

    parser = optparse.OptionParser(usage='usage: %prog [opts] ', version='%prog 1.0')
    parser.add_option('-c',  '--ch',       dest='channel', type='string',         default='semihad',    help='had/semihad')
    parser.add_option('-f',  '--fconf',    dest='config',  type='string',         default='noflav',     help='withflav/noflav/withbtaggedJet')
    parser.add_option('-s',  '--sel',      dest='sel' ,    type='string',         default='incl',       help='sig/cr')
    parser.add_option('-e',  '--ecm',      dest='ecm' ,    type='string',         default='345',        help='ecm')
    parser.add_option('-w',  '--bwp',      dest='btagWP',  type='string',         default='',           help='btagWP:loose/tight')
    parser.add_option('-l',  '--lum',      dest='lum' ,    type=float,            default=36.0,         help='lumi in fb')
    parser.add_option('-p',  '--plots',    dest='mkplots', action='store_true',   default=False,        help='make plots too')
    parser.add_option('-i',  '--sInt',     dest='showInt' ,action='store_true',   default=False,        help='show integral in legends')
    parser.add_option('--logy',            dest='logy' ,    action='store_true',  default=False,        help='use log scale for y-axis')


    (opts, args) = parser.parse_args()
    
    lumi=opts.lum*1000
    br_semihad=0.438
    br_had=0.457
    xsec_tt=0.1 if opts.ecm =="340" else 0.5
    xsec_sig=xsec_tt*(br_semihad if "semihad" in opts.channel else br_had)
    #btag_wp='%sWPpt%s'%(opts.config,opts.btagWP)
    nb_var='L_nbjets_loose' if "loose" in opts.btagWP else 'T_nbjets_loose'
    vname= if3(opts.sel == 'cr', "BDT_cut_zerobtag%s_cr"%nb_var, if3(opts.sel == 'sig',"BDT_cut_onebtag%s_sig"%nb_var,"BDT_cut_nbjets_%s"%(nb_var)))    #vname = 'no_cut_njets' #BDT_cut_nbjets' #no_cut_BDT_score' #no_cut_nbjets'
    
    xtitle= "N_{bjets}^%s} with BDT score > 0.5"%opts.btagWP 

    cards(opts.mkplots,lumi,xsec_sig,opts.channel,opts.sel,config,opts.ecm,opts.logy,vname,xtitle,opts.showInt)
        
