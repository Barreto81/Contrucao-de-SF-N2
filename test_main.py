from db import create_task, get_tasks, update_task_status, delete_task

def test_create_task():
    create_task("Test Task", "Description", "Pendente")
    tasks = get_tasks()
    assert len(tasks) == 1
    assert tasks[0][1] == "Test Task"

def test_update_task_status():
    create_task("Task to Update", "Description", "Pendente")
    tasks = get_tasks()
    task_id = tasks[0][0]
    update_task_status(task_id, "Concluído")
    updated_task = get_tasks()[0]
    assert updated_task[3] == "Concluído"

def test_delete_task():
    create_task("Task to Delete", "Description", "Pendente")
    tasks = get_tasks()
    task_id = tasks[0][0]
    delete_task(task_id)
    tasks_after_deletion = get_tasks()
    assert len(tasks_after_deletion) == 0
