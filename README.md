# Gr3_SaltedHash
# User Management Application (Python, Tkinter, SQLite)

Ky projekt është një aplikacion desktop i zhvilluar në **Python**, i cili përdor **Tkinter** për ndërfaqen grafike (GUI) dhe **SQLite** për menaxhimin e databazës. Qëllimi i aplikacionit është menaxhimi bazik i përdoruesve duke ofruar:

* Krijimin e një useri të ri (Register)
* Autentifikimin e userit (Login)
* Shfaqjen e userave ekzistues

Fjalëkalimet nuk ruhen si tekst i thjeshtë, por si **Salted Hash** për të rritur sigurinë.

---

## ⚙️ Teknologjitë e përdorura

* Python
* Tkinter (GUI)
* SQLite (Database)
* hashlib & os (për hashing dhe salt)

---

## 🔐 Siguria e Fjalëkalimeve

Për siguri, fjalëkalimet ruhen duke përdorur teknikën **Salted Hash**:

* Gjenerohet një **salt** unik për çdo user
* Password-i kombinohet me salt
* Rezultati hash-ohet me **SHA-256**

📌 Në databazë ruhen:

* username
* password_hash
* salt

Kjo metodë parandalon ruajtjen e fjalëkalimeve në formë të lexueshme dhe e bën më të vështirë sulmet si brute-force.

---

## 🗄️ Struktura e Databazës

Tabela: `users`

| Kolona        | Tipi                  |
| ------------- | --------------------- |
| id            | INTEGER (Primary Key) |
| username      | TEXT (UNIQUE)         |
| password_hash | TEXT                  |
| salt          | TEXT                  |

---

## 🖥️ Funksionalitetet

### ➕ Register (Krijimi i Userit)

* Useri vendos username dhe password
* Gjenerohet salt
* Password hash-ohet
* Ruhet në databazë

### 🔑 Login (Autentifikimi)

* Useri fut kredencialet
* Merret salt nga databaza
* Password hash-ohet përsëri
* Krahasohet me hash-in ekzistues

### 👥 Show Users

* Shfaq listën e userave (ID dhe username)

---

## ▶️ Si të ekzekutohet projekti

```bash
python main.py apo py main.py
```
Aplikacioni do të hapet me GUI ku mund të:

* Regjistroni user të ri
* Testoni login
* Shihni userat

---

## 📁 Struktura e Projektit

```
project/
│── main.py        # Starton aplikacionin
│── db.py          # Menaxhon databazën (SQLite)
│── security.py    # Hashing dhe salt
│── ui.py          # GUI (Tkinter)
│── users.db       # Databaza
│── README.md
```

---

## ⚠️ Shënime

* Ky projekt është realizuar për qëllime mësimore
* Nuk përfshin mekanizma të avancuar si:

  * session management
  * mbrojtje nga brute-force
  * validime të avancuara të password-it

---

## 🚀 Përmirësime të mundshme

* Përdorimi i **bcrypt** ose **PBKDF2** në vend të SHA-256
* Shtimi i funksionaliteteve CRUD (Update/Delete user)
* Përmirësimi i dizajnit të GUI
* Shtimi i validimeve më të forta për input

---

## 👨‍💻 Autor
*Blinera Berisha
*Bliri Berisha 
*Çiljeta Azemi 
*Edison Ukshini

