<template>
  <div class="sign-in-sign-in1">
    <button class="property-1default11" :autoFocus="true">
      <img class="property-1default-child" alt="" src="/rectangle-40.svg" />
      <button class="sign-in11" :autoFocus="true">Sign In</button>
    </button>
    <button class="property-1variant26" :autoFocus="true">
      <img class="property-1default-child" alt="" src="/rectangle-401.svg" />
      <button class="sign-in11" :autoFocus="true">Sign In</button>
    </button>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "SignInSignIn",
  });
</script>
<style scoped>
  .property-1default-child {
    width: 132px;
    position: relative;
    border-radius: var(--br-3xs);
    height: 48px;
    z-index: 0;
  }
  .sign-in11 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    width: 60px;
    position: absolute;
    margin: 0 !important;
    top: 12px;
    left: 36px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: center;
    display: inline-block;
    z-index: 1;
  }
  .property-1default11 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 20px;
    left: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-3xs);
  }
  .property-1variant26 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 88px;
    left: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-3xs);
  }
  .sign-in-sign-in1 {
    width: 172px;
    border-radius: var(--br-8xs);
    border: 1px dashed var(--color-blueviolet);
    box-sizing: border-box;
    height: 166px;
    overflow: hidden;
  }
</style>
