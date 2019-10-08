from flask import Flask, render_template, url_for, request, session
app = Flask(__name__)
vorur = [
			[0, 'Taska', 8000, "taska.jpg"], 
			[1, "bók", 3500, "book.jpg"], 
			[2, "Penni", 500, "penni.jpg"]
		]
app.config['SECRET_KEY'] = 'Leyno'

@app.route('/')
def index():
	return render_template('index.html', vorur=vorur)

def summa():
    karfa = []
    karfa = session['karfa']
    summa = 0
    for i in karfa:
        summa += vorur[i][2]
    return summa

@app.route('/add/<int:nr>')
def add(nr):
    temp_karfan = []
    #er karfa tóm, ef satt þá ekki tóm
    if 'karfa' in session:
        temp_karfan = session['karfa']
        temp_karfan.append(nr)
        session['karfa'] = temp_karfan
        return render_template('add.html', vorur=vorur)
    else:
        temp_karfan.append(nr)
        session['karfa'] = temp_karfan
        return render_template('add.html', vorur=vorur)

@app.route('/karfa')
def karfan():
    temp_karfan = []
    if 'karfa' in session:
        temp_karfan = session['karfa']

        for i in temp_karfan:
            print(i)
        return render_template('karfa.html', vkarfa=temp_karfan, vorur=vorur, summa=summa())
    else:
        return '<h1>Karfa er tóm</h1> <h1><a href="/">Home</a></h1>'
	
@app.route('/ath')
def ath():
    temp_karfa = []
    if 'karfa' in session:
        temp_karfa= session['karfa']
        print(len(temp_karfa))
    else:
        print("Karfan er tóm")
    return 'degub route'


@app.route('/eyda')
def eyda():
    session.pop('karfa', None)
    return render_template('index.html', vorur=vorur)

@app.route('/eydavoru/<int:id>')
def eydavoru(id):
    temp_karfa = []
    if 'karfa' in session:
        temp_karfa = session['karfa']
        temp_karfa.remove(id)
        session['karfa'] = temp_karfa
        return render_template('karfa.html', vorur=vorur, vkarfa=temp_karfa, summa=summa())
    else:
        return '<h1>Karfa er tóm</h1> <h1><a href="/">Home</a></h1> '
    
@app.route('/Takk', methods=['POST'])
def takk():
    session.pop('karfa', None)
    return '<h1>Takk fyrir að versla hjá okkur</h1> <h1><a href="/">Home</a></h1>'
 
@app.errorhandler(404)
def error404(error):
	return '<h1>Þessi síða er ekki til</h1>', 404


if __name__ == "__main__":
	app.run(debug=True)
	