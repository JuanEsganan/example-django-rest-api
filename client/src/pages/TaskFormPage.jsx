import { useEffect } from "react";
import {useForm} from "react-hook-form"
import { createTask, delete_tasks, update_tasks, getTask } from "../api/tasks.api"
import { useNavigate, useParams } from "react-router-dom";
import { toast } from "react-hot-toast";

export function TasksFormPage() {
    const {register, 
        handleSubmit, 
        formState: {errors}, setValue} = useForm ();

    const navigate = useNavigate ()
    const params = useParams ()

    const onSubmit = handleSubmit (async (data) =>{
        if (params.id){
            await update_tasks (params.id, data)
            toast.success("Tarea Actualizada")
        } else {
        await createTask (data)};
        toast.success("Tarea Creada");
        
        navigate ("/tasks");
    });

    useEffect (() => {
        async function loadTask () {
            if (params.id) {
            const res = await getTask (params.id);
            setValue ("titulo", res.data.titulo)
            setValue ("descripcion", res.data.descripcion)
            }
        } loadTask ()

    }, [])

    return (
        <div className="max-w-xl mx-auto">
            <form onSubmit={onSubmit}>
                <input type="text" placeholder="Tiulo"  
                {...register("titulo", {required:true})}
                className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.titulo && <span>El titulo es requierido</span>}
                <textarea rows="3" placeholder="Descripcion"
                {...register("descripcion", {required:true})}
                className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                ></textarea>
                {errors.descripcion && <span>La descripcion es requierida</span>}
                <button
                className="bg-indigo-500 p3 rounded-lg block w-full mt-3"
                >Save</button>
            </form>

        { params.id && 
        <div className="flex justify-end"> 
            <button 
            className="bg-red-500 p-3 rounded-lg w-48 mt-3"
        onClick={ async () => {
            const accepted = window.confirm("esta seguro?")
            if (accepted ) {
                await delete_tasks (params.id)
                toast.success("Tarea Eliminada")
                navigate("/tasks")
            }
        }}>Delete</button>
        </div>
        }

        </div>
    )
}