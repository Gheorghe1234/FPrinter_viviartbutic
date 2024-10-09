#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tremol fiscal printer python module."""
from Tremol_ZFPLAB.v_1_6_.FP_core import FP_core
from enum import Enum
from datetime import datetime


class FP(FP_core):
    """Tremol fiscal printer python library."""

    FP_core._timestamp = 1907301150

    def ReadDailyAvailableAmounts(self):
        """
        Provide information about the amounts on hand by type of payment.\n
        """
        return __DailyAvailableAmountsRes__(*self.do("ReadDailyAvailableAmounts"))

    def PrintArticleReport(self, OptionZeroing):
        """
        Prints an article report with or without zeroing ('Z' or 'X').\n
        :param OptionZeroing: with following values: 
         - 'Z' -Zeroing 
         - 'X' - Without zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        """
        self.do("PrintArticleReport", 'OptionZeroing', OptionZeroing)

    def ReadDecimalPoint(self):
        """
        Providesi nformation about the current (the last value stored into the FM) decimal point format.\n
        :rtype: str
        """
        return self.do("ReadDecimalPoint")

    def GetGPRS_APN(self):
        """
        Provides information about device's GRPS APN.\n
        """
        return __GetGPRS_APNRes__(*self.do("GetGPRS_APN"))

    def ProgParameters(self, POSNum, OptionPrintLogo, OptionAutoOpenDrawer, OptionAutoCut, OptionExternalDispManagement, OptionEJFontType):
        """
        Programs the number of POS, printing of logo, safe box opening, display mode, cutting permission.\n
        :param POSNum: 4 symbols for number of POS in format ####\n
        :type POSNum: float\n
        :param OptionPrintLogo: 1 symbol of value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionPrintLogo: Enums.OptionPrintLogo\n
        :param OptionAutoOpenDrawer: 1 symbol of value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionAutoOpenDrawer: Enums.OptionAutoOpenDrawer\n
        :param OptionAutoCut: 1 symbol of value: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionAutoCut: Enums.OptionAutoCut\n
        :param OptionExternalDispManagement: 1 symbol of value: 
         - '1' - Manual 
         - '0' - Auto\n
        :type OptionExternalDispManagement: Enums.OptionExternalDispManagement\n
        :param OptionEJFontType: 1 symbol of value: 
         - '1' - Low Font 
         - '0' - Normal Font\n
        :type OptionEJFontType: Enums.OptionEJFontType\n
        """
        self.do("ProgParameters", 'POSNum', POSNum, 'OptionPrintLogo', OptionPrintLogo, 'OptionAutoOpenDrawer', OptionAutoOpenDrawer, 'OptionAutoCut', OptionAutoCut, 'OptionExternalDispManagement', OptionExternalDispManagement, 'OptionEJFontType', OptionEJFontType)

    def GetTCPWiFiNetworkName(self):
        """
        Provides information about WiFi network name where the device is connected.\n
        """
        return __GetTCPWiFiNetworkNameRes__(*self.do("GetTCPWiFiNetworkName"))

    def SetBluetoothStatus(self, OptionBTstatus):
        """
        Program device's Bluetooth module to be enabled or disabled. To apply use -SaveNetworkSettings()\n
        :param OptionBTstatus: 1 symbol with value: 
         - '0' - Disabled 
         - '1' - Enabled\n
        :type OptionBTstatus: Enums.OptionBTstatus\n
        """
        self.do("SetBluetoothStatus", 'OptionBTstatus', OptionBTstatus)

    def GetBluetoothStatus(self):
        """
        Providing information about if the device's Bluetooth module is enabled or disabled.\n
        :rtype: Enums.OptionBTstatus
        """
        return self.do("GetBluetoothStatus")

    def StartWiFiTest(self):
        """
        Start WiFi test on the device and print out the result\n
        """
        self.do("StartWiFiTest")

    def StornoPLU(self, NamePLU, OptionVATClass, Price, Quantity=None, DiscAddP=None, DiscAddV=None):
        """
        Register storno of the article with name, price, quantity, VAT Class, and discount/addition over the transaction.\n
        :param NamePLU: 36 symbols for article's name included separator for MU=80h or\n
        :type NamePLU: str\n
        :param OptionVATClass: 1 symbol for article's VAT Class with optional values: 
         - 'A' - VAT class A 
         - 'B' - VAT class B 
         - 'C' - VAT class C 
         - 'D' - VAT class D 
         - 'E' - VAT class E 
         - 'F' - VAT class F 
         - 'G' - VAT class G 
         - 'H' - VAT class H 
        - 'I' - VAT class I\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: 1 to 10 digits for price, for negative value put minus sign '-'\n
        :type Price: float\n
        :param Quantity: 1 to 10 digits for sold quantity\n
        :type Quantity: float\n
        :param DiscAddP: 2 to 7 characters percentage value of the 
        Discount or Addition - must be 0\n
        :type DiscAddP: float\n
        :param DiscAddV: 2 to 8 symbols for value of discount/addition\n
        :type DiscAddV: float\n
        """
        self.do("StornoPLU", 'NamePLU', NamePLU, 'OptionVATClass', OptionVATClass, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV)

    def ReadDepartment(self, DepNum):
        """
        Provides information for the programmed data, the turnover from the stated department number\n
        :param DepNum: 2 symbols for deparment number in format: ##\n
        :type DepNum: float\n
        """
        return __DepartmentRes__(*self.do("ReadDepartment", 'DepNum', DepNum))

    def ReadLastReceiptNum(self):
        """
        Read the total counter of last issued receipt.\n
        :rtype: float
        """
        return self.do("ReadLastReceiptNum")

    def ReadEJByReceiptNum(self, StartRcpNum, EndRcpNum):
        """
        Reading Electronic Journal Report from receipt number to receipt number.\n
        :param StartRcpNum: 5 symbols for initial receipt number included in report, format #####\n
        :type StartRcpNum: float\n
        :param EndRcpNum: 5 symbols for final receipt number included in report, format #####\n
        :type EndRcpNum: float\n
        """
        self.do("ReadEJByReceiptNum", 'StartRcpNum', StartRcpNum, 'EndRcpNum', EndRcpNum)

    def ProgPLUgeneral(self, PLUNum, Name, Price, OptionPrice, OptionVATClass, BelongToDepNum, OptionTransaction=None):
        """
        Programs internal database items.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param Name: 36 symbols for article name; Symbol for LF=7Ch - '|'; separator for 
        MU=80h or 60h followed up to 3 symbols for unit.\n
        :type Name: str\n
        :param Price: 1 to 10 symbols for article price\n
        :type Price: float\n
        :param OptionPrice: 1 byte for Price flag with next value: 
         - '0'- Free price is disable /valid only programmed price/ 
         - '1'- Free price is enable 
         - '2'- Limited price\n
        :type OptionPrice: Enums.OptionPrice\n
        :param OptionVATClass: 1 symbol for article VAT class: 
         - 'A' - VAT class A 
         - 'B' - VAT class B 
         - 'C' - VAT class C 
         - 'D' - VAT class D 
         - 'E' - VAT class E 
         - 'F' - VAT class F 
         - 'G' - VAT class G 
         - 'H' - VAT class H 
         - 'I' - VAT class I\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param BelongToDepNum: BelongToDepNo + 80h. 1 symbol for article department attachment, 
        formed in the following manner: example: Dep01 = 81h, Dep02 =\n
        :type BelongToDepNum: float\n
        :param OptionTransaction: 1 symbol with value: 
         - '1' - Active Single transaction in receipt 
         - '0' - Inactive /default value/  
        Note: this parameter is not obligatory\n
        :type OptionTransaction: Enums.OptionTransaction\n
        """
        self.do("ProgPLUgeneral", 'PLUNum', PLUNum, 'Name', Name, 'Price', Price, 'OptionPrice', OptionPrice, 'OptionVATClass', OptionVATClass, 'BelongToDepNum', BelongToDepNum, 'OptionTransaction', OptionTransaction)

    def PrintEJ(self):
        """
        Reading/Printing all Electronic Journal report.\n
        """
        self.do("PrintEJ")

    def GetTCPAutoStartFlag(self):
        """
        Provides information about if the TCP connection autostart when the device enter in Line/Sale mode.\n
        :rtype: Enums.OptionTCPAutoStart
        """
        return self.do("GetTCPAutoStartFlag")

    def SetTCPpassword(self, PassLength, Password):
        """
        Program device's TCP password. To apply use - SaveNetworkSettings()\n
        :param PassLength: Up to 3 symbols for the password len\n
        :type PassLength: float\n
        :param Password: Up to 100 symbols for the TCP password\n
        :type Password: str\n
        """
        self.do("SetTCPpassword", 'PassLength', PassLength, 'Password', Password)

    def GetIdleTimeout(self):
        """
        Provides information about device's idle timeout. This timeout is seconds in which the connection will be closed when there is an inactivity. This information is available if the device has LAN or WiFi. Maximal value - 7200, minimal value 1. 0 is for never close the connection.\n
        :rtype: float
        """
        return self.do("GetIdleTimeout")

    def SellPLUFromFD_DB(self, OptionSign, PLUNum, Quantity=None, DiscAddP=None, DiscAddV=None):
        """
        Registers the sale or correction of a specified quantity of an article of the internal database of the FD.\n
        :param OptionSign: 1 symbol with optional value: 
         - '+' -Sale 
         - '-' - Correction\n
        :type OptionSign: Enums.OptionSign\n
        :param PLUNum: 5 symbols for PLU number of FD database in format #####\n
        :type PLUNum: float\n
        :param Quantity: 1..10 symbols for article's quantity sold\n
        :type Quantity: float\n
        :param DiscAddP: 2 to 7 for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 2 to 8 symbolsfor percentage of discount/addition (with\n
        :type DiscAddV: float\n
        """
        self.do("SellPLUFromFD_DB", 'OptionSign', OptionSign, 'PLUNum', PLUNum, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV)

    def GetTCPpassword(self):
        """
        Provides information about device's TCP password.\n
        """
        return __GetTCPpasswordRes__(*self.do("GetTCPpassword"))

    def ReadDateTime(self):
        """
        Provide information about the current date and time.\n
        :rtype: datetime
        """
        return self.do("ReadDateTime")

    def PayExactSum(self, OptionPaymentType):
        """
        Register the payment in the receipt with specified type of payment and exact amount received.\n
        :param OptionPaymentType: 1 symbol for payment type: 
         - '0' - Payment 0 
         - '1' - Payment 1 
         - '2' - Payment 2 
         - '3' - Payment 3 
         - '4' - Payment 4 
         - '5' - Payment 5 
         - '6' - Payment 6\n
        :type OptionPaymentType: Enums.OptionPaymentType\n
        """
        self.do("PayExactSum", 'OptionPaymentType', OptionPaymentType)

    def ReadFMfreeRecords(self):
        """
        Read the number of the remaining free records for Z-report in the Fiscal Memory.\n
        :rtype: str
        """
        return self.do("ReadFMfreeRecords")

    def CancelReceipt(self):
        """
        Available only if receipt is not closed. Void all sales in receipt and close the fiscal receipt. If payment is started, then finish payment and close the receipt.\n
        """
        self.do("CancelReceipt")

    def PrintSpecialEventsFMreport(self):
        """
        Print all special FM events report.\n
        """
        self.do("PrintSpecialEventsFMreport")

    def SetBluetoothPassword(self, PassLength, Password):
        """
        Program device's Bluetooth password. To apply use - SaveNetworkSettings()\n
        :param PassLength: Up to 3 symbols for the BT password len\n
        :type PassLength: float\n
        :param Password: Up to 100 symbols for the BT password\n
        :type Password: str\n
        """
        self.do("SetBluetoothPassword", 'PassLength', PassLength, 'Password', Password)

    def ReadVATname(self):
        """
        Provide information about the contents of the VAT Name.\n
        :rtype: str
        """
        return self.do("ReadVATname")

    def ProgOperator(self, Number, Name, Password):
        """
        Programs the operator's name and password.\n
        :param Number: Symbols from '1' to '20' corresponding to operator's number\n
        :type Number: float\n
        :param Name: 20 symbols for operator's name\n
        :type Name: str\n
        :param Password: 4 symbols for operator's password\n
        :type Password: str\n
        """
        self.do("ProgOperator", 'Number', Number, 'Name', Name, 'Password', Password)

    def SetGPRSUserName(self, gprsUserNameLength, Username):
        """
        Program device's GPRS user name. To apply use - SaveNetworkSettings()\n
        :param gprsUserNameLength: Up to 3 symbols for the username len\n
        :type gprsUserNameLength: float\n
        :param Username: Up to 100 symbols for the device's GPRS username\n
        :type Username: str\n
        """
        self.do("SetGPRSUserName", 'gprsUserNameLength', gprsUserNameLength, 'Username', Username)

    def ReadPLUqty(self, PLUNum):
        """
        Provides information about the quantity registers of the specified article.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
        :type PLUNum: float\n
        """
        return __PLUqtyRes__(*self.do("ReadPLUqty", 'PLUNum', PLUNum))

    def DisplayText2(self, Text):
        """
        Shows a 20-symbol text in the lower display line.\n
        :param Text: 20 symbols text\n
        :type Text: str\n
        """
        self.do("DisplayText2", 'Text', Text)

    def ScanAndPrintWiFiNetworks(self):
        """
        The device scan and print out the list of available WiFi networks.\n
        """
        self.do("ScanAndPrintWiFiNetworks")

    def ReadSerialAndFiscalNums(self):
        """
        Provides information about the manufactoring number of the fiscal device.\n
        """
        return __SerialAndFiscalNumsRes__(*self.do("ReadSerialAndFiscalNums"))

    def ReceivedOnAccount_PaidOut(self, OperNum, Password, OptionPaymentType, Amount, Text=None):
        """
        Received amount (RA)/ paid out amount (PO) with sign '-' in the specified type of payment assigned to the specified operator.\n
        :param OperNum: Symbols from 1 to 20in format ## 
        corresponding to the operator's number\n
        :type OperNum: float\n
        :param Password: 4 symbols for operator's password\n
        :type Password: str\n
        :param OptionPaymentType: 1 symbol for payment type: 
         - '0' - Payment 0 
         - '1' - Payment 1 
         - '2' - Payment 2 
         - '3' - Payment 3 
         - '4' - Payment 4 
         - '5' - Payment 5 
         - '6' - Payment 6\n
        :type OptionPaymentType: Enums.OptionPaymentType\n
        :param Amount: 1 to 10 symbols for the amount lodged/withdrawn\n
        :type Amount: float\n
        :param Text: Text - 34 bytes\n
        :type Text: str\n
        """
        self.do("ReceivedOnAccount_PaidOut", 'OperNum', OperNum, 'Password', Password, 'OptionPaymentType', OptionPaymentType, 'Amount', Amount, 'Text', Text)

    def SaveNetworkSettings(self):
        """
        After every change on Idle timeout, LAN/WiFi/GPRS usage, LAN/WiFi/TCP/GPRS password or TCP auto start networks settings this Save command needs to be execute.\n
        """
        self.do("SaveNetworkSettings")

    def DirectCommand(self, Input):
        """
        Executes the direct command .\n
        :param Input: Raw request to FP\n
        :type Input: str\n
        :rtype: str
        """
        return self.do("DirectCommand", 'Input', Input)

    def ReadEJByZBlocks(self, StartZNum, EndZNum):
        """
        Reading Electronic Journal Report from report number to report number.\n
        :param StartZNum: 4 symbols for initial number report in format ####\n
        :type StartZNum: float\n
        :param EndZNum: 4 symbols for final number report in format ####\n
        :type EndZNum: float\n
        """
        self.do("ReadEJByZBlocks", 'StartZNum', StartZNum, 'EndZNum', EndZNum)

    def GetDeviceTCP_Addresses(self, OptionAddressType):
        """
        Provides information about device's network IP address, subnet mask, gateway address, DNS address.\n
        :param OptionAddressType: 1 symbol with value: 
         - '2' - IP address 
         - '3' - Subnet Mask 
         - '4' - Gateway address 
         - '5' - DNS address\n
        :type OptionAddressType: Enums.OptionAddressType\n
        """
        return __GetDeviceTCP_AddressesRes__(*self.do("GetDeviceTCP_Addresses", 'OptionAddressType', OptionAddressType))

    def SetTCPWiFiPassword(self, PassLength, Password):
        """
        Program device's TCP WiFi password where it will be connected. To apply use -SaveNetworkSettings()\n
        :param PassLength: Up to 3 symbols for the WiFi password len\n
        :type PassLength: float\n
        :param Password: Up to 100 symbols for the device's WiFi password\n
        :type Password: str\n
        """
        self.do("SetTCPWiFiPassword", 'PassLength', PassLength, 'Password', Password)

    def SetTCPAutoStartFlag(self, OptionTCPAutoStart):
        """
        Program device's autostart TCP conection in sale/line mode. To apply use -SaveNetworkSettings()\n
        :param OptionTCPAutoStart: 1 symbol with value: 
         - '0' - No 
         - '1' - Yes\n
        :type OptionTCPAutoStart: Enums.OptionTCPAutoStart\n
        """
        self.do("SetTCPAutoStartFlag", 'OptionTCPAutoStart', OptionTCPAutoStart)

    def ProgCustomerData(self, CustomerNum, VATNumber, CustomerCompanyName, Address, FreeLine1, FreeLine2, FreeLine3, FreeLine4):
        """
        Programs the customer DB for special customer receipt issuing.\n
        :param CustomerNum: 3 symbols for customer number in order in format ###\n
        :type CustomerNum: float\n
        :param VATNumber: 15 symbols for customer VAT registration number\n
        :type VATNumber: str\n
        :param CustomerCompanyName: 30 symbols for customer name\n
        :type CustomerCompanyName: str\n
        :param Address: 30 symbols for address on customer\n
        :type Address: str\n
        :param FreeLine1: 20 ASCII symbols for customer data\n
        :type FreeLine1: str\n
        :param FreeLine2: 20 ASCII symbols for customer data\n
        :type FreeLine2: str\n
        :param FreeLine3: 20 ASCII symbols for customer data\n
        :type FreeLine3: str\n
        :param FreeLine4: 20 ASCII symbols for customer data\n
        :type FreeLine4: str\n
        """
        self.do("ProgCustomerData", 'CustomerNum', CustomerNum, 'VATNumber', VATNumber, 'CustomerCompanyName', CustomerCompanyName, 'Address', Address, 'FreeLine1', FreeLine1, 'FreeLine2', FreeLine2, 'FreeLine3', FreeLine3, 'FreeLine4', FreeLine4)

    def SellPLUwithSpecifiedVAT(self, NamePLU, OptionVATClass, Price, Quantity=None, DiscAddP=None, DiscAddV=None, NamePLUextension=None):
        """
        Register the sale or correction of article with specified name, price, quantity, VAT group and/or discount/addition on the transaction.\n
        :param NamePLU: 36 symbols for article's name\n
        :type NamePLU: str\n
        :param OptionVATClass: 1 symbol for article's VAT Class with optional values: 
         - 'A' - VAT class A 
         - 'B' - VAT class B 
         - 'C' - VAT class C 
         - 'D' - VAT class D 
         - 'E' - VAT class E 
         - 'F' - VAT class F 
         - 'G' - VAT class G 
         - 'H' - VAT class H 
         - 'I' - VAT class I\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param DiscAddP: 2 to 7 symbols for percentage of discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 2 to8 symbols for value of discount/addition\n
        :type DiscAddV: float\n
        :param NamePLUextension: 10 symbols for extension of the PLU Name: FP 
        Only\n
        :type NamePLUextension: str\n
        """
        self.do("SellPLUwithSpecifiedVAT", 'NamePLU', NamePLU, 'OptionVATClass', OptionVATClass, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'NamePLUextension', NamePLUextension)

    def PrintBriefFMReportByDate(self, StartRepFromDate, EndRepFromDate):
        """
        Print a brief FM report by initial and end date.\n
        :param StartRepFromDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartRepFromDate: datetime\n
        :param EndRepFromDate: 6 symbols for final date in the DDMMYY format\n
        :type EndRepFromDate: datetime\n
        """
        self.do("PrintBriefFMReportByDate", 'StartRepFromDate', StartRepFromDate, 'EndRepFromDate', EndRepFromDate)

    def ReadVATrates(self):
        """
        Read the current VAT rates (the last values stored into the FM).\n
        """
        return __VATratesRes__(*self.do("ReadVATrates"))

    def ReadOperatorNameAndPassword(self, Number):
        """
        Provide information about operators name and password.\n
        :param Number: Symbols from 1 to 20 corresponding to the number of 
        operator\n
        :type Number: float\n
        """
        return __OperatorNameAndPasswordRes__(*self.do("ReadOperatorNameAndPassword", 'Number', Number))

    def ReadOperPO(self, OpNo):
        """
        Provides information about the PO by type of payment as well as the total number of operations by specified operator\n
        :param OpNo: Symbol from 1 to 20 corresponding to operator's number\n
        :type OpNo: float\n
        """
        return __OperPORes__(*self.do("ReadOperPO", 'OpNo', OpNo))

    def SetTCPactiveModule(self, OptionUsedModule):
        """
        Selects the active communication module - LAN or WiFi. This option can be set only if the device has both modules at the same time. To apply use - SaveNetworkSettings()\n
        :param OptionUsedModule: 1 symbol with value: 
         - '1' - LAN module 
         - '2' - WiFi module\n
        :type OptionUsedModule: Enums.OptionUsedModule\n
        """
        self.do("SetTCPactiveModule", 'OptionUsedModule', OptionUsedModule)

    def ProgPLUqty(self, PLUNum, AvailableQuantity, OptionQuantityType):
        """
        Program the available quantity for a certain article (item) from the internal database.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param AvailableQuantity: 1..11 symbols for quantity in stock\n
        :type AvailableQuantity: float\n
        :param OptionQuantityType: 1 byte for Quantity flag with next value: 
         - '0'- for availability of PLU stock is not monitored 
         - '1'- for disable negative quantity 
         - '2'- for enable negative quantity\n
        :type OptionQuantityType: Enums.OptionQuantityType\n
        """
        self.do("ProgPLUqty", 'PLUNum', PLUNum, 'AvailableQuantity', AvailableQuantity, 'OptionQuantityType', OptionQuantityType)

    def ProgVATNum(self, VATname):
        """
        Program the contents of the VAT Name.\n
        :param VATname: 8 symbols for VAT Number\n
        :type VATname: str\n
        """
        self.do("ProgVATNum", 'VATname', VATname)

    def ClearDisplay(self):
        """
        Clears the display.\n
        """
        self.do("ClearDisplay")

    def SetSerialNumer(self, Password, SerialNum):
        """
        Stores the Manufacturing number into the operative memory.\n
        :param Password: 6-symbol string\n
        :type Password: str\n
        :param SerialNum: 12 symbol Manufacturing number\n
        :type SerialNum: str\n
        """
        self.do("SetSerialNumer", 'Password', Password, 'SerialNum', SerialNum)

    def SetGPRS_APN(self, gprsAPNlength, APN):
        """
        Program device's GPRS APN. To apply use - SaveNetworkSettings()\n
        :param gprsAPNlength: Up to 3 symbols for the APN len\n
        :type gprsAPNlength: float\n
        :param APN: Up to 100 symbols for the device's GPRS APN\n
        :type APN: str\n
        """
        self.do("SetGPRS_APN", 'gprsAPNlength', gprsAPNlength, 'APN', APN)

    def GetTCP_DHCPenabled(self):
        """
        Provides information about device's DHCP status\n
        :rtype: Enums.OptionDHCPEnabled
        """
        return self.do("GetTCP_DHCPenabled")

    def ReadDailyPObyOperator(self, OperNum):
        """
        Provides information about the amounts received from sales by type of payment and specified operator.\n
        :param OperNum: Symbol from 1 to 20 corresponding to operator's number\n
        :type OperNum: float\n
        """
        return __DailyPObyOperatorRes__(*self.do("ReadDailyPObyOperator", 'OperNum', OperNum))

    def PrintEJByRcpNum(self, StartRcpNum, EndRcpNum, FlagsTypeRec=None):
        """
        Printing Electronic Journal Report from receipt number to receipt number.\n
        :param StartRcpNum: 5 symbols for initial receipt number included in report, format #####\n
        :type StartRcpNum: float\n
        :param EndRcpNum: 5 symbols for final receipt number included in report, format #####\n
        :type EndRcpNum: float\n
        :param FlagsTypeRec: 1 optional byte with flag for type of included receipts as follows: 
        Flags.0 = 0 
        Flags.1 = 0 
        Flags.2 = 0 
        Flags.3 =1 For included non-fiscal receipts, 0= for not included 
        Flags.4 =1 For included Z daily reports, 0= for not included 
        Flags.5 = 0 
        Flags.6 = 1 For included fiscal sales receipts, 0= for not included  
        Flags.7 = 0\n
        :type FlagsTypeRec: str\n
        """
        self.do("PrintEJByRcpNum", 'StartRcpNum', StartRcpNum, 'EndRcpNum', EndRcpNum, 'FlagsTypeRec', FlagsTypeRec)

    def ProgPLUprice(self, PLUNum, Price, OptionPrice):
        """
        Program the price for a certain article (item) from the internal database.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param Price: 1 to 10 symbols for article price\n
        :type Price: float\n
        :param OptionPrice: 1 byte for Price flag with next value: 
         - '0'- Free price is disable /valid only programmed price/ 
         - '1'- Free price is enable 
         - '2'- Limited price\n
        :type OptionPrice: Enums.OptionPrice\n
        """
        self.do("ProgPLUprice", 'PLUNum', PLUNum, 'Price', Price, 'OptionPrice', OptionPrice)

    def RawRead(self, Count, EndChar):
        """
         Reads raw bytes from FP.\n
        :param Count: How many bytes to read if EndChar is not specified\n
        :type Count: float\n
        :param EndChar: The character marking the end of the data. If present Count parameter is ignored.\n
        :type EndChar: str\n
        :rtype: bytearray
        """
        return self.do("RawRead", 'Count', Count, 'EndChar', EndChar)

    def SetTCPWiFiNetworkName(self, WiFiNameLength, WiFiNetworkName):
        """
        Program device's TCP WiFi network name where it will be connected. To apply use -SaveNetworkSettings()\n
        :param WiFiNameLength: Up to 3 symbols for the WiFi network name len\n
        :type WiFiNameLength: float\n
        :param WiFiNetworkName: Up to 100 symbols for the device's WiFi ssid network name\n
        :type WiFiNetworkName: str\n
        """
        self.do("SetTCPWiFiNetworkName", 'WiFiNameLength', WiFiNameLength, 'WiFiNetworkName', WiFiNetworkName)

    def ProgHeader(self, OptionHeaderLine, HeaderText):
        """
        Program the contents of a header lines.\n
        :param OptionHeaderLine: 1 symbol with value: 
         - '1' - Header 1 
         - '2' - Header 2 
         - '3' - Header 3 
         - '4' - Header 4 
         - '5' - Header 5 
         - '6' - Header 6 
         - '7' - Header 7\n
        :type OptionHeaderLine: Enums.OptionHeaderLine\n
        :param HeaderText: TextLength symbols for header lines\n
        :type HeaderText: str\n
        """
        self.do("ProgHeader", 'OptionHeaderLine', OptionHeaderLine, 'HeaderText', HeaderText)

    def SetActiveLogoNum(self, LogoFileNumber):
        """
        Sets the number of logo file, which is active and will be printed as logo in the receipt header. Prints Information about active number.\n
        :param LogoFileNumber: 1 character value from '0' to '9' or '?'. The number sets the active file, and 
        the '?' invokes only printing of information\n
        :type LogoFileNumber: str\n
        """
        self.do("SetActiveLogoNum", 'LogoFileNumber', LogoFileNumber)

    def CloseNonFiscalReceipt(self):
        """
        Closes the non-fiscal receipt.\n
        """
        self.do("CloseNonFiscalReceipt")

    def DisplayDateTime(self):
        """
        Shows the current date and time on the display.\n
        """
        self.do("DisplayDateTime")

    def ProgDecPointPosition(self, Password, OptionDecimalPointPosition):
        """
        Stores a block containing the number format into the fiscal memory. Prints the current status on the printer.\n
        :param Password: 6-symbol string\n
        :type Password: str\n
        :param OptionDecimalPointPosition: 1 symbol with values: 
         - '0'- whole numbers 
         - '2' - fractions\n
        :type OptionDecimalPointPosition: Enums.OptionDecimalPointPosition\n
        """
        self.do("ProgDecPointPosition", 'Password', Password, 'OptionDecimalPointPosition', OptionDecimalPointPosition)

    def PaperFeed(self):
        """
        Feeds 1 line of paper.\n
        """
        self.do("PaperFeed")

    def CloseReceipt(self):
        """
        Closes the opened fiscal receipt.\n
        """
        self.do("CloseReceipt")

    def PrintDepartmentReport(self, OptionZeroing):
        """
        Prints departments report\n
        :param OptionZeroing: with following values: 
         - 'Z' -Zeroing 
         - 'X' - Without zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        """
        self.do("PrintDepartmentReport", 'OptionZeroing', OptionZeroing)

    def GetDeviceModuleSupport(self):
        """
        FlagsModule is a char with bits representing modules supported by the device.\n
        """
        return __GetDeviceModuleSupportRes__(*self.do("GetDeviceModuleSupport"))

    def ReadDailyCounters(self):
        """
        Provides information about the current reading of the daily-report- with-zeroing counter, the number of the last block stored in FM, the number of EJ and the date and time of the last block storage in the FM.\n
        """
        return __DailyCountersRes__(*self.do("ReadDailyCounters"))

    def SetVATAndFiscNums(self, Password, VATNo, FMNo):
        """
        Stores the VAT and Fiscal Memory number into the operative memory.\n
        :param Password: 6 symbols for access password\n
        :type Password: str\n
        :param VATNo: 15 symbol VAT number\n
        :type VATNo: str\n
        :param FMNo: 12 symbol Fiscal Memory number\n
        :type FMNo: str\n
        """
        self.do("SetVATAndFiscNums", 'Password', Password, 'VATNo', VATNo, 'FMNo', FMNo)

    def ResetOdometer(self, Password):
        """
        Reset odometer function *the command is valid for ADPOS model only.\n
        :param Password: 6 symbols for access password\n
        :type Password: str\n
        """
        self.do("ResetOdometer", 'Password', Password)

    def EraseAllPLUs(self, Password):
        """
        Programs the PLU Category for a certain article (item) from the internal database.\n
        :param Password: 6 symbols for password\n
        :type Password: str\n
        """
        self.do("EraseAllPLUs", 'Password', Password)

    def ConfirmFiscalization(self, Password):
        """
        Store VAT and Fiscal Memory numbers into the Fiscal memory.\n
        :param Password: 6-symbols string\n
        :type Password: str\n
        """
        self.do("ConfirmFiscalization", 'Password', Password)

    def ReadDailyRAbyOperator(self, OperNum):
        """
        Provides information about the RA by type of payment as well as the total number of operations by specified operator.\n
        :param OperNum: Symbol from 1 to 20 corresponding to operator's number\n
        :type OperNum: float\n
        """
        return __DailyRAbyOperatorRes__(*self.do("ReadDailyRAbyOperator", 'OperNum', OperNum))

    def ReadOdometer(self):
        """
        Read odometer result.  *the command is valid for ADPOS model only.\n
        :rtype: float
        """
        return self.do("ReadOdometer")

    def ReadHeader(self, OptionHeaderLine):
        """
        Provide information about the contents of a header lines.\n
        :param OptionHeaderLine: 1 symbol with value: 
         - '1' - Header 1 
         - '2' - Header 2 
         - '3' - Header 3 
         - '4' - Header 4 
         - '5' - Header 5 
         - '6' - Header 6 
         - '7' - Header 7\n
        :type OptionHeaderLine: Enums.OptionHeaderLine\n
        """
        return __HeaderRes__(*self.do("ReadHeader", 'OptionHeaderLine', OptionHeaderLine))

    def CutPaper(self):
        """
        Start paper cutter. The command works only in fiscal printer devices.\n
        """
        self.do("CutPaper")

    def ProgDisplayGreeting(self, DisplayGreetingText):
        """
        Program the contents of a Display Greeting message.\n
        :param DisplayGreetingText: 20 symbols for display greeting message\n
        :type DisplayGreetingText: str\n
        """
        self.do("ProgDisplayGreeting", 'DisplayGreetingText', DisplayGreetingText)

    def SetGPRSpassword(self, PassLength, Password):
        """
        Program device's GPRS password. To apply use - SaveNetworkSettings()\n
        :param PassLength: Up to 3 symbols for the GPRS password len\n
        :type PassLength: float\n
        :param Password: Up to 100 symbols for the device's GPRS password\n
        :type Password: str\n
        """
        self.do("SetGPRSpassword", 'PassLength', PassLength, 'Password', Password)

    def ProgPLUbarcode(self, PLUNum, Barcode):
        """
        Program the Barcode number for a certain article (item) from the internal database.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param Barcode: 13 symbols for barcode\n
        :type Barcode: str\n
        """
        self.do("ProgPLUbarcode", 'PLUNum', PLUNum, 'Barcode', Barcode)

    def PrintDetailedFMReportByDate(self, StartRepFromDate, EndRepFromDate):
        """
        Prints a detailed FM report by initial and end date.\n
        :param StartRepFromDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartRepFromDate: datetime\n
        :param EndRepFromDate: 6 symbols for final date in the DDMMYY format\n
        :type EndRepFromDate: datetime\n
        """
        self.do("PrintDetailedFMReportByDate", 'StartRepFromDate', StartRepFromDate, 'EndRepFromDate', EndRepFromDate)

    def GetGPRSsignal(self):
        """
        Providing information about device's GPRS user name.\n
        :rtype: str
        """
        return self.do("GetGPRSsignal")

    def ReadCustomerData(self, CustomerNum):
        """
        Provide information for specified customer from FD database.\n
        :param CustomerNum: 4 symbols for customer number in order in format ####\n
        :type CustomerNum: float\n
        """
        return __CustomerDataRes__(*self.do("ReadCustomerData", 'CustomerNum', CustomerNum))

    def ReadCurrentReceiptInfo(self):
        """
        Read the current status of the receipt.\n
        """
        return __CurrentReceiptInfoRes__(*self.do("ReadCurrentReceiptInfo"))

    def ReadEJ(self):
        """
        Reading all Electronic Journal report.\n
        """
        self.do("ReadEJ")

    def Payment(self, OptionPaymentType, OptionChange, Amount, OptionChangeType=None):
        """
        Register the payment in the receipt with specified type of payment and amount received (if the payment type is 0-5 the amount of change due is not obligatory.)\n
        :param OptionPaymentType: 1 symbol for payment type: 
         - '0' - Payment 0 
         - '1' - Payment 1 
         - '2' - Payment 2 
         - '3' - Payment 3 
         - '4' - Payment 4 
         - '5' - Payment 5 
         - '6' - Payment 6\n
        :type OptionPaymentType: Enums.OptionPaymentType\n
        :param OptionChange: 1 symbol with value: 
         - '0 - With Change default 
         - '1' - Without Change\n
        :type OptionChange: Enums.OptionChange\n
        :param Amount: 1 to 10 characters for received amount\n
        :type Amount: float\n
        :param OptionChangeType: 1 symbols with value: 
         - '0' - Change In Cash 
         - '1' - Same As The payment\n
        :type OptionChangeType: Enums.OptionChangeType\n
        """
        self.do("Payment", 'OptionPaymentType', OptionPaymentType, 'OptionChange', OptionChange, 'Amount', Amount, 'OptionChangeType', OptionChangeType)

    def ReadFMcontent(self):
        """
        Provides consequently information about every single block stored in the FM starting with ACKs and ending with end message.\n
        """
        self.do("ReadFMcontent")

    def SetDeviceTCP_Addresses(self, OptionAddressType, DeviceAddress):
        """
        Program device's network IP address, subnet mask, gateway address, DNS address. To apply use -SaveNetworkSettings()\n
        :param OptionAddressType: 1 symbol with value: 
         - '2' - IP address 
         - '3' - Subnet Mask 
         - '4' - Gateway address 
         - '5' - DNS address\n
        :type OptionAddressType: Enums.OptionAddressType\n
        :param DeviceAddress: 15 symbols for the selected address\n
        :type DeviceAddress: str\n
        """
        self.do("SetDeviceTCP_Addresses", 'OptionAddressType', OptionAddressType, 'DeviceAddress', DeviceAddress)

    def ReadLastDailyReportInfo(self):
        """
        Read the date and number of the last Z-report and the last RAM reset event.\n
        """
        return __LastDailyReportInfoRes__(*self.do("ReadLastDailyReportInfo"))

    def DisplayText1(self, Text):
        """
        Shows a 20-symbol text in the upper display line.\n
        :param Text: 20 symbols text\n
        :type Text: str\n
        """
        self.do("DisplayText1", 'Text', Text)

    def PrintText(self, Text):
        """
        Prints a free text.\n
        :param Text: Free text : [printed line symbols]- 2 symbols\n
        :type Text: str\n
        """
        self.do("PrintText", 'Text', Text)

    def GetBluetoothPassword(self):
        """
        Provides information about device's Bluetooth password.\n
        """
        return __GetBluetoothPasswordRes__(*self.do("GetBluetoothPassword"))

    def PrintOperatorReport(self, OptionZeroing, Number):
        """
        Prints an operator's report for a specified operator (0 = all operators) with or without zeroing ('Z' or 'X').\n
        :param OptionZeroing: 1 symbol with following values: 
         - 'Z' -Zeroing 
         - 'X' - Without zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        :param Number: Symbols from 0 to 20 corresponding to operator's number (0 = all 
        operators)\n
        :type Number: float\n
        """
        self.do("PrintOperatorReport", 'OptionZeroing', OptionZeroing, 'Number', Number)

    def SafeBoxOpen(self):
        """
        Opens the safe box.\n
        """
        self.do("SafeBoxOpen")

    def ReadStatus(self):
        """
        Provides detailed 5-byte information about the current status of the fiscal printer.\n
        """
        return __StatusRes__(*self.do("ReadStatus"))

    def OpenReceipt(self, OperNum, OperPass, OptionReceipType=None, OptionFiscalRcpPrintType=None):
        """
        Opens a fiscal receipt assigned to the specified operator or refund receipt.\n
        :param OperNum: Up to 2 symbols from 1 to 20 corresponding to 
        operator's number\n
        :type OperNum: float\n
        :param OperPass: 4 symbols for operator's password\n
        :type OperPass: str\n
        :param OptionReceipType: 1 symbol with value: 
         - '0' - Standard fiscal receipt  
         - '1' - Refund receipt\n
        :type OptionReceipType: Enums.OptionReceipType\n
        :param OptionFiscalRcpPrintType: 1 symbol with value: 
         - '0' - Step by step printing 
         - '2' - Postponed Printing\n
        :type OptionFiscalRcpPrintType: Enums.OptionFiscalRcpPrintType\n
        """
        self.do("OpenReceipt", 'OperNum', OperNum, 'OperPass', OperPass, 'OptionReceipType', OptionReceipType, 'OptionFiscalRcpPrintType', OptionFiscalRcpPrintType)

    def SellPLUFromDep(self, NamePLU, DepNum, Price, Quantity=None, DiscAddP=None, DiscAddV=None, NamePLUextension=None):
        """
        Registers the sale or correction in this department with specified name, price, quantity, VAT group and/or discount/addition on the transaction.\n
        :param NamePLU: 36 symbols for article's name included separator for 
        MU=80h or 60h followed up to 3 symbols for unit\n
        :type NamePLU: str\n
        :param DepNum: 1 or 2 symbols for article department 
        attachment, formed in the following manner: DepNo[HEX] + 80h 
        example: Dep01 = 81h, Dep02 = 82h ... Dep19 = 93h\n
        :type DepNum: float\n
        :param Price: 1 to 10 symbols for article's price\n
        :type Price: float\n
        :param Quantity: 1 to 10 symbols for quantity\n
        :type Quantity: float\n
        :param DiscAddP: 2 to 7 symbols for percentage of 
        discount/addition\n
        :type DiscAddP: float\n
        :param DiscAddV: 2 to8 symbols for value of discount/addition\n
        :type DiscAddV: float\n
        :param NamePLUextension: 10 symbols for extension of the PLU Name: 
        FP Only\n
        :type NamePLUextension: str\n
        """
        self.do("SellPLUFromDep", 'NamePLU', NamePLU, 'DepNum', DepNum, 'Price', Price, 'Quantity', Quantity, 'DiscAddP', DiscAddP, 'DiscAddV', DiscAddV, 'NamePLUextension', NamePLUextension)

    def ProgPLUcategory(self, PLUNum, Category):
        """
        Programs the PLU Category for a certain article (item) from the internal database.\n
        :param PLUNum: 5 symbols for article number in format: #####\n
        :type PLUNum: float\n
        :param Category: Up to 7 symbols for PLU Category code in format ####.##\n
        :type Category: float\n
        """
        self.do("ProgPLUcategory", 'PLUNum', PLUNum, 'Category', Category)

    def SetDateTime(self, DateTime):
        """
        Sets the date and time and prints the current values using the RECEIPT printer.\n
        :param DateTime: Date Time parameter in format: DD-MM-YY [Space] HH:MM:SS\n
        :type DateTime: datetime\n
        """
        self.do("SetDateTime", 'DateTime', DateTime)

    def ReadPLUprice(self, PLUNum):
        """
        Provides information about the price and price type of the specified article.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
        :type PLUNum: float\n
        """
        return __PLUpriceRes__(*self.do("ReadPLUprice", 'PLUNum', PLUNum))

    def GetTCPusedModule(self):
        """
        Provides information about which module the device is in use: LAN or WiFi module. This information can be provided if the device has mounted both modules.\n
        :rtype: Enums.OptionUsedModule
        """
        return self.do("GetTCPusedModule")

    def GetGPRSpassword(self):
        """
        Provides information about device's GPRS password.\n
        """
        return __GetGPRSpasswordRes__(*self.do("GetGPRSpassword"))

    def ReadDailyCountersByOperator(self, OperNum):
        """
        Read the last operator's report number and date and time.\n
        :param OperNum: Symbols from 1 to 20 corresponding to operator's 
        number\n
        :type OperNum: float\n
        """
        return __DailyCountersByOperatorRes__(*self.do("ReadDailyCountersByOperator", 'OperNum', OperNum))

    def ReadPayments(self):
        """
        Read the all programmed Payment types.\n
        """
        return __PaymentsRes__(*self.do("ReadPayments"))

    def ProgPayment(self, OptionPaymentType, Name):
        """
        Preprogram the name of the payment type.\n
        :param OptionPaymentType: 1 symbol for payment type: 
         - '0' - Payment 0 
         - '1' - Payment 1 
         - '2' - Payment 2 
         - '3' - Payment 3 
         - '4' - Payment 4 
         - '5' - Payment 5 
         - '6' - Payment 6\n
        :type OptionPaymentType: Enums.OptionPaymentType\n
        :param Name: 10 symbols for payment type name\n
        :type Name: str\n
        """
        self.do("ProgPayment", 'OptionPaymentType', OptionPaymentType, 'Name', Name)

    def ReadVATNumber(self):
        """
        Provides information about the programmed VAT number.\n
        :rtype: str
        """
        return self.do("ReadVATNumber")

    def PrintDiagnostics(self):
        """
        Prints out a diagnostic receipt.\n
        """
        self.do("PrintDiagnostics")

    def StartGPRStest(self):
        """
        Start GPRS test on the device and print out the result\n
        """
        self.do("StartGPRStest")

    def ProgFooter(self, FooterText):
        """
        Program the contents of a footer lines.\n
        :param FooterText: TextLength symbols for footer line\n
        :type FooterText: str\n
        """
        self.do("ProgFooter", 'FooterText', FooterText)

    def GetDeviceModuleSupportByFirmware(self):
        """
        FlagsModule is a char with bits representing modules supported by the firmware\n
        """
        return __GetDeviceModuleSupportByFirmwareRes__(*self.do("GetDeviceModuleSupportByFirmware"))

    def ProgVATrates(self, Password, VATrateA, VATrateB, VATrateC, VATrateD, VATrateF, VATrateG, VATrateH, VATrateI):
        """
        Store the VAT rates into the fiscal memory.\n
        :param Password: 6-symbols string\n
        :type Password: str\n
        :param VATrateA: Value of VAT rate A from 2 to 6 symbols with format ##.##\n
        :type VATrateA: float\n
        :param VATrateB: Value of VAT rate B from 2 to 6 symbols with format ##.##\n
        :type VATrateB: float\n
        :param VATrateC: Value of VAT rate C from 2 to 6 symbols with format ##.##\n
        :type VATrateC: float\n
        :param VATrateD: Value of VAT rate D from 2 to 6 symbols with format ##.##\n
        :type VATrateD: float\n
        :param VATrateF: Value of VAT rate F from 2 to 6 symbols with format ##.##\n
        :type VATrateF: float\n
        :param VATrateG: Value of VAT rate G from 2 to 6 symbols with format ##.##\n
        :type VATrateG: float\n
        :param VATrateH: Value of VAT rate H from 2 to 6 symbols with format ##.##\n
        :type VATrateH: float\n
        :param VATrateI: Value of VAT rate I from 2 to 6 symbols with format ##.##\n
        :type VATrateI: float\n
        """
        self.do("ProgVATrates", 'Password', Password, 'VATrateA', VATrateA, 'VATrateB', VATrateB, 'VATrateC', VATrateC, 'VATrateD', VATrateD, 'VATrateF', VATrateF, 'VATrateG', VATrateG, 'VATrateH', VATrateH, 'VATrateI', VATrateI)

    def PrintBriefFMReportByZBlocks(self, StartZNum, EndZNum):
        """
        Print a brief FM report by initial and end FM report number.\n
        :param StartZNum: 4 symbols for the initial FM report number included in report, format ####\n
        :type StartZNum: float\n
        :param EndZNum: 4 symbols for the final FM report number included in report, format ####\n
        :type EndZNum: float\n
        """
        self.do("PrintBriefFMReportByZBlocks", 'StartZNum', StartZNum, 'EndZNum', EndZNum)

    def ReadEJByDate(self, StartRepFromDate, EndRepFromDate):
        """
        Reading Electronic Journal Report from Start Date to End Date.\n
        :param StartRepFromDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartRepFromDate: datetime\n
        :param EndRepFromDate: 6 symbols for final date in the DDMMYY format\n
        :type EndRepFromDate: datetime\n
        """
        self.do("ReadEJByDate", 'StartRepFromDate', StartRepFromDate, 'EndRepFromDate', EndRepFromDate)

    def ReadPLUbarcode(self, PLUNum):
        """
        Provides information about the barcode of the specified article.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format: #####\n
        :type PLUNum: float\n
        """
        return __PLUbarcodeRes__(*self.do("ReadPLUbarcode", 'PLUNum', PLUNum))

    def SetIdleTimeout(self, IdleTimeout):
        """
        Program device's idle timeout setting. Set timeout for closing the connection if there is an inactivity. Maximal value - 7200, minimal value 1. 0 is for never close the connection. This option can be used only if the device has LAN or WiFi. To apply use - SaveNetworkSettings()\n
        :param IdleTimeout: 4 symbols for Idle timeout in format ####\n
        :type IdleTimeout: float\n
        """
        self.do("SetIdleTimeout", 'IdleTimeout', IdleTimeout)

    def ReadPLU(self, PLUNum):
        """
        Provides information about the all registers of the specified article.\n
        :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
        :type PLUNum: float\n
        """
        return __PLURes__(*self.do("ReadPLU", 'PLUNum', PLUNum))

    def ProgDepartment(self, Number, Name, OptionVATClass, Price=None, OptionDepPrice=None):
        """
        Set data for the stated department number from the internal FD database.\n
        :param Number: 2 symbols for department number in format ##\n
        :type Number: float\n
        :param Name: 34 characters department name\n
        :type Name: str\n
        :param OptionVATClass: 1 symbol for article's VAT Class with optional values: 
         - 'A' - VAT class A 
         - 'B' - VAT class B 
         - 'C' - VAT class C 
         - 'D' - VAT class D 
         - 'E' - VAT class E 
         - 'F' - VAT class F 
         - 'G' - VAT class G 
         - 'H' - VAT class H 
         - 'I' - VAT class I\n
        :type OptionVATClass: Enums.OptionVATClass\n
        :param Price: 1 to 10 symbols for department price /ECR Only/\n
        :type Price: float\n
        :param OptionDepPrice: 1 symbol for Department flags with next value: 
         - '0' - Free price disabled  
         - '1' - Free price enabled  
         - '2' - Limited price 
         - '4' - Free price disabled for single transaction 
         - '5' - Free price enabled for single transaction 
         - '6' - Limited price for single transaction\n
        :type OptionDepPrice: Enums.OptionDepPrice\n
        """
        self.do("ProgDepartment", 'Number', Number, 'Name', Name, 'OptionVATClass', OptionVATClass, 'Price', Price, 'OptionDepPrice', OptionDepPrice)

    def PrintEJByZBlocks(self, StartZNum, EndZNum, FlagsTypeRec=None):
        """
        Printing Electronic Journal Report from report number to report number.\n
        :param StartZNum: 4 symbols for initial number report in format ####\n
        :type StartZNum: float\n
        :param EndZNum: 4 symbols for final number report in format ####\n
        :type EndZNum: float\n
        :param FlagsTypeRec: 1 optional byte with flag for type of included receipts as follows: 
        Flags.0 = 0 
        Flags.1 = 0 
        Flags.2 = 0 
        Flags.3 =1 For included non-fiscal receipts, 0= for not included 
        Flags.4 =1 For included Z daily reports, 0= for not included 
        Flags.5 = 0 
        Flags.6 = 1 For included fiscal sales receipts, 0= for not included  
        Flags.7 = 0\n
        :type FlagsTypeRec: str\n
        """
        self.do("PrintEJByZBlocks", 'StartZNum', StartZNum, 'EndZNum', EndZNum, 'FlagsTypeRec', FlagsTypeRec)

    def ReadVATClassAmounts(self):
        """
        Provide information about the accumulated amount by VAT group.\n
        """
        return __VATClassAmountsRes__(*self.do("ReadVATClassAmounts"))

    def PrintLogo(self, Number):
        """
        Print the programmed graphical logo with the stated number.\n
        :param Number: Number of logo to be printed. If missing prints logo with number 0\n
        :type Number: float\n
        """
        self.do("PrintLogo", 'Number', Number)

    def PrintEJByDate(self, StartRepFromDate, EndRepFromDate, FlagsTypeRec=None):
        """
        Printing Electronic Journal Report from Start Date to End Date.\n
        :param StartRepFromDate: 6 symbols for initial date in the DDMMYY format\n
        :type StartRepFromDate: datetime\n
        :param EndRepFromDate: 6 symbols for final date in the DDMMYY format\n
        :type EndRepFromDate: datetime\n
        :param FlagsTypeRec: 1 optional byte with flag for type of included receipts as follows: 
        Flags.0 = 0 
        Flags.1 = 0 
        Flags.2 = 0 
        Flags.3 = 1 For included non-fiscal receipts, 0= for not included 
        Flags.4 = 1 For included Z daily reports, 0= for not included 
        Flags.5 = 0 
        Flags.6 =1 For included fiscal sales receipts, 0= for not included 
        Flags.7 = 0\n
        :type FlagsTypeRec: str\n
        """
        self.do("PrintEJByDate", 'StartRepFromDate', StartRepFromDate, 'EndRepFromDate', EndRepFromDate, 'FlagsTypeRec', FlagsTypeRec)

    def ReadDailyGeneralRegistersByOperator(self, OperNum):
        """
        Provides information about the number of customers (number of fiscal receipt issued), number of discounts, additions and corrections made and the accumulated amounts.\n
        :param OperNum: Symbol from 1 to 20in format corresponding to operator's 
        number\n
        :type OperNum: float\n
        """
        return __DailyGeneralRegistersByOperatorRes__(*self.do("ReadDailyGeneralRegistersByOperator", 'OperNum', OperNum))

    def PrintDetailedFMReportByZBlocks(self, StartNo, EndNo):
        """
        Print a detailed FM report by initial and end FM report number.\n
        :param StartNo: 4 symbols for the initial report number included in report, format ####\n
        :type StartNo: float\n
        :param EndNo: 4 symbols for the final report number included in report, format ####\n
        :type EndNo: float\n
        """
        self.do("PrintDetailedFMReportByZBlocks", 'StartNo', StartNo, 'EndNo', EndNo)

    def GetGPRSUserName(self):
        """
        Providing information about device's GPRS user name.\n
        """
        return __GetGPRSUserNameRes__(*self.do("GetGPRSUserName"))

    def PrintDailyReport(self, OptionZeroing):
        """
        Depending on the parameter prints:   daily fiscal report with zeroing and fiscal memory record, preceded by Electronic Journal report print ('Z');  daily fiscal report without zeroing ('X');\n
        :param OptionZeroing: 1 character with following values: 
         - 'Z' - Zeroing 
         - 'X' - Without zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        """
        self.do("PrintDailyReport", 'OptionZeroing', OptionZeroing)

    def ProgExtDisplay(self, Password):
        """
        Preprograms the external display.\n
        :param Password: 6 symbols for access password\n
        :type Password: str\n
        """
        self.do("ProgExtDisplay", 'Password', Password)

    def ReadFooter(self):
        """
        Provide information about the contents of a footer line.\n
        :rtype: str
        """
        return self.do("ReadFooter")

    def StartBluetoothTest(self):
        """
        Start Bluetooth test on the device and print out the result\n
        """
        self.do("StartBluetoothTest")

    def GetTCPWiFiPassword(self):
        """
        Providing information about WiFi password where the device is connected.\n
        """
        return __GetTCPWiFiPasswordRes__(*self.do("GetTCPWiFiPassword"))

    def OpenNonFiscalReceipt(self, OperNum, OperPass):
        """
        Open a non-fiscal receipt assigned to the specified operator.\n
        :param OperNum: Symbol from 1 to 20 corresponding to operator's number\n
        :type OperNum: float\n
        :param OperPass: 4 symbols for operator's password\n
        :type OperPass: str\n
        """
        self.do("OpenNonFiscalReceipt", 'OperNum', OperNum, 'OperPass', OperPass)

    def Subtotal(self, OptionPrinting, OptionDisplay, DiscAddV=None, DiscAddP=None):
        """
        Calculate the subtotal amount with printing and display visualization options. Provide information about values of the calculated amounts. If a percent or value discount/addition has been specified the subtotal and the discount/addition value will be printed regardless the parameter for printing.\n
        :param OptionPrinting: 1 symbol withvalue: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionPrinting: Enums.OptionPrinting\n
        :param OptionDisplay: 1 symbol withvalue: 
         - '1' - Yes 
         - '0' - No\n
        :type OptionDisplay: Enums.OptionDisplay\n
        :param DiscAddV: 1 to 10 symbols for the value of the discount/addition\n
        :type DiscAddV: float\n
        :param DiscAddP: 2 to 7 symbols for the percentage value of the 
        discount/addition\n
        :type DiscAddP: float\n
        :rtype: float
        """
        return self.do("Subtotal", 'OptionPrinting', OptionPrinting, 'OptionDisplay', OptionDisplay, 'DiscAddV', DiscAddV, 'DiscAddP', DiscAddP)

    def DisplayText1and2(self, Text):
        """
        Shows a 40-symbol text in the two display lines.\n
        :param Text: 40 symbols text\n
        :type Text: str\n
        """
        self.do("DisplayText1and2", 'Text', Text)

    def SetTCP_DHCPenabled(self, OptionDHCPEnabled):
        """
        Program device's TCP network DHCP enabled or disabled. To apply use -SaveNetworkSettings()\n
        :param OptionDHCPEnabled: 1 symbol with value: 
         - '0' - Disabled 
         - '1' - Enabled\n
        :type OptionDHCPEnabled: Enums.OptionDHCPEnabled\n
        """
        self.do("SetTCP_DHCPenabled", 'OptionDHCPEnabled', OptionDHCPEnabled)

    def ReadDailyRa(self):
        """
        Provides information about the amounts received from sales by type of payment.\n
        """
        return __DailyRaRes__(*self.do("ReadDailyRa"))

    def ReadGeneralDailyRegisters(self):
        """
        Provides information about the number of customers (number of fiscal receipt issued), number of discounts, additions and corrections made and the accumulated amounts.\n
        """
        return __GeneralDailyRegistersRes__(*self.do("ReadGeneralDailyRegisters"))

    def ReadDisplayGreetingMessage(self):
        """
        Provide information about the contents of a Display Greeting message.\n
        :rtype: str
        """
        return self.do("ReadDisplayGreetingMessage")

    def StartLANtest(self):
        """
        Start LAN test on the device and print out the result\n
        """
        self.do("StartLANtest")

    def ReadParameters(self):
        """
        Provides information about the programmed number of POS and the current values of the logo, cutting permission, display mode, enable/disable currency in receipt and enable/disableUSB host mode.\n
        """
        return __ParametersRes__(*self.do("ReadParameters"))

    def ReadVersion(self):
        """
        Provides information about the device model and firmware version.\n
        :rtype: str
        """
        return self.do("ReadVersion")

    def RawWrite(self, Bytes):
        """
         Writes raw bytes to FP \n
        :param Bytes: The bytes in BASE64 ecoded string to be written to FP\n
        :type Bytes: bytearray\n
        """
        self.do("RawWrite", 'Bytes', Bytes)

    def ReadDailyReturnedChangeAmountsByOperator(self, OperNum):
        """
        Provides information about the amounts returned as change by different payment types for the specified operator.\n
        :param OperNum: Symbol from 1 to 20 corresponding to operator's number\n
        :type OperNum: float\n
        """
        return __DailyReturnedChangeAmountsByOperatorRes__(*self.do("ReadDailyReturnedChangeAmountsByOperator", 'OperNum', OperNum))

    def CashPayCloseReceipt(self):
        """
        Close the fiscal receipt, paying the due amount in cash\n
        """
        self.do("CashPayCloseReceipt")

    def ReadDailyPO(self):
        """
        Provides information about the PO amounts by type of payment and the total number of operations.\n
        """
        return __DailyPORes__(*self.do("ReadDailyPO"))

    def PrintDetailedDailyReport(self, OptionZeroing):
        """
        Prints an extended daily financial report (an article report followed by a daily financial report) with or without zeroing ('Z' or 'X').\n
        :param OptionZeroing: with following values: 
         - 'Z' -Zeroing 
         - 'X' - Without zeroing\n
        :type OptionZeroing: Enums.OptionZeroing\n
        """
        self.do("PrintDetailedDailyReport", 'OptionZeroing', OptionZeroing)


