# Hello World Backend

Python ve FastAPI kullanılarak geliştirilmiş, frontend ile backend arasındaki temel HTTP iletişimini gösteren basit bir web projesidir.

## Proje Açıklaması

Frontend tarafında HTML, CSS ve JavaScript kullanılır. Kullanıcı butona tıkladığında JavaScript, FastAPI backend'e `GET` isteği gönderir. Backend `"Hello World"` mesajını JSON formatında döndürür ve frontend bu mesajı ekranda gösterir.

```text
Browser
   ↓
HTML + JavaScript
   ↓ HTTP GET
FastAPI Backend
   ↓ JSON Response
"Hello World"
   ↓
Browser
```

## Kullanılan Teknolojiler

- Python
- FastAPI
- Uvicorn
- HTML
- CSS
- JavaScript

## Proje Yapısı

```text
hello-world-backend/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── script.js
    └── style.css
```

## Kurulum

Projeyi klonlayın veya proje klasörüne girin:

```bash
cd hello-world-backend
```

### Virtual Environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Bağımlılıkların Kurulması

Virtual environment aktifken:

```bash
python -m pip install -r requirements.txt
```

## Projeyi Çalıştırma

Backend'i başlatmak için:

```bash
uvicorn app:app --reload
```

Backend varsayılan olarak şu adreste çalışır:

```text
http://127.0.0.1:8000
```

Tarayıcıdan aç:

```text
http://127.0.0.1:8000
```

## API Endpoint

Backend'in API endpoint'i:

```text
GET /api/hello
```

Tam adres:

```text
http://127.0.0.1:8000/api/hello
```

Response:

```json
{
  "message": "Hello World"
}
```

## Frontend → Backend İletişimi

Frontend'deki JavaScript:

```javascript
const response = await fetch("/api/hello");
```

ile backend'e HTTP `GET` isteği gönderir.

FastAPI:

```python
@app.get("/api/hello")
async def hello():
    return {"message": "Hello World"}
```

ile isteği karşılar ve `"Hello World"` mesajını JSON response olarak gönderir.

JavaScript response'u alır:

```javascript
const data = await response.json();
```

ve mesajı sayfada gösterir:

```javascript
result.textContent = data.message;
```

```text
Browser
   ↓
Frontend
   ↓
fetch("/api/hello")
   ↓
HTTP GET Request
   ↓
FastAPI Backend
   ↓
HTTP Response
   ↓
Frontend
   ↓
"Hello World"
```
