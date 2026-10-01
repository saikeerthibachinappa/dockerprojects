const API_URL = "http://localhost:5050/api";

async function loadTasks() {
    const response = await fetch(`${API_URL}/tasks`);
    const tasks = await response.json();

    const taskList = document.getElementById("taskList");
    taskList.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");

        li.innerHTML = `
            ${task.name}
            <button onclick="deleteTask('${task.id}')">Delete</button>
        `;

        taskList.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById("taskInput");
    const name = input.value.trim();

    console.log("Task being sent:", name);

    if (!name) {
        return;
    }

    const response = await fetch("http://localhost:5050/api/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name
        })
    });

    const result = await response.json();

    console.log("Backend response:", result);

    input.value = "";
    loadTasks();
}

loadTasks();