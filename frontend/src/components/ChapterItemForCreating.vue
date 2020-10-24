<template>
  <div class="mb-6 pa-6 justify-center">
    <v-card>
      <v-card-text class="col">
        <v-text-field type="text" v-model="chapter.name_chapter" label="Введите название главы"></v-text-field>
        <div v-for="(subchapter, id_subchapter) in chapter.subchapters" :key="id_subchapter" class="text-decoration-none text-lg-body-1 font-weight-light">
          {{subchapter}}
          <v-text-field type="text" v-model="subchapter.name_subchapter" label="Введите название подглавы"></v-text-field>
            <v-file-input v-model="file" label="Select Image File..."></v-file-input>
          <v-row class="justify-center">
            <v-btn class="ma-2" outlined color="indigo" @click="save_file(id_subchapter)">Сохранить</v-btn>
          </v-row>
        </div>
      </v-card-text>
      <v-card-actions class="justify-end align-end">
          <v-btn class="ma-2" outlined color="indigo" @click="create_subchapter(id_chapter)">Добавить подглаву</v-btn>
      </v-card-actions>
      <test-creator v-if="edit_test" :test="test_list" :test_title="chapter.test.title"></test-creator>
      <v-row v-if="!edit_test" class="justify-center">
        <v-btn v-if="chapter.test" class="ma-2" outlined color="indigo" @click="edit_test = !edit_test">Изментить имеющийся тест</v-btn>
        <v-btn class="ma-2" v-else outlined color="indigo" @click="create_test">Добавить итоговый тест для главы</v-btn>
      </v-row>
      <v-row class="justify-center">
        <v-btn class="ma-2" outlined color="indigo" @click="save_chapters">Сохранить</v-btn>
      </v-row>
    </v-card>
  </div>
</template>

<script>
import testCreator from './TestCreator';
import {mapMutations} from "vuex";
const axios = require('axios').default;

export default {
  name: "ChapterItemForCreating",
  components: {
    testCreator,
  },
  props: {
    chapter: Object,
    id_chapter: Number,
    id_test: Number,
  },
  data: function () {
    return {
      file: null,
      edit_test: false,
      test_list: {
        'title_test': '',
        'test': [],
        'id': null,
      },
    };
  },
  methods: {
    ...mapMutations(['create_subchapter', 'create_test_for_chapter']),
    create_test_list(test_list) {
      for (const question of test_list) {
        this.test_list.id = question.test.id
        this.test_list.test.push({'body': question.body, 'answer': question.answer})
      }
    },
    create_test(){
      this.edit_test = !this.edit_test
      this.create_test_for_chapter(this.id_chapter)
      this.test_list.title_test = this.chapter.test.title
      this.test_list.test.push({"body": "", 'answer': []})
    },
    save_chapters() {
      this.chapter.test = this.test_list
      this.chapter['id_course'] = this.$route.params.id_course
      this.$store.dispatch('create_or_edit_chapter', this.chapter)
    },
    save_file(id){
      var formData = new FormData();
      formData.append('username', 'Chris');
      this.$store.dispatch('save_file', {'file': this.file},)
    //   axios({url: 'http://127.0.0.1:8000/api/subchapters/',
    //                 data: {
    //     'name_subchapter': '1',
    //                   'body': '1',
    //                 'chapter': '1',
    //                 'test': '1'},
    //                 method: 'POST',
    //             })
    //   .then(response => console.log(response))
    }
  },
  created() {
    if (this.chapter.test){
      let data = this.chapter.test.id
      this.test_list.title_test = this.chapter.test.title
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/question',
        headers: { data }
      })
      .then(response => this.create_test_list(response.data))
    }
  }
}
</script>

<style scoped>

</style>