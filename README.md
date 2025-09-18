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
criar arquivo .env na raiz do projeto DJANGO_SECRET_KEY=django-insecure-==agq7as3o4$!0hewla7%#sr@q-a3+y11a)0#xf^y=8g4xis)y
![Minha Foto]([https://raw.githubusercontent.com/usuario/repositorio/main/assets/minha_foto.png](https://github-production-user-asset-6210df.s3.amazonaws.com/57542268/491217096-5b855ed5-fd6f-4eb8-b22a-108c99e61f81.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250918%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250918T175218Z&X-Amz-Expires=300&X-Amz-Signature=66e5876707d0dbca4ee6a33e974926b54100ba74d31ff9448daeff3387b512b9&X-Amz-SignedHeaders=host))


