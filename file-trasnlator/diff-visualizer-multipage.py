import difflib
import os
import sys
import re

def add_class_to_nowrap_cells(html_content, class_name):
    pattern = re.compile(r'(<td\s*?)nowrap="nowrap"')
    return pattern.sub(fr'\1class="{class_name}"', html_content)

def compare_files_to_html_paged(fromfile, tofile, output_folder):
    with open(fromfile, 'r', encoding='utf-8') as f:
        fromlines = f.readlines()
    with open(tofile, 'r', encoding='utf-8') as f:
        tolines = f.readlines()

    html_diff = difflib.HtmlDiff()
    num_lines = len(fromlines)
    lines_per_page = 50
    num_pages = (num_lines + lines_per_page - 1) // lines_per_page

    default_file_template = html_diff._file_template
    default_fromdesc = default_file_template.split('%(fromdesc)s')[0].split('"')[-2]
    default_todesc = default_file_template.split('%(todesc)s')[0].split('"')[-2]
    default_styles = default_file_template.split('%(styles)s')[0].split('<style type="text/css">')[-1]

    additional_styles = '''
    table.diff td.diff_header {
        width: 45%;
        text-align: left;
    }
    table.diff td.diff_next {
        
    }
    /* Añadir estilo para ajustar el ancho de las cajas */
    table.diff td.nowrap-removed,
    table.diff td[nowrap="nowrap"] {
        white-space: normal !important;
        width: 45% !important;
    }
    '''

    new_file_template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset={charset}" />
    <title>Comparing {fromdesc} and {todesc}</title>
    <style type="text/css">{styles}{additional_styles}</style>
</head>
<body>
    {diff_content}
    <p>{prev_page_link}</p>
    <p>{next_page_link}</p>
</body>
</html>
'''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(num_pages):
        start_line = i * lines_per_page
        end_line = min((i + 1) * lines_per_page, num_lines)
        diff_content = html_diff.make_table(fromlines[start_line:end_line], tolines[start_line:end_line])

        # Agregar una clase a las celdas con nowrap="nowrap" y eliminar el atributo nowrap
        diff_content = add_class_to_nowrap_cells(diff_content, 'nowrap-removed')

        prev_page_link = f'<a href="page_{i - 1}.html">Previous Page</a>' if i > 0 else ''
        next_page_link = f'<a href="page_{i + 1}.html">Next Page</a>' if i < num_pages - 1 else ''

        diff = new_file_template.format(
            charset='utf-8',
            fromdesc=default_fromdesc.format(fromfile=fromfile),
            todesc=default_todesc.format(tofile=tofile),
            styles=default_styles,
            additional_styles=additional_styles,
            diff_content=diff_content,
            prev_page_link=prev_page_link,
            next_page_link=next_page_link
        )

        with open(os.path.join(output_folder, f'page_{i}.html'), 'w', encoding='utf-8') as f:
            f.write(diff)


if __name__ == '__main__':
    fromfile = sys.argv[1]
    tofile = sys.argv[2]
    output_folder = sys.argv[3]

    compare_files_to_html_paged(fromfile, tofile, output_folder)
