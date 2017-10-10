# -*- coding: utf-8 -*-
from datetime import date

hj = date.today()
ano = str(hj.year)
dia = str(hj.day)

if hj.month == 1:
    mes = ("Janeiro")
elif hj.month == 2:
    mes = ("Fevereiro")
elif hj.month == 3:
    mes = ("Março")
elif hj.month == 4:
    mes = ("Abril")
elif hj.month == 5:
    mes = ("Maio")
elif hj.month == 6:
    mes = ("Junho")
elif hj.month == 7:
    mes = ("Julho")
elif hj.month == 8:
    mes = ("Agosto")
elif hj.month == 9:
    mes = ("Setembro")
elif hj.month == 10:
    mes = ("Outubro")
elif hj.month == 11:
    mes = ("Novembro")
elif hj.month == 12:
    mes = ("Dezembro")

db = DAL('sqlite://livrocaixa.edb')
