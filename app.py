from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "🌍 AI Tourism Planner Backend is running!"

@app.route('/api/destinations', methods=['GET'])
def get_destinations():
    destinations = [
        {"name": "Goa", "image": "https://source.unsplash.com/300x200/?goa"},
        {"name": "Paris", "image": "https://source.unsplash.com/300x200/?paris"},
        {"name": "Tokyo", "image": "https://source.unsplash.com/300x200/?tokyo"},
        {"name": "New York", "image": "https://source.unsplash.com/300x200/?newyork"},
        {"name": "Bali", "image": "https://source.unsplash.com/300x200/?bali"},
        {"name": "Hyderabad", "image": "https://source.unsplash.com/300x200/?hyderabad"},
        {"name": "Jaipur", "image": "https://source.unsplash.com/300x200/?jaipur"},
        {"name": "London", "image": "https://source.unsplash.com/300x200/?london"},
        {"name": "Bangkok", "image": "https://source.unsplash.com/300x200/?bangkok"},
        {"name": "Dubai", "image": "https://source.unsplash.com/300x200/?dubai"},
        {"name": "Delhi", "image": "https://source.unsplash.com/300x200/?delhi"},
        {"name": "Rome", "image": "https://source.unsplash.com/300x200/?rome"},
        {"name": "Singapore", "image": "https://source.unsplash.com/300x200/?singapore"},
        {"name": "Barcelona", "image": "https://source.unsplash.com/300x200/?barcelona"},
        {"name": "Istanbul", "image": "https://source.unsplash.com/300x200/?istanbul"},
        {"name": "Sydney", "image": "https://source.unsplash.com/300x200/?sydney"},
        {"name": "Kolkata", "image": "https://source.unsplash.com/300x200/?kolkata"},
        {"name": "Mumbai", "image": "https://source.unsplash.com/300x200/?mumbai"},
        {"name": "Pondicherry", "image": "https://source.unsplash.com/300x200/?pondicherry"},
        {"name": "Manali", "image": "https://source.unsplash.com/300x200/?manali"}
    ]
    return jsonify(destinations)

@app.route('/api/budget', methods=['POST'])
def calculate_budget():
    data = request.get_json()
    budget = int(data.get('budget', 0))
    breakdown = {
        "hotel": round(budget * 0.5, 2),
        "transport": round(budget * 0.2, 2),
        "food": round(budget * 0.2, 2),
        "misc": round(budget * 0.1, 2)
    }
    return jsonify(breakdown)

@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    city = request.args.get('city', 'Goa')
    hotels = [
        {"name": f"{city} Grand Hotel", "price": 3200},
        {"name": f"{city} Beach Resort", "price": 4500},
        {"name": f"{city} Budget Inn", "price": 1800}
    ]
    return jsonify(hotels)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
