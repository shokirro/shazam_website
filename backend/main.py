from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from fastapi.responses import FileResponse

app = FastAPI()

# ---------- CORS ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

shazam_history = [
    {
        "id": 1,
        "year": 1999,
        "title": "Заснування компанії",
        "description": "Кріс Бартон та Філіп Інгелбрехт заснували Shazam Entertainment у Берклі.",
        "image": ""
    },
    {
        "id": 2,
        "year": 2000,
        "title": "Пошук технології",
        "description": "Ейвері Ванг розробив революційну технологію аудіорозпізнавання.",
        "image": ""
    }
]

shazam_history = [
    {
        "id": 1,
        "year": 1999,
        "title": "Заснування компанії",
        "description": "Кріс Бартон та Філіп Інгелбрехт заснували Shazam Entertainment у Берклі. Пізніше до них приєдналися Дхірадж Мукерджі та інженер Ейвері Ванг[cite: 29, 30].",
        "image": ""
    },
    {
        "id": 2,
        "year": 2000,
        "title": "Пошук технології",
        "description": "Команда зіткнулася з проблемою розпізнавання музики через шуми. [cite_start]Ейвері Ванг розробив революційну технологію аудіорозпізнавання[cite: 7, 10].",
        "image": ""
    },
    {
        "id": 3,
        "year": 2002,
        "title": "Запуск сервісу '2580'",
        "description": "У серпні у Британії запущено сервіс. Користувачі набирали '2580', підносили телефон до музики й отримували SMS. [cite_start]Перший хіт — Eminem 'Cleanin’ Out My Closet'[cite: 31, 33].",
        "image": ""
    },
    {
        "id": 4,
        "year": 2008,
        "title": "Революція App Store",
        "description": "У липні Shazam з’являється в App Store. [cite_start]Це стало переломним моментом, що приніс мільйони користувачів без витрат на рекламу[cite: 22, 36].",
        "image": ""
    },
    {
        "id": 5,
        "year": 2012,
        "title": "10 мільйонів запитів",
        "description": "Пісня 'Somebody That I Used to Know' (Gotye) стала першою, що досягла 10 мільйонів Shazam-запитів[cite: 39].",
        "image": ""
    },
    {
        "id": 6,
        "year": 2014,
        "title": "Інтеграція з Siri",
        "description": "З виходом iOS 8 Shazam інтегрується прямо в голосовий асистент Siri, що спрощує пошук музики[cite: 42].",
        "image": ""
    },
    {
        "id": 7,
        "year": 2018,
        "title": "Придбання Apple",
        "description": "Apple купує Shazam за 400 мільйонів доларів, роблячи його повністю дочірньою компанією[cite: 47].",
        "image": ""
    },
    {
        "id": 8,
        "year": 2022,
        "title": "70 мільярдів запитів",
        "description": "Загальна кількість розпізнавань за весь час існування сервісу перевищила 70 мільярдів. [cite_start]Додаток має понад 2 мільярди завантажень[cite: 49, 50].",
        "image": ""
    }
]

@app.get("/api/history")
def get_history():
    return shazam_history

# ---------- FRONTEND ----------
BASE_DIR = Path(__file__).resolve().parent
DIST_DIR = BASE_DIR / "dist"

# Віддаємо index.html на /
@app.get("/")
def read_index():
    return FileResponse(DIST_DIR / "index.html")

# Віддаємо всі JS і CSS з assets
app.mount("/assets", StaticFiles(directory=DIST_DIR / "assets"), name="assets")

# Віддаємо всі файли з public (твоє відео)
app.mount("/public", StaticFiles(directory=DIST_DIR / "public"), name="public")
