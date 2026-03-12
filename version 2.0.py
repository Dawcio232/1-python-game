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
#--Widomości--
welcome = "Witaj w grze! Twoim celem jest zdobycie jak największej liczby punktów. Każda poprawna odpowiedź zwiększa Twój wynik, a każda błędna odpowiedź resetuje Twój combo. Powodzenia! \n"
options = "[green]1. Easy \n2. Normal \n3. Hard \n4. Expert \n5. AI \n[/green]"
#--słowniki--
modes = {
    1: {"num1":1, "num2":5, "levels":5, "win_points":1, "lose_points":0},
    2: {"num1":1, "num2":10, "levels":10, "win_points":1, "lose_points":0},
    3: {"num1":1, "num2":20, "levels":10, "win_points":1, "lose_points":0},
    4: {"num1":3, "num2":50, "levels":15, "win_points":2, "lose_points":-1},
    5: {"num1":7, "num2":200, "levels":20, "win_points":2, "lose_points":-1},
}
odp_question = {
    1: "Wybrałeś tryb Easy. Albo jesteś początkującym, albo po prostu lubisz łatwe wyzwania. \n",
    2: "Wybrałeś tryb Normal. To trochę trudniejszy poziom, ale nadal dostępny dla początkujących. \n",
    3: "Wybrałeś tryb Hard. Teraz już powinno być trochę trudniej. \n",
    4: "Wybrałeś tryb Expert. To naprawdę trudny poziom, który sprawdzi Twoje umiejętności. \n",
    5: "Wybrałeś tryb AI. Albo jesteś nauczycielem matematyki, albo jesteś sztuczną inteligencją. \n",
}
end_message = {
    1: "[red] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 1. \nSłabo ci poszło. Lepiej następnym razem! [/red]",
    2: "[yellow] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 2. \nNie jest źle, ale możesz zrobić lepiej! [/yellow]",
    3: "[green] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 3. \nŚwietna robota! [/green]",
    4: "[blue] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 4. \nNiesamowite! Jesteś prawdziwym mistrzem! [/blue]",
    5: "[magenta] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 5. \nNiesamowite! Jesteś prawdziwym geniuszem matematycznym! [/magenta]",
    6: "[cyan] Gra zakończona.\nTwój wynik to {points} punktów. Twoja ocena: 6. \nJesteś na poziomie nauczyciela matematyki! [/cyan]",
}
#--------------------------------------------------------------------------
#-=FUNKCJE=-
def question(question1):
    try:
        odp = int(input(question1))
        return odp
    except ValueError:
        print("[red]Nieprawidłowa forma odpowiedzi. Proszę podać liczbę.[/red]")
        return question(question1)
    except KeyboardInterrupt:
        print("\n[red]Gra przerwana. Do zobaczenia![/red]")
        exit()
def mainframe(z1, z2, com):
    global points
    global combo
    num1 = random.randint(z1, z2)
    num2 = random.randint(z1, z2)
    print(f"[blue]Oblicz: {num1} razy {num2   } = ?[/blue]")
    odp = question("Twoja odpowiedź: ")
    return odp == num1 * num2

#--------------------------------------------------------------------------
#-=START=-
print(welcome)
print(options)
odp = question("Podaj liczbę od 1 do 5: ")
t = odp_question[odp]
print(t)
t = modes[odp]
num1 = t["num1"]
num2 = t["num2"]
levels = t["levels"]
win_points = t["win_points"]
lose_points = t["lose_points"]
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
        print(f"[green]Brawo! \nAktualne punkty: {points} \nCombo: {combo}[/green]\n")
    else:
        points += lose_points
        combo = 0
        print(f"[red]Niestety, źle. \nAktualne punkty: {points} \nCombo zostało zresetowane \nAktualne Combo: {combo}[/red]\n")
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


