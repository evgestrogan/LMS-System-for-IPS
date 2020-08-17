<template>
  <div class="about">
    <div class="row">
      <div class="col-3">
        <ContentMenu/>
      </div>
      <div class="col-9">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
  import ContentMenu from '../components/ContentMenu'
  import { mapGetters } from 'vuex';

  export default {
    name: "Profile",
    components: {ContentMenu},

    computed: {
      ...mapGetters(['userName']),
    },
  }
</script>