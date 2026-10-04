# Dispatch Delivery API

A backend service for managing dispatch and delivery operations.

## Features

- RESTful API for order creation, status tracking, and delivery assignments
- Integration with message queues for asynchronous processing
- Dockerized deployment with Docker Compose
- Environment variable configuration
- Comprehensive test suite

## Prerequisites

- Docker & Docker Compose
- Python 3.11 (if developing locally)
- Git

## Setup

1. Clone the repository
2. Copy the example environment file
   ```bash
   cp .env.example .env
   ```
3. Install Python dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application with Docker Compose
   ```bash
   docker-compose up --build
   ```

## Usage

The API runs on http://localhost:8000. Endpoints include:

- `POST /orders` - Create a new order
- `GET /orders/{id}` - Get order details
- `PUT /orders/{id}/status` - Update order status
- `GET /health` - Health check

## Testing

Run the test suite with:
```bash
pytest
```