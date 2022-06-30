import requests
from tkinter import *

def getInformation(): 
    requisition = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisition_dic = requisition.json()
    
    cotation_dolar = requisition_dic['USDBRL']['bid']
    cotation_euro = requisition_dic['EURBRL']['bid']
    cotation_btc = requisition_dic['BTCBRL']['bid']
    
    text = f'''
    Dolar: {cotation_dolar}
    Euro: {cotation_euro}
    BTC: {cotation_btc} '''
    
    text_cotations["text"] = text
    


scream = Tk()
scream.title("Cotations Importants")
scream.geometry("300x300")

textOrientation = Label(scream, text  = "Click in button for to see the contations")
textOrientation.grid(column=0, row =0, padx = 10, pady = 10)
textOrientation = Label(scream, text  = "Click here, now")
textOrientation.grid(column=0, row =1, padx = 10, pady = 10)

button = Button(scream, text = 'Search cotation Dolar/Euro/Btc', command = getInformation)
button.grid(column = 0, row = 1, padx = 10, pady = 10)

text_cotations = Label(scream, text = "")
text_cotations.grid(column = 0, row = 2, padx = 10, pady = 10)

scream.mainloop()
