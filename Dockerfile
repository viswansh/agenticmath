# ===============================
# Stage 1 - Build React Frontend
# ===============================
FROM node:18 AS frontend-builder

WORKDIR /app
COPY frontend/agent-edu/ ./agent-edu/
WORKDIR /app/agent-edu

RUN npm install
RUN npm run build

# ===============================
# Stage 2 - Build FastAPI Backend
# ===============================
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl && apt-get clean

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy backend files
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source
COPY backend/src/ ./src/
COPY .env .env

# Copy built frontend from Stage 1
COPY --from=frontend-builder /app/agent-edu/build ./frontend/

# Expose port
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
