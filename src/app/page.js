import Link from "next/link";

export default function HomePage() {

  return (

    <div className="min-h-screen bg-[#0B1120] text-white flex flex-col items-center justify-center p-6">

      <h1 className="text-6xl font-bold mb-6">
        Task Manager
      </h1>

      <p className="text-gray-400 text-xl mb-10 text-center">
        Organize your tasks efficiently
      </p>

      <div className="flex gap-5">

        <Link
          href="/login"
          className="bg-blue-600 hover:bg-blue-700 px-8 py-4 rounded-xl"
        >
          Login
        </Link>

        <Link
          href="/register"
          className="bg-green-600 hover:bg-green-700 px-8 py-4 rounded-xl"
        >
          Register
        </Link>

      </div>

    </div>
  );
}