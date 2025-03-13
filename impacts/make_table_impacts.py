import json,math
import os,sys,re
import HiggsAnalysis.CombinedLimit.calculate_pulls as CP


def IsConstrained(param_info):
    return param_info["type"] != "Unconstrained"


fancyN={'lumi':'luminosity','norm_qq_had':'q#bar{q} had. norm.','norm_ww_semihad':'ww semihad. norm.','norm_ww_had':'ww had. norm.',"wwz_norm":'wwz norm.',"qq_semihad_norm":'q#bar{q} semihad. norm.',"btag" : 'b tagging','r':'r','norm_zz_semihad':'zz semihad. norm.', 'norm_zz_had':'zz had. norm.'}



#poi_name=data['POIs'][0]['name']
#uncert_poi=(data['POIs'][0]['fit'][0],data['POIs'][0]['fit'][-1]) #down,up
#uncert_nom_poi="{:.3f}".format(100*( (1-data['POIs'][0]['fit'][0])+ (data['POIs'][0]['fit'][-1] -1))/2)

#impacts={}
#for i in range(len(params)):
#    impact[data['params'][i]['name']]="{:.6f}".format(data['params'][i]['impact_r'])



#for ele in params:
#    # Calculate impacts and relative impacts. Note that here the impacts are signed.
#    ele["impact_hi"] = ele[POI][2] - ele[POI][1]
#    ele["impact_lo"] = ele[POI][0] - ele[POI][1]
#    # Some care needed with the relative ones, since we don't know the signs of hi and lo.
#    # We want to divide any positive impact by the positive uncert. on the POI, and similar for negative.
#    # We also need to be careful in case the uncertainties on the POI came out as zero (shouldn't happen...)
#    if (POI_fit[2] - POI_fit[1]) > 0.0 and (POI_fit[1] - POI_fit[0]) > 0.0:
#        ele["impact_rel_hi"] = ele["impact_hi"] / ((POI_fit[2] - POI_fit[1]) if ele["impact_hi"] >= 0 else (POI_fit[1] - POI_fit[0]))
#        ele["impact_rel_lo"] = ele["impact_lo"] / ((POI_fit[2] - POI_fit[1]) if ele["impact_lo"] >= 0 else (POI_fit[1] - POI_fit[0]))
#    else:
#        ele["impact_rel_hi"] = 0.0
#        ele["impact_rel_lo"] = 0.0
#
#    if IsConstrained(ele):
#        pre = ele["prefit"]
#        fit = ele["fit"]
#        pre_err_hi = pre[2] - pre[1]
#        pre_err_lo = pre[1] - pre[0]
#        fit_err_hi = fit[2] - fit[1]
#        fit_err_lo = fit[1] - fit[0]
#        pull = CP.diffPullAsym(fit[1], pre[1], fit_err_hi, pre_err_hi, fit_err_lo, pre_err_lo)
#        ele["pull"] = pull[0]
#        # Under some conditions (very small constraint) the calculated pull is not reliable.
#        # In this case, pull[1] will have a non-zero value.
#        ele["pull_ok"] = pull[1] == 0
#        if not ele["pull_ok"]:
#            print(">> Warning, the pull for {} could not be computed".format(ele["name"]))
#        ele["constraint"] = (fit[2] - fit[0]) / (pre[2] - pre[0])
#
#        sc_fit = fit[1] - pre[1]
#        sc_fit = (sc_fit / pre_err_hi) if sc_fit >= 0 else (sc_fit / pre_err_lo)
#        sc_fit_hi = fit[2] - pre[1]
#        sc_fit_hi = (sc_fit_hi / pre_err_hi) if sc_fit_hi >= 0 else (sc_fit_hi / pre_err_lo)
#        sc_fit_hi = sc_fit_hi - sc_fit
#        sc_fit_lo = fit[0] - pre[1]
#        sc_fit_lo = (sc_fit_lo / pre_err_hi) if sc_fit_lo >= 0 else (sc_fit_lo / pre_err_lo)
#        sc_fit_lo = sc_fit - sc_fit_lo
#        ele["sc_fit"] = "{:.6f}".format(sc_fit)
#        ele["sc_fit_hi"] ="{:.6f}".format( sc_fit_hi)
#        ele["sc_fit_lo"] = "{:.6f}".format(sc_fit_lo)
#        #pre_val="{:.2f}".format(ele["prefit"][1])
#        txtfile.write(fmtstring % (fancyN[ele['name']],"{:.6f}".format(ele['impact_r']),ele["sc_fit_hi"],"1.0",ele["sc_fit_lo"]))
#        txtfile.write(" \\hline \n")
#    else:
#        # For unconstrained parameters there is no pull to define. For sorting purposes we
#        # still need to set a value, so will put it to zero
#        
#        ele["pull"] = 0
#        ele["pull_ok"] = False
#        ele["constraint"] = 9999.0
#        pre = ele["prefit"]
#        fit = ele["fit"]
#        ele["sc_fit_lo"] = "{:.6f}".format(fit[0] - pre[1])
#        ele["sc_fit_hi"] = "{:.6f}".format(fit[2] - pre[1])
#        txtfile.write(fmtstring % (fancyN[ele['name']],"{:.6f}".format(ele['impact_r']),ele["sc_fit_hi"],"1.0",ele["sc_fit_lo"]))
#        txtfile.write(" \\hline \n")

#data["params"].sort(key=lambda x: abs(x["impact_%s" % POI]), reverse=True)


def info(jsonfile):
    
    f=open(jsonfile)
    data = json.load(f)
    POIs = [ele["name"] for ele in data["POIs"]]
    POI = POIs[0]
    params=data['params']

    ranking_impact = sorted([(v['name'], 100*abs(v["impact_{}".format(POI)])) for i, v in enumerate(params)], reverse=True, key=lambda X: X[1])
    uncert_nom_poi="{:.2f}".format(100*( (1-data['POIs'][0]['fit'][0])+ (data['POIs'][0]['fit'][-1] -1))/2)
    return uncert_nom_poi,ranking_impact

uncert_nom_poi_340,ranking_impact_340=info("jobs/impacts_final_btageff9_340.json")
uncert_nom_poi_345,ranking_impact_345=info("jobs/impacts_final_btageff9_345.json")
uncert_nom_poi_365,ranking_impact_365=info("jobs/impacts_final_btageff9_365_factor5.json")


txtfile = open("table.text",'w')
fmtstring = "%-25s & %15s & %15s & %15s  \\\\"
txtfile.write("\\begin{table}[] \n \\begin{tabular}{llll}\n\n")
txtfile.write("\\multicolumn{1}{c}{\multirow{2}{*}{param}} & \multicolumn{3}{l}{impact on \#mu (\%)} \\\\ \n")
txtfile.write("\\multicolumn{1}{c}{}                       & 340         & 345         & 365         \\ \\ \n")
txtfile.write(fmtstring % ("tot. unc.",uncert_nom_poi_340,uncert_nom_poi_345,uncert_nom_poi_365))


for val in ranking_impact_345:
    
    val_340="{:.2f}".format([i[1] for i in ranking_impact_340 if i[0] == val[0]][0])
    val_365="{:.2f}".format([i[1] for i in ranking_impact_365 if i[0] == val[0]][0])
    print(fancyN[val[0]],val_340,val[1],val_365)
    txtfile.write(fmtstring % (fancyN[val[0]],val_340,"{:.2f}".format(val[1]),val_365))
    txtfile.write(" \\hline \n")


    
txtfile.write(" \\hline\n\end{tabular} \n")
txtfile.write(" \n \end{table}\n")
txtfile.close()
