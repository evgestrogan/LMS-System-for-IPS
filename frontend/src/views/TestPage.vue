<template>
  <v-col class="ma-16" style="min-width: 300px; max-width: 800px">
    <v-alert v-if="test_result === true" type="success" icon="mdi-shield-check-outline">
      Congratulations!!!
    </v-alert>
    <v-alert v-if="test_result === false" type="error" icon="mdi-shield-alert-outline">
      you are loose this test. Try again!
    </v-alert>
    <v-card>
      <v-expansion-panels>
        <v-expansion-panel v-for="question in test.question" :key="question.id">
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
import router from "@/router";

export default {
  name: "TestPage",
  data: function () {
    return {
      test: {},
      answers: {},
      result: {},
      test_result: null,
    };
  },
  methods: {
    create_result(){
      if(JSON.stringify(this.result) === JSON.stringify(this.answers)) {
        this.test_result = true
      }
      else {
        this.test_result = false
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
  },
  created() {
    this.$store.dispatch('test', { id: this.$route.params.id_test })
    .then(resp => {
      this.test = resp.data
      for (const question of this.test.question) {
        this.result[question.id] = []
        this.answers[question.id] = []
        for (const answer of question.answer) {
          if (answer.choice === true) {
            this.result[question.id].push(answer.id)
          }
        }
      }
    })
    .catch(err => {router.push({name: 'Profile', params: {id_user: this.user_id}})})
  },
}
</script>

<style scoped>

</style>