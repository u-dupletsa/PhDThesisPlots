import numpy as np
import pandas as pd


# read output data from CLASS and output a dataframe of Cls
def read_Cls_from_class(dat_file, lmax, nz_bins, diag=False):
    file = open(dat_file, 'r')
    lines = file.readlines()
    file.close()

    if diag:
        nz_bins = nz_bins*2 - 1 

    Cls = np.zeros((lmax+1, nz_bins+1), dtype=float) # add one since first column is ell
                                                    # and we add l=0 and l=1
    # put to zero the Cls for ell=0 and ell=1
    Cls[0, :] = 0.
    Cls[1, 1:] = 0.
    Cls[1, 0] = 1.
    
    for ll in range(2, lmax + 1): # l=lmax is included
        Cls[ll, :] = np.array(lines[ll+5].split()).astype(np.float64)
        #divide by l(l+1)/(2pi) to get Cls
        Cls[ll, 1:] = Cls[ll, 1:]/(np.float64(ll)*(np.float64(ll)+1)/2/np.pi)

    # output Cls as a dataframe with columns as bins and rows as ell
    header = ['ell'] + ['z_bin'+str(i+1) for i in range(nz_bins)]
    # pay attention if diag is True the odd columns are the auto-correlations
    # and the even columns are the cross-correlations
    Cls_df = pd.DataFrame(Cls, columns=header)
    return Cls_df