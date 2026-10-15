# MangoBook

A small social media app. Sign up, share photos and videos with a caption, and scroll a feed of everyone's posts. You can delete your own posts.

- **Backend:** FastAPI, with login from [fastapi-users](https://fastapi-users.github.io/fastapi-users/) and a SQLite database.
- **Frontend:** a [Streamlit](https://streamlit.io/) app.
- **Media storage:** uploads are stored on [ImageKit](https://imagekit.io/), which also draws captions onto images.

## Getting started

### 1. Prerequisites

- Python 3.12
- A free ImageKit account. You need its **private key** and **URL endpoint**, both listed in the ImageKit dashboard under *Developer options*.

### 2. Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi "fastapi-users[sqlalchemy]" aiosqlite uvicorn python-multipart \
            imagekitio python-dotenv streamlit requests
```

### 3. Configure

Create a `.env` file in the project root:

```
IMAGEKIT_PRIVATE_KEY=your_private_key
IMAGEKIT_URL=https://ik.imagekit.io/your_id
```

### 4. Run

Start the API and the frontend in two separate terminals:

```bash
# Terminal 1: API on http://localhost:8000
python main.py

# Terminal 2: UI on http://localhost:8501
streamlit run frontend.py
```

Open http://localhost:8501, sign up with an email and password, then log in.

The database (`test.db`) is created automatically the first time the API starts. Interactive API docs are at http://localhost:8000/docs.

## Project layout

```
main.py          Starts the API server
frontend.py      Streamlit UI (login, feed, upload)
app/
  app.py         API routes: /upload, /feed, /posts/{id}, plus auth routes
  db.py          Database models (User, Post) and session setup
  users.py       Login and user management (JWT)
  images.py      ImageKit client
  schemas.py     Request and response schemas
```

## API overview

| Method | Path | Description |
|---|---|---|
| POST | `/auth/register` | Create an account |
| POST | `/auth/jwt/login` | Log in and get a token |
| GET | `/users/me` | Get the current user |
| POST | `/upload` | Upload an image or video with a caption |
| GET | `/feed` | List all posts, newest first |
| DELETE | `/posts/{post_id}` | Delete one of your own posts |

All routes except register and login need an `Authorization: Bearer <token>` header.
