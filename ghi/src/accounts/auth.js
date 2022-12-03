import { createContext, useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
let internalToken = null;



export async function getTokenInternal() {
  const url = `${process.env.REACT_APP_accounts}/api/accounts/me/token/`;
  try {
    const response = await fetch(url, {
      credentials: "",
    });
    if (response.ok) {
      const data = await response.json();
      internalToken = data.access_token;
      return internalToken;
    }
  } catch (e) { }
  return false;
}
export async function getToken() {
  return internalToken;
}

function handleErrorMessage(error) {
  if ("error" in error) {
    error = error.error;
    try {
      error = JSON.parse(error);
      if ("__all__" in error) {
        error = error.__all__;
      }
    } catch { }
  }
  if (Array.isArray(error)) {
    error = error.join("<br>");
  } else if (typeof error === "object") {
    error = Object.entries(error).reduce(
      (acc, x) => `${acc}<br>${x[0]}: ${x[1]}`,
      ""
    );
  }
  return error;
}

export const AuthContext = createContext({
  token: null,
  setToken: () => null,
  account: null,
  setAccount: () => null,
});

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(null);
  const [account, setAccount] = useState(null);

  return (
    <AuthContext.Provider value={{ token, setToken, account, setAccount }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuthContext = () => useContext(AuthContext);

export function useToken() {
  const { token, setToken, account, setAccount } = useAuthContext();
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchToken() {
      const [token, account] = await getTokenInternal();
      setToken(token);
      setAccount(account);

    }
    // if (!token) {
    //   fetchToken();
    // }
  }, [setToken, token, setAccount, account]);

  async function logout() {
    if (token) {
      const url = `${process.env.REACT_APP_accounts}/token/`;
      await fetch(url, { method: "delete", credentials: "include" });
      internalToken = null;
      setToken(null);
      setAccount(null);
      navigate("/");
    }
  }

  async function login(username, password) {
    const url = `${process.env.REACT_APP_accounts}/token/`;
    const form = new FormData();
    form.append("username", username);
    form.append("password", password);
    const response = await fetch(url, {
      method: "post",
      credentials: "include",
      body: form,
    });
    if (response.ok) {
      const [token, account] = await getTokenInternal();
      setToken(token);
      setAccount(account);
      return;
    }
    let error = await response.json();
    return handleErrorMessage(error);
  }

  async function signup(full_name, username, password) {
    const url = `${process.env.REACT_APP_accounts}/api/accounts/`;
    const response = await fetch(url, {
      method: "post",
      body: JSON.stringify({
        full_name,
        username,
        password

      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (response.ok) {
      navigate("/accounts/account");
    }

  }

  return [login, logout, signup];
}