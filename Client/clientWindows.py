import socket
import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# =================== FONCTIONS =====================

def apply_theme(dark):
    colors = {
        "bg": "#2E2E2E" if dark else "#F0F0F0",
        "fg": "#FFFFFF" if dark else "#000000",
        "button_bg": "#444444" if dark else "#E0E0E0",
        "entry_bg": "#3C3C3C" if dark else "#FFFFFF"
    }

    root.configure(bg=colors["bg"])
    for widget in root.winfo_children():
        cls = widget.__class__.__name__
        if cls in ["Label", "Button"]:
            widget.configure(bg=colors["bg"], fg=colors["fg"])
            if cls == "Button":
                widget.configure(activebackground=colors["button_bg"])
        elif cls == "Entry":
            widget.configure(bg=colors["entry_bg"], fg=colors["fg"], insertbackground=colors["fg"])
        elif cls == "TFrame":
            widget.configure(style="Dark.TFrame")

    style.configure("TProgressbar", troughcolor=colors["entry_bg"], background="#1DB954")

def toggle_theme():
    global is_dark
    is_dark = not is_dark
    apply_theme(is_dark)
    btn_theme.configure(text="☀️ Mode clair" if is_dark else "🌙 Mode sombre")

def send(path, is_folder):
    ip = entry_ip.get()
    port = int(entry_port.get())

    try:
        if is_folder:
            zip_name = os.path.basename(path.rstrip("/\\")) + ".zip"
            zip_path = os.path.join(os.getcwd(), zip_name)
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root_dir, dirs, files in os.walk(path):
                    for file in files:
                        abs_path = os.path.join(root_dir, file)
                        rel_path = os.path.relpath(abs_path, start=path)
                        zipf.write(abs_path, arcname=rel_path)
            file_to_send = zip_path
        else:
            file_to_send = path

        filename = os.path.basename(file_to_send)
        filesize = os.path.getsize(file_to_send)
        progress_bar['maximum'] = filesize
        progress_bar['value'] = 0

        with socket.socket() as s:
            s.connect((ip, port))
            metadata = f"{filename}|{filesize}\n".encode('utf-8')
            s.sendall(metadata)

            with open(file_to_send, "rb") as f:
                sent = 0
                while (chunk := f.read(4096)):
                    s.sendall(chunk)
                    sent += len(chunk)
                    progress_bar['value'] = sent
                    root.update_idletasks()

        if is_folder:
            os.remove(file_to_send)

        progress_bar['value'] = 0
        messagebox.showinfo("Succès", f"{'Dossier' if is_folder else 'Fichier'} envoyé avec succès.")

    except Exception as e:
        progress_bar['value'] = 0
        messagebox.showerror("Erreur", str(e))

def choose_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        send(filepath, is_folder=False)

def choose_folder():
    folderpath = filedialog.askdirectory()
    if folderpath:
        send(folderpath, is_folder=True)

# =================== INTERFACE =====================

root = tk.Tk()
root.title("Client d'envoi - Fichier & Dossier")
root.geometry("420x300")

style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", thickness=20)

is_dark = False

tk.Label(root, text="IP du serveur :").pack()
entry_ip = tk.Entry(root)
entry_ip.pack()
entry_ip.insert(0, "192.168.0.17")

tk.Label(root, text="Port :").pack()
entry_port = tk.Entry(root)
entry_port.pack()
entry_port.insert(0, "5000")

tk.Button(root, text="📁 Envoyer un dossier", command=choose_folder).pack(pady=10)
tk.Button(root, text="📄 Envoyer un fichier", command=choose_file).pack(pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=20)

btn_theme = tk.Button(root, text="🌙 Mode sombre", command=toggle_theme)
btn_theme.pack(pady=10)

apply_theme(is_dark)

root.mainloop()
