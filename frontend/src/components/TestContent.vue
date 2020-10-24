<template>
  <v-col class="ma-16" style="min-width: 300px; max-width: 800px">
    <v-alert v-if="test === 'success'" type="success" icon="mdi-shield-check-outline">
      Congratulations!!!
    </v-alert>
    <v-alert v-if="test === 'loose'" type="error" icon="mdi-shield-alert-outline">
      you are loose this test. Try again!
    </v-alert>
    <v-card>
      <v-expansion-panels>
        <v-expansion-panel v-for="question in return_question_list" :key="question.id">
            <v-expansion-panel-header color="blue-grey lighten-5">
              <div>
                <v-row class="text--disabled text-overline text-uppercase justify-center">Вопрос</v-row>
                <v-row class="text-lg-h5 font-weight-light justify-center">{{ question.body }}</v-row>
              </div>
            </v-expansion-panel-header>
            <v-expansion-panel-content class="pr-4">
              <v-list-item-group v-for="answer in question.answer" :key="answer.id" class="row pa-4">
                <v-list-item class="text-lg-body-1 font-weight-light" @click="check_answer(answer.id, question.id)">
                  {{answer.body}}
                </v-list-item>
              </v-list-item-group>
            </v-expansion-panel-content>
          </v-expansion-panel>
      </v-expansion-panels>
    </v-card>
    <v-btn class="mt-2 btn-lg" @click="create_result" outlined>Ответить</v-btn>
  </v-col>
</template>

<script>
import {mapGetters, mapMutations} from "vuex";

export default {
  name: "TestContent",
  data: function () {
    return {
      answers: {},
      result: {},
      test: '',
    };
  },
  methods: {
    create_result(){
      let questionLength = this.return_question_list.length
      for (let question = 0; question < questionLength; question++) {
        this.result[this.return_question_list[question].id] = []
        let answerLength = this.return_question_list[question].answer.length
        for(let answer = 0; answer < answerLength; answer++) {
          if(this.return_question_list[question].answer[answer].isTrue === true) {
            this.result[this.return_question_list[question].id].push(this.return_question_list[question].answer[answer].id)
          }
        }
      }
      if(JSON.stringify(this.result) === JSON.stringify(this.answers)) {
        this.test = 'success'
      }
      else {
        this.test = 'loose'
      }
    },
    check_answer(answer, question){
      try {
        if (this.answers[question].indexOf(answer) !== -1) {
          this.answers[question].splice(this.answers[question].indexOf(answer), 1)
        }
        else {
          this.answers[question].push(answer)
        }
      }
      catch (error) {
        this.answers[question] = []
        this.answers[question].push(answer)
      }
    },
    ...mapMutations(['clear_question_list']),
    createQuestion: function () {
      this.$store.dispatch(
        'get_question_list', {
        data: this.$route.params.id_test
      })
    }
  },
  computed: {
    ...mapGetters(['return_question_list']),
  },
  created() {
    this.clear_question_list()
    this.createQuestion()
  },
}
</script>

<style scoped>

</style>