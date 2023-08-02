from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)


@app.route(f"/get_request", methods=["POST"])
def get_request():
    data_request = request.get_json(force=True)
    try:
        dict_response = {"success": True, "data_received": data_request}
    except:
        dict_response = {"success": False}
    return jsonify(dict_response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)