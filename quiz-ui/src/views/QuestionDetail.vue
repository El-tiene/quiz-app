<template>
  <div class="question-detail">
    <h1>Question {{ questionNumber }}</h1>
    <h2>{{ question.title }}</h2>
    <p>{{ question.description }}</p>
    <ul>
      <li v-for="(answer, index) in question.answers" :key="index">
        <input type="radio" :id="'answer-' + index" :value="index" v-model="selectedAnswer" />
        <label :for="'answer-' + index">{{ answer.text }}</label>
      </li>
    </ul>
    <button type="button" @click="editQuestion">Éditer</button>
    <button type="button" @click="deleteQuestion">Supprimer</button>
    <router-link to="/questionList">Retour à la liste des questions</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      questionNumber: 1,
      question: {
        id: 1,
        title: 'Question 1',
        description: 'Description de la question 1',
        answers: [
          { text: 'Réponse 1', isCorrect: true },
          { text: 'Réponse 2', isCorrect: false },
          { text: 'Réponse 3', isCorrect: false },
          { text: 'Réponse 4', isCorrect: false },
        ],
      },
      selectedAnswer: null,
    };
  },
  methods: {
    editQuestion() {
      // Rediriger vers la page d'édition de la question en utilisant le router
      this.$router.push('/questionPage/' + this.question.id);
    },
    deleteQuestion() {
      // Supprimer la question (implémentation à ajouter)
      // Rediriger vers la liste des questions après la suppression
      this.$router.push('/questionList');
    },
  },
  created() {
    // Récupérer les données de la question à partir de la page QuestionPage
    this.questionNumber = this.$route.params.questionNumber;
    this.question = {
      id: this.$route.params.questionId,
      title: "Quelle est la capitale de la France ?",
      description: "Description de la question",
      answers: [
        { text: "Paris", isCorrect: true },
        { text: "Londres", isCorrect: false },
        { text: "Madrid", isCorrect: false },
        { text: "Rome", isCorrect: false },
      ],
    };
  },
};
</script>
