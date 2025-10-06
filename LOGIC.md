# 🦙 Sentiric LLM Ollama Service - Mantık ve Akış Mimarisi

**Stratejik Rol:** Ollama veya yerel olarak barındırılan diğer LLM motorlarıyla entegrasyon için esnek bir adaptör sağlar. Bu, Sentiric'in bulut dışı (on-premise) LLM yeteneklerini destekler.

---

## 1. Temel Akış: Yerel Metin Üretme (Generate)

```mermaid
sequenceDiagram
    participant Gateway as LLM Gateway
    participant OllamaService as Ollama Service
    participant OllamaAPI as Ollama REST API
    
    Gateway->>OllamaService: Generate(prompt, model_name)
    
    Note over OllamaService: 1. Model Seçimi ve Bağlantı Kontrolü
    OllamaService->>OllamaAPI: POST /api/generate
    
    OllamaAPI-->>OllamaService: JSON Response
    
    Note over OllamaService: 2. Sonucu Normalize Et (Token/Usage verisi dahil)
    OllamaService-->>Gateway: GenerateResponse(text)
```

## 2. Esneklik
* Model Adı: Doğrudan Ollama'nın desteklediği model adlarını (llama2, phi3, mistral) kullanır.
* Ağ Katmanı: Ollama, HTTP tabanlı bir API sunduğu için, bu servis httpx kullanarak asenkron HTTP çağrıları yapacaktır.