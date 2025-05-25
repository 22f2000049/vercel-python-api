import json
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler

# Load the marks data once
with open("q-vercel-python.json", "r") as f:
    students = json.load(f)
marks_dict = {student["name"]: student["marks"] for student in students}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Parse query string
        query = parse_qs(self.path[self.path.find('?') + 1:])
        names = query.get("name", [])

        # Retrieve marks
        result = [marks_dict.get(name, None) for name in names]
        response = json.dumps({"marks": result})

        self.wfile.write(response.encode())

