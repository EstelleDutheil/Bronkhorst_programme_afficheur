import serial
import serial.tools.list_ports

def listing_ports():
    comList=list(serial.tools.list_ports.comports())
    liste=['']*len(comList)
    for bla in range(0,len(comList)):
        ref=comList[bla].description
        liste[bla]=ref
    return(liste)

def cree_ports_bus():
    comList=serial.tools.list_ports.comports()
    nbre=0
    ser=[""]*20
    for bla in range(0,len(comList)):
        serTest=serial.Serial(comList[bla].device,38400,timeout=1)
        serTest.write(b':0780047163716309\r\n')
        reponse=serTest.readline()
        print(reponse)
        serTest.close()
        if(reponse[0:11]==b':0E80027163'):
            ser[nbre]=serial.Serial(comList[bla].device,38400,timeout=1)
            nbre=nbre+1
    return(ser)

#def cree_port_unique():
    #comList=serial.tools.list_ports.comports()
    #reponse=b''
    #for bla in range(0,len(comList)):
        #ser=serial.Serial(comList[bla].device,38400,timeout=1)
        #while reponse[0:11]!=b':0E80027163':
            #ser.write(b':0780047163716309\r\n')
            #reponse=ser.readline()
    #return(ser)

def cree_port_unique():
    comList=serial.tools.list_ports.comports()
    #print(comList)
    #ser=""
    for bla in range(0,len(comList)):
        for ble in range(0,5):
            serTest=serial.Serial(comList[bla].device,38400,timeout=1)
            serTest.write(b':0780047163716309\r\n')
            reponse=serTest.readline()
            serTest.close()
            if(reponse[0:11]==b':0E80027163'):
                ser=serial.Serial(comList[bla].device,38400,timeout=1)
                break
    return(ser)
