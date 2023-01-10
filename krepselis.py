from tkinter import*
from tkinter import filedialog
import pickle

langas = Tk()
langas.geometry("220x310")


#pasirinkta saraso elemnto indeksa laikome atskirai
pasirinkta = IntVar()


def _atzymejimas():
    b_keisti['state'] = DISABLED
    b_trinti['state'] = DISABLED
    e_preke.delete(0, END)
    box_prekes.selection_clear(0, END)
    pasirinkta.set(-1)


def nauja_preke():
    preke = e_preke.get()
    if preke:
        box_prekes.insert(END, preke)
        status['text'] = f'Pridėta prekė {preke}'
    _atzymejimas



def pazymeta_preke(ivykis):
    prekes = ivykis.widget
    try:
        index = prekes.curselection()[0]
    except IndexError:
        pass
    else:
        pasirinkta.set(index)
        preke = prekes.get(index)
        status['text'] = f'Pažymėta prekė {preke}'
        e_preke.delete(0, END)
        e_preke.insert(0, preke)
        b_keisti['state'] = NORMAL
        b_trinti['state'] = NORMAL

def keisti_preke():
    index = pasirinkta.get()
    sena_preke = box_prekes.get(index)
    nauja_preke = e_preke.get()
    box_prekes.delete(index)
    box_prekes.insert(index, nauja_preke)
    status['text'] = f'{sena_preke} pakeista i {nauja_preke}'
    _atzymejimas()

def trinti_preke():
    index = pasirinkta.get()
    sena_preke = box_prekes.get(index)
    box_prekes.delete(index)
    status['text'] = f'{sena_preke} pasalinta'  
    _atzymejimas()

def naujas_krepselis():
    box_prekes.delete(0, END)
    status['text'] = 'Krepselis isvalytas'
    _atzymejimas()

def issaugoti_krepseli():
    pkl_pavadinimas = filedialog.asksaveasfilename(defaultextension="pkl", filetypes=(("Pickle", ".pkl"),))
    if pkl_pavadinimas:
        with open (pkl_pavadinimas, "wb") as pkl:
            pickle.dump(box_prekes.get(0, END), pkl)
        status["text"] = f'krepselis issaugotas i {pkl_pavadinimas}'


def atidaryti_krepseli():
    pkl_pavadinimas = filedialog.askopenfilename(defaultextension=".pkl")
    if pkl_pavadinimas:
        with open(pkl_pavadinimas, 'rb') as pkl:
            box_prekes.delete(0, END)
            box_prekes.insert(0, *pickle.load(pkl))
        status['text'] = f'Krepselis atidaryti is {pkl_pavadinimas}'
        _atzymejimas()    

#sukuriam meniu ir meniu idedam krepselis submeniu su esminem funkcijom
m_pagrindinis = Menu(langas)
langas.config(menu=m_pagrindinis)
m_krepselis = Menu(m_pagrindinis, tearoff=0)
m_pagrindinis.add_cascade(label="krepselis", menu=m_krepselis)
m_krepselis.add_command(label="naujas", command=naujas_krepselis)
m_krepselis.add_command(label="Isaugoti", command=issaugoti_krepseli)
m_krepselis.add_command(label="Atidaryti", command=atidaryti_krepseli)
m_krepselis.add_separator()
m_krepselis.add_command(label="uzdaryti", command=langas.destroy)





l_prekes = Label(langas, text="Produktai")
#sukuriam konteineri prekiu sarasui
f_prekes = Frame(langas)
box_prekes = Listbox(f_prekes, selectmode=SINGLE, width=23)
box_prekes.bind('<<ListboxSelect>>', pazymeta_preke)
box_prekes_scroll = Scrollbar(f_prekes, command=box_prekes.yview)
box_prekes.config(yscrollcommand=box_prekes_scroll.set)

#sukuriam konteineri valdymo elementams (mygtukams, ivesties laukui)
f_control = Frame(langas)
e_preke = Entry(f_control)
b_naujas = Button(f_control, text="+", command=nauja_preke)
b_keisti = Button(f_control, text="atnaujinti", state=DISABLED, command=keisti_preke)
b_trinti = Button(f_control, text="-", state=DISABLED, command=trinti_preke)

#statuso juosta, skirta pranesimam, vietoje pamegto "print"
status = Label(langas, text="laukiame veiksmų", relief=SUNKEN, border=1,  wraplength=240, justify=CENTER)

#supakuojam vartotjo sasajos konteinerius ir elementus bedrai isdestyma ir paleidziame langa
l_prekes.pack()
f_prekes.pack()
box_prekes.pack(side=LEFT)
box_prekes_scroll.pack(side=RIGHT, fill=Y)
f_control.pack()
e_preke.grid(row=0, column=0)
b_naujas.grid(row=0, column=1)
b_keisti.grid(row=1, column=0)
b_trinti.grid(row=1, column=1)
status.pack(side=BOTTOM, fill=X)

langas.mainloop()