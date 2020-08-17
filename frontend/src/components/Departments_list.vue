<template>
  <div>
    <div v-for="department in return_departments_list" :key="department.id">
      <div class="jumbotron jumbotron-fluid">
        <div class="container">
          <h1 class="display-4">{{ department.subject.department.name_department }}</h1>
          <p class="lead">This is a modified jumbotron that occupies the entire horizontal space of its parent.</p>
        </div>
      </div>
    </div>
<div class="btn-group">
  <button type="button" class="btn btn-danger">Action</button>
  <button type="button" class="btn btn-danger dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    <span class="sr-only">Toggle Dropdown</span>
  </button>
  <div class="dropdown-menu">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>
    <div class="dropdown-divider"></div>
    <a class="dropdown-item" href="#">Separated link</a>
  </div>
</div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "Departments_list",
  computed: {
      ...mapGetters(['return_departments_list']),
  },
}
</script>

<style scoped>

</style>