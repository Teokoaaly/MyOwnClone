FROM python:3.11-slim

# The application source lives in api/api/. We work from the directory
# above the package root so that `from api.X import Y` resolves correctly
# (the top-level `api` package is then api/api/, with its own __init__.py).
WORKDIR /app

# Install dependencies. api/api/requirements.txt is the canonical one
# (the root api/requirements.txt is no longer shipped — it was a duplicate
# of the dead tree that was removed).
COPY api/api/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code. The build context is the repo root, so we
# copy only the api/ folder.
COPY api/ /app/api/

# Expose port
EXPOSE 5001

# Default command. We launch from /app/api/api/ so that the top-level
# `api` package (containing `app_factory.py`) is on the import path.
CMD ["flask", "--app", "app_factory", "run", "--host=0.0.0.0", "--port=5001"]
