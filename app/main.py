# sentiric-llm-ollama-service/app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from contextlib import asynccontextmanager
from app.core.logging import setup_logging
from app.core.config import settings
import structlog
# import httpx # İleride eklenecek

logger = structlog.get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("LLM Ollama Service başlatılıyor", 
                version=settings.SERVICE_VERSION, 
                env=settings.ENV,
                ollama_url=settings.OLLAMA_API_URL)
    
    # TODO: Ollama API'ye erişim kontrolü eklenecek
    
    yield
    
    logger.info("LLM Ollama Service kapatılıyor")

app = FastAPI(
    title="Sentiric LLM Ollama Service",
    description="Ollama, Llama.cpp ve Yerel LLM Adaptör Servisi",
    version=settings.SERVICE_VERSION,
    lifespan=lifespan
)

# LLM Gateway'in çağıracağı placeholder endpoint
@app.post(settings.API_V1_STR + "/generate", status_code=status.HTTP_200_OK)
async def generate_text(prompt: str, model_name: str):
    logger.info("Metin üretme isteği alındı", prompt_len=len(prompt), model=model_name)
    
    # Placeholder: Basit HTTP çağrısı simülasyonu
    response_text = f"Ollama MOCK: Yerel motor ({settings.OLLAMA_MODEL}) prompt'u işledi."
    
    # Gerçek API çağrısı Ollama REST API'ye yapılacaktır:
    # async with httpx.AsyncClient() as client:
    #     ollama_res = await client.post(f"{settings.OLLAMA_API_URL}/api/generate", json={"model": model_name, "prompt": prompt})

    return {"generated_text": response_text}

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    # TODO: Ollama API'sine ping atma mantığı eklenecek
    return {"status": "ok", "service": "llm-ollama", "target": settings.OLLAMA_API_URL}