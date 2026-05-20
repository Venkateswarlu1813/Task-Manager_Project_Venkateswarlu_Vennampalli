"use client";

import Cookies from "js-cookie";

import { useRouter } from "next/navigation";

import { useEffect } from "react";

import { useUser } from "../../context/Usercontext";

export default function DashboardPage() {

  const router = useRouter();

  const { user, loading } = useUser();

  useEffect(() => {

    const token = Cookies.get("token");

    if (!token) {

      router.push("/login");
    }

  }, []);

  const handleLogout = () => {

    Cookies.remove("token");

    router.push("/login");
  };

  if (loading) {

    return (

      <div className="min-h-screen bg-black text-white flex items-center justify-center">

        Loading...

      </div>
    );
  }

  return (

    <div className="min-h-screen bg-black text-white flex">

      {/* SIDEBAR */}

      <div className="w-[250px] bg-zinc-900 p-6">

        <h1 className="text-3xl font-bold mb-10">

          Task Manager

        </h1>

        <ul className="space-y-5">

          <li className="cursor-pointer hover:text-gray-400">

            Dashboard

          </li>

          <li className="cursor-pointer hover:text-gray-400">

            Teams

          </li>

          <li className="cursor-pointer hover:text-gray-400">

            Tasks

          </li>

          <li className="cursor-pointer hover:text-gray-400">

            Notifications

          </li>

        </ul>

        <button
          onClick={handleLogout}
          className="mt-10 bg-red-500 px-5 py-2 rounded-lg"
        >

          Logout

        </button>

      </div>

      {/* MAIN CONTENT */}

      <div className="flex-1 p-10">

        <div className="flex justify-between items-center">

          <div>

            <h1 className="text-4xl font-bold">

              Dashboard

            </h1>

            <p className="text-gray-400 mt-2">

              Welcome back,
              {" "}
              {user?.username}

            </p>

          </div>

          <div className="bg-zinc-900 px-5 py-3 rounded-xl">

            <p className="text-sm text-gray-400">

              Logged In As

            </p>

            <h2 className="text-lg font-bold">

              {user?.email}

            </h2>

          </div>

        </div>

        {/* CARDS */}

        <div className="grid grid-cols-3 gap-6 mt-10">

          <div className="bg-zinc-900 p-6 rounded-2xl">

            <h2 className="text-2xl font-bold">

              Total Tasks

            </h2>

            <p className="text-4xl mt-4">

              12

            </p>

          </div>

          <div className="bg-zinc-900 p-6 rounded-2xl">

            <h2 className="text-2xl font-bold">

              Teams

            </h2>

            <p className="text-4xl mt-4">

              4

            </p>

          </div>

          <div className="bg-zinc-900 p-6 rounded-2xl">

            <h2 className="text-2xl font-bold">

              Pending Tasks

            </h2>

            <p className="text-4xl mt-4">

              6

            </p>

          </div>

        </div>

      </div>

    </div>
  );
}