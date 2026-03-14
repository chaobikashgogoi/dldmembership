
from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

OUTPUT_FOLDER = "pdf_output/generated_files"

@app.route('/')
def home():
    return render_template("membership_form.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("name")
    mobile = request.form.get("mobile")
    address = request.form.get("address")
    mtype = request.form.get("type")

    filename = f"Membership_{name.replace(' ','_')}.pdf"
    filepath = os.path.join(OUTPUT_FOLDER, filename)

    c = canvas.Canvas(filepath)
    c.drawString(100, 750, "DISTRICT LIBRARY DIBRUGARH")
    c.drawString(100, 720, f"Name: {name}")
    c.drawString(100, 700, f"Mobile: {mobile}")
    c.drawString(100, 680, f"Address: {address}")
    c.drawString(100, 660, f"Membership Type: {mtype}")
    c.save()

    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