class __DailyAvailableAmountsRes__:
    """
    :param AmountPay0: 1..11 symbols for the accumulated amount of payment type 0\n
    :type AmountPay0: float\n
    :param AmountPay1: 1..11 symbols for the accumulated amount of payment type 1\n
    :type AmountPay1: float\n
    :param AmountPay2: 1..11 symbols for the accumulated amount of payment type 2\n
    :type AmountPay2: float\n
    :param AmountPay3: 1..11 symbols for the accumulated amount of payment type 3\n
    :type AmountPay3: float\n
    :param AmountPay4: 1..11 symbols for the accumulated amount of payment type 4\n
    :type AmountPay4: float\n
    :param AmountPay5: 1..11 symbols for the accumulated amount of payment type 5\n
    :type AmountPay5: float\n
    :param AmountPay6: 1..11 symbols for the accumulated amount of payment type 6\n
    :type AmountPay6: float\n
    """
    def __init__(self, AmountPay0, AmountPay1, AmountPay2, AmountPay3, AmountPay4, AmountPay5, AmountPay6):
        self.AmountPay0 = AmountPay0
        self.AmountPay1 = AmountPay1
        self.AmountPay2 = AmountPay2
        self.AmountPay3 = AmountPay3
        self.AmountPay4 = AmountPay4
        self.AmountPay5 = AmountPay5
        self.AmountPay6 = AmountPay6


