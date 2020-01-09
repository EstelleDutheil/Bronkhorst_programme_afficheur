from convertisseur_n_hexaDecimal_en_string_chr import*
from convertisseur_string_chr_en_n_hexaDecimal import*
from convertisseur_1int_1byte import*
from convertisseur_1byte_1int import*
from convertisseur_4hexaDecimal_1float import*
from convertisseur_1float_4hexaDecimal import*

def Identification_string_1(commande_1,valeur_1,portSerie_1):
    if commande_1=='L':
        portSerie_1.write(b':078004006100600F\r\n')
        reponse_1=portSerie_1.readline()
        reponse_1=conversion_n_hexaDecimal_en_string_chr(reponse_1[13:50])
        return(reponse_1)
    elif commande_1=='E':
        valeur_1=conversion_string_chr_en_n_hexaDecimal(valeur_1)
        longueur_1=len(valeur_1)
        longueur_1=longueur_1+4
        nbre_hexa_trame=conversion_1int_1byte(longueur_1)
        ecrit_1=b':'+nbre_hexa_trame+b'80020061'+valeur_1+b'\r\n'
        portSerie_1.write(ecrit_1)

def Primary_node_address_2(commande_2,valeur_2,portSerie_2):
    if commande_2=='L':
        portSerie_2.write(b':06800400010001\r\n')
        reponse_2=portSerie_2.readline()
        reponse_2=conversion_1byte_1int(reponse_2[11:13])
        return(reponse_2)

def Initreset_7(commande_7,valeur_7,portSerie_7):
    if commande_7=='L':
      portSerie_7.write(b':0680040001000A\r\n')
      reponse_7=portSerie_7.readline()
      reponse_7=conversion_1byte_1int(reponse_7[11:13])
      return(reponse_7)
    elif commande_7=='E':
      valeur_7=conversion_1int_1byte(valeur_7)
      ecrit_7=b':058002000A'+valeur_7+b'\r\n'
      portSerie_7.write(ecrit_7)

def Control_mode_12(commande_12,valeur_12,portSerie_12):
    if commande_12=='L':
      portSerie_12.write(b':06800401040104\r\n')
      reponse_12=portSerie_12.readline()
      reponse_12=conversion_1byte_1int(reponse_12[11:13])
      return(reponse_12)
    elif commande_12=='E':
      valeur_12=conversion_1int_1byte(valeur_12)
      ecrit_12=b':0580020104'+valeur_12+b'\r\n'
      portSerie_12.write(ecrit_12)

def Capacity_21(commande_21,valeur_21,portSerie_21):
    if commande_21=='L':
      portSerie_21.write(b':068004014D014D\r\n')
      reponse_21=portSerie_21.readline()
      reponse_21=conversion_4hexaDecimal_1float(reponse_21[11:19],2)
      return(reponse_21)
    elif commande_21=='E':
      valeur_21=conversion_1float_4hexaDecimal(valeur_21)
      ecrit_21=b':088002014D'+valeur_21+b'\r\n'
      portSerie_21.write(ecrit_21)

def Fluid_name_25(commande_25,valeur_25,portSerie_25):
    if commande_25=='L':
        portSerie_25.write(b':078004017101710F\r\n')
        reponse_25=portSerie_25.readline()
        reponse_25=conversion_n_hexaDecimal_en_string_chr(reponse_25[13:50])
        return(reponse_25)
    elif commande_25=='E':
        valeur_25=conversion_string_chr_en_n_hexaDecimal(valeur_25)
        longueur_25=len(valeur_25)
        longueur_25=longueur_25+4
        nbre_hexa_trame=conversion_1int_1byte(longueur_25)
        ecrit_25=b':'+nbre_hexa_trame+b'80020171'+valeur_25+b'\r\n'
        portSerie_25.write(ecrit_25)

def BHT_Model_number_91(commande_91,valeur_91,portSerie_91):
  if commande_91=='L':
    portSerie_91.write(b':0780047162716215\r\n')
    reponse_91=portSerie_91.readline()
    reponse_91=conversion_n_hexaDecimal_en_string_chr(reponse_91[13:55])
    return(reponse_91)
  elif commande_91=='E':
    valeur_91=conversion_string_chr_en_n_hexaDecimal(valeur_91)
    longueur_91=len(valeur_91)
    longueur_91=longueur_91+4
    nbre_hexa_trame=conversion_1int_1byte(longueur_91)
    ecrit_91=b':'+nbre_hexa_trame+b'80027162'+valeur_91+b'\r\n'
    portSerie_91.write(ecrit_91)

