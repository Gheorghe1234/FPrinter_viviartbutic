# coding=utf-8
import ctypes
import array as arr

rti1000 = ctypes.CDLL('D:\\UNISIM\\PYTHON Projects\\UNA_PrinterFP\\RTI_driver\\rti1000.dll')

rti1000.Setup.argtypes = [ctypes.c_wchar_p,
                          ctypes.c_wchar_p]  # первоначальная настройка (входные параметры: название ком порта, скорость связи)
rti1000.ZReport.restype = ctypes.c_wchar_p  # закрытие смены, печать Z отчета (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.XReport.restype = ctypes.c_wchar_p  # печать X отчета (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.PrintReceiptCopy.restype = ctypes.c_wchar_p  # печать копии последнего чека (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.ResetReceipt.restype = ctypes.c_wchar_p  # сбросить открытый чек (результат выполнения операции, может быть или 'OK' или текст ошибки )

rti1000.GetShiftNo.restype = ctypes.c_wchar_p  # получить номер текущего Z отчета (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.GetShiftNo.argtypes = [
    ctypes.c_void_p]  # параметр передается по ссылке, в который вернеться значение номера текущего Z отчета

rti1000.AddMoneyToCashDrawer.restype = ctypes.c_wchar_p  # служебный внос средст в денежный ящик (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.AddMoneyToCashDrawer.argtypes = [ctypes.c_double]  # входной параметр - сумма внесения

rti1000.GiveMoneyFromCashDrawer.restype = ctypes.c_wchar_p  # службный вынос денежных средств (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.GiveMoneyFromCashDrawer.argtypes = [ctypes.c_double]  # входной параметр сумма изъятия

rti1000.GetReceiptNo.restype = ctypes.c_wchar_p  # получить номер текущего чека
rti1000.GetReceiptNo.argtypes = [
    ctypes.c_void_p]  # параметр передается по ссылке, в который вернеться значение номера текущего чека

rti1000.GetShiftSalesAmount.restype = ctypes.c_wchar_p  # получить сумму продаж в текущей смене
rti1000.GetShiftSalesAmount.argtypes = [
    ctypes.c_void_p]  # параметр передается по ссылке, в который вернеться значение суммы продаж в текущей смене

rti1000.OpenCashDrawer.restype = ctypes.c_wchar_p  # открыть денежный ящик (результат выполнения операции, может быть или 'OK' или текст ошибки )

rti1000.GetStatus.restype = ctypes.c_wchar_p  # получение статуса фискалки (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.GetStatus.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
# все параметры передается по ссылке (серийный номер фискалки, регистрационный номер фискалки, taxNumber, версия прошивки )

rti1000.RegisterCashier.argtypes = [
    ctypes.c_wchar_p]  # регистрация кассира (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.RegisterCashier.restype = ctypes.c_wchar_p  # входной параметр ФИО КАССИРА

rti1000.GetDateTime.argtypes = [
    ctypes.c_void_p]  # получить дату/время из фискалки (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.GetDateTime.restype = ctypes.c_wchar_p  # параметр передается по ссылке в который вернется строка с текущей датой временем в фискалке в формате yyyy-MM-dd hh:mm:ss

rti1000.PrintReceipt.restype = ctypes.c_wchar_p  # продажа/печать чека (результат выполнения операции, может быть или 'OK' или текст ошибки )
rti1000.PrintReceipt.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_void_p,
                                 ctypes.c_int32, ctypes.c_void_p, ctypes.c_void_p]


# список параметров
# 1. Сумма оплаты банковской картой
# 2. Сумма оплаты наличными
# 3. Общая сумма скидки по чеку (печатается в виде комментария в конце чека)
# 4. Общая сумма чека без учета скидки (печатается в виде комментария в конце чека)
# 5. Указатель на массив записей со структурой pyReceiptRowStructure (указатель на массив строк чека)
# 6. Количество записей в массиве (по сути количество строк в чеке)
# 7. параметр передается по ссылке в результате веренться значение здачи, которая положена по чеку
# 8. параметр передается по ссылке в результате веренться строка с Warning сообщением. Пример "Заканчивается бумага"


class pyReceiptRowStructure(ctypes.Structure):
    _fields_ = [("name", ctypes.c_wchar_p),
                ("price", ctypes.c_double),
                ("count", ctypes.c_double),
                ("prod_id", ctypes.c_int32),
                ("discount", ctypes.c_double),
                ("tax_group", ctypes.c_char)]


# указываем порт и скорость связи с фискалкой
comPort = 'COM1'
baudRate = '38400'

rti1000.Setup(comPort, baudRate)

# === Пример получения статуса фискалки ==========
# rti1000.Setup(comPort,baudRate)
# serialNumber=ctypes.c_wchar_p('')
# registrationNumber=ctypes.c_wchar_p('')
# taxNumber=ctypes.c_wchar_p('')
# firmwareVersion=ctypes.c_wchar_p('')
# result=rti1000.GetStatus(ctypes.byref(serialNumber),ctypes.byref(registrationNumber),ctypes.byref(taxNumber),ctypes.byref(firmwareVersion))
# print(serialNumber.value, registrationNumber.value, taxNumber.value, firmwareVersion.value)

# === Пример печати X отчета ==========
rti1000.Setup(comPort, baudRate)
result = rti1000.XReport();
print(result)

# === Пример получения суммы продаж в текущей смене ==========
# rti1000.Setup(comPort,baudRate)
# n=ctypes.c_double(0);
# result=rti1000.GetShiftSalesAmount(ctypes.byref(n));
# print(n.value, result)


# === Пример получения номера текущей смены ==========
# rti1000.Setup(comPort,baudRate)
# n=ctypes.c_int32(0);
# result=rti1000.GetShiftNo(ctypes.byref(n));
# print(n.value)


# === Пример получения дата/время с фискалки ==========
# rti1000.Setup(comPort,baudRate)
# date=ctypes.c_wchar_p('')
# result=rti1000.GetDateTime(ctypes.byref(date));
# print(result, date.value)

# === Пример печати чека ==========
# rti1000.Setup(comPort,baudRate)
# rti1000.ResetReceipt()
# arr=(pyReceiptRowStructure*2)()

# arr[0].price=128.15
# arr[0].name='Salam CODRU'
# arr[0].count=0.125
# arr[0].prod_id=1001
# arr[0].discount=2
# arr[0].tax_group='0'

# arr[1].price=80.45
# arr[1].name='Code Nescafe 75gr'
# arr[1].count=5
# arr[1].prod_id=999
# arr[1].discount=0
# arr[1].tax_group='1'


# rest=ctypes.c_double(0);
# hasWarning=ctypes.c_bool(0);
# result=rti1000.PrintReceipt(0,500,0,0,ctypes.pointer(arr), 2, ctypes.byref(rest), ctypes.byref(hasWarning));
# print(result, 'REST: ',rest.value);
