<template>
  <div>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
  </div>
</template>



<script>
import QuestionDisplay from "@/components/QuestionDisplay.vue";
//import participationStorageService from "@/services/participationStorageService";
import quizApiService from "@/services/QuizApiService.js";

export default {
  name:"QuestionsManager",
  components: {
    QuestionDisplay
  },
  data() {
    return {
      currentQuestion: {
            questionTitle:"",
            questionText:"",
            possibleAnswers:[],
            image:""
        },
      userAnswer: [],
      currentQuestionPosition: 1,
      totalNumberOfQuestions: 0,
      score:0
    };
  },
async created() {
    const info = await quizApiService.getQuizInfo();
    if (info.status === 200) {
      this.loadQuestions(this.currentQuestionPosition);
      this.totalNumberOfQuestions = info.data.size;
    }
    else{
      console.error("Erreur récupération info");
    }
        
  },
  methods: {
    async loadQuestions(position) {
        // Appel asynchrone pour récupérer les questions du quiz
        const questionRecup = await quizApiService.getQuestionByPosition(position);
        this.currentQuestion.questionTitle = questionRecup.data.title;
        this.currentQuestion.questionText = questionRecup.data.text;
        this.currentQuestion.possibleAnswers = questionRecup.data.possibleAnswers;
        this.currentQuestion.image = questionRecup.data.image;
    },

    async answerClickedHandler(answerIndex) {
      
      const currentQuestion = this.currentQuestion;
      if((currentQuestion.possibleAnswers[answerIndex])['isCorrect']==true){
        
        this.score++;
        console.log("score=",this.score)
      }

      // Passer à la question suivante
      this.currentQuestionPosition++;

      // Vérifier s'il reste des questions à afficher
      if (this.currentQuestionPosition <= this.totalNumberOfQuestions) {
        // Charger la prochaine question
        await this.loadQuestions(this.currentQuestionPosition);
      } else {
        // Fin du quiz
        this.endQuiz();
      }
    },
    async endQuiz(){
      //this.$router.push('ScorePage'+this.score)
      // manager.vue
      this.$router.push(`/scorePage?score=${this.score}`);
    }
  }
}
</script>

<style>
h1{
  margin-left: -350px;
  color: yellow;
  font-size: 60px;
  font-family: 'Impact', fantasy;
}
</style>

