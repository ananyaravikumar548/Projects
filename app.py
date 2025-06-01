from flask import Flask, request, render_template
import os
from resume_parser import parse_resume  
from database import insert_into_db  # Assuming you have this module

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        file = request.files['resume']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            parsed_data = parse_resume(filepath)
            insert_into_db(parsed_data)
            return "Resume uploaded and data stored successfully!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

