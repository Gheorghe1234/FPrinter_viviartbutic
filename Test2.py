from datetime import datetime, timedelta

import pytz

yy = 'Ingrediente: ciocolata neagra(85%)(masa de cacao,zahar,unt '

v_datastart = datetime.strptime('310324235959', "%d%m%y%H%M%S")

v_datastart = v_datastart.strftime("%d-%m-%y %H:%M:%S DST")
print(v_datastart)
def check_dst(p_date):
    timezone = pytz.timezone('Europe/Chisinau')
    v_date = timezone.localize(datetime.strptime(p_date, "%d-%m-%y %H:%M:%S"))
    return v_date.dst() != timedelta(0)

if check_dst(datetime.now().strftime("%d-%m-%y %H:%M:%S")):
    print(11)
else:
    print(22)