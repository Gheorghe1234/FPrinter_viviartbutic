import socket
from urllib.request import urlopen
import io
from PIL import Image

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.75"
port = 9100

v_text1 = b"""P,432,576
TB,13,0,407,32,8,1,1,2,0,DATA,Product_name,Product Name,2,50,0
TB,13,72,407,85,0,1,1,2,0,DATA,Ingredient,Ingrediente,2,2000,2
TB,301,378,67,21,1,1,1,2,0,DATA,Net,Net Weight,2,15,4
TB,326,427,92,25,6,1,1,2,0,DATA,Total_price,Total price,2,15,5
TB,149,410,167,21,2,1,1,2,0,DATA,DateTime,2022-04-28 02:32:28,2,50,6
TB,101,380,73,18,1,1,1,2,0,DATA,Price,Pret,2,20,9
TB,216,379,85,18,1,1,1,2,0,TEXT,Masa neta:,10
TB,341,402,60,25,6,1,1,2,0,TEXT,Total,11
TB,25,410,118,21,2,1,1,2,0,TEXT,Data Fabricarii,12
TB,25,431,118,19,2,1,1,2,0,TEXT,Data Expirarii,13
B,106,462,53,244,2,E30,0,BC,TEXT,2,TEXT,2,DATA,barcode,01234,3,5,DATA,Net,01234,3,5,15
TB,59,381,42,18,1,1,1,2,0,TEXT,Pret:,16
TB,149,431,167,19,2,1,1,2,0,DATA,package_datetime,2022-04-28,2,50,17
TB,170,56,89,16,1,1,1,2,0,TEXT,Ingrediente,19
TB,46,32,335,24,0,1,1,2,0,DATA,place,Produced,2,1500,20
TB,368,378,24,19,1,1,1,2,0,TEXT,kg,21
TB,225,188,200,182,0,1,1,0,0,DATA,Temperature,Temperature,1,800,24
TB,221,167,210,21,1,1,1,2,0,TEXT,Durata si conditii de pastrare:,25
R,1,167,221,370,1,0,33
TB,5,200,141,18,0,1,1,2,0,TEXT,Valoarea energetica:,34
TB,137,200,72,18,0,1,1,2,0,DATA,nutritional,Nutritional value,2,1500,35
TB,4,178,216,21,0,1,1,2,0,TEXT,Valoarea Nutritiva la 100g de produs:,36
TB,5,222,61,14,0,1,1,2,0,TEXT,Proteine:,37
TB,4,263,61,14,0,1,1,2,0,TEXT,Grasimi:,38
TB,5,243,61,14,0,1,1,2,0,TEXT,Glucide:,39
TB,69,222,47,16,0,1,1,2,0,DATA,remark1,Note1,2,1500,40
TB,69,244,47,16,0,1,1,2,0,DATA,remark2,Note2,2,1500,41
TB,69,264,47,16,0,1,1,2,0,DATA,remark3,Note3,2,1500,42
L,2,218,221,218,2,0,43
L,2,197,221,197,2,0,44
L,3,240,222,240,2,0,45
L,3,262,222,262,2,0,46
L,3,281,222,281,2,0,47
ROTATE,180
"""
v_text2 = b"""
^Q90,2
^W57
^H8
^P1
^S4
^AD
^C1
^R16
~Q-16
^O0
^D0
^E18
~R255
^L
Dy2-me-dd
Th:m:s
BE,101,543,2,5,54,0,1,123456789012
VA,20,89,1,1,0,0E,Tort Banana in caramela (0.5) DL
R0,616,427,617,1,1
VB,83,120,1,1,0,0E,Fabricat in moldova, SM 238:2004
VC,151,140,1,1,0,0E,Ingrediente:
VB,31,161,1,1,0,0E,faina de griu,oua de gaina,zahar,agenti de afinare
VB,24,179,1,1,0,0E, (E450),crem din frisca vegetala,sirop,banana,lapte
VB,82,194,1,1,0,0E,cond. fiert,ciocolata, brillo,colorant
R213,0,214,228,1,1
R0,253,209,457,2,2
VG,6,257,1,1,0,0E,Valoarea Nutritiva la 100g de produs:
ATB,215,245,17,17,0,0BE,B,0,Durata si conditii de pastrare:
ATB,215,265,17,17,0,0B,B,0,180 zile la temperatura 18 
ATB,215,285,17,17,0,0B,B,0,grade C, umiditatea relativa a 
ATB,215,305,17,17,0,0B,B,0,aerului 85%.
ATB,215,325,17,17,0,0B,B,0,A se consuma dupa 
ATB,215,345,17,17,0,0B,B,0,decongelare, a se decongela 
ATB,215,365,17,17,0,0B,B,0,la temperatura de camerei. Dupa 
ATB,215,385,17,17,0,0B,B,0,decongelare a se pastra la 
ATB,215,405,17,17,0,0B,B,0,frigider 48 ore la temperatura 
ATB,215,425,17,17,0,0B,B,0,4+-2 C
ATB,215,445,17,17,0,0B,B,0,Produsul nu se recongeleaza
ATB,197,469,20,20,0,0BE,B,0,Masa neta:      0.152 kg
ATB,338,500,20,20,0,0BE,B,0,Total
ATB,338,523,20,20,0,0BE,B,0,14.86
ATB,9,500,17,17,0,0BE,B,0,Data fabricarii:   04.05.2022 14:55
ATB,9,518,17,17,0,0BE,B,0,Data expirarii:     04.05.2022 14:55
ATB,28,470,17,17,0,0BE,B,0,Pret:    97.80
E
"""

import requests
import shutil

try:
    mysocket.connect((host, port))  # connecting to host
    mysocket.send(v_text2)
    mysocket.close()  # closing connection
except Exception as ex:
    print(ex)
    print("Error with the connection")
