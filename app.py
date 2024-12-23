from flask import render_template
import config

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)
