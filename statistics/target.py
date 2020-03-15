import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_kddcup99

from preprocessing.preprocessing import label_list

'''
label_list = ['normal.', 'buffer_overflow.', 'loadmodule.', 'perl.', 'neptune.', 'smurf.',
                  'guess_passwd.', 'pod.', 'teardrop.', 'portsweep.', 'ipsweep.', 'land.', 'ftp_write.',
                  'back.', 'imap.', 'satan.', 'phf.', 'nmap.', 'multihop.', 'warezmaster.', 'warezclient.',
                  'spy.', 'rootkit.']
'''

if __name__ == '__main__':
    # Load the dataset
    kddcup99 = fetch_kddcup99()

    X = kddcup99['data']
    Y = kddcup99['target']

    # 2 types of data
    print('Normal samples:'.ljust(15), '{}'.format(X[Y == b'normal.'].shape[0]).rjust(6))
    print('Anomalies:'.ljust(15), '{}'.format(X[Y != b'normal.'].shape[0]).rjust(6))

    normal_count = (X[Y == b'normal.'].shape[0])
    buffer_overflow_count = X[Y == b'buffer_overflow.'].shape[0]
    loadmodule_count = X[Y == b'loadmodule.'].shape[0]
    perl_count = X[Y == b'perl.'].shape[0]
    neptune_count = X[Y == b'neptune.'].shape[0]
    smurf_count = X[Y == b'smurf.'].shape[0]
    guess_passwd_count = X[Y == b'guess_passwd.'].shape[0]
    pod_count = X[Y == b'pod.'].shape[0]
    teardrop_count = X[Y == b'teardrop.'].shape[0]
    portsweep_count = X[Y == b'portsweep.'].shape[0]
    ipsweep_count = X[Y == b'ipsweep.'].shape[0]
    land_count = X[Y == b'land.'].shape[0]
    ftp_write_count = X[Y == b'ftp_write.'].shape[0]
    back_count = X[Y == b'back.'].shape[0]
    nmap_count = X[Y == b'nmap.'].shape[0]
    imap_count = X[Y == b'imap.'].shape[0]
    satan_count = X[Y == b'satan.'].shape[0]
    phf_count = X[Y == b'phf.'].shape[0]
    multihop_count = X[Y == b'multihop.'].shape[0]
    warezmaster_count = X[Y == b'warezmaster.'].shape[0]
    warezclient_count = X[Y == b'warezclient.'].shape[0]
    spy_count = X[Y == b'spy.'].shape[0]
    rootkit_count = X[Y == b'rootkit.'].shape[0]

    # Sort of 23 attack types
    attack_nums = [normal_count, buffer_overflow_count, loadmodule_count, perl_count, neptune_count, smurf_count,
                   guess_passwd_count, pod_count, teardrop_count, portsweep_count, ipsweep_count, land_count,
                   ftp_write_count, back_count, imap_count, phf_count, satan_count, nmap_count, multihop_count,
                   warezmaster_count, warezclient_count, spy_count, rootkit_count]
    attack_labels = label_list

    attack_dict = sorted(dict(zip(attack_labels, attack_nums)).items(), key=lambda item: item[1], reverse=True)
    print('Sort of 23 attack types:')
    sorted(attack_dict, key=lambda item: item[1], reverse=True)
    print("labels".format().ljust(16), "counts".format().rjust(6))
    print("-----------------------")
    for i in attack_dict:
        print("{}".format(i[0]).ljust(16), "{}".format(i[1]).rjust(6))

    # Sort of 4 exceptions types
    PROBE_count = ipsweep_count + nmap_count + portsweep_count + satan_count
    DOS_count = back_count + land_count + neptune_count + pod_count + smurf_count + teardrop_count
    U2R_count = buffer_overflow_count + loadmodule_count + perl_count + rootkit_count
    R2L_count = ftp_write_count + guess_passwd_count + imap_count + multihop_count + phf_count + spy_count + warezclient_count + warezmaster_count

    exceptions_labels = ['PROBE', 'DOS', 'U2R', 'R2L']
    exceptions_nums = [PROBE_count, DOS_count, U2R_count, R2L_count]

    exceptions_dict = sorted(dict(zip(exceptions_labels, exceptions_nums)).items(), key=lambda item: item[1],
                             reverse=True)
    print('Sort of 4 exceptions types:')
    sorted(exceptions_dict, key=lambda item: item[1], reverse=True)
    print("labels".format().ljust(6), "counts".format().rjust(6))
    print("------------")
    for i in exceptions_dict:
        print("{}".format(i[0]).ljust(6), "{}".format(i[1]).rjust(6))
