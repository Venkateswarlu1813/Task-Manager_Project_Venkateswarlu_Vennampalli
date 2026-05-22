"use client";

import { useEffect } from "react";

import { useRouter } from "next/navigation";

import AdminDashboard from "../../components/AdminDashboard";

export default function Page() {

  const router = useRouter();

  useEffect(() => {

    const user = JSON.parse(
      localStorage.getItem("user")
    );

    if (
      !user ||
      user.email !== "admin1813@gmail.com"
    ) {

      router.push("/login");
    }

  }, []);

  return <AdminDashboard />;
}