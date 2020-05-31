from flask import Flask, render_template, request
import docker
from forms import CreateContainer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapp'
client = docker.from_env()

@app.route('/list-containers')
def index():
    containers_list = client.containers.list(all=False)
    for i in containers_list:
        print(i)
    return render_template('index.html', containers=containers_list)


@app.route('/create-container', methods=['POST','GET'])
def create_container():
    #client = docker.from_env()
    form = CreateContainer()
    if form.is_submitted():
        result = request.form
        for i in result:
            print(result[i])
        #client.containers.run(container_image, name=container_name, detach=True)
    return render_template('create-container.html', form=form)

