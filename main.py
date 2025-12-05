from flask import Flask, render_template, jsonify

app = Flask(__name__)

#This is the data for the clubs
clubs = {
    "Math": {"title": "Math Club", "intro": "Solve problems and compete in competitions.", "meeting": "Monday 3:00 PM", "members": "45 members", "activities": "Problem solving, competitions, tutoring", "email": "math@schoolclub.edu"},
    "Science": {"title": "Science Club", "intro": "Run experiments and explore scientific concepts.", "meeting": "Wednesday 3:30 PM", "members": "52 members", "activities": "Experiments, research, science fair", "email": "science@schoolclub.edu"},
    "Band": {"title": "Band Club", "intro": "Play instruments and perform in concerts.", "meeting": "Tuesday 4:00 PM", "members": "38 members", "activities": "Rehearsals, performances, concerts", "email": "band@schoolclub.edu"},
    "Art": {"title": "Art Club", "intro": "Create artwork and display in galleries.", "meeting": "Thursday 3:00 PM", "members": "35 members", "activities": "Painting, drawing, exhibitions", "email": "art@schoolclub.edu"},
    "Gaming": {"title": "Gaming Club", "intro": "Play games and participate in tournaments.", "meeting": "Friday 3:30 PM", "members": "67 members", "activities": "Gaming, tournaments, team matches", "email": "gaming@schoolclub.edu"}
}

# The routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/clubs')
def get_clubs():
    return jsonify(clubs)

@app.route('/api/clubs/<club_name>')
def get_club(club_name):
    club = clubs.get(club_name)
    if club:
        return jsonify(club)
    return jsonify({"error": "Club not found"}), 404

# Running the app
if __name__ == '__main__':
    app.run(debug=True)