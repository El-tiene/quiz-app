<script setup>
import { RouterLink, RouterView } from 'vue-router';

</script>

<template>
  <header>
    <div class="wrapper">
      <nav class="navbar">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/start-new-quiz-page">Nouveau quiz</RouterLink>
        <RouterLink to="/admin">Admin</RouterLink>
        <RouterLink to="/scorePage">Score</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style scoped>
nav {
  max-width: 10000px;
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
  color: yellow;
}

nav a {
  color: #3c00ff;
  text-decoration: none;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}
</style>
