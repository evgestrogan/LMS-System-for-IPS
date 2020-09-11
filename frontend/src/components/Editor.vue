<template>
  <div>
    <ckeditor ma-0 pa-0 fill-height :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
  </div>
</template>

<script>
import ClassicEditor from '@ckeditor/ckeditor5-build-classic/build/ckeditor';

export default {

  name: "Editor",

  data() {
    return {
        editor: ClassicEditor,
        editorData: '',
        editorConfig: {
             language: 'ru'
        }
    };
  },
}
</script>

<style scoped>

</style>