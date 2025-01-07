import numpy as np

def get_confidence_interval(samples, params, confidence_level):
    """
    Compute the confidence intervals
    """
    confidence_level /= 100
    conf_int = {}
    for param in params:
        conf_int[param] = np.percentile(samples[param], [100 * (1 - confidence_level) / 2, 100 * (1 + confidence_level) / 2])
    
    return conf_int


def get_label(detectors_list, event, estimator, snr_thr, name_tag, additional_tag = None):
    """
    Provide fast way to create labels and retrieve file names
    """
    detectors_labels = list(detectors_list[event])
    connector = '_'
    network_lbs = detectors_labels[0]
    for j in range(1, len(detectors_labels)):
        network_lbs += connector + detectors_labels[j]
    if estimator == 'averaged':
        if name_tag == 'errors':
            if additional_tag == None:
                label = 'Errors_%s_BBH_%s_SNR%s.txt' %(network_lbs, event, snr_thr)
            else:
                label = 'Errors_%s_%s_BBH_%s_SNR%s.txt' %(network_lbs, additional_tag, event, snr_thr)
        elif name_tag == 'fishers':
            if additional_tag == None:
                label = 'fisher_matrices_%s_BBH_%s_SNR%s.npy' %(network_lbs, event, snr_thr)
            else:
                label = 'fisher_matrices_%s_%s_BBH_%s_SNR%s.npy' %(network_lbs, additional_tag, event, snr_thr)
        elif name_tag == 'inv_fishers':
            if additional_tag == None:
                label = 'inv_fisher_matrices_%s_BBH_%s_SNR%s.npy' %(network_lbs, event, snr_thr)
            else:
                label = 'inv_fisher_matrices_%s_%s_BBH_%s_SNR%s.npy' %(network_lbs, additional_tag, event, snr_thr)

    else:
        if name_tag == 'errors':
            if additional_tag == None:
                label = 'Errors_%s_%s_BBH_%s_SNR%s.txt' %(network_lbs, estimator, event, snr_thr)
            else:
                label = 'Errors_%s_%s_%s_BBH_%s_SNR%s.txt' %(network_lbs, estimator, additional_tag, event, snr_thr)
        elif name_tag == 'fishers':
            if additional_tag == None:
                label = 'fisher_matrices_%s_%s_BBH_%s_SNR%s.npy' %(network_lbs, estimator, event, snr_thr)
            else:
                label = 'fisher_matrices_%s_%s_%s_BBH_%s_SNR%s.npy' %(network_lbs, estimator, additional_tag, event, snr_thr)
        elif name_tag == 'inv_fishers':
            if additional_tag == None:
                label = 'inv_fisher_matrices_%s_%s_BBH_%s_SNR%s.npy' %(network_lbs, estimator, event, snr_thr)
            else:
                label = 'inv_fisher_matrices_%s_%s_%s_BBH_%s_SNR%s.npy' %(network_lbs, estimator, additional_tag, event, snr_thr)
    return label


def from_m1_m2_to_mChirp_q(m1, m2):
    """
    Compute the transformation from m1, m2 to mChirp, q
    """
    mChirp = (m1 * m2)**(3/5) / (m1 + m2)**(1/5)
    q = m2 / m1
    return mChirp, q



def from_mChirp_q_to_m1_m2(mChirp, q):
    """
    Compute the transformation from mChirp, q to m1, m2
    """
    m1 = mChirp * (1 + q)**(1/5) * q**(-3/5)
    m2 = mChirp * (1 + q)**(1/5) * q**(2/5)
    return m1, m2
