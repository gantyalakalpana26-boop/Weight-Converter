from flask import Flask,render_template,request
import os


print(os.getcwd())
print(os.path.exists("index.html"))
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='/static')

@app.route('/', methods=['GET','POST'])
def home():

    result= None
    if request.method=='POST':
        weight=float(request.form.get('weight'))
        unit=request.form.get('unit')

        if unit=='L':
            converted=weight*0.45
            result=f"Your weight is {converted:.2f} kilos."

        elif unit=='K':
            converted=weight/0.45
            result=f"Your weight is {converted:.2f} pounds."
        else:
            result="Invalid data :("
    return render_template('index.html', result=result)


if __name__ == "__main__":
    import webbrowser
    from threading import Timer

    Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000/")).start()
    app.run(debug=True, use_reloader=False)