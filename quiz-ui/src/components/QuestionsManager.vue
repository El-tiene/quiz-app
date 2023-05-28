<template>
  <div>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
  </div>
</template>

<script>
import QuestionDisplay from "@/components/QuestionDisplay.vue";
import participationStorageService from "@/services/participationStorageService";

export default {
  components: {
    QuestionDisplay
  },
  data() {
    return {
      questions: [],
      currentQuestionPosition: 1,
      totalNumberOfQuestions: 0
    };
  },
  created() {
    this.loadQuestions();
  },
  methods: {
    async loadQuestions() {
      try {
        // Appel asynchrone pour récupérer les questions du quiz
        const response = await quizApiService.getQuestions();
        this.questions = response.data;
        this.totalNumberOfQuestions = this.questions.length;
      } catch (error) {
        console.error(error);
      }
    },

    async answerClickedHandler(answerIndex) {
      // Récupérer la question actuelle
      const currentQuestion = this.questions[this.currentQuestionPosition - 1];

      // Vérifier si la réponse sélectionnée est correcte
      const isCorrectAnswer = currentQuestion.correctAnswerIndex === answerIndex;

      // Enregistrer la réponse de l'utilisateur dans le service de stockage de participation
      participationStorageService.saveAnswer({
        question: currentQuestion,
        selectedAnswerIndex: answerIndex,
        isCorrect: isCorrectAnswer
      });

      // Passer à la question suivante
      this.currentQuestionPosition++;

      // Vérifier s'il reste des questions à afficher
      if (this.currentQuestionPosition <= this.totalNumberOfQuestions) {
        // Charger la prochaine question
        await this.loadQuestionByPosition(this.currentQuestionPosition);
      } else {
        // Fin du quiz
        this.endQuiz();
      }
    },
  }
}
</script>
