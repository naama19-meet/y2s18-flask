from flask import Flask, render_template,url_for
app = Flask(__name__)

@app.route('/')
def home_page():
    
    favplyers = ["rony", "shahar", "hadar", "noa", "lihi"]

   



    return render_template("index.html", favplyers=favplyers,
    likes_same_sport= False)

    

   
   

if __name__ == '__main__':
    app.run(debug = True, port = 5050)