from coinbase.wallet.client import Client
import time
from playsound import playsound
import sys

client = Client('xkOqNAojzWlATB2b', 't6pFXekGdWasj6dPntciPOzWMSzBAUvn')
value = float(sys.argv[2])
state = sys.argv[1]
if(len(sys.argv)>3):
    value2 = float(sys.argv[3])

while True:
    currencies = client.get_buy_price(currency_pair = 'FIL-BRL');
    print(currencies['amount'])
    if(state == 'abaixo'):
        if(float(currencies['amount']) <= value):
            playsound('alert.mp3')
            print('Ta abaixo');
    elif(state == 'acima'):
        if(float(currencies['amount']) >= value):
            playsound('alert.mp3')
            print('Ta acima');
    else:
        if(float(currencies['amount']) >= value):
            playsound('alert.mp3')
            print('Ta acima');
        if(float(currencies['amount']) <= value2):
            playsound('alert.mp3')
            print('Ta abaixo');
    time.sleep(15)
