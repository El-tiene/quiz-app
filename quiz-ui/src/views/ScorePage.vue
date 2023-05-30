<template>
  <div class="score-page">
    <h1>Page de Scores</h1>
    <p>Votre score : {{ score }}</p>
    <!-- <p>Classement : {{ ranking }}</p>
    <p>Meilleurs scores :</p> -->
    <ul>
      <li v-for="(score, index) in topScores" :key="index">
        {{ score }}
      </li>
    </ul>
    <button class="btn btn-primary" @click="goToHomePage">Retour à la Home page</button>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  data() {
    return {
      ranking: 0,
      topScores: [],
    };
  },
  created() {
    // Appel asynchrone pour récupérer les informations de score
    //const myScore = this.$route.query.score;
    this.getScoreInfo();
  },
  methods: {
    async getScoreInfo() {
      try {
        const response = await quizApiService.getQuizInfo();
        this.score = response.score;
        this.ranking = response.ranking;
        this.topScores = response.topScores;
      } catch (error) {
        console.error(error);
      }
    },
    goToHomePage() {
      this.$router.push('/');
    },
  },
  computed: {
  score() {
    const scoreParam = this.$route.query.score;
    return parseInt(scoreParam) || 0;
  },
},

};
</script>
<style>
.score-page {
  max-width: 600px;
  margin-right: 400px;
  color: yellow;
}

.score-page h1 {
  font-size: 24px;
  margin-bottom: 20px;

}

.score-page p {
  margin-bottom: 10px;
}

.score-page ul {
  list-style-type: none;
  padding: 0;
  margin-bottom: 20px;
}

.score-page li {
  margin-bottom: 10px;
}

.score-page button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.score-page button:hover {
  background-color: #0056b3;
}
</style>