import pandas as pd

# Datele pentru tabel traduse ?n limba rus? pentru comanda API Get Orders
data_orders_ru = {
    "Поле": [
        "status", "message", "data", "data.nrord", "data.nrdoc", "data.nrmanual",
        "data.dlvr_date", "data.date_activated", "data.dlvr_time_im_1", "data.clcdlvr_time_im_1t",
        "data.dep", "data.dep_supplier", "data.clcdep_suppliert", "data.order_state_im_2",
        "data.clcorder_state_im_2t", "data.txt_comment", "data.bgcolor", "data.sysfid", "data.doc_at2",
        "data.order_details", "data.order_details.sc", "data.order_details.cant", "data.order_details.suma",
        "data.order_details.clcsct", "data.order_details.barcode", "data.order_details.codvechi", "errors"
    ],
    "Тип данных": [
        "boolean", "string", "array of objects", "string", "string or null", "string", "string", "string",
        "string", "string", "string", "string", "string", "string", "string", "string", "string", "string",
        "string", "array of objects", "string", "string", "string", "string", "string", "string or null",
        "null or array of objects"
    ],
    "Описание": [
        "Указывает, был ли запрос API выполнен успешно или нет.",
        "Информационное сообщение о результате запроса.",
        "Содержит всю релевантную информацию о заказе.",
        "Номер документа заказа из приложения UNA.",
        "Номер документа заказа из приложения UNA.",
        "Описание или комментарий к документу.",
        "Дата доставки.",
        "Дата активации.",
        "Код времени доставки.",
        "Описание/название времени доставки (например, утро, день, вечер).",
        "Код склада.",
        "Код поставщика.",
        "Название поставщика.",
        "Код статуса документа.",
        "Название статуса документа (например, подтверждено).",
        "Комментарий к заказу.",
        "Цвет фона.",
        "Уникальный идентификатор типа документа.",
        "Документ AT2.",
        "Содержит детали заказа.",
        "Код продукта из приложения UNA.",
        "Количество продукта.",
        "Сумма.",
        "Название продукта.",
        "Штрихкод продукта.",
        "Альтернативный код продукта.",
        "Любая ошибка, связанная с запросом. В данном примере значение `null`, что означает отсутствие ошибок."
    ]
}

# Crearea DataFrame-ului ?n rus?
df_orders_ru = pd.DataFrame(data_orders_ru)

# Salvarea ?n fi?ier Excel
file_path_orders_ru = "/mnt/data/описание_полей_заказов.xlsx"
df_orders_ru.to_excel(file_path_orders_ru, index=False)

file_path_orders_ru
