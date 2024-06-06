
import uproot
import os
import matplotlib.pyplot as plt
from datetime import datetime

ecm_scan = [345, 350, 355] # List of ecm values to scan

def plot_signal_background(ecm):
    infile_s = 'outputs/treemaker/WbWb/semilept/wzp6_ee_WbWb_semihad_ecm{}.root'.format(ecm)
    infile_b = 'outputs/treemaker/WbWb/semilept/p8_ee_WW_ecm{}.root'.format(ecm)

    tree_s = uproot.open(infile_s)["events"]
    tree_b = uproot.open(infile_b)["events"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = 'outputs/all_plots/{}_WbWb_ecm{}'.format(timestamp,ecm)
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    for var in tree_b.keys():
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
    print(f'Plotting ecm = {ecm} GeV')
    plot_signal_background(ecm)
    print()