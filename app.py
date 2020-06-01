from flask import Flask, render_template, request, redirect, url_for, flash
import docker
from forms import CreateContainer, ManageContainers

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapp'
client = docker.from_env()

@app.route('/', methods=['POST','GET'])
def index():
    form = ManageContainers()
    containers_list = client.containers.list(all=True)
    return render_template('index.html', containers=containers_list, form=form)

@app.route('/create-container', methods=['POST','GET'])
def create_container():
    form = CreateContainer()
    if form.is_submitted():
        params = {}
        container_image = form.containerimage.data
        container_name = form.containername.data
        if form.is_interactive_tty.data == True:
            params['stdin_open'] = True
            params['tty'] = True
        x = client.containers.run(container_image, name=container_name, detach=True, **params)
        flash(f"{container_name} {x.short_id} created")

        return redirect(url_for('index'))
    return render_template('create-container.html', form=form)


@app.route('/<id>')
def container(id):
    return (f"This is {id} container")



@app.route('/stop-container/<id>', methods=['POST'])
def stop_container(id):
    container_instance = client.containers.get(container_id=str(id))
    container_instance.stop()
    flash(f"Stopped {id}")
    return redirect(url_for('index'))

@app.route('/start-container/<id>', methods=['POST'])
def start_container(id):
    container_instance = client.containers.get(container_id=str(id))
    container_instance.start()
    flash(f"Started {id}")
    return redirect(url_for('index'))

@app.route('/remove-container/<id>', methods=['POST'])
def remove_container(id):
    container_instance = client.containers.get(container_id=str(id))
    container_instance.stop()
    container_instance.remove()
    flash(f"Deleted {id}")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')