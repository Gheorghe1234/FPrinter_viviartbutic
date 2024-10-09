from FPrinter_Driver.FP_Tremol_ZFPLAB import *

fpt = FP_Tremol()
# fp = FP()
# # dev = fp.serverFindDevice()
# fp.serverSetDeviceSerialSettings('COM10', int(115200))
#
# print("fp.OpenReceipt")
# fp.OpenReceipt(1, "0000", Enums.OptionReceipType.Standard_fiscal_receipt, Enums.OptionFiscalRcpPrintType.Step_by_step_printing)
#
# print("fp.SellPLUwithSpecifiedVAT")
# fp.SellPLUwithSpecifiedVAT("Article", Enums.OptionVATClass.VAT_class_A, 1.2)
#
# fp.Payment(2, 1, 1, 1)
#
# print("fp.CashPayCloseReceipt")
# fp.CashPayCloseReceipt()

fpt.FindPort()
fpt.OpenPort()
# fpt.OpenFiscalBon(1, '0000')
# fpt.SellFreeEx('Prod 1 ', 'B', 3)
# fpt.PaymentEx(1, 0)
# fpt.PaymentEx(1, 1)
# fpt.PaymentEx(1, 3)
# fpt.CloseFiscalBon()
# fpt.OfficialSumsEx(1.00)
# fpt.PrintBarcode('111111111', 'H')
# fpt.PrintArticleReport('X')

code = ('205')

fpt.fiscal_receipt(code, 'server')
# fpt.ReadParameters()
print(fpt.response_text)