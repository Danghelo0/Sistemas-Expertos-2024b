from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Inicializa la base de datos y precarga respuestas
def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT UNIQUE,
            answer TEXT
        )
    ''')
    # Respuestas precargadas
    precargadas = [
        ('Hola', '¡Hola! ¿Cómo estás?'),
        ('¿Cómo estás?', 'Estoy bien, gracias por preguntar.'),
        ('¿De qué te gustaría hablar?', 'Podemos hablar de lo que quieras.')
    ]
    for question, answer in precargadas:
        try:
            c.execute('INSERT INTO responses (question, answer) VALUES (?, ?)', (question, answer))
        except sqlite3.IntegrityError:
            pass
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('SELECT answer FROM responses WHERE question = ?', (user_message,))
    result = c.fetchone()
    if result:
        bot_reply = result[0]
    else:
        bot_reply = 'No conozco esa respuesta, ¿puedes enseñarme cómo debería responder?'
    conn.close()
    return jsonify({'reply': bot_reply})

@app.route('/learn', methods=['POST'])
def learn():
    data = request.json
    question = data.get('question')
    answer = data.get('answer')
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO responses (question, answer) VALUES (?, ?)', (question, answer))
    conn.commit()
    conn.close()
    return jsonify({'message': '¡He aprendido una nueva respuesta!'})

if __name__ == '__main__':
    app.run(debug=True)
