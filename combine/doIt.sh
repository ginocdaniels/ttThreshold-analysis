#!/bin/bash
for ecm in  340 345 365 #340 345 365 #350 355 345 365 340
do
    for channel in semihad had #had #lep
    do
	for var in njets_R5 BDT_score singlebin  #nbjets_R5_eff_p9 jet1_R5_p jet2_R5_p jet1_R5_theta jet2_R5_theta  jet3_R5_p jet3_R5_theta jet4_R5_p jet4_R5_theta nbjets_R5_true njets_R5 lep_p lep_theta
	do
	    python plotter_withsyst.py  --vname ${var} --sel zerob  -c ${channel} -e ${ecm}
	    python plotter_withsyst.py  --vname ${var} --sel oneb   -c ${channel} -e ${ecm}
	    python plotter_withsyst.py  --vname ${var} --sel twob   -c ${channel} -e ${ecm}
	    #python plotter_withsyst_singleNP.py  --vname ${var} --sel zerob  -c ${channel} -e ${ecm}
	    #python plotter_withsyst_singleNP.py  --vname ${var} --sel oneb   -c ${channel} -e ${ecm}
	    #python plotter_withsyst_singleNP.py  --vname ${var} --sel twob   -c ${channel} -e ${ecm}

	    python plotter_v1.py   --vname ${var} --sel no_cut -p  -c ${channel} -e ${ecm}  --style norm
	    python plotter_v1.py   --vname ${var} --sel zerob  -p  -c ${channel} -e ${ecm}  --style norm
	    python plotter_v1.py   --vname ${var} --sel twob  -p  -c ${channel} -e ${ecm}   --style norm 
	    python plotter_v1.py   --vname ${var} --sel oneb  -p  -c ${channel} -e ${ecm}   --style norm
	done
    done	
done 