class __GetGPRS_APNRes__:
    """
    :param gprsAPNlength: Up to 3 symbols for the APN length\n
    :type gprsAPNlength: float\n
    :param APN: (APN) Up to 100 symbols for the device's GPRS APN\n
    :type APN: str\n
    """
    def __init__(self, gprsAPNlength, APN):
        self.gprsAPNlength = gprsAPNlength
        self.APN = APN


class __GetTCPWiFiNetworkNameRes__:
    """
    :param WiFiNameLength: Up to 3 symbols for the WiFi name length\n
    :type WiFiNameLength: float\n
    :param WiFiNetworkName: (Name) Up to 100 symbols for the device's WiFi network name\n
    :type WiFiNetworkName: str\n
    """
    def __init__(self, WiFiNameLength, WiFiNetworkName):
        self.WiFiNameLength = WiFiNameLength
        self.WiFiNetworkName = WiFiNetworkName


class __DepartmentRes__:
    """
    :param DepNum: (Department Number) 2 symbols for department in format: 
    ##\n
    :type DepNum: str\n
    :param DepName: (Department Name) 30 symbols for department name\n
    :type DepName: str\n
    :param OptionVATClass: 1 symbol for article's VAT Class with optional values: 
     - 'A' - VAT class A 
     - 'B' - VAT class B 
     - 'C' - VAT class C 
     - 'D' - VAT class D 
     - 'E' - VAT class E 
     - 'F' - VAT class F 
     - 'G' - VAT class G 
     - 'H' - VAT class H 
     - 'I' - VAT class I\n
    :type OptionVATClass: Enums.OptionVATClass\n
    :param Turnover: 1..11 symbols for accumulated turnover of the department\n
    :type Turnover: float\n
    :param SoldQuantity: 1..11 symbols for sold quantity of the department\n
    :type SoldQuantity: float\n
    :param LastZReportNumber: 1..5 symbols for the number of last Z report\n
    :type LastZReportNumber: float\n
    :param LastZReportDate: 16 symbols for the date and time of the last article report 
    with zeroing  
    in format DD-MM-YYYY HH:MM\n
    :type LastZReportDate: datetime\n
    :param Price: 1 to 10 symbols for department price\n
    :type Price: float\n
    :param OptionDepPrice: 1 symbol for Department flags with next value: 
     - '0' - Free price disabled  
     - '1' - Free price enabled  
     - '2' - Limited price 
     - '4' - Free price disabled for single transaction 
     - '5' - Free price enabled for single transaction 
     - '6' - Limited price for single transaction\n
    :type OptionDepPrice: Enums.OptionDepPrice\n
    """
    def __init__(self, DepNum, DepName, OptionVATClass, Turnover, SoldQuantity, LastZReportNumber, LastZReportDate, Price, OptionDepPrice):
        self.DepNum = DepNum
        self.DepName = DepName
        self.OptionVATClass = OptionVATClass
        self.Turnover = Turnover
        self.SoldQuantity = SoldQuantity
        self.LastZReportNumber = LastZReportNumber
        self.LastZReportDate = LastZReportDate
        self.Price = Price
        self.OptionDepPrice = OptionDepPrice


