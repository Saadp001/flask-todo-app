#Import necessary modules
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



# My app
app = Flask(__name__)

#SCSS configuration
#Scss(app, static_dir='static', asset_dir='static/sass')

#Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Database model
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String, default="pending")  # New field to track completion status                            
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
            
    def __repr__(self) -> str:
        return f'Task {self.id}'

with app.app_context():
    db.create_all()

#routes to web pages
#home page
@app.route("/", methods=['GET', 'POST'])
def index():
    #add task
    if request.method == 'POST':
        task_content = request.form['content']     # from the form input front-end
        new_task = MyTask(content=task_content)    # create new task instance in the database
        try:
            db.session.add(new_task)               # add new task to the database session
            db.session.commit()                     # commit the session to save the task
            return redirect('/')                    # redirect to home page
        except:
            return "There was an issue adding your task"

# see all current tasks
    else:
        tasks = MyTask.query.order_by(MyTask.date_created).all()  # query all tasks ordered by creation date
        return render_template('index.html', tasks=tasks)  # render the index template with tasks

#mark task as complete status 
@app.route('/complete/<int:id>')
def complete(id):
    task = MyTask.query.get_or_404(id)
    task.status = "completed"
    db.session.commit()
    return redirect('/')


#delete task after done
@app.route("/delete/<int:id>")
def delete(id:int):
    task_to_delete = MyTask.query.get_or_404(id)  # get task by id or return 404 if not found
    try:
        db.session.delete(task_to_delete)          # delete the task from the session
        db.session.commit()                         # commit the session to save changes
        return redirect('/')                        # redirect to home page
    except:
        return "There was a problem deleting that task"

#edit task
@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id:int):
    task = MyTask.query.get_or_404(id)  # get task by id or return 404 if not found
    if request.method == 'POST':
        task.content = request.form['content']  # update task content from form input
        try:
            db.session.commit()                  # commit the session to save changes
            return redirect('/')                 # redirect to home page
        except:
            return "There was an issue updating your task"
    else:
        return render_template('edit.html', task=task)  # render the edit template with the task


#API route to get all tasks in JSON format for external use 

# get all tasks
@app.route('/api/tasks', methods=['GET'])
def api_get_tasks():
    tasks = MyTask.query.all()
    output = []

    for t in tasks:
        output.append({
            "id": t.id,
            "content": t.content,
            "status": t.status
        })

    return jsonify(output)

#POST create task
@app.route('/api/tasks', methods=['POST'])
def api_add_task():
    data = request.json
    content = data.get("content")

    new_task = MyTask(content=content)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task created"}), 201

# GET a single task
@app.route('/api/tasks/<int:id>', methods=['GET'])
def api_get_task(id):
    task = MyTask.query.get_or_404(id)

    return jsonify({
        "id": task.id,
        "content": task.content,
        "status": task.status
    })

# PUT update/edit task
@app.route('/api/tasks/<int:id>', methods=['PUT'])
def api_update_task(id):
    task = MyTask.query.get_or_404(id)
    data = request.json

    task.content = data.get("content", task.content)
    db.session.commit()

    return jsonify({"message": "Task updated"})


# DELETE a task
@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def api_delete_task(id):
    task = MyTask.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"})

# PATCH → mark as completed status
@app.route('/api/tasks/<int:id>/complete', methods=['PATCH'])
def api_complete_task(id):
    task = MyTask.query.get_or_404(id)
    task.status = "completed"
    db.session.commit()

    return jsonify({"message": "Task marked as completed"})




#runner and debug mode
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


