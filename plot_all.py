
import uproot
import os
import matplotlib.pyplot as plt
from datetime import datetime

ecm_scan = [345, 350, 355] # List of ecm values to scan

def plot_signal_background(ecm,channel):
    infile_s = 'outputs/treemaker/WbWb/{0}/wzp6_ee_WbWb_{0}_ecm{1}.root'.format(channel,ecm)
    infile_b = 'outputs/treemaker/WbWb/{}/p8_ee_WW_ecm{}.root'.format(channel,ecm)

    tree_s = uproot.open(infile_s)["events"]
    tree_b = uproot.open(infile_b)["events"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = 'outputs/all_plots/{}_WbWb_{}_ecm{}'.format(timestamp,channel,ecm)
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    for var in tree_b.keys():
        if var == 'nlep': continue
        print(f'Plotting {var}')
        plt.hist(tree_s[var].array(), bins=50, alpha=0.5, label='WbWb', color='red', density=True)
        plt.hist(tree_b[var].array(), bins=50, alpha=0.5, label='WW', color='blue', density=True)
        plt.xlabel(var)
        plt.ylabel('Normalised distribution')
        plt.title('{} {} GeV'.format(var, ecm))
        plt.legend()
        plt.savefig('{}/{}.png'.format(outdir, var))
        plt.close()

    # to be fixed
    os.system('cp -r {} /eos/user/m/mdefranc/www/'.format(outdir))
    os.system('cp ~anmehta/public/index.php /eos/user/m/mdefranc/www/{}'.format(outdir.split('/')[-1]))


for ecm in ecm_scan:
    for channel in ['semihad','had']:
        print(f'Plotting ecm = {ecm} GeV, channel {channel}')
        plot_signal_background(ecm,channel)
        print()