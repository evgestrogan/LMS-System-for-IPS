<template>
  <div class="mb-6 mx-3">
    <v-card>
      <v-card-title>
        <v-text-field type="text" label="Введите название теста"  v-model="test.title_test"></v-text-field>
      </v-card-title>
      <question-content v-for="question in test.test" :question="question" :key="question.id"></question-content>
      <v-card-actions class="justify-center">
        <v-btn class="ma-2" fab dark large color="pink" @click="create_new_question"><v-icon dark>mdi-plus</v-icon></v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import questionContent from './QuestionContent'
import {mapGetters} from "vuex";

export default {
  name: "TestCreator",
  components: {
    questionContent,
  },
  props: {
    test: Object,
    test_title: String,
  },
  data: function () {
    return {
    };
  },
  methods: {
    create_new_question(){
      this.test.test.push({'body': '', 'answer': []})
    },
  }
}
</script>

<style scoped>

</style>