class __GetTCPpasswordRes__:
    """
    :param PassLength: Up to 3 symbols for the password length\n
    :type PassLength: float\n
    :param Password: (Password) Up to 100 symbols for the TCP password\n
    :type Password: str\n
    """
    def __init__(self, PassLength, Password):
        self.PassLength = PassLength
        self.Password = Password


class __PLUqtyRes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
    :type PLUNum: float\n
    :param AvailableQuantity: Up to13 symbols for quantity in stock\n
    :type AvailableQuantity: float\n
    :param OptionQuantityType: 1 byte for Quantity flag with next value: 
     - '0'- for availability of PLU stock is not monitored 
     - '1'- for disable negative quantity 
     - '2'- for enable negative quantity\n
    :type OptionQuantityType: Enums.OptionQuantityType\n
    """
    def __init__(self, PLUNum, AvailableQuantity, OptionQuantityType):
        self.PLUNum = PLUNum
        self.AvailableQuantity = AvailableQuantity
        self.OptionQuantityType = OptionQuantityType


class __SerialAndFiscalNumsRes__:
    """
    :param SerialNum: 10 symbols for individual number of the fiscal device\n
    :type SerialNum: str\n
    :param FMNum: 12 symbol Fiscal Memory number\n
    :type FMNum: str\n
    """
    def __init__(self, SerialNum, FMNum):
        self.SerialNum = SerialNum
        self.FMNum = FMNum


class __GetDeviceTCP_AddressesRes__:
    """
    :param OptionAddressType: (Address type) 1 symbol with value: 
     - '2' - IP address 
     - '3' - Subnet Mask 
     - '4' - Gateway address 
     - '5' - DNS address\n
    :type OptionAddressType: Enums.OptionAddressType\n
    :param DeviceAddress: 15 symbols for the device's addresses\n
    :type DeviceAddress: str\n
    """
    def __init__(self, OptionAddressType, DeviceAddress):
        self.OptionAddressType = OptionAddressType
        self.DeviceAddress = DeviceAddress


class __VATratesRes__:
    """
    :param VATrateA: 6 symbols for VATrates of VAT class A in format ##.##%\n
    :type VATrateA: float\n
    :param VATrateB: 6 symbols for VATrates of VAT class B in format ##.##%\n
    :type VATrateB: float\n
    :param VATrateC: 6 symbols for VATrates of VAT class C in format ##.##%\n
    :type VATrateC: float\n
    :param VATrateD: 6 symbols for VATrates of VAT class D in format ##.##%\n
    :type VATrateD: float\n
    :param VATrateF: 6 symbols for VATrates of VAT class F in format ##.##%\n
    :type VATrateF: float\n
    :param VATrateG: 6 symbols for VATrates of VAT class G in format ##.##%\n
    :type VATrateG: float\n
    :param VATrateI: 6 symbols for VATrates of VAT class I in format ##.##%\n
    :type VATrateI: float\n
    """
    def __init__(self, VATrateA, VATrateB, VATrateC, VATrateD, VATrateF, VATrateG, VATrateI):
        self.VATrateA = VATrateA
        self.VATrateB = VATrateB
        self.VATrateC = VATrateC
        self.VATrateD = VATrateD
        self.VATrateF = VATrateF
        self.VATrateG = VATrateG
        self.VATrateI = VATrateI


class __OperatorNameAndPasswordRes__:
    """
    :param Number: Symbols from 1 to 20 corresponding to the number of operator\n
    :type Number: float\n
    :param Name: 20 symbols for operator's name\n
    :type Name: str\n
    :param Password: 4 symbols for operator's password\n
    :type Password: str\n
    """
    def __init__(self, Number, Name, Password):
        self.Number = Number
        self.Name = Name
        self.Password = Password


class __OperPORes__:
    """
    :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
    :type OperNum: float\n
    :param AmountPO_Payment0: Up to 13 symbols for the RA by type of payment 0\n
    :type AmountPO_Payment0: float\n
    :param AmountPO_Payment1: Up to 13 symbols for the RA by type of payment 1\n
    :type AmountPO_Payment1: float\n
    :param AmountPO_Payment2: Up to 13 symbols for the RA by type of payment 2\n
    :type AmountPO_Payment2: float\n
    :param AmountPO_Payment3: Up to 13 symbols for the RA by type of payment 3\n
    :type AmountPO_Payment3: float\n
    :param AmountPO_Payment4: Up to 13 symbols for the RA by type of payment 4\n
    :type AmountPO_Payment4: float\n
    :param AmountPO_Payment5: Up to 13 symbols for the RA by type of payment 5\n
    :type AmountPO_Payment5: float\n
    :param AmountPO_Payment6: Up to 13 symbols for the RA by type of payment 6\n
    :type AmountPO_Payment6: float\n
    :param NoPO: Up to 5 symbols for the total number of operations\n
    :type NoPO: float\n
    """
    def __init__(self, OperNum, AmountPO_Payment0, AmountPO_Payment1, AmountPO_Payment2, AmountPO_Payment3, AmountPO_Payment4, AmountPO_Payment5, AmountPO_Payment6, NoPO):
        self.OperNum = OperNum
        self.AmountPO_Payment0 = AmountPO_Payment0
        self.AmountPO_Payment1 = AmountPO_Payment1
        self.AmountPO_Payment2 = AmountPO_Payment2
        self.AmountPO_Payment3 = AmountPO_Payment3
        self.AmountPO_Payment4 = AmountPO_Payment4
        self.AmountPO_Payment5 = AmountPO_Payment5
        self.AmountPO_Payment6 = AmountPO_Payment6
        self.NoPO = NoPO


class __DailyPObyOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
    :type OperNum: float\n
    :param ReceivedSalesAmountPayment0: Up to 13 symbols for amounts received by sales for payment 0\n
    :type ReceivedSalesAmountPayment0: float\n
    :param ReceivedSalesAmountPayment1: Up to 13 symbols for amounts received by sales for payment 1\n
    :type ReceivedSalesAmountPayment1: float\n
    :param ReceivedSalesAmountPayment2: Up to 13 symbols for amounts received by sales for payment 2\n
    :type ReceivedSalesAmountPayment2: float\n
    :param ReceivedSalesAmountPayment3: Up to 13 symbols for amounts received by sales for payment 3\n
    :type ReceivedSalesAmountPayment3: float\n
    :param ReceivedSalesAmountPayment4: Up to 13 symbols for amounts received by sales for payment 4\n
    :type ReceivedSalesAmountPayment4: float\n
    :param ReceivedSalesAmountPayment5: Up to 13 symbols for amounts received by sales for payment 5\n
    :type ReceivedSalesAmountPayment5: float\n
    :param ReceivedSalesAmountPayment6: Up to 13 symbols for amounts received by sales for payment 6\n
    :type ReceivedSalesAmountPayment6: float\n
    """
    def __init__(self, OperNum, ReceivedSalesAmountPayment0, ReceivedSalesAmountPayment1, ReceivedSalesAmountPayment2, ReceivedSalesAmountPayment3, ReceivedSalesAmountPayment4, ReceivedSalesAmountPayment5, ReceivedSalesAmountPayment6):
        self.OperNum = OperNum
        self.ReceivedSalesAmountPayment0 = ReceivedSalesAmountPayment0
        self.ReceivedSalesAmountPayment1 = ReceivedSalesAmountPayment1
        self.ReceivedSalesAmountPayment2 = ReceivedSalesAmountPayment2
        self.ReceivedSalesAmountPayment3 = ReceivedSalesAmountPayment3
        self.ReceivedSalesAmountPayment4 = ReceivedSalesAmountPayment4
        self.ReceivedSalesAmountPayment5 = ReceivedSalesAmountPayment5
        self.ReceivedSalesAmountPayment6 = ReceivedSalesAmountPayment6


