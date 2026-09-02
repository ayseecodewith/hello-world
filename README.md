# Hello World Backend

Python, FastAPI ve Docker kullanılarak geliştirilmiş basit bir frontend-backend iletişim projesidir.

Frontend, FastAPI backend'e HTTP `GET` isteği gönderir. Backend ise `"Hello World"` mesajını JSON formatında döndürür.

## Kullanılan Teknolojiler

- Python
- FastAPI
- Uvicorn
- HTML
- CSS
- JavaScript
- Docker
- Docker Compose
- Nginx

## Proje Yapısı

```text
hello-world-backend/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   ├── nginx.conf
│   └── Dockerfile
│
├── compose.dev.yaml
├── README.md
└── .gitignore
```

## Docker ile Çalıştırma

Docker Desktop'ın açık olduğundan emin olun.

Proje klasöründe:

```bash
docker compose -f compose.dev.yaml up -d --build
```

Container'ların çalıştığını kontrol etmek için:

```bash
docker compose -f compose.dev.yaml ps
```

Uygulamayı tarayıcıda açmak için:

```text
http://localhost:3000
```

## API

Backend endpoint:

```text
GET /api/hello
```

Response:

```json
{
  "message": "Hello World"
}
```

## Docker Container Yapısı

Frontend ve backend ayrı container'larda çalışır:

```text
Browser
   ↓
localhost:3000
   ↓
Frontend Container
   ↓
backend:8000
   ↓
Backend Container
```

Container'ları durdurmak için:

```bash
docker compose -f compose.dev.yaml down
```
