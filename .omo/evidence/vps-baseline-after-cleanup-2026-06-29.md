Context
- Phase A cleanup of dead Ollama models after local embeddings went live.

Ollama inventory after cleanup
- kept (active path):
  - mxbai-embed-large:latest
  - embeddinggemma:latest
- removed (dead experiments):
  - aroxima/gte-qwen2-1.5b-instruct:q4_k_m
  - rjmalagon/gte-qwen2-1.5b-instruct-embed-f16:latest

Resource baseline after cleanup
- RAM: total 3.8Gi / used 1.3Gi / free 903Mi / avail 2.5Gi
- Swap: 2G total, 570.9M used
- Ollama process: PID 3652438, RSS ~31MB (running, idle)
- Backend latency to /readyz: ~10ms (3 samples)

Backend still healthy
- /readyz returns 200
- Containers: api, ollama, postgres, redis, weaviate all running

Conclusion
- Phase A complete. The active model inventory is now unambiguous.
- Next: Phase D env governance inventory.