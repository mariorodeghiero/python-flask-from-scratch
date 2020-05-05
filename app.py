from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/article/<string:id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % id

# About
@app.route('/about')
def about():
    return render_template('about.html')

    
if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)