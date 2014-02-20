# ppro

Programming Paradigms class materials.


## Programming Language Tutorial

Tutorial about the [Io](http://iolanguage.org/) programming language. Uses the [reveal.js](https://github.com/hakimel/reveal.js) html presentation framework.


### Installation

1. Install [Node.js](http://nodejs.org/) and [Grunt](http://gruntjs.com/getting-started#installing-the-cli)

2. Navigate to the project folder
```sh
$ cd ppro
```

3. Install dependencies
```sh
$ npm install
```

4. Navigate to the reveal.js directory
```sh
$ cd reveal.js
```

5. Serve the presentation and monitor source files for changes
```sh
$ grunt serve
```

6. Open [http://localhost:8000](http://localhost:8000) to view your presentation

## Protein Folding Analysis - Proteilysis.com

### Installation

1. Install [pip](http://pip.readthedocs.org/en/latest/installing.html)

2. Install [virtualenv](https://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
```sh
$ pip install virtualenvwrapper
```

3. After virtualenvwrapper is installed, add the following to your .bash_profile
```sh
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/directory-you-do-development-in
source /usr/local/bin/virtualenvwrapper.sh
```

4. Create a new virtual environment
```sh
$ mkvirtualenv proteylysis
```

5. Navigate to the repo folder
```sh
$ cd ppro
```

6. Install dependencies
```sh
$ pip install -r requirements.txt
```

7. Install [Postgres.app](http://postgresapp.com/) and start it

8. Navigate to the project folder
```sh
$ cd proteilysis
```

9. Sync database and run migrations
```sh
$ python manage.py syncdb
$ python manage.py migrate protein_folding_analysis
```

10. Start local server
```sh
$ python manage.py runserver
```

## Related Resources

+ [Starting a Django project the right way](http://www.jeffknupp.com/blog/2013/12/18/starting-a-django-16-project-the-right-way/)
+ [Io official site](http://iolanguage.org/)
+ [Io - progopedia.com](http://progopedia.com/language/io/)
+ [A successful git branching model](http://nvie.com/posts/a-successful-git-branching-model/) 
