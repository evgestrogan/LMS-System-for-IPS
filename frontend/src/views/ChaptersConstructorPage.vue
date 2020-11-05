<template>
  <v-col class="ma-16" style="min-width: 300px; max-width: 800px">
    <alert-component v-if="error" :status="error"></alert-component>
    <chapter-item-for-creating v-for="(chapter, id_chapter) in course.chapter" :chapter='chapter' :key="id_chapter"></chapter-item-for-creating>
    <v-row class="justify-center">
      <v-btn class="ma-2" outlined color="indigo" @click="create_chapter">Добавить главу</v-btn>
    </v-row>
  </v-col>
</template>

<script>
import chapterItemForCreating from "@/components/CreatorComponents/ChapterItemForCreating";
import alertComponent from "@/components/AlertComponent";
import {mapGetters, mapMutations} from "vuex";
import router from "@/router";

export default {
  name: "ChaptersConstructorPage",
  components: {
    chapterItemForCreating,
    alertComponent,
  },
  data() {
    return {
      error: null,
    };
  },
  methods: {
    ...mapMutations(['clear_course']),
    create_chapter() {
      this.course.chapter.push({ "id_course": this.course.id, "id": '', "number": '', "name": "", "test": null, "subchapter": [] })
    }
  },
  computed: {
    ...mapGetters(['course']),
  },
  created() {
    this.$store.dispatch('course', { id: this.$route.params.id_course })
    .catch(err => {
      router.push({name: 'Profile', params: {id_user: this.user_id}})
    })
  },
}
</script>

<style scoped>

</style>