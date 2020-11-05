<template>
    <v-card class="mb-6 pa-6">
      <v-card-title>
        <v-text-field type="text" label="Введите название теста"  v-model="test.title"></v-text-field>
      </v-card-title>
      <question-content v-for="(question, id_question) in test.question" :question="question" :key="id_question"></question-content>
      <v-card-actions class="justify-center">
        <v-btn class="ma-2" fab dark large color="pink" @click="create_new_question"><v-icon dark>mdi-plus</v-icon></v-btn>
      </v-card-actions>
    </v-card>
</template>

<script>
import questionContent from './QuestionContent'

export default {
  name: "TestCreator",
  components: {
    questionContent,
  },
  props: {
    test: Object,
  },
  methods: {
    create_new_question(){
      this.test.question.push({'id': '', 'body': '', 'answer': []})
    },
  }
}
</script>

<style scoped>

</style>