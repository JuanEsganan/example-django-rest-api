import axios from "axios"

const tasksApi = axios.create (
    {baseURL:"http://127.0.0.1:8000/tasks/api/v1/tareas/"})

export const getALLTaks = () => {
    return tasksApi.get ("/")
    };

export const createTask = (task) => {
    return tasksApi.post("/", task)
};

export const getTask = (id) => tasksApi.get(`/${id}/`)

export const delete_tasks = (id) => tasksApi.delete("/" + id)

export const update_tasks = (id, task) => tasksApi.put(`/${id}/`,task)
