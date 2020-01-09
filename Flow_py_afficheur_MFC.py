from tkinter import*
from tkinter.messagebox import*
from recherche_creation_ports import*
from trames_fonctions import*

numeroDeSerie=''

class instrument:
    def __init__(self):
        self.nom="INSTRUMENT"

    def liste_port(self):
        port_disponible=listing_ports()
        return(port_disponible)

    def cree_port(self):
        monPort=cree_port_unique()
        return(monPort)

    def Control_mode(self,monPort,modeControle):
        Control_mode_12('E',modeControle,monPort)

    def laCapacite(self,monPort):
        capacite=Capacity_21('L',0,monPort)
        return(capacite)

    def numeroSerie(self,monPort):
        numeroDeSerie=Serial_number_92('L',0,monPort)
        return(numeroDeSerie)

    def capaciteUnit(self,monPort):
        uniteCapacite=Capacity_unit_129('L',0,monPort)
        return(uniteCapacite)

    def laMesure(self,monPort):
        maMesure=fMeasure_205('L',0,monPort)
        return(maMesure)

    def laConsigne(self,monPort,consigne):
        fSetpoint_206('E',consigne,monPort)

canal1=instrument()
portDisponible=canal1.liste_port()
nbrePort=len(portDisponible)
monPort=canal1.cree_port()

lesCOMs=[""]*20
for bla in range(0,nbrePort):
    lesCOMs[bla]=str(portDisponible[bla])

if monPort=="":
  port_actif="Pas d'instrument en ligne"
  instruction="Pour sortir fermer cette fenêtre"
else:
  port_actif="Un instrument en ligne"
  instruction="Pour poursuivre : fermer cette fenêtre"

fenCom=Tk()
fenCom.geometry("400x400+150+50")
fenCom.title("CONFUGURATION")
fenCom['bg']='white'

etiquette_port_actif=Label(fenCom,text=port_actif,bg='white',font="ARIAL 15",fg='red')
etiquette_port_actif.pack()
for bla in range(0,nbrePort):
    etiquette_port_present=Label(fenCom,text=lesCOMs[bla],bg='white',font="ARIAL 12",fg='blue')
    etiquette_port_present.pack()
etiquette_instruction=Label(fenCom,text=instruction,bg='white',font="ARIAL 15",fg='red')
etiquette_instruction.pack()
fenCom.mainloop()

if monPort !="":
    while numeroDeSerie=='':
        numeroDeSerie=canal1.numeroSerie(monPort)
    canal1.Control_mode(monPort,0)
    mesure=canal1.laMesure(monPort)
    capacite=canal1.laCapacite(monPort)
    unite=canal1.capaciteUnit(monPort)

    def admission_consigne():
        valeur=ent1.get()
        valeur=float(valeur)
        if valeur>capacite:
            message_erreur_cons_max()
        if valeur<(capacite/50)and valeur>0:
            message_erreur_cons_min()
        canal1.laConsigne(monPort,valeur)

    def message_erreur_cons_max():
        maxi='Consigne maximale = '+str(capacite)
        showerror('Attention ', maxi +''+unite)

    def message_erreur_cons_min():
        miniCapacite=capacite/50
        mini='Consigne minimale = '+str(miniCapacite)
        showerror('Attention ', mini +''+unite)

    counter=0
    def report_mesure(etiquette_mesure_reelle):
        def count():
            global counter
            counter += 1
            valeur_mesure=str(canal1.laMesure(monPort))
            etiquette_mesure_reelle.config(text=valeur_mesure+" "+unite)
            etiquette_mesure_reelle.after(100, count)
        count()

    fen=Tk()
    fen.geometry("450x150+50+50")
    fen.title("Affichage du flux")
    fen['bg']='gray95'

    etiquette_serie=Label(fen,text=numeroDeSerie,bg="#88ff88",width=65,font="ARIAL 20",fg='blue')
    etiquette_serie.pack()

    etiquette_mesure=Label(fen,text="MESURE",bg="gray96",fg="green",font="ARIAL 15")
    etiquette_mesure.place(x='40',y='50')

    etiquette_consigne=Label(fen,text="CONSIGNE",bg="gray96",fg="red",font="ARIAL 15")
    etiquette_consigne.place(x='270',y='50')

    etiquette_mesure_reelle=Label(fen,bg="gray96",fg="green",font="ARIAL 30")
    etiquette_mesure_reelle.place(x='35',y='85')
    report_mesure(etiquette_mesure_reelle)
    bouton=Button(fen,text='oK',command=admission_consigne,bg="gray96",fg="blue",bd=5,font="ARIAL 10")
    bouton.place(x='400',y='90')
    ent1=Entry(fen,width=10,font="ARIAL 18",bd=5)
    ent1.place(x='250',y='90')
    
    fen.mainloop()
