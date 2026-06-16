from flask import Flask, render_template, request, jsonify
import sqlite3
import joblib
import os

app = Flask(__name__)

DB_NAME = "truthlens.db"

MODEL_FILE = "fake_news_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"


# Load ML Model


if not os.path.exists(MODEL_FILE):
    raise FileNotFoundError(
        "fake_news_model.pkl not found. Run train_model.py"
    )

if not os.path.exists(VECTORIZER_FILE):
    raise FileNotFoundError(
        "tfidf_vectorizer.pkl not found. Run train_model.py"
    )

model = joblib.load(MODEL_FILE)
vectorizer = joblib.load(VECTORIZER_FILE)


# Category Detection


def detect_category(text):

    text = text.lower()

    categories = {
        "Technology": [
            "ai",
            "software",
            "google",
            "microsoft",
            "computer",
            "technology"
        ],

        "Politics": [
            "election",
            "government",
            "president",
            "minister",
            "politics"
        ],

        "Sports": [
            "cricket",
            "football",
            "sports",
            "match",
            "tournament"
        ],

        "Health": [
            "health",
            "doctor",
            "hospital",
            "medicine",
            "covid"
        ],

        "Business": [
            "stock",
            "market",
            "finance",
            "economy",
            "company"
        ]
    }

    for category, words in categories.items():

        for word in words:

            if word in text:
                return category

    return "General"


# AI Explanation


def generate_reason(prediction, confidence):

    if prediction == "FAKE":

        if confidence > 90:
            return (
                "The article contains strong patterns "
                "commonly associated with misinformation."
            )

        return (
            "Some suspicious language patterns were found."
        )

    else:

        if confidence > 90:
            return (
                "The article closely matches patterns "
                "seen in reliable reporting."
            )

        return (
            "Most indicators suggest the article is genuine."
        )


# Save History


def save_history(
    article,
    prediction,
    confidence,
    category,
    reason
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history
        (
            article,
            prediction,
            confidence,
            category,
            reason
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            article,
            prediction,
            confidence,
            category,
            reason
        )
    )

    conn.commit()
    conn.close()


# Routes


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Prediction API

@app.route("/predict", methods=["POST"])
def predict():

    try:

        article = request.form.get("article")

        if not article:
            return jsonify({
                "error": "Article text required"
            })

        vector = vectorizer.transform([article])

        prediction = model.predict(vector)[0]

        confidence = max(
            model.predict_proba(vector)[0]
        )

        confidence = round(
            confidence * 100,
            2
        )

        result = (
            "REAL"
            if prediction == 1
            else "FAKE"
        )

        category = detect_category(article)

        reason = generate_reason(
            result,
            confidence
        )

        save_history(
            article,
            result,
            confidence,
            category,
            reason
        )

        word_count = len(
            article.split()
        )

        reading_time = round(
            word_count / 200,
            1
        )

        credibility_score = confidence

        if confidence >= 90:
            risk = "LOW"

        elif confidence >= 70:
            risk = "MEDIUM"

        else:
            risk = "HIGH"

        return jsonify({
            "prediction": result,
            "confidence": confidence,
            "credibility": credibility_score,
            "risk": risk,
            "category": category,
            "reason": reason,
            "words": word_count,
            "reading_time": reading_time
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

# History API


@app.route("/history")
def history():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            prediction,
            confidence,
            category,
            created_at
        FROM history
        ORDER BY id DESC
        LIMIT 10
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return jsonify(rows)


# Dashboard Stats


@app.route("/stats")
def stats():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM history"
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE prediction='REAL'
        """
    )

    real = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE prediction='FAKE'
        """
    )

    fake = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "total": total,
        "real": real,
        "fake": fake
    })
@app.route("/categories")
def categories():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT category,
               COUNT(*)
        FROM history
        GROUP BY category
    """)

    data = cursor.fetchall()

    conn.close()

    return jsonify(data)


@app.route("/latest")
def latest():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM history
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "count": count
    })

# Run App


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )