import numpy as np
from keras.utils import to_categorical
from sklearn.datasets import kddcup99
from keras import backend as k

label_list = ['normal.', 'buffer_overflow.', 'loadmodule.', 'perl.', 'neptune.', 'smurf.',
                  'guess_passwd.', 'pod.', 'teardrop.', 'portsweep.', 'ipsweep.', 'land.', 'ftp_write.',
                  'back.', 'imap.', 'satan.', 'phf.', 'nmap.', 'multihop.', 'warezmaster.', 'warezclient.',
                  'spy.', 'rootkit.']

def preHandel_data(data_source):
    for i in range(data_source.shape[0]):
        row = data_source[i]  # 获取数据
        data[i][1] = handleProtocol(row)  # 将源文件行中3种协议类型转换成数字标识
        data[i][2] = handleService(row)  # 将源文件行中70种网络服务类型转换成数字标识
        data[i][3] = handleFlag(row)  # 将源文件行中11种网络连接状态转换成数字标识
    return data


def preHandel_target(target_data_source):
    target = target_data_source
    for i in range(target_data_source.shape[0]):
        row = target_data_source[i]
        target[i] = handleLabel(row)  # 将源文件行中23种攻击类型转换成数字标识
    return to_categorical(target)


# 定义将源文件行中3种协议类型转换成数字标识的函数
def handleProtocol(input):
    protocol_list = ['tcp', 'udp', 'icmp']
    tmp = bytes.decode(input[1])
    if tmp in protocol_list:
        return protocol_list.index(tmp)


# 定义将源文件行中70种网络服务类型转换成数字标识的函数
def handleService(input):
    service_list = ['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u',
                    'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest',
                    'hostnames',
                    'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell',
                    'ldap',
                    'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', 'netstat', 'nnsp',
                    'nntp',
                    'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i', 'remote_job', 'rje',
                    'shell',
                    'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time',
                    'urh_i', 'urp_i',
                    'uucp', 'uucp_path', 'vmnet', 'whois', 'X11', 'Z39_50']
    tmp = bytes.decode(input[2])
    if tmp in service_list:
        return service_list.index(tmp)


# 定义将源文件行中11种网络连接状态转换成数字标识的函数
def handleFlag(input):
    flag_list = ['OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH']
    tmp = bytes.decode(input[3])
    if tmp in flag_list:
        return flag_list.index(tmp)


# 定义将源文件行中攻击类型转换成数字标识的函数(训练集中共出现了22个攻击类型，而剩下的17种只在测试集中出现)
def handleLabel(label):

    tmp = bytes.decode(label)
    if tmp in label_list:
        return label_list.index(tmp)

dataset = kddcup99.fetch_kddcup99(shuffle=True)
data = dataset.data
label = dataset.target
data = preHandel_data(data)
label = preHandel_target(label)

input_data_train_set = data[0:343000]
target_data_train_set = label[0:343000]
input_data_test_set = data[343000::]
target_data_test_set = label[343000::]

if k.image_data_format() == 'channels_first':
    input_data_train_set = input_data_train_set.reshape(np.array(input_data_train_set).shape[0], 1, 41)
    input_data_test_set = input_data_test_set.reshape(np.array(input_data_test_set).shape[0], 1, 41)
    input_shape = (1, 41)
else:
    input_data_train_set = input_data_train_set.reshape(np.array(input_data_train_set).shape[0], 41, 1)
    input_data_test_set = input_data_test_set.reshape(np.array(input_data_test_set).shape[0], 41, 1)
    input_shape = (41, 1)
