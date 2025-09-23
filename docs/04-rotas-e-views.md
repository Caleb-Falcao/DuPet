
---

### 🔁 `04-rotas-e-views.md`

```markdown
# 🔁 Rotas e Views

## Roteamento por app

### `users/urls.py`
- `/users/login/` → login
- `/users/signup/` → signup
- `/users/logout/` → logout

### `pets/urls.py`
- `/pets/` → listagem de pets
- `/pets/novo/` → criação de pets
- `/pets/<id>/editar/` → edição de clinicas

### `clinics/urls.py`
- `/clinics/` → listagem de clínica
- `/nova/` → adicionar nova clínica
- `proximas/` → listagem de clínicas proximas 
- `<int:pk>/editar/` → edição de clínica
- `<int:pk>/excluir/` → exclusão de clínica