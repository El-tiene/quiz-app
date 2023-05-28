<template>
  <div class="home-page">
    <h1 class="title">Bienvenue sur le Quiz de MMA</h1>
    <div class="score-item" v-for="score in sortedScores" :key="score.id">
      Score: {{ score }}
    </div>

    <form class="player-form">
      <div class="start-quiz">
        <router-link to="/start-new-quiz-page">
          <button type="button" class="btn btn-primary" @click="launchNewQuiz">Démarrer le quiz !</button>
        </router-link>
      </div>
    </form>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
      username: ""
    };
  },

  async created() {
    console.log("Composant Home page 'created'");
    try {
      const response = await quizApiService.getQuizInfo(); // Appel asynchrone pour récupérer les scores
      this.registeredScores = response.data; // Stockage de la valeur adéquate dans registeredScores
    } catch (error) {
      console.error(error);
    }
  },

  computed: {
    sortedScores() {
      return this.registeredScores.sort((a, b) => b - a); // Tri des scores dans l'ordre décroissant
    }
  },

  methods: {
    launchNewQuiz() {
      if (this.username) {
        participationStorageService.savePlayerName(this.username); // Stockage du nom du joueur
        this.$router.push('/questions'); // Redirection vers la première question du quiz
      }
      console.log("Launch new quiz with", this.username);
    },

    startQuiz() {
      if (this.username !== "") {
        console.log("Démarrer le quiz avec le joueur : ", this.username);
      } else {
        console.log("Veuillez saisir un nom de joueur avant de démarrer le quiz.");
      }
    }
  }
};
</script>
<style>
.home-page .title {
  margin-left: -350px;
  color: yellow;
  font-size: 60px;
}

.home-page .score-item {
  padding: 50px;
  margin-bottom: 10px;

}

.home-page .player-form {
  margin-top: 20px;
}

.home-page .start-quiz button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.home-page .start-quiz button:hover {
  background-color: #0056b3;
}
</style> 
