from flask import Flask, jsonify, request, redirect, render_template
import faceSwap

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", image_returned=False, add_class="offset-md-1")


@app.route("/dress", methods=['POST'])
def dress():
    print (request.files)
    file1 = request.files["file1"]
    print(file1)
    file2 = request.files["file2"]
    file1_name =  'static/' + file1.filename
    file2_name = 'static/' + file2.filename
    file1.save(file1_name)
    file1.close()
    file2.save(file2_name)
    file2.close()

    faceSwap.swap(file1_name, file2_name)
    result_image = file1.filename.split(".")[0] + file2.filename.split(".")[0] + ".jpg"
    return render_template("index.html", image_returned=True,file1_name=file1.filename, file2_name=file2.filename, result_image=result_image, add_class="")


if __name__ == "__main__":
    print("Hai")
    app.run(host='0.0.0.0', port=5001, debug=True)
