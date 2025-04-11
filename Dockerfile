# Stage 1: Build
FROM python:3.9-slim as builder

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /install

# Install Python dependencies globally
COPY req_prod.txt .
RUN pip install --upgrade pip && \
    pip install -r req_prod.txt && \
    pip cache purge

# Stage 2: Final
FROM python:3.9-slim

WORKDIR /app

# Copy installed packages
COPY --from=builder /usr/local /usr/local

# Copy app source code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "home.py", "--server.port=8501", "--server.address=0.0.0.0"]
