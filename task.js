 
        const apiUrl = "http://127.0.0.1:8000/tasks";

        async function fetchTasks() {
            const res = await fetch(apiUrl);
            const tasks = await res.json();

            const list = document.getElementById("task-list");
            list.innerHTML = "";

            tasks.forEach(task => {
                const item = document.createElement("li");
                item.textContent = `${task.id}: ${task.title} - ${task.completed ? "✅" : "❌"}`;

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

        document.getElementById("task-form").onsubmit = async function(e) {
            e.preventDefault();
            const id = document.getElementById("id").value;
            const title = document.getElementById("title").value;

            await fetch(apiUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ id: Number(id), title, completed: false })
            });

            fetchTasks();
            this.reset();
        };

        fetchTasks();
    