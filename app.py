from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model and scaler
with open("model.pkl", "rb") as f:
    pca, scaler = pickle.load(f)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        aapl = float(request.form['aapl'])
        googl = float(request.form['googl'])
        msft = float(request.form['msft'])
        amzn = float(request.form['amzn'])

        input_df = pd.DataFrame([[aapl, googl, msft, amzn]],
                                columns=["AAPL", "GOOGL", "MSFT", "AMZN"])
        scaled_data = scaler.transform(input_df)
        result = pca.transform(scaled_data)

        df_result = pd.DataFrame(result, columns=["PC1", "PC2"])
        result_table = df_result.to_html(classes="table", index=False)

        return render_template("result.html", table=result_table)

    except:
        return "Invalid input. Please try again."

if __name__ == "__main__":
    app.run(debug=True)
