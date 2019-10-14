# sinistralidadeansr

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Run your end-to-end tests
```
npm run test:e2e
```

### Run your unit tests
```
npm run test:unit
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## Create virtual env 

### Create a directory to your project
```
mkdir django-vue
```

### Move the cursor to it
```
cd django-vue
```

### Initialize a virtual env on it
```
python3 -m venv ./
```

### Activate venv
```
source ./bin/activate
```

### Install django
```
pip install django
```

### Create django project
```
django-admin startproject djangovue .
```

### Migrate db and start server 
```
python manage.py migrate
python manage.py runserver
```

## Install dependencies
```
pip install -r requirements.txt
```

## Update dependencies
```
pip freeze > requirements.txt
```


