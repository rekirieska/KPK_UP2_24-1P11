# Auth Service

## 1. Описание сервиса

Сервис аутентификации пользователей.  
Предоставляет функциональность регистрации, управления пользователями, работы с refresh-токенами и сброса пароля.

---

## 2. Сущности системы

### User
- id (PK)
- username (уникальный)
- email (уникальный)
- password_hash
- is_active
- created_at

### RefreshToken
- id (PK)
- user_id (FK → User)
- token
- expires_at
- created_at

### PasswordReset
- id (PK)
- user_id (FK → User)
- reset_token
- expires_at
- is_used

---

## 3. ER-диаграмма
![Диаграмма] (erd.png)
---

## 4. Список функций

### User
- create_user
- update_user
- delete_user
- get_user
- list_users

### RefreshToken
- create_refresh_token
- update_refresh_token
- delete_refresh_token
- get_refresh_token
- list_refresh_tokens

### PasswordReset
- create_password_reset
- update_password_reset
- delete_password_reset
- get_password_reset
- list_password_resets

---

## 5. Описание операций

# ================= USER =================

## Добавить User

### Входные данные

| Параметр       | Обязательность | Тип     | Ограничение | Значение по умолчанию |
|----------------|----------------|---------|-------------|------------------------|
| username       | Да             | string  | уникальный  | -                      |
| email          | Да             | string  | уникальный  | -                      |
| password_hash  | Да             | string  | -           | -                      |
| is_active      | Нет            | bool    | -           | true                   |

### Уникальные комбинации
- username
- email

### Ответ

| Параметр    | Тип      |
|------------|----------|
| id         | int      |
| username   | string   |
| email      | string   |
| is_active  | bool     |
| created_at | datetime |

---

## Изменить User по ID

### Входные данные

| Параметр      | Обязательность | Тип     |
|---------------|----------------|---------|
| username      | Нет            | string  |
| email         | Нет            | string  |
| password_hash | Нет            | string  |
| is_active     | Нет            | bool    |

### Ответ

| Параметр | Тип |
|----------|-----|
| id       | int |

---

## Удалить User по ID

Ответ:
- True / False

---

## Получить User по ID

### Ответ

| Параметр | Тип |
|----------|-----|
| id       | int |
| username | string |
| email    | string |

---

## Получить список User

### Параметры

| Параметр | Тип |
|----------|-----|
| username | string |
| email    | string |

---

# ================= REFRESH TOKEN =================

## Добавить RefreshToken

### Входные данные

| Параметр   | Обязательность | Тип |
|------------|----------------|-----|
| user_id    | Да             | int |
| token      | Да             | string |
| expires_at | Да             | datetime |

### Ответ

| Параметр | Тип |
|----------|-----|
| id       | int |

---

## Изменить RefreshToken по ID

### Входные данные

| Параметр   | Тип |
|------------|-----|
| token      | string |
| expires_at | datetime |

---

## Удалить RefreshToken по ID

Ответ:
- True / False

---

## Получить RefreshToken по ID

### Ответ

| Параметр | Тип |
|----------|-----|
| id       | int |
| token    | string |

---

## Получить список RefreshToken

### Параметры

| Параметр | Тип |
|----------|-----|
| user_id  | int |

---

# ================= PASSWORD RESET =================

## Добавить PasswordReset

### Входные данные

| Параметр    | Обязательность | Тип |
|-------------|----------------|-----|
| user_id     | Да             | int |
| reset_token | Да             | string |
| expires_at  | Да             | datetime |

---

## Изменить PasswordReset по ID

### Входные данные

| Параметр    | Тип |
|-------------|-----|
| reset_token | string |
| expires_at  | datetime |
| is_used     | bool |

---

## Удалить PasswordReset по ID

Ответ:
- True / False

---

## Получить PasswordReset по ID

### Ответ

| Параметр    | Тип |
|-------------|-----|
| id          | int |
| reset_token | string |

---

## Получить список PasswordReset

### Параметры

| Параметр | Тип |
|----------|-----|
| user_id  | int |
