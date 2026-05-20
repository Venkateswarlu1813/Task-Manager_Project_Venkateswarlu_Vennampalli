"use client";

import { useEffect, useState } from "react";

export default function AdminDashboard() {

  const [users, setUsers] = useState([]);

  const [tasks, setTasks] = useState([]);

  useEffect(() => {

    const token = localStorage.getItem("access");

    // Fetch Tasks
    fetch("http://127.0.0.1:8000/api/tasks/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {

        console.log("Tasks:", data);

        if (Array.isArray(data)) {

          setTasks(data);

        } else if (data.results) {

          setTasks(data.results);

        } else {

          setTasks([]);
        }
      })
      .catch((err) => console.log(err));

    // Fetch Users
    fetch("http://127.0.0.1:8000/api/users/all-users/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {

        console.log("Users:", data);

        if (Array.isArray(data)) {

          setUsers(data);

        } else if (data.results) {

          setUsers(data.results);

        } else {

          setUsers([]);
        }
      })
      .catch((err) => console.log(err));

  }, []);

  const completedTasks = tasks.filter(
    (task) => task.status === "completed"
  ).length;

  const pendingTasks = tasks.filter(
    (task) => task.status !== "completed"
  ).length;

  const highPriorityTasks = tasks.filter(
    (task) => task.priority === "high"
  ).length;

  return (

    <div className="min-h-screen bg-gray-100 p-8">

      <h1 className="text-4xl font-bold text-blue-900 mb-8">
        Admin Dashboard
      </h1>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-5 gap-6 mb-10">

        <div className="bg-white p-6 rounded-2xl shadow">
          <h2 className="text-xl font-semibold">
            Total Tasks
          </h2>

          <p className="text-4xl font-bold text-blue-600 mt-3">
            {tasks.length}
          </p>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow">
          <h2 className="text-xl font-semibold">
            Completed
          </h2>

          <p className="text-4xl font-bold text-green-600 mt-3">
            {completedTasks}
          </p>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow">
          <h2 className="text-xl font-semibold">
            Pending
          </h2>

          <p className="text-4xl font-bold text-yellow-500 mt-3">
            {pendingTasks}
          </p>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow">
          <h2 className="text-xl font-semibold">
            High Priority
          </h2>

          <p className="text-4xl font-bold text-red-500 mt-3">
            {highPriorityTasks}
          </p>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow">
          <h2 className="text-xl font-semibold">
            Total Users
          </h2>

          <p className="text-4xl font-bold text-purple-600 mt-3">
            {users.length}
          </p>
        </div>

      </div>

      {/* Users Table */}
      <div className="bg-white rounded-2xl shadow p-6 mb-10">

        <h2 className="text-2xl font-bold mb-6">
          All Users
        </h2>

        <div className="overflow-x-auto">

          <table className="w-full border-collapse">

            <thead>

              <tr className="bg-gray-200">

                <th className="p-3 text-left">
                  Username
                </th>

                <th className="p-3 text-left">
                  Email
                </th>

                <th className="p-3 text-left">
                  Role
                </th>

              </tr>

            </thead>

            <tbody>

              {users.map((user) => (

                <tr
                  key={user.id}
                  className="border-b"
                >

                  <td className="p-3">
                    {user.username}
                  </td>

                  <td className="p-3">
                    {user.email}
                  </td>

                  <td className="p-3 capitalize">
                    {user.role}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

      {/* Tasks Table */}
      <div className="bg-white rounded-2xl shadow p-6">

        <h2 className="text-2xl font-bold mb-6">
          All Tasks
        </h2>

        <div className="overflow-x-auto">

          <table className="w-full border-collapse">

            <thead>

              <tr className="bg-gray-200">

                <th className="p-3 text-left">
                  Title
                </th>

                <th className="p-3 text-left">
                  Priority
                </th>

                <th className="p-3 text-left">
                  Status
                </th>

                <th className="p-3 text-left">
                  Due Date
                </th>

              </tr>

            </thead>

            <tbody>

              {tasks.map((task) => (

                <tr
                  key={task.id}
                  className="border-b"
                >

                  <td className="p-3">
                    {task.title}
                  </td>

                  <td className="p-3 capitalize">
                    {task.priority}
                  </td>

                  <td className="p-3 capitalize">
                    {task.status}
                  </td>

                  <td className="p-3">
                    {task.due_date
                      ? task.due_date.split("T")[0]
                      : "No Date"}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

    </div>
  );
}