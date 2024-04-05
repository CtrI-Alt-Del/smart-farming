from flask import Flask, render_template

def get_sensors_records_page():
    return render_template("pages/sensors_records.html")

