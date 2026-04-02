from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def get_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        f.write("\n".join(tasks))


@app.route("/")
def index():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task and task.strip():
        tasks = get_tasks()
        tasks.append(task)
        save_tasks(tasks)
    return redirect("/")


@app.route("/delete/<int:index>")
def delete(index):
    tasks = get_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
