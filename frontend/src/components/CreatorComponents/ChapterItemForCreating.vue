<template>
  <v-card class="mb-6 pa-6 justify-center">
    <alert-component v-if="error !== null" :status="error"></alert-component>
    <v-row>
      <v-col cols="2" class="mr-0 pr-0">
        <v-card-title><v-text-field type="number" v-model="chapter.number" label="№ Главы"></v-text-field></v-card-title>
      </v-col>
      <v-col cols="10" class="ml-0 pl-0">
        <v-card-title><v-text-field type="text" v-model="chapter.name" label="Введите название главы"></v-text-field></v-card-title>
      </v-col>
    </v-row>

    <v-card class="col text-decoration-none text-lg-body-1 font-weight-light mb-2" v-for="(subchapter, id_subchapter) in chapter.subchapter" :key="id_subchapter" :color="color[id_subchapter]">
      <v-row>
        <v-col cols="2">
          <v-text-field type="number" v-model="subchapter.number" label="№ Подглавы"></v-text-field>
        </v-col>
        <v-col cols="10">
          <v-text-field type="text" v-model="subchapter.name" label="Введите название подглавы"></v-text-field>
        </v-col>
      </v-row>
      <v-file-input v-if="!subchapter.body" v-model="subchapter.body" label="Select Image File..."></v-file-input>
      <v-text-field v-if="subchapter.body" v-model="subchapter.body" label="Select Image File..." @click="edit_file(id_subchapter)"></v-text-field>
    </v-card>
    <v-card-actions class="justify-end align-end">
      <v-btn class="ma-2" outlined color="indigo" @click="create_subchapter">Добавить подглаву</v-btn>
    </v-card-actions>
    <test-creator v-if="edit_test" :test="test_list"></test-creator>
    <v-row v-if="!edit_test" class="justify-center">
      <v-btn v-if="chapter.test" class="ma-2" outlined color="indigo" @click="edit_test = !edit_test">Изментить имеющийся тест</v-btn>
      <v-btn class="ma-2" v-else outlined color="indigo" @click="edit_test = !edit_test">Добавить итоговый тест для главы</v-btn>
    </v-row>
    <v-row class="justify-center">
      <v-btn class="ma-2" outlined color="indigo" @click="save_chapters">Сохранить главу</v-btn>
    </v-row>
  </v-card>
</template>

<script>
import testCreator from './TestCreator';
import alertComponent from "@/components/AlertComponent";
const axios = require('axios').default;

export default {
  name: "ChapterItemForCreating",
  components: {
    testCreator,
    alertComponent,
  },
  props: {
    chapter: Object,
  },
  data: function () {
    return {
      error: null,
      file: null,
      edit_test: false,
      test_list: {
        'id': null,
        'title': '',
        'question': [],
      },
      color: [
          'red lighten-5',
          'pink lighten-5',
          'purple lighten-5',
          'deep-purple lighten-5',
          'indigo lighten-5',
          'blue lighten-5',
          'light-blue lighten-5',
          'cyan lighten-5',
          'teal lighten-5',
          'green lighten-5',
          'yellow lighten-5',
      ]
    };
  },
  created() {
    // this.edit_test = !this.edit_test
    if (this.chapter.test) {
      this.$store.dispatch('test', { id: this.chapter.test.id})
      .then(resp => {
        this.test_list = resp.data
      })
      .catch(err => {
        this.error = err.request.status
      })
    }
  },
  methods: {
    save_chapters() {
      this.$store.dispatch('test_creator_editor', this.test_list)
      .then(resp => {
        this.chapter.test_id = resp.data.test_id
        this.$store.dispatch('chapter_creator_editor', this.chapter)
        .then(response => {
          for (const subchapter of this.chapter.subchapter) {
            subchapter.chapter_id = response.data.chapter_id
            this.$store.dispatch('subchapter_creator_editor', subchapter)
            .then((respo => {
              subchapter.id = respo.data.subchapter_id
            }))
            .catch(err => {
              this.error = err.request.status
            })
          }
        })
        .catch(err => {
          this.error = err.request.status
        })
      })
      .catch(err => {
        this.error = err.request.status
      })
    },
    create_subchapter() {
      this.chapter.subchapter.push({ "id": '', "number": '', "name": "", "body": null })
    },
    edit_file(id){
      this.chapter.subchapter[id].body = null
    }
  },
}
</script>

<style scoped>

</style>