"use client";

import Cookies from "js-cookie";
import { useRouter } from "next/navigation";

export default function Navbar() {

  const router = useRouter();

  const logout = () => {

    Cookies.remove("access");
    Cookies.remove("refresh");
    Cookies.remove("user");

    router.push("/login");
  };

  return (

    <div
      style={{
        width: "100%",
        padding: "20px",
        background: "#111827",
        color: "white",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >

      <h2>Task Manager</h2>

      <button
        onClick={logout}
        style={{
          padding: "10px 20px",
          border: "none",
          borderRadius: "8px",
          background: "#ef4444",
          color: "white",
          cursor: "pointer",
        }}
      >
        Logout
      </button>

    </div>
  );
}