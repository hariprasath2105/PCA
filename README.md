# PCA-Based Stock Market Analysis Web App

This project demonstrates a simple web-based application that performs **Principal Component Analysis (PCA)** on uploaded stock market data. The application is built using **Flask**, **HTML**, and **CSS**.

## 🔍 Objective
To reduce the dimensionality of financial datasets and visualize the main components of variance using PCA.

## 📁 File Structure

```
PCA_Stock_Analysis/
│
├── static/
│ └── style.css 
│
├── templates/
│ ├── index.html 
│ └── result.html 
│
├── app.py 
├── model.py 
├── stock_data.csv 
└── README.md 
```

---

## 🧠 Libraries Used
- Flask
- Pandas
- Scikit-learn
- NumPy
---

## 🧠 Input Features
- **Daily Usage (Minutes)** — total time spent per day
- **Sessions Per Day** — number of app/site sessions per day
- **Average Session Length (Minutes)** — avg. time per session

---

## ⚙️ How It Works
1. User uploads a `.csv` file containing stock market features (e.g., Open, High, Low, Close, Volume).
2. The PCA model processes and transforms the data into principal components (e.g., PC1, PC2).
3. The results are rendered in a styled table.

---

## ⚙️ How to Run

1. Install dependencies:
```bash
pip install flask numpy pandas matplotlib scipy scikit-learn
```

2. Run the model training (if not done yet):
```bash
python model.py
```

3. Start the Flask app:
```bash
python app.py
```

4. Open your browser and visit `http://127.0.0.1:5000`

---

## 📥 Input Format
Upload a `.csv` file with numerical stock data. For example:

| Open   | High   | Low    | Close  | Volume |
|--------|--------|--------|--------|--------|
| 145.3  | 147.2  | 144.9  | 146.1  | 123456 |
| 147.1  | 148.0  | 145.9  | 147.3  | 145678 |

<img width="556" height="562" alt="image" src="https://github.com/user-attachments/assets/2aa598fc-73b4-48db-a6fa-bbf76a6f5e93" />

## 📊 Output Example
- Cluster Number: `Cluster 1`
- Visualization: Cluster plot with your data point highlighted

<img width="713" height="348" alt="image" src="https://github.com/user-attachments/assets/9d667ac7-c797-4361-8688-a43df76ce03e" />

---

## 📌 Use Case
This application is ideal for financial analysts and data scientists interested in understanding trends and structure in stock market data.

---
## 🙋‍♂️ Author

**Hari Prasath**  
[GitHub Profile](https://github.com/hariprasath2105)

---

## 📘 License

This project is open source and free to use.
