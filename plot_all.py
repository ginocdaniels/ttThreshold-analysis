
import uproot
import os
import matplotlib.pyplot as plt

infile = 'outputs/treemaker/WbWb/semilept/wzp6_ee_WbWb_semihad_ecm345.root'

tree = uproot.open(infile)["events"]

if not os.path.exists('outputs/all_plots'):
    os.makedirs('outputs/all_plots')

for var in tree.keys():
    print(f'Plotting {var}')
    plt.hist(tree[var].array(), bins=50)
    plt.xlabel(var)
    plt.ylabel('Counts')
    plt.title(var)
    plt.savefig(f'outputs/all_plots/{var}.png')
    plt.close()