class __GetDeviceModuleSupportRes__:
    """
    :param OptionLAN: 1 symbol for LAN suppor 
    - '0' - No 
     - '1' - Yes\n
    :type OptionLAN: Enums.OptionLAN\n
    :param OptionWiFi: 1 symbol for WiFi support 
    - '0' - No 
     - '1' - Yes\n
    :type OptionWiFi: Enums.OptionWiFi\n
    :param OptionGPRS: 1 symbol for GPRS support 
    - '0' - No 
     - '1' - Yes 
    BT (Bluetooth) 1 symbol for Bluetooth support 
    - '0' - No 
     - '1' - Yes\n
    :type OptionGPRS: Enums.OptionGPRS\n
    :param OptionBT: (Bluetooth) 1 symbol for Bluetooth support 
    - '0' - No 
     - '1' - Yes\n
    :type OptionBT: Enums.OptionBT\n
    """
    def __init__(self, OptionLAN, OptionWiFi, OptionGPRS, OptionBT):
        self.OptionLAN = OptionLAN
        self.OptionWiFi = OptionWiFi
        self.OptionGPRS = OptionGPRS
        self.OptionBT = OptionBT


class __DailyCountersRes__:
    """
    :param LastReportNumFromReset: Up to 5 symbols for number of the last report from reset\n
    :type LastReportNumFromReset: float\n
    :param LastFMBlockNum: Up to 5 symbols for number of the last FM report\n
    :type LastFMBlockNum: float\n
    :param EJNum: Up to 5 symbols for number of EJ\n
    :type EJNum: float\n
    :param DateTime: 16 symbols for date and time of the last block storage in FM in 
    format "DD-MM-YYYY HH:MM"\n
    :type DateTime: datetime\n
    """
    def __init__(self, LastReportNumFromReset, LastFMBlockNum, EJNum, DateTime):
        self.LastReportNumFromReset = LastReportNumFromReset
        self.LastFMBlockNum = LastFMBlockNum
        self.EJNum = EJNum
        self.DateTime = DateTime


