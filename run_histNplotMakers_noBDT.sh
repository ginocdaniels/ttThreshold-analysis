#!/bin/bash
#channel=${1}; shift;
#ecm=${1}; shift;
#useflav=${1}; shift;
#usebtagged=${1}; shift;
for ecm in  340  345 365 #355 340
do
    for channel in semihad had #lep
    do
	fnameH=histmaker_WbWb_reco_${ecm}_${channel}_noBDT.py
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
