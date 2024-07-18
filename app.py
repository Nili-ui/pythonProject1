from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Daten aus dem Formular abrufen
    vollmachtgeber_name = request.form['vollmachtgeber_name']
    vollmachtgeber_geburtsdatum = request.form['vollmachtgeber_geburtsdatum']
    vollmachtgeber_geburtsort = request.form['vollmachtgeber_geburtsort']
    vollmachtgeber_adresse = request.form['vollmachtgeber_adresse']
    vollmachtgeber_telefon = request.form['vollmachtgeber_telefon']
    vollmachtgeber_email = request.form['vollmachtgeber_email']
    bevollmaechtigter_name = request.form['bevollmaechtigter_name']
    bevollmaechtigter_geburtsdatum = request.form['bevollmaechtigter_geburtsdatum']
    bevollmaechtigter_geburtsort = request.form['bevollmaechtigter_geburtsort']
    bevollmaechtigter_adresse = request.form['bevollmaechtigter_adresse']
    bevollmaechtigter_telefon = request.form['bevollmaechtigter_telefon']
    bevollmaechtigter_email = request.form['bevollmaechtigter_email']
    ort = request.form['ort']
    datum = request.form['datum']

    # CSV-Datei Pfad
    csv_file = 'form_data.csv'
    file_exists = os.path.isfile(csv_file)

    # Daten in die CSV-Datei schreiben
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Vollmachtgeber Name', 'Vollmachtgeber Geburtsdatum', 'Vollmachtgeber Geburtsort',
                             'Vollmachtgeber Adresse', 'Vollmachtgeber Telefon', 'Vollmachtgeber Email',
                             'Bevollmächtigter Name', 'Bevollmächtigter Geburtsdatum', 'Bevollmächtigter Geburtsort',
                             'Bevollmächtigter Adresse', 'Bevollmächtigter Telefon', 'Bevollmächtigter Email',
                             'Ort', 'Datum'])  # Header schreiben
        writer.writerow([vollmachtgeber_name, vollmachtgeber_geburtsdatum, vollmachtgeber_geburtsort,
                         vollmachtgeber_adresse, vollmachtgeber_telefon, vollmachtgeber_email,
                         bevollmaechtigter_name, bevollmaechtigter_geburtsdatum, bevollmaechtigter_geburtsort,
                         bevollmaechtigter_adresse, bevollmaechtigter_telefon, bevollmaechtigter_email,
                         ort, datum])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