class __DailyRAbyOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
    :type OperNum: float\n
    :param AmountRA_Payment0: Up to 13 symbols for the RA by type of payment 0\n
    :type AmountRA_Payment0: float\n
    :param AmountRA_Payment1: Up to 13 symbols for the RA by type of payment 1\n
    :type AmountRA_Payment1: float\n
    :param AmountRA_Payment2: Up to 13 symbols for the RA by type of payment 2\n
    :type AmountRA_Payment2: float\n
    :param AmountRA_Payment3: Up to 13 symbols for the RA by type of payment 3\n
    :type AmountRA_Payment3: float\n
    :param AmountRA_Payment4: Up to 13 symbols for the RA by type of payment 4\n
    :type AmountRA_Payment4: float\n
    :param AmountRA_Payment5: Up to 13 symbols for the RA by type of payment 5\n
    :type AmountRA_Payment5: float\n
    :param AmountRA_Payment6: Up to 13 symbols for the RA by type of payment 6\n
    :type AmountRA_Payment6: float\n
    :param NoRA: Up to 5 symbols for the total number of operations\n
    :type NoRA: float\n
    """
    def __init__(self, OperNum, AmountRA_Payment0, AmountRA_Payment1, AmountRA_Payment2, AmountRA_Payment3, AmountRA_Payment4, AmountRA_Payment5, AmountRA_Payment6, NoRA):
        self.OperNum = OperNum
        self.AmountRA_Payment0 = AmountRA_Payment0
        self.AmountRA_Payment1 = AmountRA_Payment1
        self.AmountRA_Payment2 = AmountRA_Payment2
        self.AmountRA_Payment3 = AmountRA_Payment3
        self.AmountRA_Payment4 = AmountRA_Payment4
        self.AmountRA_Payment5 = AmountRA_Payment5
        self.AmountRA_Payment6 = AmountRA_Payment6
        self.NoRA = NoRA


class __HeaderRes__:
    """
    :param OptionHeaderLine: (Line Number)1 symbol with value: 
     - '1' - Header 1 
     - '2' - Header 2 
     - '3' - Header 3 
     - '4' - Header 4 
     - '5' - Header 5 
     - '6' - Header 6 
     - '7' - Header 7\n
    :type OptionHeaderLine: Enums.OptionHeaderLine\n
    :param HeaderText: TextLength symbols for header lines\n
    :type HeaderText: str\n
    """
    def __init__(self, OptionHeaderLine, HeaderText):
        self.OptionHeaderLine = OptionHeaderLine
        self.HeaderText = HeaderText


class __CustomerDataRes__:
    """
    :param CustomerNum: 3 symbols for customer number in order in format ####\n
    :type CustomerNum: float\n
    :param CustomerVatNum: 15 symbols for customer VAT registration number\n
    :type CustomerVatNum: str\n
    :param CustomerName: 30 symbols for customer name\n
    :type CustomerName: str\n
    :param CustomerAddress: 30 symbols for customer address\n
    :type CustomerAddress: str\n
    :param FreeLine1: 20 ASCII symbols for customer data\n
    :type FreeLine1: str\n
    :param FreeLine2: 20 ASCII symbols for customer data\n
    :type FreeLine2: str\n
    :param FreeLine3: 20 ASCII symbols for customer data\n
    :type FreeLine3: str\n
    :param FreeLine4: 20 ASCII symbols for customer data\n
    :type FreeLine4: str\n
    """
    def __init__(self, CustomerNum, CustomerVatNum, CustomerName, CustomerAddress, FreeLine1, FreeLine2, FreeLine3, FreeLine4):
        self.CustomerNum = CustomerNum
        self.CustomerVatNum = CustomerVatNum
        self.CustomerName = CustomerName
        self.CustomerAddress = CustomerAddress
        self.FreeLine1 = FreeLine1
        self.FreeLine2 = FreeLine2
        self.FreeLine3 = FreeLine3
        self.FreeLine4 = FreeLine4


class __CurrentReceiptInfoRes__:
    """
    :param IsReceiptOpened: 1 symbol with value '1' for initiated (opened) receipt\n
    :type IsReceiptOpened: str\n
    :param SalesNumber: 3 symbols for number of sales\n
    :type SalesNumber: str\n
    :param SubtotalAmountVATGA: 1..11 symbols for subtotal by VAT group A\n
    :type SubtotalAmountVATGA: float\n
    :param SubtotalAmountVATGB: 1..11 symbols for subtotal by VAT group B\n
    :type SubtotalAmountVATGB: float\n
    :param SubtotalAmountVATGC: 1..11 symbols for subtotal by VAT group C\n
    :type SubtotalAmountVATGC: float\n
    :param SubtotalAmountVATGD: 1..11 symbols for subtotal by VAT group D\n
    :type SubtotalAmountVATGD: float\n
    :param SubtotalAmountVATGE: 1..11 symbols for subtotal by VAT group E\n
    :type SubtotalAmountVATGE: float\n
    :param SubtotalAmountVATGF: 1..11 symbols for subtotal by VAT group F\n
    :type SubtotalAmountVATGF: float\n
    :param SubtotalAmountVATGG: 1..11 symbols for subtotal by VAT group G\n
    :type SubtotalAmountVATGG: float\n
    :param SubtotalAmountVATGH: 1..11 symbols for subtotal by VAT group H\n
    :type SubtotalAmountVATGH: float\n
    :param SubtotalAmountVATGI: 1..11 symbols for subtotal by VAT group I\n
    :type SubtotalAmountVATGI: float\n
    :param OptionForbiddenVoid: 1 symbol with value: 
     - '0' - allowed 
     - '1' - forbidden\n
    :type OptionForbiddenVoid: Enums.OptionForbiddenVoid\n
    :param OptionVATinReceipt: 1 symbol with value: 
     - '0' - with printing 
     - '1' - without printing\n
    :type OptionVATinReceipt: Enums.OptionVATinReceipt\n
    :param OptionDetailedReceipt: 1 symbol with value:  
     - '0' - brief 
     - '1' - detailed format\n
    :type OptionDetailedReceipt: Enums.OptionDetailedReceipt\n
    :param OptionInitiatedPayment: 1 symbol with value: 
     - '0' - initiated payment 
     - '1' - not initiated payment\n
    :type OptionInitiatedPayment: Enums.OptionInitiatedPayment\n
    :param OptionFinalizedPayment: 1 symbol with value: 
     - '0' - finalized payment 
     - '1' - not finalized payment\n
    :type OptionFinalizedPayment: Enums.OptionFinalizedPayment\n
    :param OptionFlagPowerDown: 1 symbol with value: 
     - '0' - no power down 
     - '1' - power down\n
    :type OptionFlagPowerDown: Enums.OptionFlagPowerDown\n
    :param OptionClientReceipt: 1 symbol with value: 
     - '0' - standard receipt 
     - '1' - invoice (client) receipt\n
    :type OptionClientReceipt: Enums.OptionClientReceipt\n
    :param ChangeAmount: 1..11 symbols the amount of the due change in the stated 
    payment type\n
    :type ChangeAmount: float\n
    :param OptionRcpChangeType: 1 symbols with value: 
     - '0' - Change In Cash 
     - '1' - Same As The payment 
     - '2' - Change In Currency\n
    :type OptionRcpChangeType: Enums.OptionRcpChangeType\n
    """
    def __init__(self, IsReceiptOpened, SalesNumber, SubtotalAmountVATGA, SubtotalAmountVATGB, SubtotalAmountVATGC, SubtotalAmountVATGD, SubtotalAmountVATGE, SubtotalAmountVATGF, SubtotalAmountVATGG, SubtotalAmountVATGH, SubtotalAmountVATGI, OptionForbiddenVoid, OptionVATinReceipt, OptionDetailedReceipt, OptionInitiatedPayment, OptionFinalizedPayment, OptionFlagPowerDown, OptionClientReceipt, ChangeAmount, OptionRcpChangeType):
        self.IsReceiptOpened = IsReceiptOpened
        self.SalesNumber = SalesNumber
        self.SubtotalAmountVATGA = SubtotalAmountVATGA
        self.SubtotalAmountVATGB = SubtotalAmountVATGB
        self.SubtotalAmountVATGC = SubtotalAmountVATGC
        self.SubtotalAmountVATGD = SubtotalAmountVATGD
        self.SubtotalAmountVATGE = SubtotalAmountVATGE
        self.SubtotalAmountVATGF = SubtotalAmountVATGF
        self.SubtotalAmountVATGG = SubtotalAmountVATGG
        self.SubtotalAmountVATGH = SubtotalAmountVATGH
        self.SubtotalAmountVATGI = SubtotalAmountVATGI
        self.OptionForbiddenVoid = OptionForbiddenVoid
        self.OptionVATinReceipt = OptionVATinReceipt
        self.OptionDetailedReceipt = OptionDetailedReceipt
        self.OptionInitiatedPayment = OptionInitiatedPayment
        self.OptionFinalizedPayment = OptionFinalizedPayment
        self.OptionFlagPowerDown = OptionFlagPowerDown
        self.OptionClientReceipt = OptionClientReceipt
        self.ChangeAmount = ChangeAmount
        self.OptionRcpChangeType = OptionRcpChangeType


class __LastDailyReportInfoRes__:
    """
    :param LastZDailyReportDate: 10 symbols for last Z-report date in DD-MM-YYYY format\n
    :type LastZDailyReportDate: datetime\n
    :param NoLastZDailyReport: 1..4 symbols for the number of the last daily report in format ####\n
    :type NoLastZDailyReport: float\n
    :param NoLastRAMReset: 1..4 symbols for the number of the lastRAM reset in format ####\n
    :type NoLastRAMReset: float\n
    """
    def __init__(self, LastZDailyReportDate, NoLastZDailyReport, NoLastRAMReset):
        self.LastZDailyReportDate = LastZDailyReportDate
        self.NoLastZDailyReport = NoLastZDailyReport
        self.NoLastRAMReset = NoLastRAMReset


class __GetBluetoothPasswordRes__:
    """
    :param PassLength: Up to 3 symbols for the BT password length\n
    :type PassLength: float\n
    :param Password: Up to 100 symbols for the BT password\n
    :type Password: str\n
    """
    def __init__(self, PassLength, Password):
        self.PassLength = PassLength
        self.Password = Password


class __StatusRes__:
    """
    :param FM_Read_only: FM Read only  ( ST3.0 or ST3.1 or ST3.2 )\n
    :type FM_Read_only: bool\n
    :param Power_down_in_opened_fiscal_receipt: Power down in opened fiscal receipt\n
    :type Power_down_in_opened_fiscal_receipt: bool\n
    :param Printer_not_ready_or_overheated: Printer not ready or overheated\n
    :type Printer_not_ready_or_overheated: bool\n
    :param Incorrect_time: Incorrect time\n
    :type Incorrect_time: bool\n
    :param Incorrect_date: Incorrect date\n
    :type Incorrect_date: bool\n
    :param RAM_reset: RAM reset\n
    :type RAM_reset: bool\n
    :param Date_and_time_hardware_error: Date and time hardware error\n
    :type Date_and_time_hardware_error: bool\n
    :param Printer_not_ready_or_no_paper: Printer not ready or no paper\n
    :type Printer_not_ready_or_no_paper: bool\n
    :param Reports_registers_overflow: Reports registers overflow\n
    :type Reports_registers_overflow: bool\n
    :param Blocking_after_24_hours: Blocking after 24 hours\n
    :type Blocking_after_24_hours: bool\n
    :param Non_zero_daily_report: Non-zero daily report\n
    :type Non_zero_daily_report: bool\n
    :param Non_zero_article_report: Non-zero article report\n
    :type Non_zero_article_report: bool\n
    :param Non_zero_operator_report: Non-zero operator report\n
    :type Non_zero_operator_report: bool\n
    :param Non_printed_copy: Non-printed copy\n
    :type Non_printed_copy: bool\n
    :param Opened_Non_fiscal_Receipt: Opened Non-fiscal Receipt\n
    :type Opened_Non_fiscal_Receipt: bool\n
    :param Opened_Fiscal_Receipt: Opened Fiscal Receipt\n
    :type Opened_Fiscal_Receipt: bool\n
    :param Standard_Cash_Receipt: Standard Cash Receipt\n
    :type Standard_Cash_Receipt: bool\n
    :param VAT_included_in_the_receipt: VAT included in the receipt\n
    :type VAT_included_in_the_receipt: bool\n
    :param Invoice: Invoice\n
    :type Invoice: bool\n
    :param EJ_near_full: EJ near full\n
    :type EJ_near_full: bool\n
    :param EJ_full: EJ full\n
    :type EJ_full: bool\n
    :param No_FM_module: No FM module\n
    :type No_FM_module: bool\n
    :param FM_error: FM error\n
    :type FM_error: bool\n
    :param FM_full: FM full\n
    :type FM_full: bool\n
    :param FM_near_full: FM near full\n
    :type FM_near_full: bool\n
    :param Decimal_point: Decimal point (1=fract, 0=whole)\n
    :type Decimal_point: bool\n
    :param FM_fiscalized: FM fiscalized\n
    :type FM_fiscalized: bool\n
    :param FM_produced: FM produced\n
    :type FM_produced: bool\n
    :param Printer_automatic_cutting: Printer: automatic cutting\n
    :type Printer_automatic_cutting: bool\n
    :param External_Display_Management: External Display Management\n
    :type External_Display_Management: bool\n
    :param Brief_or_Detailed_EJ: Brief or Detailed EJ\n
    :type Brief_or_Detailed_EJ: bool\n
    :param Drawer_automatic_opening: Drawer: automatic opening\n
    :type Drawer_automatic_opening: bool\n
    :param Customer_logo_included_in_the_receipt: Customer logo included in the receipt\n
    :type Customer_logo_included_in_the_receipt: bool\n
    """
    def __init__(self, FM_Read_only, Power_down_in_opened_fiscal_receipt, Printer_not_ready_or_overheated, Incorrect_time, Incorrect_date, RAM_reset, Date_and_time_hardware_error, Printer_not_ready_or_no_paper, Reports_registers_overflow, Blocking_after_24_hours, Non_zero_daily_report, Non_zero_article_report, Non_zero_operator_report, Non_printed_copy, Opened_Non_fiscal_Receipt, Opened_Fiscal_Receipt, Standard_Cash_Receipt, VAT_included_in_the_receipt, Invoice, EJ_near_full, EJ_full, No_FM_module, FM_error, FM_full, FM_near_full, Decimal_point, FM_fiscalized, FM_produced, Printer_automatic_cutting, External_Display_Management, Brief_or_Detailed_EJ, Drawer_automatic_opening, Customer_logo_included_in_the_receipt):
        self.FM_Read_only = FM_Read_only
        self.Power_down_in_opened_fiscal_receipt = Power_down_in_opened_fiscal_receipt
        self.Printer_not_ready_or_overheated = Printer_not_ready_or_overheated
        self.Incorrect_time = Incorrect_time
        self.Incorrect_date = Incorrect_date
        self.RAM_reset = RAM_reset
        self.Date_and_time_hardware_error = Date_and_time_hardware_error
        self.Printer_not_ready_or_no_paper = Printer_not_ready_or_no_paper
        self.Reports_registers_overflow = Reports_registers_overflow
        self.Blocking_after_24_hours = Blocking_after_24_hours
        self.Non_zero_daily_report = Non_zero_daily_report
        self.Non_zero_article_report = Non_zero_article_report
        self.Non_zero_operator_report = Non_zero_operator_report
        self.Non_printed_copy = Non_printed_copy
        self.Opened_Non_fiscal_Receipt = Opened_Non_fiscal_Receipt
        self.Opened_Fiscal_Receipt = Opened_Fiscal_Receipt
        self.Standard_Cash_Receipt = Standard_Cash_Receipt
        self.VAT_included_in_the_receipt = VAT_included_in_the_receipt
        self.Invoice = Invoice
        self.EJ_near_full = EJ_near_full
        self.EJ_full = EJ_full
        self.No_FM_module = No_FM_module
        self.FM_error = FM_error
        self.FM_full = FM_full
        self.FM_near_full = FM_near_full
        self.Decimal_point = Decimal_point
        self.FM_fiscalized = FM_fiscalized
        self.FM_produced = FM_produced
        self.Printer_automatic_cutting = Printer_automatic_cutting
        self.External_Display_Management = External_Display_Management
        self.Brief_or_Detailed_EJ = Brief_or_Detailed_EJ
        self.Drawer_automatic_opening = Drawer_automatic_opening
        self.Customer_logo_included_in_the_receipt = Customer_logo_included_in_the_receipt


class __PLUpriceRes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
    :type PLUNum: float\n
    :param Price: 1..10 symbols for article price\n
    :type Price: float\n
    :param OptionPrice: 1 byte for Price flag with next value: 
     - '0'- Free price is disable /valid only programmed price/ 
     - '1'- Free price is enable 
     - '2'- Limited price\n
    :type OptionPrice: Enums.OptionPrice\n
    """
    def __init__(self, PLUNum, Price, OptionPrice):
        self.PLUNum = PLUNum
        self.Price = Price
        self.OptionPrice = OptionPrice


