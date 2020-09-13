# BOLO

***

# Table of Contents

* **[Get Started](#get-started)**

* **[Notes](#notes)**

***

# Get Started

* Install python (Use whatever method you want. Make sure it is in system path).
    * [Brew](https://brew.sh/) (MacOS).

* Install virtualenv
    *   ```
        pip install virtualenv
        ```
    *   ```
        pip3 install virtualenv
        ```

## MacOS

* Navigate to directory you wish to develop in.

```
mkdir BOLO
cd BOLO
virtualenv -p python3.8 venv
source venv/bin/activate
git clone https://github.com/cflore/BOLO.git
cd BOLO
pip install -r requirements.txt
python manage.py runserver
```
## Windows

# Notes

