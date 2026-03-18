# ┌───────────────────────────────────────────────┐
# │                                               │
# │               Gra python 1 v2.0               │
# │                                               │
# │ Autor: Dawcio232                              │
# │ GitHub: Dawcio232                             │
# │ Znany też jako: 0Verox                        │
# │ Rok: 2026                                     │
# │                                               │
# │ Info: Gra do ulepszania umiejętności          │
# │              matematycznych z combo, levelami │
# │              punktami i ocenami               │
# │                                               │
# └───────────────────────────────────────────────┘
#-=IMPORT=-
from rich import print
import time
import random
#--------------------------------------------------------------------------
#-=ZMIENNNE=-
points = 0
combo = 0
odp = ""
num1 = 0
num2 = 0
levels = 0
win_points = 0
lose_points = 0
result = 0
gained = 0
correct = 0
ratio = 0
choose = 0
played = 0
#--Widomości--
welcome = "Witaj w grze! Twoim celem jest zdobycie jak największej liczby punktów. Każda poprawna odpowiedź zwiększa Twój wynik, a każda błędna odpowiedź resetuje Twój combo. Powodzenia! \n"
options = "[green]1. Easy \n2. Normal \n3. Hard \n4. Expert \n5. AI \n[/green]"
instruction_text = "[green]Najpierw wybierz który dział matematyki chcesz poćwiczyć.[/green]"
#--słowniki--
modes = {
    1: {"num1":1, "num2":5, "levels":5, "win_points":1, "lose_points":0},
    2: {"num1":1, "num2":10, "levels":10, "win_points":1, "lose_points":0},
    3: {"num1":1, "num2":20, "levels":10, "win_points":1, "lose_points":0},
    4: {"num1":3, "num2":50, "levels":15, "win_points":2, "lose_points":-1},
    5: {"num1":7, "num2":200, "levels":20, "win_points":2, "lose_points":-1},
}
odp_question = {
    1: "\nWybrałeś tryb Easy. Albo jesteś początkującym, albo po prostu lubisz łatwe wyzwania. \n",
    2: "\nWybrałeś tryb Normal. To trochę trudniejszy poziom, ale nadal dostępny dla początkujących. \n",
    3: "\nWybrałeś tryb Hard. Teraz już powinno być trochę trudniej. \n",
    4: "\nWybrałeś tryb Expert. To naprawdę trudny poziom, który sprawdzi Twoje umiejętności. \n",
    5: "\nWybrałeś tryb AI. Albo jesteś nauczycielem matematyki, albo jesteś sztuczną inteligencją. \n",
}
end_message = {
    1: "[red] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 1. \nSłabo ci poszło. Lepiej następnym razem! [/red]",
    2: "[yellow] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 2. \nNie jest źle, ale możesz zrobić lepiej! [/yellow]",
    3: "[green] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 3. \nŚwietna robota! [/green]",
    4: "[blue] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 4. \nNiesamowite! Jesteś prawdziwym mistrzem! [/blue]",
    5: "[magenta] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 5. \nNiesamowite! Jesteś prawdziwym geniuszem matematycznym! [/magenta]",
    6: "[cyan] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 6. \nJesteś na poziomie nauczyciela matematyki! [/cyan]"
}
poprawne_opcje = ("+", "-", "/", "*")

#--------------------------------------------------------------------------
#-=FUNKCJE=-
def question(question1):
    try:
        odp_val = int(input(question1))
        return odp_val
    except ValueError:
        print("[red]Nieprawidłowa forma odpowiedzi. Proszę podać liczbę.[/red]")
        return question(question1)
    except KeyboardInterrupt:
        print("\n[red]Gra przerwana. Do zobaczenia![/red]")
        exit()

def mainframe(z1, z2, com):
    global points, combo, choose # Dodane, aby mainframe widział Twój wybór działania
    num1 = random.randint(z1, z2)
    num2 = random.randint(z1, z2)
   
    if choose == "+":
        poprawny_wynik = num1 + num2
        print(f"[blue]Oblicz: {num1} dodać {num2} = ?[/blue]")
    elif choose == "-":
        poprawny_wynik = num1 - num2
        print(f"[blue]Oblicz: {num1} minus {num2} = ?[/blue]")
    elif choose == "/":
        # Uwaga: dla dzielenia przyjmujemy wynik całkowity, żeby int(input) działał
        if num2 == 0: num2 = 1
        poprawny_wynik = num1 // num2
        print(f"[blue]Oblicz: {num1} podzielić przez {num2} (całkowicie) = ?[/blue]")
    elif choose == "*":
        poprawny_wynik = num1 * num2
        print(f"[blue]Oblicz: {num1} razy {num2} = ?[/blue]")

    uzytkownik_odp = question("Twoja odpowiedź: ")
   
    if uzytkownik_odp == poprawny_wynik:
        return True
    else:
        print(f"[yellow]Błędna odpowiedź! Prawidłowy wynik to: {poprawny_wynik}[/yellow]")
        return False

#--------------------------------------------------------------------------
#-=START=-
print(welcome)
print(instruction_text)
while True:
  choose = input("Wybierz. (+, -, /, *): ").strip()
  if choose in poprawne_opcje:
    break
  else:
    print("Prosimy wpisać POPRAWNĄ odpowiedź! \n")
print("\nProszę podaj numer trybu trudności na jakiej raczysz grać.")
print(options)
odp_idx = question("Podaj liczbę od 1 do 5: ")
t_msg = odp_question[odp_idx]
print(t_msg)

t_mode = modes[odp_idx]
num1 = t_mode["num1"]
num2 = t_mode["num2"]
levels = t_mode["levels"]
win_points = t_mode["win_points"]
lose_points = t_mode["lose_points"]
time.sleep(1)

#--------------------------------------------------------------------------
#-=MAINFRAME=-
for i in range(levels):
    if mainframe(num1, num2, combo):
        if combo == 0:
            points += win_points
        else:
            points += win_points * combo
        combo += 1
        correct += 1
        played += 1
        print(f"[green]Brawo! \nAktualne punkty: {points} \nCombo: {combo}. \nJest to {played}/{levels} leveli.\nZostało[/green]", levels - played, "[green]leweli.[/green]\n")
    else:
        points += lose_points
        combo = 0
        played += 1
        print(f"[red]Niestety, źle. \nAktualne punkty: {points} \nCombo zostało zresetowane \nAktualne Combo: {combo}. \nJest to {played}/{levels} leveli.\n Zostało [/red]", levels - played, "[red]leweli. [/red] \n")


#--------------------------------------------------------------------------
#-=END=-
ratio = correct / levels
if ratio < 0.2:
    grade = 1
elif ratio < 0.4:
    grade = 2
elif ratio < 0.6:
    grade = 3
elif ratio < 0.8:
    grade = 4
elif ratio < 0.95:
    grade = 5
else:
    grade = 6

print(end_message[grade].format(points=points))
#--------------------------------------------------------------------------
#-=Credits=-
print()
print("[bold cyan]Dzięki za grę![/bold cyan]")
print("[dim]© 2026 Dawcio232 | GitHub: Dawcio232 | aka 0Verox[/dim]")
