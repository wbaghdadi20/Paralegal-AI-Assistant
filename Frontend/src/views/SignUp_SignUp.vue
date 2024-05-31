<template>
  <div class="sighupsignup1">
    <div class="property-1default5">
      <button class="sign-up7" :autoFocus="true">
        <div class="sign-up-inner" />
        <button class="sign-up8" :autoFocus="true">Sign Up</button>
      </button>
    </div>
    <div class="property-1variant21">
      <button class="sign-up7" :autoFocus="true">
        <div class="sign-up-child1" />
        <button class="sign-up8" :autoFocus="true">Sign Up</button>
      </button>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "SighUpSignUp",
  });
</script>
<style scoped>
  .sign-up-inner {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-darkolivegreen);
    width: 132px;
    height: 48px;
  }
  .sign-up8 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 13px;
    left: 36px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: center;
    display: inline-block;
    width: 60px;
  }
  .sign-up7 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    width: 132px;
    position: relative;
    height: 48px;
  }
  .property-1default5 {
    position: absolute;
    top: 20px;
    left: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
  }
  .sign-up-child1 {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: #001831;
    width: 132px;
    height: 48px;
  }
  .property-1variant21 {
    position: absolute;
    top: 88px;
    left: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
  }
  .sighupsignup1 {
    width: 172px;
    border-radius: var(--br-8xs);
    border: 1px dashed var(--color-blueviolet);
    box-sizing: border-box;
    height: 156px;
    overflow: hidden;
  }
</style>
