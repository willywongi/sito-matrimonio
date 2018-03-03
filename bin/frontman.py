from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	page = """<html>

<head>
    <meta charset="utf8">
    <title>Matrimonio - Francesco &amp; Francesca 2018 Edition</title>
    <link href="https://fonts.googleapis.com/css?family=Josefin+Sans:300,400|Reem+Kufi" rel="stylesheet">
    <link href="static/base.css" rel="stylesheet">
    <script src="static/index.js" type="text/javascript"></script>
    <meta name="viewport" content="width=device-width">
</head>

<body>
    <nav>
        <ul>
            <li><a href="#via">Via!</a></li>
            <li><a href="#cerimonia">Cerimonia</a></li>
            <li><a href="#ricevimento">Ricevimento</a></li>
            <li><a href="#lista">Lista</a></li>
            <li><a href="#imprevisti">Imprevisti</a></li>
        </ul>
    </nav>
    <section id="via">
        <div>
            <h1>Matrimonio</h1>
            <h2>Francesco &amp; Francesca 2018 Edition</h2>
        </div>
    </section>
    <section id="cerimonia">
        <div>
            <h3>Cerimonia</h3>
            <p>Si svolger&agrave; Sabato 26 maggio 2018 alle 16,30 nella chiesa di San Vincenzo a Modena (Corso Canalgrande 77).
            </p>
        </div>
    </section>
    <section id="ricevimento">
        <div>
            <h3>Ricevimento</h3>
            <p>Festeggeremo presso il "Golf Club di San Valentino"</p>
        </div>
    </section>
    <section id="lista">
        <div>
            <h3>Lista</h3>
            <p>Per chi volesse contribuire, apriremo una lista presso l'agenzia viaggi XXX</p>
        </div>
    </section>
    <section id="imprevisti">
        <div>
            <h3>Imprevisti</h3>
            <p>Vuoi ricevere notifiche riguardo al matrimonio?</p>
        </div>
    </section>
</body>

</html>"""
	return page

