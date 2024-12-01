from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Konfiguracja Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
redis_client = redis.StrictRedis(host=redis_host, port=int(redis_port), decode_responses=True)

@app.route('/')
def home():
    redis_client.set("message", "Hello, World!")
    return redis_client.get("message")

@app.route('/api')
def api():
    return jsonify({"message": "This is a simple API with Redis!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

