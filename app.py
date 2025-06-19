from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

messages = [
    "เค้ารักบะบี๋มู้กๆนะ อยู่กับเค้าไปนานๆเลยนะบะบี๋ เค้าไม่รู้ว่าที่เค้าทำอันนี้ให้บะบี๋จะชอบมั้ยอิอิ เค้าอยู่กับบะบี๋เค้ามีความสุขมากเลยนะ เค้าดีใจที่มีบะบี๋นะ แล้วก็ตั้งใจรักบะบี๋มากๆด้วย แล้วก็ถ้ามีอะไรไม่พอใจหรืออะไรที่บะบี๋ไม่ชอบบอกเค้าได้เลยนะ เค้าพร้อมปรับตัวเข้าหาบะบี๋อยู่แล้วว รักบะบี๋มากๆนะ💖",
    "หน้านี้ไม่มีอะไรเพิ่ม ให้มันเยอะเฉยๆ 🧸",
    "หน้านี้ก็เหมือนกัน 😜",
    "หน้านี้ด้วย อิอิ",
    "หน้าสุดท้ายแย้วว หมดแยะ 💖"
]

HTML = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>happyaniversary 6m 💌</title>
    <style>
        body {
            font-family: "Kanit", sans-serif;
            background: #ffe6f0;
            color: #4d194d;
            text-align: center;
            padding-top: 100px;
            overflow: hidden;
        }
        .box {
            background: #fff0f5;
            border-radius: 20px;
            padding: 40px;
            max-width: 600px;
            margin: auto;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
            position: relative;
            z-index: 2;
        }
        h1 {
            font-size: 2em;
        }
        .msg {
            font-size: 1.5em;
            margin-top: 20px;
        }
        button {
            margin-top: 30px;
            padding: 10px 20px;
            font-size: 1em;
            background-color: #f06292;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        .heart {
            position: fixed;
            top: -50px;
            color: #ff69b4;
            font-size: 24px;
            animation: fall 5s linear infinite;
            opacity: 0.8;
            z-index: 1;
        }
        @keyframes fall {
            to {
                transform: translateY(100vh) rotate(360deg);
                opacity: 0;
            }
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>💌 aniversary 6m 💌</h1>
        <div id="msg" class="msg">{{ first_message }}</div>
        <button onclick="nextMessage()">ลองกดตรงนี้จิ 💖</button>
    </div>

    <script>
    let page = 1;
    const maxPage = {{ total }};
    const button = document.querySelector("button");

    function nextMessage() {
        if (page < maxPage) {
            page += 1;
            fetch(`/get_message?page=${page}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById("msg").innerHTML = data.message;
                    if (page === maxPage) {
                        button.style.display = "none"; // ซ่อนปุ่มเมื่อถึงหน้าสุดท้าย
                    }
                });
        }
    }

    function createHeart() {
        const heart = document.createElement('div');
        heart.classList.add('heart');
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.animationDuration = (Math.random() * 2 + 3) + "s";
        heart.innerHTML = "💖";
        document.body.appendChild(heart);
        setTimeout(() => {
            heart.remove();
        }, 5000);
    }

    setInterval(createHeart, 300);
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML, first_message=messages[0], total=len(messages))

@app.route("/get_message")
def get_message():
    from flask import request
    page = int(request.args.get("page", 1))
    if page > len(messages):
        page = len(messages)
    return jsonify(message=messages[page - 1])

if __name__ == "__main__":
    app.run(debug=True)
