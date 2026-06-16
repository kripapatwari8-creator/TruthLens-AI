function analyzeNews() {

    const article =
    document.getElementById("article").value;

    if (article.trim() === "") {
        alert("Please enter article text.");
        return;
    }

    document.getElementById(
        "loading"
    ).style.display = "block";

    fetch("/predict", {
        method: "POST",

        headers: {
            "Content-Type":
            "application/x-www-form-urlencoded"
        },

        body:
        "article=" +
        encodeURIComponent(article)
    })

    .then(res => res.json())

    .then(data => {

        document.getElementById(
            "loading"
        ).style.display = "none";

        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById(
            "resultCard"
        ).style.display = "block";

        const prediction =
        document.getElementById(
            "prediction"
        );

        prediction.innerText =
        data.prediction;

        if (data.prediction === "REAL") {

            prediction.className =
            "real";

            document.getElementById(
                "confidenceBar"
            ).style.background =
            "#22c55e";

        } else {

            prediction.className =
            "fake";

            document.getElementById(
                "confidenceBar"
            ).style.background =
            "#ef4444";
        }

        document.getElementById(
            "confidence"
        ).innerText =
        "Confidence: " +
        data.confidence + "%";

        document.getElementById(
            "credibility"
        ).innerText =
        "Credibility Score: " +
        data.credibility + "/100";

        document.getElementById(
            "risk"
        ).innerText =
        "Risk Level: " +
        data.risk;

        document.getElementById(
            "category"
        ).innerText =
        "Category: " +
        data.category;

        document.getElementById(
            "words"
        ).innerText =
        "Word Count: " +
        data.words;

        document.getElementById(
            "readingTime"
        ).innerText =
        "Reading Time: " +
        data.reading_time +
        " min";

        document.getElementById(
            "reason"
        ).innerText =
        data.reason;

        document.getElementById(
            "confidenceBar"
        ).style.width =
        data.confidence + "%";

        loadHistory();
        loadCounter();

    })

    .catch(error => {

        document.getElementById(
            "loading"
        ).style.display = "none";

        console.log(error);

        alert("Prediction failed.");
    });
}

function loadHistory() {

    fetch("/history")

    .then(res => res.json())

    .then(data => {

        const container =
        document.getElementById(
            "historyContainer"
        );

        container.innerHTML = "";

        data.forEach(item => {

            container.innerHTML += `
            <div class="history-item">

                <strong>${item[0]}</strong>

                <br><br>

                Confidence:
                ${item[1]}%

                <br>

                Category:
                ${item[2]}

                <br>

                ${item[3]}

            </div>
            `;
        });
    });
}

function loadCounter() {

    fetch("/latest")

    .then(res => res.json())

    .then(data => {

        const counter =
        document.getElementById(
            "counter"
        );

        if(counter){
            counter.innerText =
            data.count;
        }

    });
}

function copyResult() {

    const text =
    document.getElementById(
        "prediction"
    ).innerText +

    "\n" +

    document.getElementById(
        "confidence"
    ).innerText;

    navigator.clipboard.writeText(
        text
    );

    alert("Result copied!");
}

function shareResult() {

    const text =
    document.getElementById(
        "prediction"
    ).innerText;

    navigator.clipboard.writeText(
        text
    );

    alert(
        "Result copied for sharing!"
    );
}

function filterHistory() {

    let input =
    document.getElementById(
        "historySearch"
    ).value.toLowerCase();

    let items =
    document.getElementsByClassName(
        "history-item"
    );

    for (let i = 0; i < items.length; i++) {

        let txt =
        items[i].innerText
        .toLowerCase();

        if (txt.includes(input)) {

            items[i].style.display =
            "";

        } else {

            items[i].style.display =
            "none";
        }
    }
}

function toggleTheme() {

    document.body.classList.toggle(
        "dark"
    );
}

loadHistory();
loadCounter();