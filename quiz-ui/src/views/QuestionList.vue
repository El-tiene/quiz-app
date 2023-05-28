<template>
  <div class="question-list">
    <h1>Liste des questions</h1>
    <router-link to="/questionEdit" class="create-question-btn">Créer une question</router-link>
    <router-link v-for="question in questions" :to="'/questionEdit/' + question.id" class="question-item"
      :key="question.id">
      {{ question.title }}
    </router-link>
    <router-link to="/" class="logout-btn">Déconnexion</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      questions: [
        { id: 1, title: 'Question 1' },
        { id: 2, title: 'Question 2' },
        { id: 3, title: 'Question 3' },
      ],
    };
  },
};
</script>


<style scoped>
.question-item {
  display: block;
  margin-bottom: 10px;
}
</style>
