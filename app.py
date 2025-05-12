from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    df = pd.read_csv("project_list.csv")
    projects = df[[
        "Title", "Description", "GitHub Link", "Project Type",
        "Frontend Languages", "Backend Languages", "Frameworks",
        "Libraries", "Database", "Status"
    ]].to_dict(orient="records")
    
    return render_template("index.html", projects=projects)

if __name__ == '__main__':
    app.run(debug=True)