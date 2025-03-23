import tkinter as tk
from tkinter import filedialog, messagebox
import re

def hyehyaa_nkyerɛmu(nkyerɛmu):
    """
    Saa fonkɛshan yi bɛyi nkyerɛmu mu nsensanee na ɛbɛma nsateaa nyɛ dodoɔ.
    - Ɛbɛyi nsateaa dodoɔ a ɛwɔ asɛm no mu
    - Ɛbɛma nsensanee (empty lines) nko ara ka nsɛm no ntam
    """
    nsɛm = nkyerɛmu.split('\n')
    nsɛm_akosiesie = []
    nsensanee = False  # Hwɛ sɛ nsensanee a ɛdɔɔso wɔ hɔ anaa

    for nsɛm_bi in nsɛm:
        nsɛm_siesie = re.sub(r'\s+', ' ', nsɛm_bi).strip()  # Yi nsateaa dodoɔ fi nsɛm no mu
        
        if nsɛm_siesie:
            nsɛm_akosiesie.append(nsɛm_siesie)
            nsensanee = False  # Sɛ nsɛm bi ba a, yɛmma nsensanee
        else:
            if not nsensanee:
                nsɛm_akosiesie.append('')  # Fa nsensanee baako pɛ na gyae
                nsensanee = True  # Kyerɛ sɛ nsensanee aba

    # Ma file no nwie ne nsensanee baako pɛ
    if nsɛm_akosiesie and nsɛm_akosiesie[-1] != '':
        nsɛm_akosiesie.append('')
    
    return '\n'.join(nsɛm_akosiesie)

def bue_file():
    """
    Fonkɛshan yi bɛma yɛatumi abue .txt file bi na ɛbɛda GUI no so.
    """
    file_nkrataa = filedialog.askopenfilename(filetypes=[("Nkrataa a ɛyɛ Text", "*.txt")])
    
    if file_nkrataa:
        with open(file_nkrataa, 'r', encoding='utf-8') as file:
            nkyerɛmu = file.read()
        
        text_editor.delete(1.0, tk.END)
        text_editor.insert(tk.END, nkyerɛmu)
        
        global file_ɛda
        file_ɛda = file_nkrataa

def sie_file(sie_foɔ=False):
    """
    Fonkɛshan yi bɛsie file no.
    - Sɛ ɛsɛ sɛ yebɔ din foforɔ a, ɛbɛfrɛ save as...
    """
    global file_ɛda

    if sie_foɔ or not file_ɛda:
        file_nkrataa = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Nkrataa a ɛyɛ Text", "*.txt")])
    else:
        file_nkrataa = file_ɛda

    if file_nkrataa:
        with open(file_nkrataa, 'w', encoding='utf-8') as file:
            file.write(text_editor.get(1.0, tk.END))
        
        messagebox.showinfo("Yɛyɛ!", "File no asie yie!")
        file_ɛda = file_nkrataa

def siesie_file():
    """
    Fonkɛshan yi bɛfa nsɛm a ɛwɔ editor no mu, na ɛbɛteateam no.
    """
    nkyerɛmu = text_editor.get(1.0, tk.END)
    nkyerɛmu_siesie = hyehyaa_nkyerɛmu(nkyerɛmu)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.END, nkyerɛmu_siesie)

# **GUI (Graphical User Interface) ho nsɛm**
root = tk.Tk()
root.title("Kal Text File Cleaner [KTF Cleaner]")

# **Nkrataa akyerɛwbea (Text Editor)**
text_editor = tk.Text(root, wrap='word')
text_editor.pack(expand=True, fill='both')

# **Menu Bar**
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# **File Menu**
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Nkrataa", menu=file_menu)
file_menu.add_command(label="Bue", command=bue_file)
file_menu.add_command(label="Sie", command=sie_file)
file_menu.add_command(label="Sie Sɛ...", command=lambda: sie_file(sie_foɔ=True))
file_menu.add_separator()
file_menu.add_command(label="Gyae", command=root.quit)

# **Clean Menu**
clean_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Siesie", menu=clean_menu)
clean_menu.add_command(label="Siesie Nkrataa", command=siesie_file)

file_ɛda = None

# **Run GUI no**
root.mainloop()
