<template>
    <div class="login-container">
      <div class="login-left">
        <img src="@/assets/logo.png" alt="Logo" class="logo"/>
      </div>
      <div class="login-right">
        <div class="login-box">
          <button @click="selectRole('paralegal')">Paralegal</button>
          <button @click="selectRole('customer')">Customer</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      selectRole(role) {
        // Here you might want to save the role or route to different paths based on the role
        console.log(role); // For demonstration
        // this.$router.push('/some-path');
      }
    }
  };
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    width: 100vw;
    height: 100vh;
  }
  
  .login-left {
    width: 40%;
    background-color: #003366; /* Dark blue */
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .logo {
    max-width: 60%; /* Adjust size accordingly */
    height: auto;
  }
  
  .login-right {
    width: 60%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .login-box {
    width: 300px; /* Adjust size accordingly */
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Soft shadow for the box */
    border-radius: 10px; /* Rounded corners */
    text-align: center;
  }
  
  button {
    margin: 10px;
    padding: 10px 20px;
    width: 100%;
    cursor: pointer;
  }
  </style>
  