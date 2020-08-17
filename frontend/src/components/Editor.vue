<template>
  <div>
    <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
    <p>Using v-html directive: <span v-html="this.editorData"></span></p>
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