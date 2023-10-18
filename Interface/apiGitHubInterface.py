import tkinter as tk
from tkinter import ttk
import requests

def on_search():
    user_name = entry_user.get()
    repo_name = entry_repo.get()

    result_text.config(state='normal', bg='#431c53', fg='white')  # Cor de fundo e texto

    if not user_name:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Por favor, insira o nome de um usuário do GitHub.")
    elif not repo_name:
        # Se o nome do repositório estiver vazio, listar todos os repositórios do usuário
        result = get_user_repos(user_name)
        if result:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Repositórios de " + user_name + ":\n" + '\n'.join(result))
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Nenhum repositório encontrado para " + user_name)
    else:
        # Se houver um nome de repositório, obter informações sobre esse repositório
        repo_info = get_repo_info(user_name, repo_name)
        if repo_info:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Repositório: {repo_info['name']}\nDescrição: {repo_info['description']}")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Repositório {repo_name} não encontrado para o usuário {user_name}")

    result_text.config(state='disabled')  # Desabilita a edição do Text

def get_user_repos(user_name):
    url = f"https://api.github.com/users/{user_name}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = [repo['name'] for repo in response.json()]
        return repos
    else:
        return None

def get_repo_info(user_name, repo_name):
    url = f"https://api.github.com/repos/{user_name}/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        repo_info = response.json()
        return repo_info
    else:
        return None

# Criar a janela principal
root = tk.Tk()
root.title("GitHub Repository Info")
root.configure(bg='#251627')  # Roxo escuro
#Defines window height and width
window_height = 350
window_width = 500

#Receives screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
games = []
#Define coordinates based on monitor 
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

#Defines the screen geometry
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
# Adicionar frame acinzentado
style = ttk.Style()
style.configure('TFrame', background='#4B0082')  # Roxo escuro

frame = ttk.Frame(root, padding=(10, 10, 10, 10), style='TFrame')
frame.pack(pady=10)

# Adicionar widgets ao frame
label_user = ttk.Label(frame, text="Digite o nome do usuário do GitHub:")
label_user.grid(row=0, column=0, padx=5, pady=5, sticky='w')  # Adicionando sticky='w' para alinhar à esquerda

entry_user = ttk.Entry(frame, width=20, font=('Helvetica', 12))
entry_user.grid(row=0, column=1, padx=5, pady=5, sticky='w')  # Adicionando sticky='w' para alinhar à esquerda

label_repo = ttk.Label(frame, text="Digite o nome do repositório (opcional):")
label_repo.grid(row=1, column=0, padx=5, pady=5, sticky='w')  # Adicionando sticky='w' para alinhar à esquerda

entry_repo = ttk.Entry(frame, width=20, font=('Helvetica', 12))
entry_repo.grid(row=1, column=1, padx=5, pady=5, sticky='w')  # Adicionando sticky='w' para alinhar à esquerda

search_button = ttk.Button(frame, text="Pesquisar", command=on_search)
search_button.grid(row=2, column=0, columnspan=2, pady=5, sticky='w')  # Adicionando sticky='w' para alinhar à esquerda

# Adicionar uma barra de rolagem
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Adicionar widget de Text para exibir resultados
result_text = tk.Text(root, wrap="none", height=10, width=40, state='disabled', yscrollcommand=scrollbar.set,background="#491e3c")
result_text.pack(pady=10)

# Configurar a barra de rolagem para o widget de Text
scrollbar.config(command=result_text.yview)

# Estilo para o frame acinzentado
style = ttk.Style()
style.configure('TFrame', background='#431c53')  # Roxo escuro

# Iniciar o loop principal
root.mainloop()