class __GetGPRSpasswordRes__:
    """
    :param PassLength: Up to 3 symbols for the GPRS password length\n
    :type PassLength: float\n
    :param Password: Up to 100 symbols for the device's GPRS password\n
    :type Password: str\n
    """
    def __init__(self, PassLength, Password):
        self.PassLength = PassLength
        self.Password = Password


class __DailyCountersByOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
    :type OperNum: float\n
    :param WorkOperatorsCounter: Up to 5 symbols for number of the work operators\n
    :type WorkOperatorsCounter: float\n
    :param LastOperatorReportDateTime: 16 symbols for date and time of the last operator's report in 
    format DD-MM-YYYY HH:MM\n
    :type LastOperatorReportDateTime: datetime\n
    """
    def __init__(self, OperNum, WorkOperatorsCounter, LastOperatorReportDateTime):
        self.OperNum = OperNum
        self.WorkOperatorsCounter = WorkOperatorsCounter
        self.LastOperatorReportDateTime = LastOperatorReportDateTime


class __PaymentsRes__:
    """
    :param NamePaym0: 10 symbols for payment name of type 0\n
    :type NamePaym0: str\n
    :param NamePaym1: 10 symbols for payment name of type 1\n
    :type NamePaym1: str\n
    :param NamePaym2: 10 symbols for payment name of type 2\n
    :type NamePaym2: str\n
    :param NamePaym3: 10 symbols for payment name of type 3\n
    :type NamePaym3: str\n
    :param NamePaym4: 10 symbols for payment name of type 4\n
    :type NamePaym4: str\n
    :param NamePaym5: 10 symbols for payment name of type 5\n
    :type NamePaym5: str\n
    :param NamePaym6: 10 symbols for payment name of type 6\n
    :type NamePaym6: str\n
    """
    def __init__(self, NamePaym0, NamePaym1, NamePaym2, NamePaym3, NamePaym4, NamePaym5, NamePaym6):
        self.NamePaym0 = NamePaym0
        self.NamePaym1 = NamePaym1
        self.NamePaym2 = NamePaym2
        self.NamePaym3 = NamePaym3
        self.NamePaym4 = NamePaym4
        self.NamePaym5 = NamePaym5
        self.NamePaym6 = NamePaym6


class __GetDeviceModuleSupportByFirmwareRes__:
    """
    :param OptionLAN: 1 symbol for LAN suppor 
    - '0' - No 
     - '1' - Yes\n
    :type OptionLAN: Enums.OptionLAN\n
    :param OptionWiFi: 1 symbol for WiFi support 
    - '0' - No 
     - '1' - Yes\n
    :type OptionWiFi: Enums.OptionWiFi\n
    :param OptionGPRS: 1 symbol for GPRS support 
    - '0' - No 
     - '1' - Yes 
    BT (Bluetooth) 1 symbol for Bluetooth support 
    - '0' - No 
     - '1' - Yes\n
    :type OptionGPRS: Enums.OptionGPRS\n
    :param OptionBT: (Bluetooth) 1 symbol for Bluetooth support 
    - '0' - No 
     - '1' - Yes\n
    :type OptionBT: Enums.OptionBT\n
    """
    def __init__(self, OptionLAN, OptionWiFi, OptionGPRS, OptionBT):
        self.OptionLAN = OptionLAN
        self.OptionWiFi = OptionWiFi
        self.OptionGPRS = OptionGPRS
        self.OptionBT = OptionBT


class __PLUbarcodeRes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
    :type PLUNum: float\n
    :param Barcode: 13 symbols for article barcode\n
    :type Barcode: str\n
    """
    def __init__(self, PLUNum, Barcode):
        self.PLUNum = PLUNum
        self.Barcode = Barcode


class __PLURes__:
    """
    :param PLUNum: 5 symbols for article number with leading zeroes in format #####\n
    :type PLUNum: float\n
    :param PLUName: 34 symbols for article name (LF=7Ch)\n
    :type PLUName: str\n
    :param Price: 1..11 symbols for article price\n
    :type Price: float\n
    :param FlagsPricePLU: 1 symbol for flags = 0x80 + FlagSinglTr + FlagQTY + OptionPrice 
    Where  
    OptionPrice: 
    0x00 - for free price is disable /valid only programmed price/ 
    0x01 - for free price is enable 
    0x02 - for limited price 
    FlagQTY: 
    0x00 - for availability of PLU stock is not monitored 
    0x04 - for disable negative quantity 
    0x08 - for enable negative quantity 
    FlagSingleTr: 
    0x00 - no single transaction 
    0x10 - single transaction is active\n
    :type FlagsPricePLU: str\n
    :param OptionVATClass: 1 symbol for article's VAT Class with optional values: 
     - 'A' - VAT class A 
     - 'B' - VAT class B 
     - 'C' - VAT class C 
     - 'D' - VAT class D 
     - 'E' - VAT class E 
     - 'F' - VAT class F 
     - 'G' - VAT class G 
     - 'H' - VAT class H 
     - 'I' - VAT class I\n
    :type OptionVATClass: Enums.OptionVATClass\n
    :param DepNum: DepNum + 80h, 1 symbol for article department attachment, formed in 
    the following manner: example: Dep01 = 81h, Dep02 = 82h … Dep19 
    = 93h\n
    :type DepNum: float\n
    :param Turnover: 11 symbols for PLU accumulated turnover\n
    :type Turnover: float\n
    :param QuantitySold: 11 symbols for Sales quantity of the article\n
    :type QuantitySold: float\n
    :param LastZReportNumber: 5 symbols for the number of the last article report with zeroing\n
    :type LastZReportNumber: float\n
    :param LastZReportDate: 16 symbols for the date and time of the last article report with zeroing  
    in format DD-MM-YYYY HH:MM\n
    :type LastZReportDate: datetime\n
    :param AvailableQuantity: (Available Quantity) - 1..11 symbols for quantity in stock\n
    :type AvailableQuantity: float\n
    :param Barcode: 13 symbols for article barcode\n
    :type Barcode: str\n
    """
    def __init__(self, PLUNum, PLUName, Price, FlagsPricePLU, OptionVATClass, DepNum, Turnover, QuantitySold, LastZReportNumber, LastZReportDate, AvailableQuantity, Barcode):
        self.PLUNum = PLUNum
        self.PLUName = PLUName
        self.Price = Price
        self.FlagsPricePLU = FlagsPricePLU
        self.OptionVATClass = OptionVATClass
        self.DepNum = DepNum
        self.Turnover = Turnover
        self.QuantitySold = QuantitySold
        self.LastZReportNumber = LastZReportNumber
        self.LastZReportDate = LastZReportDate
        self.AvailableQuantity = AvailableQuantity
        self.Barcode = Barcode


class __VATClassAmountsRes__:
    """
    :param AmountVATGrA: 1..11 symbols for the amount accumulated in the VAT group A\n
    :type AmountVATGrA: float\n
    :param AmountVATGrB: 1..11 symbols for the amount accumulated in the VAT group B\n
    :type AmountVATGrB: float\n
    :param AmountVATGrC: 1..11 symbols for the amount accumulated in the VAT group C\n
    :type AmountVATGrC: float\n
    :param AmountVATGrD: 1..11 symbols for the amount accumulated in the VAT group D\n
    :type AmountVATGrD: float\n
    :param AmountVATGrE: 1..11 symbols for the amount accumulated in the VAT group E\n
    :type AmountVATGrE: float\n
    :param AmountVATGrF: 1..11 symbols for the amount accumulated in the VAT group F\n
    :type AmountVATGrF: float\n
    :param AmountVATGrG: 1..11 symbols for the amount accumulated in the VAT group G\n
    :type AmountVATGrG: float\n
    :param AmountVATGrH: 1..11 symbols for the amount accumulated in the VAT group H\n
    :type AmountVATGrH: float\n
    :param AmountVATGrI: 1..11 symbols for the amount accumulated in the VAT group I\n
    :type AmountVATGrI: float\n
    """
    def __init__(self, AmountVATGrA, AmountVATGrB, AmountVATGrC, AmountVATGrD, AmountVATGrE, AmountVATGrF, AmountVATGrG, AmountVATGrH, AmountVATGrI):
        self.AmountVATGrA = AmountVATGrA
        self.AmountVATGrB = AmountVATGrB
        self.AmountVATGrC = AmountVATGrC
        self.AmountVATGrD = AmountVATGrD
        self.AmountVATGrE = AmountVATGrE
        self.AmountVATGrF = AmountVATGrF
        self.AmountVATGrG = AmountVATGrG
        self.AmountVATGrH = AmountVATGrH
        self.AmountVATGrI = AmountVATGrI


class __DailyGeneralRegistersByOperatorRes__:
    """
    :param OperNum: (Operator Number) Symbol from 1 to 20in format corresponding to 
    operator's number\n
    :type OperNum: float\n
    :param CustomersNum: Up to 5 symbols for number of customers\n
    :type CustomersNum: float\n
    :param DiscountsNum: Up to 5 symbols for number of discounts\n
    :type DiscountsNum: float\n
    :param DiscountsAmount: Up to 11 symbols for accumulated amount of discounts\n
    :type DiscountsAmount: float\n
    :param AdditionsNum: Up to 5 symbols for number ofadditions\n
    :type AdditionsNum: float\n
    :param AdditionsAmount: Up to 11 symbols for accumulated amount of additions\n
    :type AdditionsAmount: float\n
    :param CorrectionsNum: Up to 5 symbols for number of corrections\n
    :type CorrectionsNum: float\n
    :param CorrectionsAmount: Up to 11 symbols for accumulated amount of corrections\n
    :type CorrectionsAmount: float\n
    """
    def __init__(self, OperNum, CustomersNum, DiscountsNum, DiscountsAmount, AdditionsNum, AdditionsAmount, CorrectionsNum, CorrectionsAmount):
        self.OperNum = OperNum
        self.CustomersNum = CustomersNum
        self.DiscountsNum = DiscountsNum
        self.DiscountsAmount = DiscountsAmount
        self.AdditionsNum = AdditionsNum
        self.AdditionsAmount = AdditionsAmount
        self.CorrectionsNum = CorrectionsNum
        self.CorrectionsAmount = CorrectionsAmount


