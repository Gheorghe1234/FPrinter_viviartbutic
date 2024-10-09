import clr

clr.AddReference(r"D:\UNISIM\PYTHON Projects\UNA_PrinterFP\RTI_driver\rti1000_new.dll")

from RTI1000 import FiscalPrinter

x = FiscalPrinter()

print(x.Connect('COM1', 9600))

print(x.OpenCashDrawer())
print(x.LineFeed())

print(x.Disconnect())

