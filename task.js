        
        const apiUrl = "http://127.0.0.1:8000/tasks";
// This script fetches tasks from a fastAPI 
        async function fetchTasks() {
            const res = await fetch(apiUrl);
            const tasks = await res.json();

            // Updates the task list in the html
            const list = document.getElementById("task-list");
            list.innerHTML = "";
            
// This script displays the tasks in a list format
            tasks.forEach(task => {
                const item = document.createElement("li");
                item.textContent = `${task.id}: ${task.title} - ${task.completed ? "successful" : "failed"}`;

                const del = document.createElement("button");
                del.textContent = "Delete";
                del.onclick = async () => {
                    await fetch(`${apiUrl}/${task.id}`, { method: "DELETE" });
                    fetchTasks();
                };

                item.appendChild(del);
                list.appendChild(item);
            });
        }
//  This script handles the form submission to add a new task
        document.getElementById("task-form").onsubmit = async function(e) {
            e.preventDefault();
            const id = document.getElementById("id").value;
            const title = document.getElementById("title").value;
// This script sends a POST request to add a new task 
            await fetch(apiUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ id: Number(id), title, completed: false })
            });

            // Refresh the task list after adding a new task
            fetchTasks();
            this.reset();
        };

        fetchTasks();
    