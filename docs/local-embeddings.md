# Local Embeddings with Zep

This stack is configured to use **local embeddings** via the `zep-nlp` service. This allows you to run Zep without an external API key (like OpenAI) and keeps your data private.

## Configuration

The `zep-nlp` service is defined in `docker-compose.yml`:

```yaml
  zep-nlp:
    image: getzep/zep-nlp:latest
    container_name: ai-zep-nlp
    environment:
      - ZEP_NLP_MODEL=sentence-transformers/all-MiniLM-L6-v2
    volumes:
      - ./data/zep-nlp:/app/cache
```

### The Model
We are using `sentence-transformers/all-MiniLM-L6-v2`.
- **Size**: ~80MB (very lightweight).
- **Performance**: Fast inference on CPU.
- **Dimensions**: 384.

### Changing the Model
To use a different Hugging Face model:
1. Edit `docker-compose.yml`.
2. Change the `ZEP_NLP_MODEL` environment variable.
   Example: `ZEP_NLP_MODEL=sentence-transformers/all-mpnet-base-v2`
3. Update `config/zep.yaml` to match the new model's dimensions if necessary (e.g., 768 for mpnet-base).
4. Restart the service: `docker compose up -d`

## Hardware Usage
This setup is optimized for your **Intel Core i7**. The model is small enough that CPU inference is very fast (milliseconds).
If you wish to use your GPU (Quadro P1000), you would need to configure the `zep-nlp` container to use the NVIDIA runtime, but for this specific model, CPU is sufficient and simpler to manage.
