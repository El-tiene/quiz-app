<template>
  <div>
    <!-- <h2>{{ question.questionTitle }}</h2> -->
    
    <img v-if="question.image" :src="question.image" class="question-image" />
    <p>{{ question.questionText }}</p>
    <ul>
      <li v-for="(answer, index) in question.possibleAnswers" :key="index" @click="$emit('answer-selected', index)">
        {{ answer.text }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'QuestionDisplay',
  emits: ["answer-selected"],
  props: {
    question: {
      type: Object
    }
  },
  data() {
      return {
        selectedAnswerId: null
      };
    },
    methods: {
      selectAnswer(index) {
        const selectedAnswerId = index+1;
        this.$emit('answer-selected', selectedAnswerId);
      }
    }
};
</script>

<style>
p{
  margin-left: -350px;
  color: yellow;
  font-size: 40px;
  font-family: 'Impact', fantasy;
}
ul{
  margin-left: -350px;
  color: yellow;
  font-size: 25px;
  font-family: 'Impact', fantasy;
}
.question-image {
  width: 400px;
  height: auto;
  margin-right: 20px;
}
</style>