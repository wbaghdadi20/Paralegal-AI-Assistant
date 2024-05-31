<template>
  <div class="home-page-sign-in1">
    <div class="property-1default6">
      <button class="sign-in9" :autoFocus="true" @click="onSignInClick">
        Sign In
      </button>
    </div>
    <div class="property-1variant22">
      <button class="sign-in10" :autoFocus="true">Sign In</button>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "HomePageSignIn",
    methods: {
      onSignInClick() {
        this.$router.push("/sign-in");
      },
    },
  });
</script>
<style scoped>
  .sign-in9 {
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
    text-align: left;
    display: inline-block;
  }
  .property-1default6 {
    position: absolute;
    top: 20px;
    left: 20px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .sign-in10 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: relative;
    font-size: var(--paragraph-size);
    text-decoration: underline;
    line-height: 150%;
    font-weight: 900;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: left;
    display: inline-block;
  }
  .property-1variant22 {
    position: absolute;
    top: 64px;
    left: 20px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .home-page-sign-in1 {
    width: 92px;
    border-radius: var(--br-8xs);
    border: 1px dashed var(--color-blueviolet);
    box-sizing: border-box;
    height: 108px;
    overflow: hidden;
  }
</style>
