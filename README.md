# Gr3_SaltedHash

Ky projekt është një aplikacion desktop i zhvilluar në **Python**, i cili përdor **Tkinter** për ndërfaqen grafike (GUI) dhe **SQLite** për menaxhimin e databazës. Qëllimi i aplikacionit është menaxhimi bazik i përdoruesve duke ofruar:

* Krijimin e një useri të ri (Register)
* Autentifikimin e userit (Login)
* Shfaqjen e userave ekzistues

Fjalëkalimet nuk ruhen si tekst i thjeshtë, por si **Salted Hash** për të rritur sigurinë.

---

## Teknologjitë e përdorura

* Python
* Tkinter (GUI)
* SQLite (Database)
* hashlib & os (për hashing dhe salt)

---

## Struktura e Databazës

Tabela: `users`

| Kolona        | Tipi                  |
| ------------- | --------------------- |
| id            | INTEGER (Primary Key) |
| username      | TEXT (UNIQUE)         |
| password_hash | TEXT                  |
| salt          | TEXT                  |

---

## Funksionalitetet

*Register (Krijimi i Userit)

*Login (Autentifikimi)

*Show Users

---

## Si të ekzekutohet projekti

```bash
cd user_manager_app
```

```bash
python main.py apo py main.py
```
---

## Struktura e Projektit

```
user_manager_app/
│── main.py        # Starton aplikacionin
│── database.py    # Menaxhon databazën (SQLite)
│── security.py    # Hashing dhe salt
│── ui.py          # GUI (Tkinter)
│── users.db       # Databaza
```

---

##  Autor

* Blinera Berisha
* Bliri Berisha
* Çiljeta Azemi 
* Edison Ukshini

