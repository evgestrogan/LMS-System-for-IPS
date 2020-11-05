<template>
  <v-row justify="center" class="ma-16">
    <v-subheader>Курс: {{ course.name }}</v-subheader>
    <v-expansion-panels accordion>
      <v-expansion-panel v-for="(chapter, count) in course.chapter" :key="chapter.id">
        <v-expansion-panel-header>

          <v-row align="center" class="spacer" no-gutters>

            <v-col cols="1">
<!--              <v-avatar size="36px">-->
                <v-icon color="teal" >mdi-filter-variant</v-icon>
<!--              </v-avatar>-->
            </v-col>

            <v-col cols="7">
              <strong>Глава {{chapter.number}} &mdash; {{chapter.name}}</strong>
              <span class="grey--text">
                &mdash;Количество подглав:
                &nbsp;({{ chapter.subchapter.length }})
              </span>
            </v-col>

            <v-col cols="2" class="text-no-wrap">

              <router-link :to="{ name: 'TestPage', params: { id_test: chapter.test.id }}" class="text-decoration-none">
                <v-chip class="ma-2" color="red" text-color="white">
                  <v-avatar left>
                    <v-icon>mdi-close-circle</v-icon>
                  </v-avatar>
                  {{chapter.test.title}}
                </v-chip>
<!--                <v-chip class="ma-2" color="teal" text-color="white">-->
<!--                  <v-avatar left>-->
<!--                    <v-icon>mdi-checkbox-marked-circle</v-icon>-->
<!--                  </v-avatar>-->
<!--                  {{chapter.test.title}}-->
<!--                </v-chip>-->
              </router-link>
            </v-col>

            <v-col cols="2" class="grey--text text-truncate hidden-sm-and-down">
              &mdash;
              Курс: {{ course.name }}
            </v-col>

          </v-row>

        </v-expansion-panel-header>
        <v-expansion-panel-content>
        <v-col cols="12" v-for="subchapter in chapter.subchapter" :key="subchapter.id">
          <v-card color="red lighten-1" dark>
            <v-card-title class="headline">{{subchapter.name}}</v-card-title>

            <v-card-subtitle>{{subchapter.number}} Подглава</v-card-subtitle>
            <router-link :to="{ name: 'SubchapterPage', params: { id_department: department_id, id_course: course_id, id_subchapter: subchapter.id }}" class="text-decoration-none text-lg-body-1 font-weight-light">
              <v-card-actions>
                <v-btn text>Изучить</v-btn>
              </v-card-actions>
            </router-link>
          </v-card>
        </v-col>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-row>
<!--    <v-col class="ma-16">-->
<!--        <v-card class="row mb-2" v-for="(chapter, count) in course.chapter" :key="chapter.id">-->
<!--            <v-col cols="2">-->
<!--                <v-card-subtitle>Курс: {{course.name}}</v-card-subtitle>-->
<!--                <v-list-group color="gray">-->
<!--                    <template v-slot:activator>-->
<!--                      <v-card-text>Глава {{chapter.number}}: {{chapter.name}}</v-card-text>-->
<!--                    </template>-->
<!--                  <v-col>-->
<!--                    <router-link v-for="subchapter in chapter.subchapter" :key="subchapter.id" :to="{ name: 'SubchapterPage', params: { id_department: department_id, id_course: course_id, id_subchapter: subchapter.id }}"  class="text-decoration-none text-lg-body-1 font-weight-light">-->
<!--                      {{subchapter.name}}-->
<!--                    </router-link>-->
<!--                    </v-col>-->
<!--                </v-list-group>-->
<!--            </v-col>-->
<!--            <v-col>-->
<!--                <v-card-subtitle class="text-end">Результирующий тест: {{chapter.test.title}}</v-card-subtitle>-->
<!--                <router-link :to="{ name: 'TestPage', params: { id_test: chapter.test.id }}" class="text-decoration-none text-lg-body-1 font-weight-light">-->
<!--                  <v-card-text class="text-end">Пройти итоговый тест</v-card-text>-->
<!--                </router-link>-->
<!--            </v-col>-->
<!--        </v-card>-->
<!--    </v-col>-->
<!--  <v-col  class="mx-16">-->
<!--    <div v-for="(chapter, count) in course.chapter" :key="chapter.id">-->
<!--      <v-row align="center">-->
<!--        <v-item-group v-model="window[count]" class="shrink mr-6" mandatory tag="v-flex">-->
<!--          <v-item v-for="subchapter in chapter.subchapter" :key="subchapter.id" v-slot:default="{ active, toggle }">-->
<!--            <div>-->
<!--              <v-btn :input-value="active" icon @click="toggle">-->
<!--                <v-icon>mdi-record</v-icon>-->
<!--              </v-btn>-->
<!--            </div>-->
<!--          </v-item>-->
<!--        </v-item-group>-->

<!--        <v-col>-->
<!--          <v-window v-model="window[count]" class="elevation-1" vertical>-->
<!--            <v-window-item v-for="subchapter in chapter.subchapter" :key="subchapter.id">-->
<!--              <v-card flat>-->
<!--                <v-card-text>-->
<!--                  <v-row class="mb-4" align="center">-->
<!--                    <v-card-title class="title text-uppercase justify-center">-->
<!--                      <router-link :to="{ name: 'SubchapterPage', params: { id_department: department_id, id_course: course_id, id_subchapter: subchapter.id }}" class="text-decoration-none text-lg-body-1 font-weight-light">-->
<!--                        {{ subchapter.number }} {{subchapter.name}}-->
<!--                      </router-link>-->
<!--                    </v-card-title>-->
<!--                    <v-spacer></v-spacer>-->
<!--                    <router-link :to="{ name: 'TestPage', params: { id_test: chapter.test.id }}" class="text-decoration-none text-lg-body-1 font-weight-light">-->
<!--                      <v-card-actions class="text-lg-body-1 font-weight-light">-->
<!--                        <v-icon>mdi-account</v-icon>-->
<!--                      </v-card-actions>-->
<!--                    </router-link>-->
<!--                  </v-row>-->

<!--                  <iframe style="width: 100%; height: 100%; min-height: 750px" :src="'http://127.0.0.1:8000' + subchapter.body"></iframe>-->
<!--                </v-card-text>-->
<!--              </v-card>-->
<!--            </v-window-item>-->
<!--          </v-window>-->
<!--        </v-col>-->
<!--      </v-row>-->
<!--    </div>-->
<!--  </v-col>-->
</template>

<script>
import {mapGetters, mapMutations} from "vuex";
import router from "@/router";

export default {
  name: "CoursePage",
  data() {
    return {
      e6: [],
      course: [],
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
      ],
      department_id: this.$route.params.id_department,
      course_id: this.$route.params.id_course,
    }
  },
  computed: {
    // ...mapGetters(['course']),
  },
  methods: {
    ...mapMutations(['clear_course']),
  },
  created() {
    this.clear_course()
    this.$store.dispatch('course', { id: this.course_id })
    .then(resp => {
      this.course = resp.data
      for (const course of resp.data.chapter) {
        this.e6.push(0)
      }
    })
    .catch(err => {
      router.push({name: 'Profile', params: {id_user: this.user_id}})
    })
  },
}
</script>

<style scoped>

</style>