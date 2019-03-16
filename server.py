from flask import Flask, jsonify, request, redirect, render_template
import faceSwap

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/dress", methods=['POST'])
def dress():
    file1 = request.files["file1"]
    file2 = request.files["file2"]
    file1.save('_one.jpg')
    file1.close()
    file2.save('_two.jpg')
    file2.close()

    faceSwap.swap("_one.jpg", "_two.jpg")
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    print("Hai")
    app.run(host='0.0.0.0', port=5001, debug=True)


