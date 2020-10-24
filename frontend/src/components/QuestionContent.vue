<template>
  <div>
    <v-card-title>
      <v-text-field color="red" label="Введите вопрос" v-model="question.body"></v-text-field>
    </v-card-title>
    <v-card-subtitle v-for="(answer, id_answer)  in question.answer" :key="id_answer" class="v-list-item">
      <v-text-field color="indigo" label="Введите ответ" v-model="answer.body"></v-text-field>
      <v-checkbox v-model="answer.isTrue"></v-checkbox>
    </v-card-subtitle>
    <v-card-actions class="justify-end align-end">
      <v-btn class="ma-2" fab dark large color="indigo" @click="create_answer"><v-icon dark>mdi-plus</v-icon></v-btn>
    </v-card-actions>
  </div>
</template>

<script>
export default {
  name: "QuestionContent",
  props: {
    question: Object,
  },
  methods: {
    create_answer() {
      this.question.answer.push({'body': '', 'isTrue': false})
    },
  },
}
</script>

<style scoped>

</style>