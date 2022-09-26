from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('workout_page00.html/')

@app.route('/page1')
def page1():
   return render_template('workout_page01.html')

@app.route('/page2')
def page2():
   return render_template('workout_page02.html')

@app.route('/page3')
def page3():
   return render_template('workout_page03.html')

@app.route('/page4')
def page4():
   return render_template('workout_page04.html')

@app.route('/page5')
def page5():
   return render_template('workout_page05.html')

@app.route('/page6')
def page6():
   return render_template('workout_page06.html')

@app.route('/page7')
def page7():
   return render_template('workout_page07.html')

@app.route('/page8')
def page8():
   return render_template('workout_page08.html')

@app.route('/page9')
def page9():
   return render_template('workout_page09.html')

@app.route('/page10')
def page10():
   return render_template('workout_page10.html')

@app.route('/page11')
def page11():
   return render_template('workout_page11.html')

@app.route('/page12')
def page12():
   return render_template('workout_page12.html')

@app.route('/page13')
def page13():
   return render_template('workout_page13.html')

@app.route('/page14')
def page14():
   return render_template('workout_page14.html')

@app.route('/page15')
def page15():
   return render_template('workout_page15.html')

@app.route('/page16')
def page16():
   return render_template('workout_page16.html')

@app.route('/page17')
def page17():
   return render_template('workout_page17.html')

@app.route('/page18')
def page18():
   return render_template('workout_page18.html')

@app.route('/page19')
def page19():
   return render_template('workout_page19.html')

@app.route('/page20')
def page20():
   return render_template('workout_page20.html')

@app.route('/page21')
def page21():
   return render_template('workout_page21.html')

@app.route('/page22')
def page22():
   return render_template('workout_page22.html')

@app.route('/page23')
def page23():
   return render_template('workout_page23.html')

@app.route('/page24')
def page24():
   return render_template('workout_page24.html')







if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
