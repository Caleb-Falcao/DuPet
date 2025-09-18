<<<<<<< HEAD
# DuPet – Gerenciador de Pets e Clínicas

![License](https://img.shields.io/badge/license-Proprietary-red)

DuPet é um aplicativo web feito com Django, que permite aos tutores cadastrarem seus pets, visualizarem suas informações e encontrarem clínicas veterinárias próximas.

---

## 🚀 Funcionalidades

- Cadastro e login de usuários
- Cadastro de pets com foto, nome, espécie, raça, idade
- Listagem de pets por usuário
- Busca de clínicas veterinárias (com API do google, caso vc tenha uma api key criar um arquivo .env GOOGLE_MAPS_API_KEY = "APIKEY GOOGLE MAPS")
- Layout com Tailwind CSS

---

## 🧰 Tecnologias utilizadas

- Python 3.13
- Django 5.2
- Tailwind CSS (via CDN)
- SQLite (para desenvolvimento)
- HTML5 e Templates Django

---

## 🛠️ Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/Caleb-Falcao/DuPet.git
cd dupet
python -m venv venv
pip install -r .\requirements.txt
venv\Scripts\activate
python manage.py runserver
criar arquivo .env na raiz do projeto e adicionar esse trecho de codigo: DJANGO_SECRET_KEY=django-insecure-==agq7as3o4$!0hewla7%#sr@q-a3+y11a)0#xf^y=8g4xis)y


