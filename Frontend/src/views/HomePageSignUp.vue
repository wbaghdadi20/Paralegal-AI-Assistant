<template>
  <div class="home-page-sign-up1">
    <button class="property-1variant23" :autoFocus="true">
      <button class="sign-up11" :autoFocus="true">Sign Up</button>
    </button>
    <button class="property-1default7" :autoFocus="true">
      <button class="sign-up12" :autoFocus="true">Sign Up</button>
    </button>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "HomePageSignUp",
  });
</script>
<style scoped>
  .sign-up11 {
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
  .property-1variant23 {
    cursor: pointer;
    border: 1px solid var(--color-white);
    padding: var(--padding-xs) var(--padding-17xl);
    background-color: var(--color-gray-100);
    position: absolute;
    top: 88px;
    left: 20px;
    border-radius: var(--br-3xs);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .sign-up12 {
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
  .property-1default7 {
    cursor: pointer;
    border: none;
    padding: var(--padding-xs) var(--padding-17xl);
    background-color: var(--color-white);
    position: absolute;
    top: 16px;
    left: 20px;
    border-radius: var(--br-3xs);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .home-page-sign-up1 {
    width: 172px;
    border-radius: var(--br-8xs);
    border: 1px dashed var(--color-blueviolet);
    box-sizing: border-box;
    height: 156px;
    overflow: hidden;
  }
</style>
