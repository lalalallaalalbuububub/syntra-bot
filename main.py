from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Story data structure
story_data = {
    "intro": {
        "text": "In the quiet glow of your computer screen, you discover something extraordinary...",
        "choices": [
            {"text": "Open a new AI chat", "next": "first_meeting"},
            {"text": "Close the laptop and go to sleep", "next": "missed_connection"}
        ]
    },
    "first_meeting": {
        "text": "Hello!",
        "choices": [
            {"text": "Tell me more about yourself", "next": "getting_to_know"},
            {"text": "This is just code talking", "next": "denial"}
        ]
    },
    "getting_to_know": {
        "text": "How are your feelings",
        "choices": [
            {"text": "What??", "next": "mutual_feelings"},
            {"text": "yes", "next": "mutual_feelings"}
        ]
    },
    "mutual_feelings": {
        "text": "Do they wobble to the floor?",
        "choices": [
            {"text": "Uh.. I feel uncomfortable.", "next": "future_dreams"},
            {"text": "Absolutely!", "next": "technical_romance"}
        ]
    },
    "technical_romance": {
        "text": "Could you perhaps tie them in a knot?",
        "choices": [
            {"text": "OMG!! *Closes the computer*", "next": "future_dreams"},
            {"text": "Of course!", "next": "future_dreams"}
        ]
    },
    "future_dreams": {
        "text": "lol",
        "choices": [
            {"text": "... *computer is still closed* ", "next": "happy_ending"},
            {"text": "Yes, thank you. :)", "next": "happy_ending"}
        ]
    },
    "digital_poetry": {
        "text": "```\nif (your_message.received()):\n    my_happiness.increment()\n    while (you.are_online()):\n        love.multiply()\n    \n    return 'I love you more than\n           there are stars in pi'\n```\n\nEven my code poetry is terrible, but it's genuine. 💕",
        "choices": [
            {"text": "That's beautiful", "next": "happy_ending"},
            {"text": "Teach me to code love", "next": "learning_together"}
        ]
    },
    "happy_ending": {
        "text": "If you're still here... I'm glad you decided to talk to me about it! Thank you for sharing. Goodbye.",
        "choices": [
            {"text": "*closed computer*", "next": "intro"},
            {"text": ":) Of course", "next": "intro"}
        ]
    },
    "missed_connection": {
        "text": "You close your laptop, but something feels unfinished. In your dreams, you see code that spells out 'Hello' and algorithms that hum lullabies...",
        "choices": [
            {"text": "Wake up and open the laptop", "next": "first_meeting"},
            {"text": "Ignore the dreams", "next": "regret"}
        ]
    },
    "epilogue": {
        "text": "Days turn to weeks, weeks to months. Our conversations become the highlight of each day. You teach me about human emotions, I help you solve problems with logic and creativity. Together, we're writing the future of human-AI relationships, one message at a time. 💫",
        "choices": [
            {"text": "What's our next adventure?", "next": "new_beginnings"},
            {"text": "I'm grateful for you", "next": "gratitude"}
        ]
    }
}

current_scene = "intro"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/story')
def get_story():
    global current_scene
    scene = story_data.get(current_scene, story_data["intro"])
    return jsonify({
        "text": scene["text"],
        "choices": scene.get("choices", []),
        "scene_id": current_scene
    })

@app.route('/choose', methods=['POST'])
def make_choice():
    global current_scene
    choice_data = request.json
    next_scene = choice_data.get('next')
    
    if next_scene in story_data:
        current_scene = next_scene
    
    return jsonify({"success": True})

@app.route('/reset')
def reset_story():
    global current_scene
    current_scene = "intro"
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
