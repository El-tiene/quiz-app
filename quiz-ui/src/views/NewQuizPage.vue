<template>
  <div class="NewQuiz-page">

    <form class="player-form">
      <div class="mb-3">
        <label for="player-name" class="form-label">Nom du joueur :</label>
        <input type="text" class="form-control" id="player-name" v-model="username" />
        <p>{{ username }}</p>
      </div>
      <router-link to="/QuestionsManager">
        <button type="button" class="btn btn-primary" @click="launchNewQuiz">C'est parti !!!</button>
      </router-link>
    </form>
  </div>
</template>

<script>
//import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: ""
    };
  },
  methods: {
    launchNewQuiz() {
      console.log("Launch new quiz with", this.username);
      if (this.username !== "") {
        participationStorageService.savePlayerName(this.username);
        this.$router.push("/questions");
      } else {
        this.showErrorBubble = true; // Afficher la bulle d'erreur
      }
    },
  },
};
</script>
<style>
.NewQuiz-page {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  color: yellow;
}

.NewQuiz-page .player-form {
  margin-top: 20px;
}

.NewQuiz-page .form-label {
  font-weight: bold;
}

.NewQuiz-page .form-control {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  margin-bottom: 10px;
}

.NewQuiz-page button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.NewQuiz-page button:hover {
  background-color: #0056b3;
}
</style>