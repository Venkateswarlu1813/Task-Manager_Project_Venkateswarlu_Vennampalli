"use client";

import {
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";

import API from "../services/api";

const UserContext = createContext();

export const UserProvider = ({ children }) => {

  const [user, setUser] = useState(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    fetchUser();

  }, []);

  const fetchUser = async () => {

    try {

      const response = await API.get(
        "users/me/"
      );

      setUser(response.data);

    } catch (error) {

      console.log(error);

      setUser(null);

    } finally {

      setLoading(false);
    }
  };

  return (

    <UserContext.Provider
      value={{
        user,
        loading,
        setUser,
      }}
    >

      {children}

    </UserContext.Provider>
  );
};

export const useUser = () => useContext(UserContext);