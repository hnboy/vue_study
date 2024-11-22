import toml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate_html_from_toml(toml_path, html_template_path, html_output_path):
    """Generates HTML, converting hex strings to hex numbers for display."""
    try:
        with open(toml_path, 'r', encoding='utf-8') as f:
            toml_data = toml.load(f)
    except FileNotFoundError:
        print(f"Error: TOML file '{toml_path}' not found.")
        return False
    except toml.TomlDecodeError as e:
        print(f"Error: Invalid TOML format in '{toml_path}': {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while reading '{toml_path}': {e}")
        return False

    # Convert hexadecimal strings to integers
    for section, data in toml_data.items():
        try:
            new_data = []
            for pair in data['data']:
                try:
                    new_pair = [int(x, 16) for x in pair]  # Convert hex strings to ints
                    new_data.append(new_pair)
                except ValueError as e:
                    print(f"Warning: Invalid hex string in section '{section}': {e}. Skipping this data pair.")
            data['data'] = new_data
        except KeyError:
            print(f"Warning: 'data' key missing in section '{section}'. Skipping this section.")
            continue


    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(html_template_path)

    try:
        html_output = template.render(toml_data=toml_data)
        with open(html_output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"HTML file generated successfully at '{html_output_path}'.")
        return True
    except Exception as e:
        print(f"Error rendering or writing HTML: {e}")
        return False


# Example usage:
toml_file = Path("./test.toml")
html_template_file = "template.html"
html_output_file = Path("./output.html")

# Create a sample template.html if it doesn't exist.
if not Path(html_template_file).exists():
    sample_template = """<!DOCTYPE html>
<html>
<head>
<title>TOML Data Visualization</title>
<style>
body { font-family: sans-serif; }
table { 
display: inline-block;
text-align: center;
margin: auto;
display:block;
overflow-x:auto;
width: 100%; border-collapse: collapse; margin-bottom: 20px; border: 1px solid #ccc; }
th, td { border: 1px solid #ccc; padding: 10px; text-align: center; word-break: keep-all; white-space: nowrap; }
th { background-color: #f2f2f2; font-weight: bold; }
h1, h2 { color: #333; }
h2 { margin-top: 30px; }
</style>
</head>
<body>
<h1>TOML Data</h1>

{% for section, data in toml_data.items() %}
    <h2>{{ section }}</h2>
    <table>
        <tr>
         <td>Index</td>
            {% for i in range(data.index|length) %}
                <th>{{ data.index[i] }}</th>
            {% endfor %}
        </tr>
        <tr>
        <td>Data</td>
            {% for i in range(data.index|length) %}
                <td>{% if i < data.data|length %}0x{{ '%02X' % data.data[i][0] }}->0x{{ '%02X' % data.data[i][1] }}{% endif %}</td>
            {% endfor %}
        </tr>
    </table>
{% endfor %}

</body>
</html>
"""
    Path(html_template_file).write_text(sample_template, encoding='utf-8')


success = generate_html_from_toml(toml_file, html_template_file, html_output_file)
if success:
    print("HTML generation successful.")