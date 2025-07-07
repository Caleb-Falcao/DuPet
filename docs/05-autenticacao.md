# 🔐 Autenticação

## Sistema atual

- Baseado no `django.contrib.auth`
- Uso de `@login_required` nas views protegidas
- Redirecionamento automático para `/users/login/` se não autenticado

## A fazer

- Integração com Google e Facebook via `django-allauth` ou `social-auth-app-django`
