from flask import Flask
import pandas as pd
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


@app.route("/read_cleaned")
def read_cleaned():
    csv_filenames = [fn for fn in os.listdir("data/cleaned/") if fn.endswith(".csv")]
    csv_filenames = sorted(csv_filenames)
    filename = csv_filenames[-1]

    df = pd.read_csv(f"data/cleaned/{filename}")

    return df.to_html()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)