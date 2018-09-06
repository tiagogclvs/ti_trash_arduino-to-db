#  /////////////////////
# //       TI-Trash      //
# //                     //
# //       Author:       //
# //   Tiago Goncalves   //
#   /////////////////////

#Testado com Python 2.7.13 e Arduino UNO

import sqlite3
import serial

dbConn = sqlite3.connect('C:\\xamp1\htdocs\Projeto\db.db')
cursor = dbConn.cursor()

device = "COM4"
# porta do arduino uno

try:
    print("CONECTANDO A PORTA ", device)
    arduino = serial.Serial(device, 9600)
    print("CONECTADO")
    print("")
except:
    print("FALHA A CONECTAR A ", device)

while True:
    try:
        data = arduino.readline()  # ler output do arduino ide
        pieces = data.split("\t")  # dividir dados a partir do ta
        
        try:
            cursor.execute("INSERT INTO garbage (rfid, user_id, container_id, quantity, timestamp) VALUES (?,?,?,?,?)", (pieces[0], pieces[1], pieces[2], pieces[3], pieces[4]))
            dbConn.commit()  # executar a insercao
            print("Peso Registado")
            print("RFID: {} | CONTAINER: {} | QUANTITY: {} | DATE: {}".format(pieces[0],pieces[2],pieces[3],pieces[4]))
    
        except sqlite3.IntegrityError:
            print("FALHA AO INSERIR DADOS")
    
    finally:
        print("")
        

