from UNA_Support.config_util import *

config = CFG('setup.ini')
config.conf.add_section('Connection')
config.conf.set('Connection', 'ip', '192.168.200.21')
config.conf.set('Connection', 'port', '8000')
config.conf.set('Connection', 'pass', '1234')

config.conf.add_section('FP_TYPE_PAY')
config.conf.set('FP_TYPE_PAY', 'type_pay', '{"N":0, "P":1, "E":2, "U":3}')

config.conf.add_section('OTHER')
config.conf.set('OTHER', ';Versiune protocol datecs, [1]- <= Wtdedit 1.6.7.0, [2]- >= 1- > '
                         'Wtdedit 1.6.6.1, [3]- >= 1- > Wtdedit 1.6.7.0_old', '')
config.conf.set('OTHER', 'datecs_protocol', '1')
config.conf.set('OTHER', ';Top citire mesaj UAMenu. 1-Doar mesaj, 2-lungimea msg si dupa mesajul', '')
config.conf.set('OTHER', 'type_read_message', '1')
config.conf.set('OTHER', 'iqos_url', 'https://iqos.linella.md/api/sale/warranty')
config.conf.set('OTHER', ';Activam/Dezactivam TypeProtocol si TypeModel: 1-Activ (FpTypeProtocol_NEW, FpTypeModel_DP25); 0-Dezactivat', '')
config.conf.set('OTHER', 'datecs_type_Protocol_Model', '0')
config.conf.set('OTHER', 'len_printing_text', '42')
config.conf.set('OTHER', ';activam/dezactivam modificarea TinaFpDatecs: 1-activ, 0-dezactivat', '')
config.conf.set('OTHER', 'is_tinafpdatecs', '0')

config.conf.add_section('TinaFpDatecs')
config.conf.set('TinaFpDatecs', 'ComTCPIpAddr', '172.20.13.42')
config.conf.set('TinaFpDatecs', 'ComTCPIpPort', '3999')
config.conf.set('TinaFpDatecs', 'LogMode', '1')
config.conf.set('TinaFpDatecs', 'ComMediaType', '0')
config.conf.set('TinaFpDatecs', 'FP700_As_FP550', '0')
config.conf.set('TinaFpDatecs', 'ConvertAnsiOem', '1')
config.conf.set('TinaFpDatecs', 'InterruptCloseFiscalReceipt', '0')
config.conf.set('TinaFpDatecs', 'InterruptTotal', '0')
config.conf.set('TinaFpDatecs', 'TypeProtocol', '0')
config.conf.set('TinaFpDatecs', 'ModelAutoDetect', '0')

config.create_cfg_file()