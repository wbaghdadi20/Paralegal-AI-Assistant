<template>
  <div class="sign-upsign-in1">
    <div class="property-1default4">
      <div class="sign-in7" @click="onSignInTextClick">Sign In</div>
    </div>
    <div class="property-1variant2">
      <b class="sign-in8">Sign In</b>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "SignUpsignIn",
    methods: {
      onSignInTextClick() {
        this.$router.push("/sign-in");
      },
    },
  });
</script>
<style scoped>
  .sign-in7 {
    position: relative;
    font-weight: 500;
    cursor: pointer;
  }
  .property-1default4 {
    position: absolute;
    top: 20px;
    left: 20px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
  }
  .sign-in8 {
    position: relative;
  }
  .property-1variant2 {
    position: absolute;
    top: 87px;
    left: 20px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
  }
  .sign-upsign-in1 {
    width: 122px;
    border-radius: var(--br-8xs);
    border: 1px dashed var(--color-blueviolet);
    box-sizing: border-box;
    height: 154px;
    overflow: hidden;
    text-align: center;
    font-size: var(--font-size-lg);
    color: var(--color-black);
    font-family: var(--font-poppins);
  }
</style>
