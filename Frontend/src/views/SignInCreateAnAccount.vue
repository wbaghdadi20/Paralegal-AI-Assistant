<template>
  <div class="sign-in-create-an-account">
    <div class="property-1default9">
      <div class="create-an-account3" @click="onCreateAnAccount1Click">
        create an account
      </div>
    </div>
    <div class="property-1variant25">
      <div class="create-an-account4">create an account</div>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "SignInCreateAnAccount",
    methods: {
      onCreateAnAccount1Click() {
        this.$router.push("/sign-up");
      },
    },
  });
</script>
<style scoped>
  .create-an-account3 {
    position: relative;
    line-height: 120%;
    font-weight: 500;
    cursor: pointer;
  }
  .property-1default9 {
    position: absolute;
    top: 20px;
    left: 20px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
  }
  .create-an-account4 {
    position: relative;
    text-decoration: underline;
    line-height: 120%;
    font-weight: 500;
  }
  .property-1variant25 {
    position: absolute;
    top: 82px;
    left: 20px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
  }
  .sign-in-create-an-account {
    width: 215px;
    border-radius: var(--br-8xs);
    border: 1px dashed var(--color-blueviolet);
    box-sizing: border-box;
    height: 144px;
    overflow: hidden;
    text-align: center;
    font-size: var(--font-size-lg);
    color: var(--color-darkslategray);
    font-family: var(--paragraph);
  }
</style>
