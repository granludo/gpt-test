from flask import Flask, render_template_string
import difflib

app = Flask(__name__)

@app.route('/')
def visualize_diff():
    # Llegeix les dues versions dels documents de text
    with open('document_v1.txt', 'r') as file1:
        text1 = file1.read().splitlines()
    with open('document_v2.txt', 'r') as file2:
        text2 = file2.read().splitlines()

    # Utilitza difflib per a comparar les diferències
    differ = difflib.HtmlDiff()
    diff_table = differ.make_table(text1, text2)

    # Renderitza les diferències en una pàgina HTML
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            table.diff {font-family:Courier; border:medium;}
            .diff_header {background-color:#e0e0e0;}
            td.diff_header {text-align:right;}
            .diff_next {background-color:#c0c0c0;}
            .diff_add {background-color:#aaffaa;}
            .diff_chg {background-color:#ffff77;}
            .diff_sub {background-color:#ffaaaa;}
        </style>
    </head>
    <body>
        <h1>Comparació de documents</h1>
        <table>{{ diff_table | safe }}</table>
    </body>
    </html>
    '''
    return render_template_string(template, diff_table=diff_table)


if __name__ == '__main__':
    app.run(debug=True)
