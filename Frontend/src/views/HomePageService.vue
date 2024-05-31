<template>
  <div class="home-page-service4">
    <div class="property-1default10">
      <button class="service2" :autoFocus="true">Service</button>
    </div>
    <div class="property-1hover">
      <button class="service3" :autoFocus="true">Service</button>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "HomePageService",
  });
</script>
<style scoped>
  .service2 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: relative;
    font-size: var(--font-size-mini);
    line-height: 150%;
    font-weight: 600;
    font-family: var(--font-raleway);
    color: var(--color-black);
    text-align: left;
    display: inline-block;
  }
  .property-1default10 {
    position: absolute;
    top: 20px;
    left: 20px;
    border-radius: var(--br-3xs);
    width: 117px;
    height: 44px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
    box-sizing: border-box;
  }
  .service3 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: relative;
    font-size: var(--font-size-mini);
    text-decoration: underline;
    line-height: 150%;
    font-weight: 800;
    font-family: var(--font-raleway);
    color: rgba(0, 0, 0, 0.99);
    text-align: left;
    display: inline-block;
  }
  .property-1hover {
    position: absolute;
    top: 105px;
    left: 20px;
    border-radius: var(--br-3xs);
    width: 117px;
    height: 43px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
    box-sizing: border-box;
  }
  .home-page-service4 {
    width: 167px;
    border-radius: var(--br-8xs);
    border: 1px dashed var(--color-blueviolet);
    box-sizing: border-box;
    height: 190px;
    overflow: hidden;
  }
</style>
