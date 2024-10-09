import win32print


def print_text(text, printer_name=None):
    # Obtine lista de printere disponibile
    printers = win32print.EnumPrinters(2)

    if printer_name is None:
        # Daca nu este specificat un nume de printer, foloseste printerul implicit
        default_printer = win32print.GetDefaultPrinter()
        for printer in printers:
            if printer[2] == default_printer:
                printer_name = printer[2]
                break
    else:
        # Verifica daca numele printerului specificat este valid
        printer_names = [printer[2] for printer in printers]
        if printer_name not in printer_names:
            print(f"Printerul {printer_name} nu este disponibil.")
            return

    # Configurare obiect printer
    printer_handle = win32print.OpenPrinter(printer_name)
    defaults = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
    properties = win32print.GetPrinter(printer_handle, 2)
    devmode = properties["pDevMode"]

    try:
        # Setare parametri de tiparire
        devmode.DefaultSource = win32print.PRINTER_ATTRIBUTE_DEFAULT
        devmode.Orientation = 2
        devmode.Fields |= win32print.DM_DEFAULTSOURCE | win32print.DM_ORIENTATION
        win32print.DocumentProperties(None, printer_handle, printer_name, devmode, devmode,
                                      1)

        # Trimite textul la printare
        job_info = win32print.StartDocPrinter(printer_handle, 1, ("Text printat", None, "RAW"))
        win32print.StartPagePrinter(printer_handle)
        win32print.WritePrinter(printer_handle, text.encode())
        win32print.EndPagePrinter(printer_handle)
        win32print.EndDocPrinter(printer_handle)
        print("Textul a fost trimis la printare cu succes.")
    finally:
        # Inchide conexiunea cu printerul
        win32print.ClosePrinter(printer_handle)


# Exemplu de utilizare
text_de_printat = "Acesta este textul de printat."
nume_printer = "POS-80"

print_text(text_de_printat, nume_printer)
