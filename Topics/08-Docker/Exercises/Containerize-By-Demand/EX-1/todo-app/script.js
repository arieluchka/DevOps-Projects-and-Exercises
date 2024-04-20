function addTask() {
    const taskInput = document.getElementById('new-task');
    const newTask = taskInput.value.trim();
    if (newTask !== '') {
        const listItem = document.createElement('li');
        listItem.textContent = newTask;
        listItem.onclick = function () { this.classList.toggle('completed'); };
        document.getElementById('task-list').appendChild(listItem);
        taskInput.value = '';
    }
}

function clearCompleted() {
    const list = document.getElementById('task-list');
    Array.from(list.children)
        .filter(item => item.classList.contains('completed'))
        .forEach(item => list.removeChild(item));
}
