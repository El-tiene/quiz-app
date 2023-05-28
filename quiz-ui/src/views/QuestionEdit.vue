<template>
  <div class="question-edit">
    <h1>Édition de la question</h1>
    <label for="position-input">Position :</label>
    <input id="position-input" type="text" v-model="question.position" />
    <label for="title-input">Titre :</label>
    <input id="title-input" type="text" v-model="question.title" />
    <label for="description-input">Intitulé :</label>
    <textarea id="description-input" v-model="question.description"></textarea>
    <label for="image-upload">Image :</label>
    <input id="image-upload" type="file" @change="uploadImage" />
    <div class="image-preview" v-if="question.image">
      <img :src="question.image" alt="Image preview" />
    </div>
    <h2>Réponses possibles :</h2>
    <div v-for="(option, index) in question.options" :key="index">
      <input type="text" v-model="option.text" />
      <input type="checkbox" v-model="option.correct" />
    </div>
    <button @click="saveQuestion">Sauvegarder</button>
    <button @click="cancelEdit">Annuler</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      question: {
        position: 1,
        title: "Titre de la question",
        description: "Intitulé de la question",
        image: null,
        options: [
          { text: "Option 1", correct: false },
          { text: "Option 2", correct: false },
          { text: "Option 3", correct: false },
          { text: "Option 4", correct: false },
        ],
      },
    };
  },
  methods: {
    uploadImage(event) {
    },
    saveQuestion() {

      this.$router.push('/questionEdit');
    },
    cancelEdit() {
      this.$router.push('/questionEdit');
    },
  },
};
</script>

<style scoped>
.image-preview img {
  max-width: 200px;
  max-height: 200px;
  margin-bottom: 10px;
}
</style>
