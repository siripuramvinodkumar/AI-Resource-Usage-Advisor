
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    if request.method == "POST":
        electricity = int(request.form.get("electricity", 0))
        water = int(request.form.get("water", 0))

        if electricity > 200:
            recommendations.append("Reduce electricity usage by turning off unused appliances.")
        if water > 150:
            recommendations.append("Reduce water usage during daily activities.")
        if not recommendations:
            recommendations.append("Your resource usage is within sustainable limits.")

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
