<template>
  <div class="bg-light border" id="sidebar-wrapper">
      <div class="list-group list-group-flush">
        <div v-if="userName.staff === false" >
          <a href="#" class="list-group-item list-group-item-action bg-light">Мои крусы</a>
          <router-link to="/profile/departments" class="list-group-item list-group-item-action bg-light">Список доступных курсов</router-link>
        </div>
        <div v-else>
          <router-link to="/profile/createCourse" class="list-group-item list-group-item-action bg-light">Создать курс</router-link>
          <a href="#" class="list-group-item list-group-item-action bg-light">Изменить курсы</a>
          <a href="#" class="list-group-item list-group-item-action bg-light">Управление доступом</a>
        </div>
      </div>
    </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "ContentMenu",

  computed: {
    ...mapGetters(['userName']),
  },
}
</script>

<style scoped>

</style>