def Serial_number_92(commande_92,valeur_92,portSerie_92):
  if commande_92=='L':
    portSerie_92.write(b':078004716371630F\r\n')
    reponse_92=portSerie_92.readline()
    reponse_92=conversion_n_hexaDecimal_en_string_chr(reponse_92[13:50])
    return(reponse_92)
  elif commande_92=='E':
    valeur_92=conversion_string_chr_en_n_hexaDecimal(valeur_92)
    longueur_92=len(valeur_92)
    longueur_92=longueur_92+4
    nbre_hexa_trame=conversion_1int_1byte(longueur_92)
    ecrit_92=b':'+nbre_hexa_trame+b'80027163'+valeur_92+b'\r\n'
    portSerie_92.write(ecrit_92)

def Capacity_unit_129(commande_129,valeur_129,portSerie_129):
  if commande_129=='L':
    portSerie_129.write(b':078004017F017F0F\r\n')
    reponse_129=portSerie_129.readline()
    reponse_129=conversion_n_hexaDecimal_en_string_chr(reponse_129[13:50])
    return(reponse_129)
  elif commande_129=='E':
    valeur_129=conversion_string_chr_en_n_hexaDecimal(valeur_129)
    longueur_129=len(valeur_129)
    longueur_129=longueur_129+4
    nbre_hexa_trame=conversion_1int_1byte(longueur_129)
    ecrit_129=b':'+nbre_hexa_trame+b'8002017F'+valeur_129+b'\r\n'
    portSerie_129.write(ecrit_129)

def PID_Kp_167(commande_167,valeur_167,portSerie_167):
  if commande_167=='L':
    portSerie_167.write(b':06800472557255\r\n')
    reponse_167=portSerie_167.readline()
    reponse_167=conversion_4hexaDecimal_1float(reponse_167[11:19],2)
    return(reponse_167)
  elif commande_167=='E':
    valeur_167=conversion_1float_4hexaDecimal(valeur_167)
    ecrit_167=b':0880027255'+valeur_167+b'\r\n'
    portSerie_167.write(ecrit_167)

def PID_Ti_168(commande_168,valeur_168,portSerie_168):
  if commande_168=='L':
    portSerie_168.write(b':06800472567256\r\n')
    reponse_168=portSerie_168.readline()
    reponse_168=conversion_4hexaDecimal_1float(reponse_168[11:19],2)
    return(reponse_168)
  elif commande_168=='E':
    valeur_168=conversion_1float_4hexaDecimal(valeur_168)
    ecrit_168=b':0880027256'+valeur_168+b'\r\n'
    portSerie_168.write(ecrit_168)

def PID_Td_169(commande_169,valeur_169,portSerie_169):
  if commande_169=='L':
    portSerie_169.write(b':06800472577257\r\n')
    reponse_169=portSerie_169.readline()
    reponse_169=conversion_4hexaDecimal_1float(reponse_169[11:19],2)
    return(reponse_169)
  elif commande_169=='E':
    valeur_169=conversion_1float_4hexaDecimal(valeur_169)
    ecrit_169=b':0880027257'+valeur_169+b'\r\n'
    portSerie_169.write(ecrit_169)

def fMeasure_205(commande_205,valeur_205,portSerie_205):
  if commande_205=='L':
    portSerie_205.write(b':06800421402140\r\n')
    reponse_205=portSerie_205.readline()
    reponse_205=conversion_4hexaDecimal_1float(reponse_205[11:19],2)
    return(reponse_205)

def fSetpoint_206(commande_206,valeur_206,portSerie_206):
  if commande_206=='L':
    portSerie_206.write(b':06800421432143\r\n')
    reponse_206=portSerie_206.readline()
    reponse_206=conversion_4hexaDecimal_1float(reponse_206[11:19],2)
    return(reponse_206)
  elif commande_206=='E':
    valeur_206=conversion_1float_4hexaDecimal(valeur_206)
    ecrit_206=b':0880022143'+valeur_206+b'\r\n'
    portSerie_206.write(ecrit_206)
