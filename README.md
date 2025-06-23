# Late Show API Challenge

## Setup Instructions

1. **Install PostgreSQL**
2. **Create DB:**
   ```bash
   sudo -i -u postgres psql
   CREATE DATABASE late_show_db;
   \q
   ```
3. **Set DB password:**
   ```sql
   ALTER USER postgres WITH PASSWORD 'yourpassword';
   ```
4. **Clone repo & install dependencies:**
   ```bash
   git clone <your-github-repo-url>
   cd late-show-api-challenge
   pip install -r requirements.txt  # or use pipenv
   ```
5. **Set env vars in `server/config.py`:**
   ```python
   SQLALCHEMY_DATABASE_URI = "postgresql://postgres:yourpassword@localhost:5432/late_show_db"
   JWT_SECRET_KEY = "your-secret-key"
   ```

## How to Run
```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python -m server.seed
FLASK_APP=server.app flask run
```

## Auth Flow
- **Register:** `POST /register` (username, password)
- **Login:** `POST /login` (get JWT token)
- **Protected:** Send `Authorization: Bearer <token>` header

## Routes
| Route                  | Method | Auth | Description                  |
|------------------------|--------|------|------------------------------|
| /register              | POST   | ❌   | Register user                |
| /login                 | POST   | ❌   | Login, get JWT               |
| /episodes              | GET    | ❌   | List episodes                |
| /episodes/<id>         | GET    | ❌   | Get episode + appearances    |
| /episodes/<id>         | DELETE | ✅   | Delete episode + appearances |
| /guests                | GET    | ❌   | List guests                  |
| /appearances           | POST   | ✅   | Create appearance            |

**Sample Register Request:**
```json
POST /register
{
  "username": "testuser",
  "password": "testpass"
}
```

**Sample Login Response:**
```json
{
  "access_token": "<JWT>"
}
```

## Postman Usage
- Import `challenge-4-lateshow.postman_collection.json` into Postman.
- Use the requests to test all endpoints.
- For protected routes, set the `jwt_token` variable with your login token.

## GitHub Repo
[https://github.com/<your-username>/late-show-api-challenge](https://github.com/<your-username>/late-show-api-challenge)
