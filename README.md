https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ 

python3 -m venv .venv
source .venv/bin/activate
pip install setuptools
pip install -r requirements.txt

export ACTIVE_ENV=Local
export graph_insight=True

#Create a env for local

uvicorn main:app --host 0.0.0.0 --port 7074

pip freeze > requirements.txt