class __GetGPRSUserNameRes__:
    """
    :param gprsUserNameLength: Up to 3 symbols for the GPRS username length\n
    :type gprsUserNameLength: float\n
    :param Username: Up to 100 symbols for the device's GPRS username\n
    :type Username: str\n
    """
    def __init__(self, gprsUserNameLength, Username):
        self.gprsUserNameLength = gprsUserNameLength
        self.Username = Username


class __GetTCPWiFiPasswordRes__:
    """
    :param PassLength: Up to 3 symbols for the WiFi password length\n
    :type PassLength: float\n
    :param Password: Up to 100 symbols for the device's WiFi password\n
    :type Password: str\n
    """
    def __init__(self, PassLength, Password):
        self.PassLength = PassLength
        self.Password = Password


class __DailyRaRes__:
    """
    :param AmountPayment0: Up to 11 symbols for the accumulated amount by payment type 0\n
    :type AmountPayment0: float\n
    :param AmountPayment1: Up to 11 symbols for the accumulated amount by payment type 1\n
    :type AmountPayment1: float\n
    :param AmountPayment2: Up to 11 symbols for the accumulated amount by payment type 2\n
    :type AmountPayment2: float\n
    :param AmountPayment3: Up to 11 symbols for the accumulated amount by payment type 3\n
    :type AmountPayment3: float\n
    :param AmountPayment4: Up to 11 symbols for the accumulated amount by payment type 4\n
    :type AmountPayment4: float\n
    :param AmountPayment5: Up to 11 symbols for the accumulated amount by payment type 5 
    AmountPayment6 Up to 11 symbols for the accumulated amount by payment type 6\n
    :type AmountPayment5: float\n
    :param AmountPayment: 0 Up to 11 symbols for the accumulated amount by payment type 0\n
    :type AmountPayment: float\n
    """
    def __init__(self, AmountPayment0, AmountPayment1, AmountPayment2, AmountPayment3, AmountPayment4, AmountPayment5, AmountPayment):
        self.AmountPayment0 = AmountPayment0
        self.AmountPayment1 = AmountPayment1
        self.AmountPayment2 = AmountPayment2
        self.AmountPayment3 = AmountPayment3
        self.AmountPayment4 = AmountPayment4
        self.AmountPayment5 = AmountPayment5
        self.AmountPayment = AmountPayment


class __GeneralDailyRegistersRes__:
    """
    :param CustomersNum: Up to 5 symbols for number of customers\n
    :type CustomersNum: float\n
    :param DiscountsNum: Up to 5 symbols for number of discounts\n
    :type DiscountsNum: float\n
    :param DiscountsAmount: Up to 11 symbols for accumulated amount of discounts\n
    :type DiscountsAmount: float\n
    :param AdditionsNum: Up to 5 symbols for number of additions\n
    :type AdditionsNum: float\n
    :param AdditionsAmount: Up to 11 symbols for accumulated amount of additions\n
    :type AdditionsAmount: float\n
    :param CorrectionsNum: Up to 5 symbols for number of corrections\n
    :type CorrectionsNum: float\n
    :param CorrectionsAmount: Up to 11 symbols for accumulated amount of corrections\n
    :type CorrectionsAmount: float\n
    """
    def __init__(self, CustomersNum, DiscountsNum, DiscountsAmount, AdditionsNum, AdditionsAmount, CorrectionsNum, CorrectionsAmount):
        self.CustomersNum = CustomersNum
        self.DiscountsNum = DiscountsNum
        self.DiscountsAmount = DiscountsAmount
        self.AdditionsNum = AdditionsNum
        self.AdditionsAmount = AdditionsAmount
        self.CorrectionsNum = CorrectionsNum
        self.CorrectionsAmount = CorrectionsAmount


class __ParametersRes__:
    """
    :param POSNum: (POS Number) 4 symbols for number of POS in format ####\n
    :type POSNum: float\n
    :param OptionPrintLogo: (Print Logo) 1 symbol of value: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionPrintLogo: Enums.OptionPrintLogo\n
    :param OptionAutoOpenDrawer: (Auto Open Drawer) 1 symbol of value: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionAutoOpenDrawer: Enums.OptionAutoOpenDrawer\n
    :param OptionAutoCut: (Auto Cut) 1 symbol of value: 
     - '1' - Yes 
     - '0' - No\n
    :type OptionAutoCut: Enums.OptionAutoCut\n
    :param OptionExternalDispManagement: (External Display Management) 1 symbol of value: 
     - '1' - Manual 
     - '0' - Auto\n
    :type OptionExternalDispManagement: Enums.OptionExternalDispManagement\n
    :param OptionArticleReportType: (Article Report) 1 symbol of value: 
     - '1' - Detailed 
     - '0' - Brief\n
    :type OptionArticleReportType: Enums.OptionArticleReportType\n
    :param OptionCurrency: 1 symbol of value: 
     - '1' - Enabled 
     - '0' - Disabled\n
    :type OptionCurrency: Enums.OptionCurrency\n
    :param OptionEJFontType: (EJ Font) 1 symbol of value: 
     - '1' - Low Font 
     - '0' - Normal Font\n
    :type OptionEJFontType: Enums.OptionEJFontType\n
    """
    def __init__(self, POSNum, OptionPrintLogo, OptionAutoOpenDrawer, OptionAutoCut, OptionExternalDispManagement, OptionArticleReportType, OptionCurrency, OptionEJFontType):
        self.POSNum = POSNum
        self.OptionPrintLogo = OptionPrintLogo
        self.OptionAutoOpenDrawer = OptionAutoOpenDrawer
        self.OptionAutoCut = OptionAutoCut
        self.OptionExternalDispManagement = OptionExternalDispManagement
        self.OptionArticleReportType = OptionArticleReportType
        self.OptionCurrency = OptionCurrency
        self.OptionEJFontType = OptionEJFontType


class __DailyReturnedChangeAmountsByOperatorRes__:
    """
    :param OperNum: Symbols from 1 to 20 corresponding to operator's number\n
    :type OperNum: float\n
    :param ChangeAmountPayment0: Up to 13 symbols for amounts received by type of payment 0\n
    :type ChangeAmountPayment0: float\n
    :param ChangeAmountPayment1: Up to 13 symbols for amounts received by type of payment 1\n
    :type ChangeAmountPayment1: float\n
    :param ChangeAmountPayment2: Up to 13 symbols for amounts received by type of payment 2\n
    :type ChangeAmountPayment2: float\n
    :param ChangeAmountPayment3: Up to 13 symbols for amounts received by type of payment 3\n
    :type ChangeAmountPayment3: float\n
    :param ChangeAmountPayment4: Up to 13 symbols for amounts received by type of payment 4\n
    :type ChangeAmountPayment4: float\n
    :param ChangeAmountPayment5: Up to 13 symbols for amounts received by type of payment 5\n
    :type ChangeAmountPayment5: float\n
    :param ChangeAmountPayment6: Up to 13 symbols for amounts received by type of payment 6\n
    :type ChangeAmountPayment6: float\n
    """
    def __init__(self, OperNum, ChangeAmountPayment0, ChangeAmountPayment1, ChangeAmountPayment2, ChangeAmountPayment3, ChangeAmountPayment4, ChangeAmountPayment5, ChangeAmountPayment6):
        self.OperNum = OperNum
        self.ChangeAmountPayment0 = ChangeAmountPayment0
        self.ChangeAmountPayment1 = ChangeAmountPayment1
        self.ChangeAmountPayment2 = ChangeAmountPayment2
        self.ChangeAmountPayment3 = ChangeAmountPayment3
        self.ChangeAmountPayment4 = ChangeAmountPayment4
        self.ChangeAmountPayment5 = ChangeAmountPayment5
        self.ChangeAmountPayment6 = ChangeAmountPayment6


class __DailyPORes__:
    """
    :param AmountPayment0: Up to 11 symbols for the accumulated amount by payment type 0\n
    :type AmountPayment0: float\n
    :param AmountPayment1: Up to 11 symbols for the accumulated amount by payment type 1\n
    :type AmountPayment1: float\n
    :param AmountPayment2: Up to 11 symbols for the accumulated amount by payment type 2\n
    :type AmountPayment2: float\n
    :param AmountPayment3: Up to 11 symbols for the accumulated amount by payment type 3\n
    :type AmountPayment3: float\n
    :param AmountPayment4: Up to 11 symbols for the accumulated amount by payment type 4\n
    :type AmountPayment4: float\n
    :param AmountPayment5: Up to 11 symbols for the accumulated amount by payment type 5 
    AmountPayment6 Up to 11 symbols for the accumulated amount by payment type 6\n
    :type AmountPayment5: float\n
    :param AmountPayment: 0 Up to 11 symbols for the accumulated amount by payment type 0\n
    :type AmountPayment: float\n
    :param PONum: Up to 5 symbols for the total number of operations\n
    :type PONum: float\n
    """
    def __init__(self, AmountPayment0, AmountPayment1, AmountPayment2, AmountPayment3, AmountPayment4, AmountPayment5, AmountPayment, PONum):
        self.AmountPayment0 = AmountPayment0
        self.AmountPayment1 = AmountPayment1
        self.AmountPayment2 = AmountPayment2
        self.AmountPayment3 = AmountPayment3
        self.AmountPayment4 = AmountPayment4
        self.AmountPayment5 = AmountPayment5
        self.AmountPayment = AmountPayment
        self.PONum = PONum


class Enums:
    """Enumerations"""

    class OptionZeroing(Enum):
        Without_zeroing = u'X'
        Zeroing = u'Z'

    class OptionPrintLogo(Enum):
        No = u'0'
        Yes = u'1'

    class OptionAutoOpenDrawer(Enum):
        No = u'0'
        Yes = u'1'

    class OptionAutoCut(Enum):
        No = u'0'
        Yes = u'1'

    class OptionExternalDispManagement(Enum):
        Auto = u'0'
        Manual = u'1'

    class OptionEJFontType(Enum):
        Low_Font = u'1'
        Normal_Font = u'0'

    class OptionBTstatus(Enum):
        Disabled = u'0'
        Enabled = u'1'

    class OptionVATClass(Enum):
        VAT_class_A = u'A'
        VAT_class_B = u'B'
        VAT_class_C = u'C'
        VAT_class_D = u'D'
        VAT_class_E = u'E'
        VAT_class_F = u'F'
        VAT_class_G = u'G'
        VAT_class_H = u'H'
        VAT_class_I = u'I'

    class OptionDepPrice(Enum):
        Free_price_disabled = u'0'
        Free_price_disabled_for_single_transaction = u'4'
        Free_price_enabled = u'1'
        Free_price_enabled_for_single_transaction = u'5'
        Limited_price = u'2'
        Limited_price_for_single_transaction = u'6'

    class OptionPrice(Enum):
        Free_price_is_disable_valid_only_programmed_price = u'0'
        Free_price_is_enable = u'1'
        Limited_price = u'2'

    class OptionTransaction(Enum):
        Active_Single_transaction_in_receipt = u'1'
        Inactive_default_value = u'0'

    class OptionTCPAutoStart(Enum):
        No = u'0'
        Yes = u'1'

    class OptionSign(Enum):
        Correction = u'-'
        Sale = u'+'

    class OptionPaymentType(Enum):
        Payment_0 = u'0'
        Payment_1 = u'1'
        Payment_2 = u'2'
        Payment_3 = u'3'
        Payment_4 = u'4'
        Payment_5 = u'5'
        Payment_6 = u'6'

    class OptionQuantityType(Enum):
        for_availability_of_PLU_stock_is_not_monitored = u'0'
        for_disable_negative_quantity = u'1'
        for_enable_negative_quantity = u'2'

    class OptionAddressType(Enum):
        DNS_address = u'5'
        Gateway_address = u'4'
        IP_address = u'2'
        Subnet_Mask = u'3'

    class OptionUsedModule(Enum):
        LAN_module = u'1'
        WiFi_module = u'2'

    class OptionDHCPEnabled(Enum):
        Disabled = u'0'
        Enabled = u'1'

    class OptionHeaderLine(Enum):
        Header_1 = u'1'
        Header_2 = u'2'
        Header_3 = u'3'
        Header_4 = u'4'
        Header_5 = u'5'
        Header_6 = u'6'
        Header_7 = u'7'

    class OptionDecimalPointPosition(Enum):
        fractions = u'2'
        whole_numbers = u'0'

    class OptionLAN(Enum):
        No = u'0'
        Yes = u'1'

    class OptionWiFi(Enum):
        No = u'0'
        Yes = u'1'

    class OptionGPRS(Enum):
        No = u'0'
        Yes = u'1'

    class OptionBT(Enum):
        No = u'0'
        Yes = u'1'

    class OptionForbiddenVoid(Enum):
        allowed = u'0'
        forbidden = u'1'

    class OptionVATinReceipt(Enum):
        with_printing = u'0'
        without_printing = u'1'

    class OptionDetailedReceipt(Enum):
        brief = u'0'
        detailed_format = u'1'

    class OptionInitiatedPayment(Enum):
        initiated_payment = u'0'
        not_initiated_payment = u'1'

    class OptionFinalizedPayment(Enum):
        finalized_payment = u'0'
        not_finalized_payment = u'1'

    class OptionFlagPowerDown(Enum):
        no_power_down = u'0'
        power_down = u'1'

    class OptionClientReceipt(Enum):
        invoice_client_receipt = u'1'
        standard_receipt = u'0'

    class OptionRcpChangeType(Enum):
        Change_In_Cash = u'0'
        Change_In_Currency = u'2'
        Same_As_The_payment = u'1'

    class OptionChange(Enum):
        With_Change_default = u'0'
        Without_Change = u'1'

    class OptionChangeType(Enum):
        Change_In_Cash = u'0'
        Same_As_The_payment = u'1'

    class OptionReceipType(Enum):
        Refund_receipt = u'1'
        Standard_fiscal_receipt = u'0'

    class OptionFiscalRcpPrintType(Enum):
        Postponed_Printing = u'2'
        Step_by_step_printing = u'0'

    class OptionPrinting(Enum):
        No = u'0'
        Yes = u'1'

    class OptionDisplay(Enum):
        No = u'0'
        Yes = u'1'

    class OptionArticleReportType(Enum):
        Brief = u'0'
        Detailed = u'1'

    class OptionCurrency(Enum):
        Disabled = u'0'
        Enabled = u'1'


