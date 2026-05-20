"use client";

import { useState } from "react";

import { useRouter } from "next/navigation";

import Cookies from "js-cookie";

import { toast, Toaster } from "react-hot-toast";

import { GoogleLogin } from "@react-oauth/google";

import API from "../../services/api";

export default function LoginPage() {

  const router = useRouter();

  const [formData, setFormData] = useState({
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

  const handleLogin = async (e) => {

    e.preventDefault();

    try {

      setLoading(true);

      const response = await API.post(
        "auth/login/",
        formData
      );

      Cookies.set(
        "access",
        response.data.access,
        { expires: 3 }
      );

      localStorage.setItem(
        "access",
        response.data.access
      );

      Cookies.set(
        "refresh",
        response.data.refresh,
        { expires: 3 }
      );

      Cookies.set(
        "username",
        response.data.user.username,
        { expires: 3 }
      );

      localStorage.setItem(
        "user",
        JSON.stringify(response.data.user)
      );

      toast.success("Login Successful");

      if (response.data.user.role === "admin") {

        router.push("/admin-dashboard");

      } else {

        router.push("/dashboard");
      }

    } catch (error) {

      console.log(error);

      toast.error("Invalid Credentials");

    } finally {

      setLoading(false);
    }
  };

  const handleGoogleSuccess = async (
    credentialResponse
  ) => {

    try {

      const response = await API.post(
        "auth/google-login/",
        {
          token: credentialResponse.credential,
        }
      );

      Cookies.set(
        "access",
        response.data.access,
        { expires: 3 }
      );

      Cookies.set(
        "refresh",
        response.data.refresh,
        { expires: 3 }
      );

      Cookies.set(
        "username",
        response.data.user.username,
        { expires: 3 }
      );

      localStorage.setItem(
        "user",
        JSON.stringify(response.data.user)
      );

      localStorage.setItem(
        "access",
        response.data.access
      );

      toast.success(
        "Google Login Successful"
      );

      if (response.data.user.role === "admin") {

        router.push("/admin-dashboard");

      } else {

        router.push("/dashboard");
      }

    } catch (error) {

      console.log(error);

      toast.error("Google Login Failed");
    }
  };

  return (

    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-indigo-100 flex justify-center items-center p-6">

      <Toaster position="top-right" />

      <div className="bg-white p-10 rounded-3xl shadow-2xl w-full max-w-md">

        <h1 className="text-4xl font-bold text-center text-blue-700 mb-2">
          Task Manager
        </h1>

        <p className="text-center text-gray-500 mb-8">
          Login to continue
        </p>

        <form
          onSubmit={handleLogin}
          className="space-y-5"
        >

          <input
            type="email"
            name="email"
            placeholder="Enter Email"
            value={formData.email}
            onChange={handleChange}
            required
            className="w-full p-4 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <input
            type="password"
            name="password"
            placeholder="Enter Password"
            value={formData.password}
            onChange={handleChange}
            required
            className="w-full p-4 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white p-4 rounded-xl font-bold transition duration-300"
          >

            {
              loading
                ? "Logging in..."
                : "Login"
            }

          </button>

        </form>

        <div className="my-6 text-center text-gray-400">
          OR
        </div>

        <div className="flex justify-center">

          <GoogleLogin
            onSuccess={handleGoogleSuccess}
            onError={() => {
              toast.error(
                "Google Login Failed"
              );
            }}
          />

        </div>

      </div>

    </div>
  );
}