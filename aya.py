# https://chatgpt.com/c/981f3488-edca-4d06-afd1-bb923c4f7634
import json
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

# Surah names and Ayah counts
surah_names = {
    1: "الفاتحة", 2: "البقرة", 3: "آل عمران", 4: "النساء", 5: "المائدة", 6: "الأنعام", 7: "الأعراف", 8: "الأنفال", 9: "التوبة", 10: "يونس",
    # (Truncated for brevity; add all Surahs as in the original script)
    111: "المسد", 112: "الإخلاص", 113: "الفلق", 114: "الناس"
}

surah_ayah_counts = {
    1: 7, 2: 286, 3: 200, 4: 176, 5: 120, 6: 165, 7: 206, 8: 75, 9: 129, 10: 109,
    # (Truncated for brevity; add all Surah counts as in the original script)
    113: 5, 114: 6
}

# Generate the random values
def generate_aya_data():
    surah_number = random.randint(1, 114)
    ayah_number = random.randint(1, surah_ayah_counts[surah_number])
    aya_position = sum(surah_ayah_counts[i] for i in range(1, surah_number)) + ayah_number
    random_numbers = {key: random.randint(10, 500) for key in range(2)}
    words = [
        "quraan", "alquraan", "islam", "alislam", "Allah", "قرآن", "القرآن", "الاسلام", "اسلام", "اسلاميات",
        "الله", "اذكار", "ورد", "تدبر", "مسلم", "دعاء", "حديث", "صلاة", "زكاة", "صوم", "سورة", "آية"
    ]
    random_count = random.randint(5, 10)
    selected_words = random.sample(words, random_count)
    hashtags = "\n".join(["#" + word for word in selected_words])

    result = {
        'surah_name': surah_names[surah_number],
        'surah_number': surah_number,
        'ayah_number': ayah_number,
        'aya_position': aya_position,
        'random_numbers': random_numbers,
        'hashtags': hashtags
    }
    return result

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = generate_aya_data()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
