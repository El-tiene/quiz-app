<template>
  <div class="question-page">
    <h1>Question {{ questionNumber }} :</h1>
    <p>{{ question }}</p>
    <ul>
      <li v-for="(option, index) in options" :key="index">
        <input type="radio" :id="'option-' + index" :value="index" v-model="selectedOption" />
        <label :for="'option-' + index">{{ option }}</label>
      </li>
    </ul>
    <button type="button" class="btn btn-primary" @click="nextQuestion">Question suivante</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      questionNumber: 1,
      question: "Quelle est la capitale de la France ?",
      options: ["Paris", "Londres", "Madrid", "Rome"],
      selectedOption: null,
    };
  },
  methods: {
    nextQuestion() {
      if (this.selectedOption !== null) {
        console.log("Question", this.questionNumber, "Réponse sélectionnée :", this.options[this.selectedOption]);
        this.questionNumber++;
        this.question = "Nouvelle question...";
        this.options = ["Option 1", "Option 2", "Option 3", "Option 4"];
        this.selectedOption = null;
      }
    },
  },
};
</script>

<style>
.question-page {
  max-width: 60px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

ul {
  list-style-type: none;
  padding: 0;
  margin-bottom: 20px;
}

li {
  margin-bottom: 10px;
}

label {
  margin-left: 5px;
}

.btn-primary {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>
