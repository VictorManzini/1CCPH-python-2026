from colorama import init, Fore, Back, Style
init()

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago","Set", "Out", "Nov", "Dez"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for meses, ano in zip(meses, dias):
    print(f"O mês {Fore.RED}{meses}{Fore.RESET} tem {Fore.BLUE}{ano}{Fore.RESET} dias. ")
