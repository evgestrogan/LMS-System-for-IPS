<template>
    <v-alert :type="typeMessage">
      {{textMessage}}
    </v-alert>
</template>

<script>
export default {
  name: "AlertComponent",
  props: {
    status: Number,
  },
  data() {
    return {
      typeMessage: '',
      textMessage: '',
    };
  },
  created() {
    if(this.status === 0) {
      this.typeMessage = 'error'
      this.textMessage = 'Ошибка сервера. Попробуйте в другой раз или перезагрузите страницу'
    }
    if(this.status === 401) {
      this.typeMessage = 'error'
      this.textMessage = 'Ошибка авторизации. Проверьте логин или пароль'
    }
    if(this.status === 500) {
      this.typeMessage = 'error'
      this.textMessage = 'Проверьте корректность введенных данных'
    }
  }
}
</script>

<style scoped>

</style>