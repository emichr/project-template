# Create a python environment 
python3 -m venv --copies ~/python-envs/mkdocs

# Activate the environment
source ~/python-envs/mkdocs/bin/activate

# Install the packages from the requirements.txt
pip install -r requirements.txt --upgrade

# Run "mkdocs serve" to start the project webserver
mkdocs serve
# Open http://127.0.0.1:8000/ in your browser

# VSCode: Set the "python.defaultInterpreterPath" in the "project.code-workspace" file to the path of your Python(environment) executable.

# Visit https://squidfunk.github.io/mkdocs-material/reference/ for more information about elements you can use in your mkdocs project