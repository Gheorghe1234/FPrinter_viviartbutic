import pandas as pd

# Datele pentru tabel traduse ?n limba rus? pentru comanda API Get Orders
data_orders_ru = {
    "����": [
        "status", "message", "data", "data.nrord", "data.nrdoc", "data.nrmanual",
        "data.dlvr_date", "data.date_activated", "data.dlvr_time_im_1", "data.clcdlvr_time_im_1t",
        "data.dep", "data.dep_supplier", "data.clcdep_suppliert", "data.order_state_im_2",
        "data.clcorder_state_im_2t", "data.txt_comment", "data.bgcolor", "data.sysfid", "data.doc_at2",
        "data.order_details", "data.order_details.sc", "data.order_details.cant", "data.order_details.suma",
        "data.order_details.clcsct", "data.order_details.barcode", "data.order_details.codvechi", "errors"
    ],
    "��� ������": [
        "boolean", "string", "array of objects", "string", "string or null", "string", "string", "string",
        "string", "string", "string", "string", "string", "string", "string", "string", "string", "string",
        "string", "array of objects", "string", "string", "string", "string", "string", "string or null",
        "null or array of objects"
    ],
    "��������": [
        "���������, ��� �� ������ API �������� ������� ��� ���.",
        "�������������� ��������� � ���������� �������.",
        "�������� ��� ����������� ���������� � ������.",
        "����� ��������� ������ �� ���������� UNA.",
        "����� ��������� ������ �� ���������� UNA.",
        "�������� ��� ����������� � ���������.",
        "���� ��������.",
        "���� ���������.",
        "��� ������� ��������.",
        "��������/�������� ������� �������� (��������, ����, ����, �����).",
        "��� ������.",
        "��� ����������.",
        "�������� ����������.",
        "��� ������� ���������.",
        "�������� ������� ��������� (��������, ������������).",
        "����������� � ������.",
        "���� ����.",
        "���������� ������������� ���� ���������.",
        "�������� AT2.",
        "�������� ������ ������.",
        "��� �������� �� ���������� UNA.",
        "���������� ��������.",
        "�����.",
        "�������� ��������.",
        "�������� ��������.",
        "�������������� ��� ��������.",
        "����� ������, ��������� � ��������. � ������ ������� �������� `null`, ��� �������� ���������� ������."
    ]
}

# Crearea DataFrame-ului ?n rus?
df_orders_ru = pd.DataFrame(data_orders_ru)

# Salvarea ?n fi?ier Excel
file_path_orders_ru = "/mnt/data/��������_�����_�������.xlsx"
df_orders_ru.to_excel(file_path_orders_ru, index=False)

file_path_orders_ru
