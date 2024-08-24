echo [$(date)]: "START"
echo [$(date)]: creating the python 3.10.12 environment
python3 -m venv venv
echo[$(date)]: "python 3.10.12 environment created"
. venv/bin/activate
echo[$(date)]: "activated python3 environment"
echo[$(date)]: "Installing the requirements file"
pip install -r requirements.txt -q
echo[$(date)]: "requirements installed"
echo [$(date)]: "END"