from flask import Blueprint

app=Blueprint("general",__name__)

@app.route('/')
def main():
    return 'Hello word'


@app.route('/about')
def about_us():
    return 'about us'