from dotenv import load_dotenv
from fastapi import FastAPI
from routers import manage_docker, manage_broker_messages, manage_files, manage_market_data, manage_backtesting

load_dotenv()
app = FastAPI()

app.include_router(manage_docker.router)
app.include_router(manage_broker_messages.router)
app.include_router(manage_files.router)
app.include_router(manage_market_data.router)
app.include_router(manage_backtesting.router)
