from flask import Flask, render_template, request
from flask_cors import CORS
import weapons
import json

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/')
def get_index():
  return render_template('index.html', available_plots=weapons.get_available_plots())

@app.route('/weapons')
def get_weapons():
  return render_template('weapons.html', available_plots=weapons.get_available_plots())

@app.route('/get_plot_data')
def get_plot_data():
  plot_id = int(request.args.get("plot_id"))
  plot_type_id = int(request.args.get("plot_type_id"))
  data = weapons.get_plot(plot_id, plot_type_id)
  return data

app.run(host='0.0.0.0', port=54000, debug=True)