<template>
  <v-col class="ma-16" style="min-width: 300px; max-width: 800px">
    <v-select @change="get_subject" v-model="department_selected"  :items="department" label="Выберите кафедру" solo item-text="name" item-value="value"></v-select>
    <v-select :items='subject' v-model="subject_selected" label="Выберите предмет" solo item-text="name" item-value="value"></v-select>
    <v-text-field v-model="name_course" label="Введите название курса"></v-text-field>
    <v-text-field v-model="title_test" label="Введите название итогового теста для курса"></v-text-field>
    <v-card class="mb-6" v-for="(i, count_question) in question">
      <v-card-title>
        <v-text-field color="red"  v-model=i[0] label="Введите вопрос"></v-text-field>
      </v-card-title>
      <v-card-subtitle class="v-list-item" v-for="j in i[1]">
        <v-text-field color="indigo" v-model=j[0] label="Введите ответ"></v-text-field>
        <v-checkbox v-model=j[1]></v-checkbox>
      </v-card-subtitle>
      <v-card-actions class="justify-end align-end">
        <v-btn @click="addAnswer(count_question)" class="ma-2" fab dark large color="indigo"><v-icon dark>mdi-plus</v-icon></v-btn>
      </v-card-actions>
    </v-card>
    <v-row class="justify-center">
      <v-btn class="ma-2" @click="addQuestion()" fab dark large color="pink"><v-icon dark>mdi-plus</v-icon></v-btn>
    </v-row>
    <v-row class="justify-center">
      <v-btn class="ma-2" @click="create_course()" outlined color="indigo">Создать курс</v-btn>
    </v-row>
  </v-col>
</template>

<script>
import {mapGetters} from "vuex";
import router from "@/router";

export default {
  name: "return_departments_list",
  computed: {
    ...mapGetters(['return_departments_list', 'return_subjects_list', 'client']),
  },
  data: function () {
    return {
      department: [],
      department_selected: {},
      subject: [],
      subject_selected: {},
      name_course: '',
      title_test: '',
      question: [],
    };
  },
  methods: {
    create_course() {
      this.$store.dispatch('create_course', {'department_selected': this.department_selected, 'subject_selected': this.subject_selected, 'name_course': this.name_course, 'title_test': this.title_test, 'user': this.client.id, 'question': this.question})
      .then(resp => {
        router.push({ name: 'courseContent', params: {'id_department': this.department_selected, 'id_course': resp.data.id }})
      })
      .catch()
    },
    addQuestion(){
      this.question.push(['', []])
    },
    addAnswer(number_question){
      this.question[number_question][1].push(["", false])
    },
    get_subject() {
      this.subject = []
      this.$store.dispatch('get_subjects_list', { data: this.department_selected })
      .then(resp => {
        let objectLength = this.return_subjects_list.length
        for (let subject = 0; subject < objectLength; subject++) {
          this.subject.push({
            'name': this.return_subjects_list[subject].name_subject,
            'value': this.return_subjects_list[subject].id
          })
        }
      })
      .catch()
    },
  },
  created() {
    this.$store.dispatch('get_departmets_list')
      .then(resp => {
        let objectLength = this.return_departments_list.length
        for (let depart = 0; depart < objectLength; depart++) {
          this.department.push({
            'name': this.return_departments_list[depart].name_department,
            'value': this.return_departments_list[depart].id
          })
        }
      })
      .catch()
  },
}
</script>

<style scoped>

</style>