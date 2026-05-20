"use client";

import { useEffect, useState } from "react";
import Cookies from "js-cookie";
import API from "../../services/api";
import { useRouter } from "next/navigation";
import toast, { Toaster } from "react-hot-toast";

export default function DashboardPage() {

  const router = useRouter();

  const [mounted, setMounted] = useState(false);

  const [darkMode, setDarkMode] = useState(false);

  const [tasks, setTasks] = useState([]);

  const [loading, setLoading] = useState(false);

  const [search, setSearch] = useState("");

  const [filterPriority, setFilterPriority] =
    useState("all");

  const [editTaskId, setEditTaskId] =
    useState(null);

  const [formData, setFormData] = useState({
    title: "",
    description: "",
    priority: "medium",
    due_date: "",
  });

  useEffect(() => {

    setMounted(true);

    if (!Cookies.get("access")) {
      router.push("/login");
    }

    fetchTasks();

  }, []);

  const fetchTasks = async () => {

    try {

      const token = Cookies.get("access");

      const response = await API.get(
        "tasks/",
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const updatedTasks = response.data.map(
        (task) => ({
          ...task,
          expanded: false,
        })
      );

      setTasks(updatedTasks);

    } catch (error) {

      console.log(error);
    }
  };

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleCreateTask = async () => {

  try {

    setLoading(true);

    const token = Cookies.get("access");

    const payload = {
      title: formData.title,
      description: formData.description,
      priority: formData.priority,
      due_date: formData.due_date || null,
    };

    if (editTaskId) {

      await API.put(
        `tasks/${editTaskId}/`,
        payload,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      toast.success("Task Updated");

      setEditTaskId(null);

    } else {

      await API.post(
        "tasks/",
        payload,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      toast.success("Task Created");
    }

    setFormData({
      title: "",
      description: "",
      priority: "medium",
      due_date: "",
    });

    fetchTasks();

  } catch (error) {

    console.log(error);

    toast.error("Operation Failed");

  } finally {

    setLoading(false);
  }
};

  const handleDelete = async (id) => {

    try {

      const token = Cookies.get("access");

      await API.delete(
        `tasks/${id}/`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      fetchTasks();

      toast.success("Task Deleted");

    } catch (error) {

      console.log(error);

      toast.error("Delete Failed");
    }
  };

  const handleStatus = async (task) => {

  try {

    const token = Cookies.get("access");

    const updatedStatus =
      task.status === "completed"
        ? "todo"
        : "completed";

    await API.patch(
      `tasks/tasks/${task.id}/status/`,
      {
        status: updatedStatus,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    toast.success("Status Updated");

    fetchTasks();

  } catch (error) {

    console.log(error);

    toast.error("Status Failed");
  }
};


  const handleEdit = (task) => {

    setEditTaskId(task.id);

    setFormData({
      title: task.title,
      description: task.description,
      priority: task.priority,
      due_date: task.due_date
        ? String(task.due_date).split("T")[0]
        : "",
    });

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  const logout = () => {

    Cookies.remove("access");
    Cookies.remove("refresh");
    Cookies.remove("user");

    router.push("/login");
  };

  const filteredTasks = tasks.filter((task) => {

    const matchesSearch =
      task.title.toLowerCase().includes(
        search.toLowerCase()
      );

    const matchesPriority =
      filterPriority === "all"
        ? true
        : task.priority === filterPriority;

    return matchesSearch && matchesPriority;
  });

  const completedTasks = tasks.filter(
    (task) => task.status === "completed"
  ).length;

  const pendingTasks = tasks.filter(
    (task) => task.status === "todo"
  ).length;

  const highPriorityTasks = tasks.filter(
    (task) => task.priority === "high"
  ).length;

  if (!mounted) return null;

  return (

    <div
      className={`min-h-screen p-8 transition-all duration-300 ${
        darkMode
          ? "bg-[#0f172a] text-white"
          : "bg-[#f5f7fb] text-black"
      }`}
    >

      <Toaster />

      {/* HEADER */}

      <div className="bg-white rounded-3xl shadow-md px-10 py-6 flex justify-between items-center mb-10">

        <div>

          <h1 className="text-5xl font-bold text-[#172554]">
            Task Manager
          </h1>

          <p className="text-gray-500 text-lg mt-2">
            Organize your tasks efficiently
          </p>

        </div>

        <div className="flex items-center gap-4">

          <button
            onClick={() =>
              setDarkMode(!darkMode)
            }
            className="bg-black hover:bg-gray-800 text-white px-6 py-4 rounded-2xl font-bold"
          >

            {darkMode ? "Light" : "Dark"}

          </button>

          <button
            onClick={logout}
            className="bg-red-500 hover:bg-red-600 text-white px-8 py-4 rounded-2xl font-bold"
          >
            Logout
          </button>

        </div>

      </div>

      {/* STATS */}

      <div className="grid md:grid-cols-4 gap-6 mb-10">

        <div className="bg-white rounded-3xl p-8 shadow-md border border-blue-200">

          <h2 className="text-5xl font-bold text-blue-600">
            {tasks.length}
          </h2>

          <p className="text-xl mt-3">
            Total Tasks
          </p>

        </div>

        <div className="bg-white rounded-3xl p-8 shadow-md border border-green-200">

          <h2 className="text-5xl font-bold text-green-600">
            {completedTasks}
          </h2>

          <p className="text-xl mt-3">
            Completed
          </p>

        </div>

        <div className="bg-white rounded-3xl p-8 shadow-md border border-yellow-200">

          <h2 className="text-5xl font-bold text-yellow-500">
            {pendingTasks}
          </h2>

          <p className="text-xl mt-3">
            Pending
          </p>

        </div>

        <div className="bg-white rounded-3xl p-8 shadow-md border border-red-200">

          <h2 className="text-5xl font-bold text-red-500">
            {highPriorityTasks}
          </h2>

          <p className="text-xl mt-3">
            High Priority
          </p>

        </div>

      </div>

      {/* SEARCH FILTER */}

      <div className="grid md:grid-cols-2 gap-5 mb-10">

        <input
          type="text"
          placeholder="Search tasks..."
          value={search}
          onChange={(e) =>
            setSearch(e.target.value)
          }
          className="border-2 border-blue-300 rounded-2xl p-5 text-lg bg-white"
        />

        <select
          value={filterPriority}
          onChange={(e) =>
            setFilterPriority(e.target.value)
          }
          className="border-2 border-yellow-300 rounded-2xl p-5 text-lg bg-white"
        >

          <option value="all">
            All Priorities
          </option>

          <option value="high">
            High
          </option>

          <option value="medium">
            Medium
          </option>

          <option value="low">
            Low
          </option>

        </select>

      </div>

      {/* CREATE TASK */}

      <div className="bg-white rounded-3xl shadow-md p-10 mb-10">

        <h2 className="text-5xl font-bold text-green-600 mb-10">
          {editTaskId
            ? "Edit Task"
            : "Create New Task"}
        </h2>

        <div className="grid md:grid-cols-2 gap-6 mb-6">

          <input
            type="text"
            name="title"
            value={formData.title}
            onChange={handleChange}
            placeholder="Task title"
            className="border-2 border-blue-300 rounded-2xl p-5 text-lg"
          />

          <select
            name="priority"
            value={formData.priority}
            onChange={handleChange}
            className="border-2 border-yellow-300 rounded-2xl p-5 text-lg"
          >

            <option value="low">
              Low
            </option>

            <option value="medium">
              Medium
            </option>

            <option value="high">
              High
            </option>

          </select>

        </div>

        <textarea
          rows="5"
          name="description"
          value={formData.description}
          onChange={handleChange}
          placeholder="Task description..."
          className="w-full border-2 border-blue-300 rounded-2xl p-5 text-lg mb-6"
        />

        <input
          type="date"
          name="due_date"
          value={formData.due_date}
          onChange={handleChange}
          className="border-2 border-green-300 rounded-2xl p-5 text-lg mb-6 w-full"
        />

        <button
          onClick={handleCreateTask}
          className="bg-green-500 hover:bg-green-600 text-white px-12 py-5 rounded-2xl text-2xl font-bold"
        >

          {loading
            ? "Processing..."
            : editTaskId
            ? "Update Task"
            : "Create Task"}

        </button>

      </div>

      {/* TASK LIST */}

      <div className="space-y-8">

        {filteredTasks.map((task) => (

          <div
            key={task.id}
            className="bg-white rounded-3xl shadow-md p-8 border-l-[10px] border-blue-500 hover:scale-[1.01] transition-all"
          >

            <div className="flex justify-between items-start">

              {/* LEFT */}

              <div className="flex-1">

                <div
                  className="cursor-pointer"
                  onClick={() =>
                    setTasks(
                      tasks.map((t) =>
                        t.id === task.id
                          ? {
                              ...t,
                              expanded: !t.expanded,
                            }
                          : t
                      )
                    )
                  }
                >

                  <h2 className="text-3xl font-bold text-blue-600 mb-4 hover:text-blue-800">

                    {task.title}

                  </h2>

                </div>

                {/* DESCRIPTION */}

                {task.expanded && (

                  <div className="mt-4">

                    <p className="text-gray-700 text-xl mb-5">

                      {task.description}

                    </p>

                  </div>

                )}

                {/* TAGS */}

                <div className="flex gap-4 mt-4 flex-wrap">

                  <span className="bg-blue-100 text-blue-600 px-5 py-3 rounded-xl font-bold capitalize">

                    {task.priority}

                  </span>

                  <span
                    className={`px-5 py-3 rounded-xl font-bold capitalize ${
                      task.status === "completed"
                        ? "bg-green-100 text-green-600"
                        : "bg-yellow-100 text-yellow-600"
                    }`}
                  >

                    {task.status}

                  </span>

                  <span className="bg-red-100 text-red-600 px-5 py-3 rounded-xl font-bold">

                    Due:{" "}
                    {task.due_date
                      ? String(task.due_date).split("T")[0]
                      : "No Date"}

                  </span>

                </div>

              </div>

              {/* BUTTONS */}

              <div className="flex flex-col gap-4 ml-6">

                <button
                  onClick={() =>
                    handleEdit(task)
                  }
                  className="bg-blue-500 hover:bg-blue-600 text-white px-8 py-4 rounded-2xl font-bold"
                >
                  Edit
                </button>

                <button
                  onClick={() =>
                    handleStatus(task)
                  }
                  className="bg-yellow-400 hover:bg-yellow-500 text-white px-8 py-4 rounded-2xl font-bold"
                >

                  {task.status === "completed"
                    ? "Pending"
                    : "Complete"}

                </button>

                <button
                  onClick={() =>
                    handleDelete(task.id)
                  }
                  className="bg-red-500 hover:bg-red-600 text-white px-8 py-4 rounded-2xl font-bold"
                >
                  Delete
                </button>

              </div>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}