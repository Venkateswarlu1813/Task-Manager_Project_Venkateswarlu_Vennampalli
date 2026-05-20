"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import API from "../../services/api";

export default function RegisterPage() {

  const router = useRouter();

  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });

  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      setLoading(true);

      const response = await API.post(
        "auth/register/",
        formData
      );

      console.log(response.data);

      alert("Registration Successful");

      router.push("/login");

    } catch (error) {

      console.log(error.response?.data);

      alert(
        JSON.stringify(
          error.response?.data || "Registration Failed"
        )
      );

    } finally {

      setLoading(false);

    }
  };

  return (

    <div className="min-h-screen flex items-center justify-center bg-[#0f172a]">

      <form
        onSubmit={handleSubmit}
        className="bg-[#1e293b] p-10 rounded-2xl w-[400px] shadow-2xl"
      >

        <h1 className="text-4xl font-bold text-white text-center mb-8">
          Register
        </h1>

        <div className="mb-5">

          <label className="text-gray-300 block mb-2">
            Username
          </label>

          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            placeholder="Enter Username"
            className="w-full p-4 rounded-xl bg-[#0f172a] border border-gray-700 text-white"
            required
          />

        </div>

        <div className="mb-5">

          <label className="text-gray-300 block mb-2">
            Email
          </label>

          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Enter Email"
            className="w-full p-4 rounded-xl bg-[#0f172a] border border-gray-700 text-white"
            required
          />

        </div>

        <div className="mb-8">

          <label className="text-gray-300 block mb-2">
            Password
          </label>

          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            placeholder="Enter Password"
            className="w-full p-4 rounded-xl bg-[#0f172a] border border-gray-700 text-white"
            required
          />

        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-blue-600 hover:bg-blue-700 p-4 rounded-xl text-white font-semibold"
        >

          {
            loading
              ? "Registering..."
              : "Register"
          }

        </button>

      </form>

    </div>
  );
}