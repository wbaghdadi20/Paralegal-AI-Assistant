<template>
  <div class="home-page-get-started1">
    <div class="property-1default8" @click="onProperty1DefaultContainerClick">
      <button class="get-started2" :autoFocus="true">Get Started</button>
    </div>
    <div class="property-1variant24">
      <button class="get-started3" :autoFocus="true">Get Started</button>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "HomePageGetStarted",
    methods: {
      onProperty1DefaultContainerClick() {
        this.$router.push("/");
      },
    },
  });
</script>
<style scoped>
  .get-started2 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: relative;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-darkslategray);
    text-align: center;
    display: inline-block;
  }
  .property-1default8 {
    position: absolute;
    top: 20px;
    left: calc(50% - 105.5px);
    border-radius: var(--br-3xs);
    background-color: var(--color-white);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-lg) var(--padding-42xl);
    cursor: pointer;
  }
  .get-started3 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: relative;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: center;
    display: inline-block;
  }
  .property-1variant24 {
    position: absolute;
    top: 100px;
    left: calc(50% - 105.5px);
    border-radius: var(--br-3xs);
    background-color: var(--color-gray-100);
    border: 1px solid var(--color-white);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-lg) var(--padding-42xl);
  }
  .home-page-get-started1 {
    width: 251px;
    border-radius: var(--br-8xs);
    border: 1px dashed var(--color-blueviolet);
    box-sizing: border-box;
    height: 180px;
    overflow: hidden;
  }
</style>
