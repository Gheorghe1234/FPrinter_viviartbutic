from Tremol_ZFPLAB.v_1_6_.FP import FP

try:
    zfp = FP()
    zfp.serverSetDeviceTcpSettings('192.168.200.21', 8000, '1234')
    version = zfp.ReadVersion()
    res = 0
    response_text = None
    error_text = version
    print(error_text)
except Exception as fpe:
    print(fpe)

# time.sleep(15)
