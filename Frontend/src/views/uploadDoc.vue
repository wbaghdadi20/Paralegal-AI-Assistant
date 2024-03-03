<template>
  <div>
    <input type="file" ref="fileInput" @change="handleFileUpload" accept=".pdf" style="display: none" />
    <button @click="openFileInput">Upload PDF</button>
  </div>
</template>

<script>
export default {
  methods: {
    openFileInput() {
      this.$refs.fileInput.click();
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      // Handle the uploaded file here
      console.log(file);
    },
  },
};
</script>
