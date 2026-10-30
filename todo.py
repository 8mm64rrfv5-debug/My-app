import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("Keine Aufgaben vorhanden.")
        return
    for i, t in enumerate(tasks, 1):
        mark = "✓" if t["done"] else " "
        print(f"{i}. [{mark}] {t['title']}")

def ask_number(tasks):
    show_tasks(tasks)
    try:
        n = int(input("Nummer: ")) - 1
    except ValueError:
        print("Bitte eine Zahl eingeben.")
        return None
    if 0 <= n < len(tasks):
        return n
    print("Ungültige Nummer.")
    return None

def main():
    tasks = load_tasks()
    while True:
        print("\n1) Anzeigen  2) Hinzufügen  3) Erledigt  4) Löschen  5) Beenden")
        choice = input("Auswahl: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Neue Aufgabe: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
        elif choice == "3":
            n = ask_number(tasks)
            if n is not None:
                tasks[n]["done"] = True
                save_tasks(tasks)
        elif choice == "4":
            n = ask_number(tasks)
            if n is not None:
                tasks.pop(n)
                save_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Ungültige Auswahl.")

main()
