# Fast-api-template
A Fast-api template with asynchronous queries, migration and oAuth2



## How to use it

Go to the directory where you want to create your project and run:

```bash
pip install cookiecutter
cookiecutter https://github.com/GuilhermeVBeira/fast-api-template
```
Install dependencies.

We use [poetry](https://poetry.eustace.io/) to manage dependencies, so make sure you have it installed.
```
make install
```
Create .env
```
cp default.env .env
```
After create database test and set on [.env](https://github.com/GuilhermeVBeira/fast-api-template/blob/main/%7B%7Bcookiecutter.project_name%7D%7D/default.env) file
Update the values of databases and SECRET_KEY

Sync migrations

```
make migrate
```
Run
```
make run
```
