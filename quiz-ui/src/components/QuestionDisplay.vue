<template>
  <div>
    <h2>{{ question.title }}</h2>
    <p>{{ question.description }}</p>
    <img v-if="question.image" :src="question.image" />
    <ul>
      <li v-for="(answer, index) in question.answers" :key="index" @click="$emit('answer-selected', index)">
        {{ answer }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    question: {
      type: Object
    }
  }
};
</script>
