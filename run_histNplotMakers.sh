#!/bin/bash
#channel=${1}; shift;
#ecm=${1}; shift;
#useflav=${1}; shift;
#usebtagged=${1}; shift;
for ecm in  350 355 345 365 340
do
    for channel in semihad had #lep
    do
	for useflav in False #True
	do
	    for usebtagged in False #True
	    do
		fnameH=histmaker_WbWb_reco_${ecm}_${channel}_usebtagged${usebtagged}_useflav${useflav}.py
		#fnameP=plots_WbWb_reco_${ecm}_${channel}_usebtagged${usebtagged}_useflav${useflav}.py
		cat histmaker_WbWb_reco.py > dummy.py
		sed -e 's/CHANNELHERE/'$channel'/g;s/ECMHERE/'$ecm'/g;s/useflavHERE/'$useflav'/g;s/usebtaggedHERE/'$usebtagged'/g' dummy.py > $fnameH
		#cat plots_WbWb_reco.py >  dummy.py
		#sed -e 's/CHANNELHERE/'$channel'/g;s/ECMHERE/'$ecm'/g;s/useflavHERE/'$useflav'/g;s/usebtaggedHERE/'$usebtagged'/g' dummy.py > $fnameP
		fccanalysis run $fnameH
		#fccanalysis plots $fnameP
		mv $fnameH jobs/
		#mv $fnameP jobs/
		#cd ../
	    done
	done
    done
done
