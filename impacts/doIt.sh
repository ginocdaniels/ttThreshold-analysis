#!/bin/bash
spl_str="final"

ecms=("345" "340") # "365") 
channels=("semihad" "had")
more="" #_factor5"
RANGE="0.95,1.05"
wp="9"

plt="/eos/user/a/anmehta/www/FCC_top/impacts_njcat_March/"
opts="    --cminDefaultMinimizerStrategy 0  --setParameterRanges norm_ww_semihad=0.99,1.01:norm_ww_had=0.995,1.005:norm_qq_had=0.995,1.005 --X-rtd MINIMIZER_MaxCalls=9999999999999 "
#--setCrossingTolerance 0.001  --X-rtd MINIMIZER_MaxCalls=5000000 --setRobustFitTolerance 0.001 --setRobustFitStrategy 2 --stepSize 0.001 --autoRange 2 "

for ecm in  "${ecms[@]}" 
do
    if [ ${ecm} == "365" ]
    then
	more="_factor5"
	 opts="   --cminDefaultMinimizerStrategy 0  --X-rtd MINIMIZER_MaxCalls=9999999999999 --setCrossingTolerance 0.000001 --setParameterRanges  norm_ww_semihad=0.9995,1.0005:norm_ww_had=0.99,1.01:norm_qq_had=0.9,1.1 " 
	 #opts="   --cminDefaultMinimizerStrategy 0  --setParameterRanges norm_ww_semihad=0.99,1.01:norm_ww_had=0.995,1.005:norm_qq_had=0.995,1.005 --X-rtd MINIMIZER_MaxCalls=9999999999999 " #norm_qq_semihad=0.9999,1.0001:
    fi

    for channel in  "${channels[@]}"
    do
	cat datacard_template_${channel}${more}.txt > dummy.txt
	dName=datacard_${channel}_btageff${wp}_${ecm}${more}
	echo "running for ${channel}_${ecm}${more}"
        sed -e 's/CHANNELNAME/'$channel'/g;s/ECM/'$ecm'/g;s/BTAG/'$wp'/g' dummy.txt > ${dName}.txt
	text2workspace.py ${dName}.txt
	fname_str=${channel}_${spl_str}_btageff${wp}_${ecm}${more}
	combine -M FitDiagnostics ${dName}.root -t -1 --expectSignal=1  --X-rtd MINIMIZER_MaxCalls=9999999999999 #--verbose 3 --robustHesse=1
	combineTool.py -M Impacts -d ${dName}.root -m 200 --rMin -1  -t -1  --expectSignal=1  --rMax 2 --robustFit 1 --doInitialFit $opts 
	combineTool.py -M Impacts -d ${dName}.root -m 200 --rMin -1  -t -1  --expectSignal=1  --rMax 2 --robustFit 1 --doFits $opts
	combineTool.py -M Impacts -d ${dName}.root -m 200 --rMin -1  -t -1  --expectSignal=1  --rMax 2 --robustFit 1 $opts -o impacts_$fname_str.json
	plotImpacts_fcc.py -i impacts_$fname_str.json -o impacts_$fname_str
	mv  impacts_$fname_str.pdf ${plt}/
	mv ${dName}.txt jobs/
    done
done




for ecm in  "${ecms[@]}"
do
    more=""
    if [ ${ecm} == "365" ]
    then
	more="_factor5"
    fi    
    cd jobs/
    dName=datacard_btageff${wp}_${ecm}${more}
    echo "running for combination ${dName}"
    combineCards.py datacard_had_btageff${wp}_${ecm}${more}.txt datacard_semihad_btageff${wp}_${ecm}${more}.txt > ${dName}.txt
    text2workspace.py ${dName}.txt
    fname_str=${spl_str}_btageff${wp}_${ecm}${more}
    combine -M FitDiagnostics ${dName}.root -t -1  --expectSignal=1 --X-rtd MINIMIZER_MaxCalls=9999999999999 # --saveShapes --saveWithUncertainties --plots #--verbose 3 --robustHesse=1
    #mv *.png /eos/user/a/anmehta/www/FCC_top/impacts_njcat_Feb/
    #echo "done FD "
    combineTool.py -M Impacts -d ${dName}.root -m 200 --rMin -1.1  -t -1  --expectSignal=1  --rMax 1.1 --robustFit 1  --doInitialFit $opts
    combineTool.py -M Impacts -d ${dName}.root -m 200 --rMin -1.1  -t -1  --expectSignal=1  --rMax 1.1 --robustFit 1  --doFits $opts
    combineTool.py -M Impacts -d ${dName}.root -m 200 --rMin -1.1  -t -1  --expectSignal=1  --rMax 1.1 --robustFit 1 $opts -o impacts_$fname_str.json
    plotImpacts_fcc.py -i impacts_$fname_str.json -o impacts_$fname_str --label-size=0.05
    mv  impacts_$fname_str.pdf ${plt}/
    cd ../
    
done

 
