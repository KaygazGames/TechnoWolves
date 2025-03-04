from flask import Flask, render_template, request

app = Flask(__name__)

# Dinamik veriler: Takım üyeleri ve etkinlikler
team_members = [
    {"name": "Ahmet", "role": "Takım Kaptanı", "bio": "Robotik yarışmalarda lider, fikirleri pırıl pırıl!", "image": "static/img/ahmet.jpg"},
    {"name": "Zeynep", "role": "Yazılım Uzmanı", "bio": "Kodları hack'lemeye hazır; hata muhabbetlerine bayılır!", "image": "static/img/zeynep.jpg"},
]

events = [
    {"title": "Turnuva Hazırlıkları", "date": "2025-04-15", "description": "Takımın turnuva öncesi hazırlıkları ve strateji toplantısı."},
    {"title": "Robot Gösterisi", "date": "2025-05-01", "description": "Robotumuzun sahne performansıyla fark yarattığı gün."}
]

@app.route('/')
def home():
    return render_template("index.html", events=events)

@app.route('/team')
def team():
    return render_template("team.html", team_members=team_members)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Not: "Mesajın, robotumuz kadar hızlı işlenecek!" 😎
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # Gerçek bir uygulamada mesajı kaydedebilir veya e-posta gönderebilirsiniz.
        return render_template("contact.html", success=True, name=name)
    return render_template("contact.html", success=False)

if __name__ == '__main__':
    app.run(debug=True)
