<!-- <template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.png" width="125" height="125" />

    <nav>
      <RouterLink to="/">Home</RouterLink>
    </nav>
  </header>

  <RouterView />
</template> -->

<template>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<!-- <style scoped>
/* .logo {
  display: block;
  margin: 0 auto;
}

nav {
  text-align: center;
  margin-top: 1rem;
} */
#app {
  /* Ensuring the app fills the entire screen; adjust as needed */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

</style> -->
