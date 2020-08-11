README


C:\Users\Cindy>cd  /d D:\Coding_Temple

D:\Coding_Temple>cd week5

D:\Coding_Temple\week5>cd day1

D:\Coding_Temple\week5\day1>mkdir Project

D:\Coding_Temple\week5\day1>cd Project

D:\Coding_Temple\week5\day1\Project> git init
Initialized empty Git repository in D:/Coding_Temple/week5/day1/Project/.git/

D:\Coding_Temple\week5\day1\Project>git add README.md

D:\Coding_Temple\week5\day1\Project>git commit -m "first commit"
[master (root-commit) 95a95ae] first commit
 1 file changed, 3 insertions(+)
 create mode 100644 README.md

D:\Coding_Temple\week5\day1\Project>git remote add origin https://github.com/cstevenson7/Flask_week5-day1-Fav_Five.git

D:\Coding_Temple\week5\day1\Project>git push origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 227 bytes | 227.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/cstevenson7/Flask_week5-day1-Fav_Five.git
 * [new branch]      master -> master

D:\Coding_Temple\week5\day1\Project>python -m venv fave_five_env

D:\Coding_Temple\week5\day1\Project>fave_five_env\scripts\activate.bat

(fave_five_env) D:\Coding_Temple\week5\day1\Project>pip install flask
Collecting flask
  Using cached https://files.pythonhosted.org/packages/f2/28/2a03252dfb9ebf377f40fba6a7841b47083260bf8bd8e737b0c6952df83f/Flask-1.1.2-py2.py3-none-any.whl
Collecting itsdangerous>=0.24 (from flask)
  Using cached https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Werkzeug>=0.15 (from flask)
  Using cached https://files.pythonhosted.org/packages/cc/94/5f7079a0e00bd6863ef8f1da638721e9da21e5bacee597595b318f71d62e/Werkzeug-1.0.1-py2.py3-none-any.whl
Collecting Jinja2>=2.10.1 (from flask)
  Using cached https://files.pythonhosted.org/packages/30/9e/f663a2aa66a09d838042ae1a2c5659828bb9b41ea3a6efa20a20fd92b121/Jinja2-2.11.2-py2.py3-none-any.whl
Collecting click>=5.1 (from flask)
  Using cached https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->flask)
  Using cached https://files.pythonhosted.org/packages/65/c6/2399700d236d1dd681af8aebff1725558cddfd6e43d7a5184a675f4711f5/MarkupSafe-1.1.1-cp37-cp37m-win_amd64.whl
Installing collected packages: itsdangerous, Werkzeug, MarkupSafe, Jinja2, click, flask
Successfully installed Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0
WARNING: You are using pip version 19.2.3, however version 20.2.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command



To get back into the virtual env
D:\Coding_Temple\week5\day1\Project>python -m venv fave_five_env

D:\Coding_Temple\week5\day1\Project>fave_five_env\scripts\activate.bat

Then create app.py
then these two commands

(fave_five_env) D:\Coding_Temple\week5\day1\Project>set FLASK_APP=app.py         

(fave_five_env) D:\Coding_Temple\week5\day1\Project>set FLASK_ENV=development

then flask run 
(fave_five_env) D:\Coding_Temple\week5\day1\Project>flask run