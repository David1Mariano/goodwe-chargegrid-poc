import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from demand_manager import DemandManager
from ai_manager import AIManager
from billing import Billing


class ChargeGridApp:

    def __init__(self, root):

        self.root = root
        self.root.title("ChargeGrid Intelligence")
        self.root.geometry("900x700")
        self.root.configure(bg="#f2f2f2")

        self.distribuicao_atual = []
        self.total_custo = 0

        titulo = tk.Label(
            root,
            text="ChargeGrid Intelligence",
            font=("Arial", 22, "bold"),
            bg="#f2f2f2"
        )
        titulo.pack(pady=10)

        entrada_frame = tk.LabelFrame(
            root,
            text="Dados dos Carregadores",
            padx=15,
            pady=15
        )
        entrada_frame.pack(pady=10)

        tk.Label(entrada_frame, text="Limite de Energia (kW)").grid(row=0, column=0, padx=5, pady=5)
        self.limite_entry = tk.Entry(entrada_frame)
        self.limite_entry.grid(row=0, column=1)

        tk.Label(entrada_frame, text="Carregador 1 (Fabricante A)").grid(row=1, column=0, padx=5, pady=5)
        self.c1 = tk.Entry(entrada_frame)
        self.c1.grid(row=1, column=1)

        tk.Label(entrada_frame, text="Carregador 2 (Fabricante B)").grid(row=2, column=0, padx=5, pady=5)
        self.c2 = tk.Entry(entrada_frame)
        self.c2.grid(row=2, column=1)

        tk.Label(entrada_frame, text="Carregador 3 (Fabricante C)").grid(row=3, column=0, padx=5, pady=5)
        self.c3 = tk.Entry(entrada_frame)
        self.c3.grid(row=3, column=1)

        botoes_frame = tk.Frame(root, bg="#f2f2f2")
        botoes_frame.pack(pady=10)

        ttk.Button(
            botoes_frame,
            text="Otimizar Distribuição",
            command=self.processar
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            botoes_frame,
            text="Gerar Relatório",
            command=self.gerar_relatorio
        ).grid(row=0, column=1, padx=10)

        cards_frame = tk.Frame(root, bg="#f2f2f2")
        cards_frame.pack(pady=15)

        self.card_limite = self.criar_card(cards_frame, "Limite")
        self.card_limite.grid(row=0, column=0, padx=10)

        self.card_demanda = self.criar_card(cards_frame, "Demanda")
        self.card_demanda.grid(row=0, column=1, padx=10)

        self.card_distribuido = self.criar_card(cards_frame, "Distribuído")
        self.card_distribuido.grid(row=0, column=2, padx=10)

        self.card_custo = self.criar_card(cards_frame, "Custo Total")
        self.card_custo.grid(row=0, column=3, padx=10)

        status_frame = tk.LabelFrame(
            root,
            text="Status da IA",
            padx=10,
            pady=10
        )
        status_frame.pack(pady=10, fill="x", padx=20)

        self.status_label = tk.Label(
            status_frame,
            text="Aguardando análise...",
            justify="left",
            font=("Arial", 10)
        )

        self.status_label.pack(anchor="w")

        resultado_frame = tk.LabelFrame(
            root,
            text="Resultados",
            padx=10,
            pady=10
        )

        resultado_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.resultado = tk.Text(
            resultado_frame,
            height=12
        )

        self.resultado.pack(fill="both", expand=True)

    def criar_card(self, parent, titulo):

        frame = tk.Frame(
            parent,
            bg="white",
            relief="raised",
            bd=2,
            width=150,
            height=80
        )

        frame.pack_propagate(False)

        tk.Label(
            frame,
            text=titulo,
            font=("Arial", 10, "bold"),
            bg="white"
        ).pack()

        valor = tk.Label(
            frame,
            text="--",
            font=("Arial", 14),
            bg="white"
        )

        valor.pack(expand=True)

        frame.valor = valor

        return frame

    def processar(self):

        try:

            limite = float(self.limite_entry.get())

            demandas = [
                float(self.c1.get()),
                float(self.c2.get()),
                float(self.c3.get())
            ]

            demanda_total = sum(demandas)

            limite_ajustado = AIManager.ajustar_limite(limite)

            gerenciador = DemandManager(limite_ajustado)

            distribuicao = gerenciador.distribuir_energia(demandas)

            self.distribuicao_atual = distribuicao

            self.resultado.delete("1.0", tk.END)

            custo_total = 0

            for i, energia in enumerate(distribuicao, start=1):

                custo = Billing.calcular_custo(energia)

                custo_total += custo

                self.resultado.insert(
                    tk.END,
                    f"Carregador {i}: {energia:.2f} kW | Custo: R$ {custo:.2f}\n"
                )

            self.resultado.insert(
                tk.END,
                "\nInteroperabilidade:\n"
                "Todos os carregadores foram integrados via protocolo aberto.\n"
            )

            self.total_custo = custo_total

            self.card_limite.valor.config(
                text=f"{limite_ajustado:.2f} kW"
            )

            self.card_demanda.valor.config(
                text=f"{demanda_total:.2f} kW"
            )

            self.card_distribuido.valor.config(
                text=f"{sum(distribuicao):.2f} kW"
            )

            self.card_custo.valor.config(
                text=f"R$ {custo_total:.2f}"
            )

            status = []

            if AIManager.horario_pico():
                status.append("⚠ Horário de pico detectado")
                status.append("✓ Potência reduzida automaticamente")
            else:
                status.append("✓ Horário normal")

            if demanda_total > limite:
                status.append("✓ Sobrecarga evitada")
                status.append("✓ Distribuição otimizada")
            else:
                status.append("✓ Energia distribuída normalmente")

            self.status_label.config(
                text="\n".join(status)
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Digite apenas números válidos."
            )

    def gerar_relatorio(self):

        if not self.distribuicao_atual:

            messagebox.showwarning(
                "Aviso",
                "Execute a simulação primeiro."
            )

            return

        nome_arquivo = "relatorio_chargegrid.txt"

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

            arquivo.write("CHARGEGRID INTELLIGENCE\n")
            arquivo.write("=" * 40 + "\n\n")

            arquivo.write(
                f"Data: {datetime.now()}\n\n"
            )

            arquivo.write(
                f"Limite de Energia: {self.limite_entry.get()} kW\n\n"
            )

            for i, energia in enumerate(self.distribuicao_atual, start=1):

                arquivo.write(
                    f"Carregador {i}: {energia:.2f} kW\n"
                )

            arquivo.write(
                f"\nValor Total: R$ {self.total_custo:.2f}\n"
            )

            arquivo.write(
                "\nStatus: Distribuição Inteligente Concluída\n"
            )

        messagebox.showinfo(
            "Sucesso",
            f"Relatório salvo como:\n{nome_arquivo}"
        )


root = tk.Tk()
app = ChargeGridApp(root)
root.mainloop()